"""
Twitter/X social analysis for crypto tokens

Analyzes:
- Twitter penetration (how many tokens have Twitter)
- Social presence quality
- Engagement patterns
- Correlation with token success
"""

import asyncio
import json
import os
import re
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
from urllib.parse import quote_plus

import httpx


class TwitterAnalyzer:
    """Twitter/X social analysis for crypto tokens"""
    
    DEX_API = "https://api.dexscreener.com/tokens/v1/solana"
    PUMP_API = "https://frontend-api-v3.pump.fun"
    
    def __init__(self, data_dir: str = "data/twitter-data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
    
    def _load_json(self, path: str, default: Any = None) -> Any:
        if os.path.exists(path):
            try:
                with open(path) as f:
                    return json.load(f)
            except:
                pass
        return default or {}
    
    def _save_json(self, path: str, data: Any):
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
    
    async def get_token_info(self, mint: str) -> Dict:
        """Get token info from DexScreener"""
        try:
            async with httpx.AsyncClient(timeout=15) as c:
                r = await c.get(f"{self.DEX_API}/{mint}")
                if r.status_code == 200:
                    data = r.json()
                    if data and isinstance(data, list) and data:
                        return data[0]
        except Exception:
            pass
        return {}
    
    async def get_recent_tokens(self, limit: int = 30) -> List[Dict]:
        """Get recently graduated tokens"""
        try:
            async with httpx.AsyncClient(timeout=15) as c:
                r = await c.get(f"{self.PUMP_API}/coins", params={
                    "sort": "created_timestamp", "order": "DESC",
                    "limit": limit, "offset": 0, "complete": "true",
                })
                if r.status_code == 200:
                    return r.json()
        except Exception:
            pass
        return []
    
    async def check_twitter_exists(self, username: str) -> bool:
        """Check if Twitter username exists"""
        try:
            async with httpx.AsyncClient(timeout=10, follow_redirects=True) as c:
                r = await c.get(f"https://nitter.net/{username}", headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                })
                return r.status_code == 200
        except:
            return False
    
    def extract_twitter_username(self, text: str) -> Optional[str]:
        """Extract Twitter username from text"""
        if not text:
            return None
        
        patterns = [
            r'(?:twitter\.com|x\.com)/@?([A-Za-z0-9_]+)',
            r'@([A-Za-z0-9_]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1)
        
        return None
    
    async def analyze_token_social(self, mint: str) -> Dict:
        """Analyze social presence for a token"""
        pair = await self.get_token_info(mint)
        if not pair:
            return {"error": "Token not found"}
        
        symbol = pair.get("baseToken", {}).get("symbol", "?")
        mcap = float(pair.get("marketCap", 0) or pair.get("fdv", 0) or 0)
        
        # Extract Twitter info
        info = pair.get("info", {})
        twitter = info.get("twitter")
        websites = info.get("websites", [])
        
        has_twitter = bool(twitter)
        twitter_username = self.extract_twitter_username(twitter) if twitter else None
        
        has_website = len(websites) > 0
        
        return {
            "symbol": symbol,
            "mint": mint,
            "mcap": mcap,
            "has_twitter": has_twitter,
            "twitter_username": twitter_username,
            "has_website": has_website,
            "social_score": (1 if has_twitter else 0) + (1 if has_website else 0),
        }
    
    async def scan_tokens_social(self, limit: int = 30) -> Dict:
        """Scan multiple tokens for social presence"""
        tokens = await self.get_recent_tokens(limit)
        
        results = []
        with_twitter = 0
        without_twitter = 0
        
        for token in tokens:
            mint = token.get("mint", "")
            if not mint:
                continue
            
            analysis = await self.analyze_token_social(mint)
            results.append(analysis)
            
            if analysis.get("has_twitter"):
                with_twitter += 1
            else:
                without_twitter += 1
            
            await asyncio.sleep(0.5)
        
        total = len(results)
        penetration = (with_twitter / total * 100) if total > 0 else 0
        
        # Calculate metrics by MCap range
        high_mcap = [r for r in results if r.get("mcap", 0) > 50000]
        high_mcap_twitter = sum(1 for r in high_mcap if r.get("has_twitter"))
        
        return {
            "total_tokens": total,
            "with_twitter": with_twitter,
            "without_twitter": without_twitter,
            "twitter_penetration": penetration,
            "high_mcap_count": len(high_mcap),
            "high_mcap_twitter_count": high_mcap_twitter,
            "tokens": results,
            "analyzed_at": datetime.now(timezone.utc).isoformat(),
        }
    
    def format_report(self, data: Dict) -> str:
        """Format as clean Telegram report"""
        report = []
        
        report.append("🐦 **TWITTER ANALYSIS**")
        report.append("━━━━━━━━━━━━━━━━━━")
        report.append(f"• Tokens scanned: **{data.get('total_tokens', 0)}**")
        report.append(f"• Twitter penetration: **{data.get('twitter_penetration', 0):.0f}%**")
        report.append(f"• High-MCap with Twitter: **{data.get('high_mcap_twitter_count', 0)}**")
        
        # Top tokens with Twitter
        tokens_with_twitter = [t for t in data.get("tokens", []) if t.get("has_twitter")]
        if tokens_with_twitter:
            report.append("\n**Tokens with Twitter:**")
            for t in tokens_with_twitter[:5]:
                report.append(f"• ${t['symbol']} — @{t.get('twitter_username', '?')}")
        
        return "\n".join(report)


# CLI interface
async def main():
    import argparse
    parser = argparse.ArgumentParser(description="Twitter Analyzer")
    parser.add_argument("--scan", action="store_true", help="Scan tokens for social presence")
    parser.add_argument("--analyze", type=str, help="Analyze specific mint")
    args = parser.parse_args()
    
    analyzer = TwitterAnalyzer()
    
    if args.scan:
        print("🔍 Scanning tokens for Twitter presence...")
        result = await analyzer.scan_tokens_social()
        print(analyzer.format_report(result))
    
    elif args.analyze:
        print(f"🔍 Analyzing {args.analyze[:20]}...")
        result = await analyzer.analyze_token_social(args.analyze)
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
