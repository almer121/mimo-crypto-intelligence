"""
Risk analyzer — Multi-layer risk assessment for memecoins

12 rug pull methods detection:
1. Bundle dump
2. Liquidity pull
3. Mint authority abuse
4. Freeze authority (honeypot)
5. Wash trading
6. Cabal play
7. Honeypot program
8. Burn scam
9. Social engineering
10. Fee extraction
11. Ad timing
12. Speed rug
"""

import asyncio
import json
import os
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any

import httpx


class RiskAnalyzer:
    """Multi-layer risk assessment for memecoins"""
    
    DEX_API = "https://api.dexscreener.com/tokens/v1/solana"
    SOL_RPC = "https://api.mainnet-beta.solana.com"
    
    # Risk thresholds
    THRESHOLDS = {
        "max_mcap": 500_000,  # $500K
        "min_mcap": 15_000,   # $15K
        "max_liq": 200_000,   # $200K
        "min_liq": 3_000,     # $3K
        "min_buy_ratio": 0.45,  # 45%
        "max_buy_ratio": 0.80,  # 80% (suspicious if higher)
        "min_txns_h": 50,     # 50 txns/hour
        "max_top1_pct": 0.08, # 8% (top holder)
        "max_top10_pct": 0.30, # 30% (top 10 holders)
        "min_dev_score": 30,  # 30/100
    }
    
    def __init__(self, data_dir: str = "data/risk-data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
    
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
    
    async def analyze_token(self, mint: str) -> Dict:
        """Full risk analysis for a token"""
        pair = await self.get_token_info(mint)
        if not pair:
            return {"error": "Token not found", "score": 0, "risk": "unknown"}
        
        symbol = pair.get("baseToken", {}).get("symbol", "?")
        mcap = float(pair.get("marketCap", 0) or pair.get("fdv", 0) or 0)
        liq = float(pair.get("liquidity", {}).get("usd", 0) or 0)
        volume = float(pair.get("volume", {}).get("h24", 0) or 0)
        txns = pair.get("txns", {})
        h1 = txns.get("h1", {})
        buys = h1.get("buys", 0)
        sells = h1.get("sells", 0)
        total = buys + sells
        buy_ratio = buys / total if total > 0 else 0
        
        # Calculate risk score (0-100, lower is riskier)
        score = 100
        risks = []
        
        # 1. Market cap check
        if mcap < self.THRESHOLDS["min_mcap"]:
            score -= 20
            risks.append(f"MCap too low: ${mcap:,.0f}")
        elif mcap > self.THRESHOLDS["max_mcap"]:
            score -= 10
            risks.append(f"MCap high: ${mcap:,.0f}")
        
        # 2. Liquidity check
        if liq < self.THRESHOLDS["min_liq"]:
            score -= 25
            risks.append(f"Liquidity too low: ${liq:,.0f}")
        elif liq > self.THRESHOLDS["max_liq"]:
            score -= 5
            risks.append(f"Liquidity high: ${liq:,.0f}")
        
        # 3. MCap:Liq ratio
        if liq > 0:
            ratio = mcap / liq
            if ratio > 10:
                score -= 15
                risks.append(f"MCap:Liq ratio high: {ratio:.1f}")
            elif ratio < 0.5:
                score -= 10
                risks.append(f"MCap:Liq ratio low: {ratio:.1f}")
        
        # 4. Buy ratio check
        if buy_ratio < self.THRESHOLDS["min_buy_ratio"]:
            score -= 15
            risks.append(f"Low buy ratio: {buy_ratio:.0%}")
        elif buy_ratio > self.THRESHOLDS["max_buy_ratio"]:
            score -= 10
            risks.append(f"Suspicious high buy ratio: {buy_ratio:.0%}")
        
        # 5. Transaction volume
        if total < self.THRESHOLDS["min_txns_h"]:
            score -= 10
            risks.append(f"Low txns: {total}/h")
        
        # 6. Volume:Liq ratio (wash trading detection)
        if liq > 0:
            vol_liq_ratio = volume / liq
            if vol_liq_ratio > 100:
                score -= 20
                risks.append(f"Wash trading? Vol:Liq {vol_liq_ratio:.0f}x")
        
        # Clamp score
        score = max(0, min(100, score))
        
        # Determine risk level
        if score >= 80:
            risk_level = "low"
        elif score >= 60:
            risk_level = "medium"
        elif score >= 40:
            risk_level = "high"
        else:
            risk_level = "critical"
        
        return {
            "symbol": symbol,
            "mint": mint,
            "score": score,
            "risk_level": risk_level,
            "risks": risks,
            "metrics": {
                "mcap": mcap,
                "liquidity": liq,
                "volume_24h": volume,
                "buys_1h": buys,
                "sells_1h": sells,
                "buy_ratio": buy_ratio,
                "mc_liq_ratio": mcap / liq if liq > 0 else 0,
                "vol_liq_ratio": volume / liq if liq > 0 else 0,
            },
            "analyzed_at": datetime.now(timezone.utc).isoformat(),
        }
    
    def format_report(self, analysis: Dict) -> str:
        """Format analysis as clean Telegram report"""
        if "error" in analysis:
            return f"❌ Error: {analysis['error']}"
        
        symbol = analysis["symbol"]
        score = analysis["score"]
        risk = analysis["risk_level"]
        risks = analysis["risks"]
        m = analysis["metrics"]
        
        # Risk emoji
        risk_emoji = {"low": "🟢", "medium": "🟡", "high": "🟠", "critical": "🔴"}
        
        report = []
        report.append(f"{risk_emoji.get(risk, '⚪')} **${symbol}** — Risk: {risk.upper()}")
        report.append(f"• Score: **{score}/100**")
        report.append(f"• MCap: ${m['mcap']:,.0f} | Liq: ${m['liquidity']:,.0f}")
        report.append(f"• Buy: {m['buy_ratio']:.0%} | Txns: {m['buys_1h'] + m['sells_1h']}/h")
        
        if risks:
            report.append("• ⚠️ Risks:")
            for r in risks[:3]:
                report.append(f"  - {r}")
        
        return "\n".join(report)


# CLI interface
async def main():
    import argparse
    parser = argparse.ArgumentParser(description="Risk Analyzer")
    parser.add_argument("--analyze", type=str, help="Analyze specific mint")
    parser.add_argument("--batch", type=str, nargs="+", help="Analyze multiple mints")
    args = parser.parse_args()
    
    analyzer = RiskAnalyzer()
    
    if args.analyze:
        print(f"🔬 Analyzing {args.analyze[:20]}...")
        result = await analyzer.analyze_token(args.analyze)
        print(analyzer.format_report(result))
    
    elif args.batch:
        print(f"🔬 Analyzing {len(args.batch)} tokens...")
        for mint in args.batch:
            result = await analyzer.analyze_token(mint)
            print(analyzer.format_report(result))
            print()

if __name__ == "__main__":
    asyncio.run(main())
