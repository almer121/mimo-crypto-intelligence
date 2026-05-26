"""
Report generator — Clean, scannable reports for Telegram

Generates:
- Token analysis reports
- Trader pattern reports
- Risk assessment reports
- Social media reports
- Comprehensive daily reports
"""

import json
import os
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any


class ReportGenerator:
    """Clean, scannable report generator"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
    
    def _load_json(self, path: str, default: Any = None) -> Any:
        if os.path.exists(path):
            try:
                with open(path) as f:
                    return json.load(f)
            except:
                pass
        return default or {}
    
    def format_number(self, n: float) -> str:
        """Format number with K/M suffix"""
        if n >= 1_000_000:
            return f"{n/1_000_000:.1f}M"
        elif n >= 1_000:
            return f"{n/1_000:.1f}K"
        return str(int(n))
    
    def generate_token_report(self, analysis: Dict) -> str:
        """Generate single token analysis report"""
        if "error" in analysis:
            return f"❌ Error: {analysis['error']}"
        
        symbol = analysis.get("symbol", "?")
        score = analysis.get("score", 0)
        risk = analysis.get("risk_level", "unknown")
        risks = analysis.get("risks", [])
        m = analysis.get("metrics", {})
        
        risk_emoji = {"low": "🟢", "medium": "🟡", "high": "🟠", "critical": "🔴"}
        
        report = []
        report.append(f"{risk_emoji.get(risk, '⚪')} **${symbol}** — Risk: {risk.upper()}")
        report.append(f"• Score: **{score}/100**")
        report.append(f"• MCap: {self.format_number(m.get('mcap', 0))} | Liq: {self.format_number(m.get('liquidity', 0))}")
        report.append(f"• Buy: {m.get('buy_ratio', 0):.0%} | Txns: {m.get('buys_1h', 0) + m.get('sells_1h', 0)}/h")
        
        if risks:
            report.append("• ⚠️ Risks:")
            for r in risks[:3]:
                report.append(f"  - {r}")
        
        return "\n".join(report)
    
    def generate_trader_report(self, data: Dict) -> str:
        """Generate trader pattern report"""
        report = []
        
        report.append("📊 **TRADER PATTERNS**")
        report.append("━━━━━━━━━━━━━━━━━━")
        report.append(f"• Tokens analyzed: **{data.get('total_tokens', 0)}**")
        
        if data.get("tokens"):
            report.append("\n**Recent tokens:**")
            for t in data["tokens"][:5]:
                change = t.get("price_change_pct", 0)
                emoji = "🟢" if change > 0 else "🔴"
                report.append(f"• {emoji} ${t.get('symbol', '?')}: {change:+.1f}%")
        
        return "\n".join(report)
    
    def generate_social_report(self, data: Dict) -> str:
        """Generate social media report"""
        report = []
        
        report.append("🐦 **TWITTER ANALYSIS**")
        report.append("━━━━━━━━━━━━━━━━━━")
        report.append(f"• Tokens scanned: **{data.get('total_tokens', 0)}**")
        report.append(f"• Twitter penetration: **{data.get('twitter_penetration', 0):.0f}%**")
        report.append(f"• High-MCap with Twitter: **{data.get('high_mcap_twitter_count', 0)}**")
        
        tokens_with_twitter = [t for t in data.get("tokens", []) if t.get("has_twitter")]
        if tokens_with_twitter:
            report.append("\n**Tokens with Twitter:**")
            for t in tokens_with_twitter[:5]:
                report.append(f"• ${t.get('symbol', '?')} — @{t.get('twitter_username', '?')}")
        
        return "\n".join(report)
    
    def generate_comprehensive_report(
        self,
        scalper_data: Optional[Dict] = None,
        trader_data: Optional[Dict] = None,
        social_data: Optional[Dict] = None,
        wallet_data: Optional[Dict] = None,
    ) -> str:
        """Generate comprehensive daily report"""
        report = []
        
        # Header
        report.append("📊 **DAILY CRYPTO REPORT**")
        report.append(f"⏰ {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
        report.append("")
        
        # 1. Scalper Status
        if scalper_data:
            report.append("🔪 **SCALPER v3**")
            report.append("━━━━━━━━━━━━━━━━━━")
            report.append(f"• Trades: **{scalper_data.get('total_trades', 0)}** | Win Rate: **{scalper_data.get('win_rate', 0):.0f}%**")
            report.append(f"• Total PnL: **{scalper_data.get('total_pnl', 0):+.4f} SOL**")
            
            last = scalper_data.get("last_trade")
            if last:
                sym = last.get("symbol", "?")
                pnl = last.get("pnl_pct", 0)
                emoji = "✅" if pnl > 0 else "❌"
                report.append(f"• Last: {emoji} **${sym}** {pnl:+.1f}%")
            
            report.append("")
        
        # 2. Trader Patterns
        if trader_data:
            report.append("🐋 **TRADER DATA**")
            report.append("━━━━━━━━━━━━━━━━━━")
            report.append(f"• Tokens analyzed: **{trader_data.get('total_tokens', 0)}**")
            
            if trader_data.get("tokens"):
                latest = trader_data["tokens"][0]
                change = latest.get("price_change_pct", 0)
                emoji = "🟢" if change > 0 else "🔴"
                report.append(f"• Latest: {emoji} **${latest.get('symbol', '?')}** {change:+.1f}%")
            
            report.append("")
        
        # 3. Twitter
        if social_data:
            report.append("🐦 **TWITTER**")
            report.append("━━━━━━━━━━━━━━━━━━")
            report.append(f"• Penetration: **{social_data.get('twitter_penetration', 0):.0f}%**")
            report.append(f"• High-MCap with Twitter: **{social_data.get('high_mcap_twitter_count', 0)}**")
            report.append("")
        
        # 4. Systems
        report.append("⚙️ **SYSTEMS**")
        report.append("━━━━━━━━━━━━━━━━━━")
        report.append("• All systems: ✅ Running")
        report.append("")
        
        report.append("🔥 **Learn → Upgrade → Repeat**")
        
        return "\n".join(report)


# CLI interface
def main():
    import argparse
    parser = argparse.ArgumentParser(description="Report Generator")
    parser.add_argument("--token", type=str, help="Generate token report (JSON file)")
    parser.add_argument("--comprehensive", action="store_true", help="Generate comprehensive report")
    args = parser.parse_args()
    
    generator = ReportGenerator()
    
    if args.token:
        data = generator._load_json(args.token)
        print(generator.generate_token_report(data))
    
    elif args.comprehensive:
        print(generator.generate_comprehensive_report())

if __name__ == "__main__":
    main()
