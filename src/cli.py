"""
Main platform CLI — Entry point for mimo-crypto-intelligence

Commands:
  analyze    — Analyze tokens (risk, social, trader patterns)
  discover   — Discover active tokens
  report     — Generate reports
  monitor    — Monitor tokens in real-time
"""

import argparse
import asyncio
import json
import sys
from typing import List, Optional

from src.analyzers import TraderAnalyzer, RiskAnalyzer, TwitterAnalyzer
from src.reports import ReportGenerator


def setup_parser():
    """Setup CLI argument parser"""
    parser = argparse.ArgumentParser(
        prog="mimo-crypto",
        description="AI-powered crypto trading intelligence platform",
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze tokens")
    analyze_parser.add_argument("--token", type=str, help="Token mint address")
    analyze_parser.add_argument("--risk", action="store_true", help="Risk analysis")
    analyze_parser.add_argument("--social", action="store_true", help="Social analysis")
    analyze_parser.add_argument("--batch", type=str, nargs="+", help="Analyze multiple tokens")
    
    # discover command
    discover_parser = subparsers.add_parser("discover", help="Discover active tokens")
    discover_parser.add_argument("--limit", type=int, default=30, help="Number of tokens to scan")
    discover_parser.add_argument("--min-txns", type=int, default=20, help="Minimum transactions/hour")
    discover_parser.add_argument("--min-liq", type=float, default=3000, help="Minimum liquidity USD")
    
    # report command
    report_parser = subparsers.add_parser("report", help="Generate reports")
    report_parser.add_argument("--type", choices=["token", "trader", "social", "comprehensive"], 
                              default="comprehensive", help="Report type")
    report_parser.add_argument("--token", type=str, help="Token mint for token report")
    report_parser.add_argument("--output", type=str, help="Output file (default: stdout)")
    
    # monitor command
    monitor_parser = subparsers.add_parser("monitor", help="Monitor tokens in real-time")
    monitor_parser.add_argument("--token", type=str, help="Token mint to monitor")
    monitor_parser.add_argument("--duration", type=int, default=15, help="Monitor duration in minutes")
    monitor_parser.add_argument("--discover", action="store_true", help="Auto-discover and monitor")
    
    return parser


async def cmd_analyze(args):
    """Analyze tokens"""
    risk_analyzer = RiskAnalyzer()
    social_analyzer = TwitterAnalyzer()
    
    if args.token:
        # Single token analysis
        print(f"🔍 Analyzing {args.token[:20]}...\n")
        
        if args.risk or not args.social:
            result = await risk_analyzer.analyze_token(args.token)
            print(risk_analyzer.format_report(result))
            print()
        
        if args.social or not args.risk:
            result = await social_analyzer.analyze_token_social(args.token)
            print(json.dumps(result, indent=2))
    
    elif args.batch:
        # Batch analysis
        print(f"🔍 Analyzing {len(args.batch)} tokens...\n")
        
        for mint in args.batch:
            result = await risk_analyzer.analyze_token(mint)
            print(risk_analyzer.format_report(result))
            print()
    
    else:
        print("❌ Please specify --token or --batch")


async def cmd_discover(args):
    """Discover active tokens"""
    trader_analyzer = TraderAnalyzer()
    
    print("🔍 Discovering active tokens...")
    active = await trader_analyzer.discover_active(
        limit=args.limit,
        min_txns=args.min_txns,
        min_liq=args.min_liq,
    )
    
    print(f"\n📊 Found {len(active)} active tokens:\n")
    
    for i, t in enumerate(active[:10], 1):
        emoji = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "•"
        print(f"{emoji} **${t['symbol']}**")
        print(f"   MCap: ${t.get('mcap', 0):,.0f} | Liq: ${t['liquidity']:,.0f}")
        print(f"   Txns: {t['txns_1h']}/h | Buy: {t['buy_ratio']:.0%}")
        print()


async def cmd_report(args):
    """Generate reports"""
    generator = ReportGenerator()
    
    if args.type == "token":
        if not args.token:
            print("❌ Please specify --token for token report")
            return
        
        risk_analyzer = RiskAnalyzer()
        analysis = await risk_analyzer.analyze_token(args.token)
        report = generator.generate_token_report(analysis)
    
    elif args.type == "social":
        social_analyzer = TwitterAnalyzer()
        data = await social_analyzer.scan_tokens_social()
        report = generator.generate_social_report(data)
    
    elif args.type == "comprehensive":
        report = generator.generate_comprehensive_report()
    
    else:
        report = generator.generate_comprehensive_report()
    
    # Output
    if args.output:
        with open(args.output, "w") as f:
            f.write(report)
        print(f"✅ Report saved to {args.output}")
    else:
        print(report)


async def cmd_monitor(args):
    """Monitor tokens in real-time"""
    trader_analyzer = TraderAnalyzer()
    
    if args.discover:
        print("🔍 Discovering active tokens to monitor...")
        active = await trader_analyzer.discover_active()
        
        if not active:
            print("❌ No active tokens found")
            return
        
        print(f"\n📊 Monitoring top {min(5, len(active))} tokens for {args.duration}m:\n")
        
        for token in active[:5]:
            mint = token["mint"]
            symbol = token["symbol"]
            
            print(f"👀 Starting ${symbol}...")
            
            def print_update(update):
                emoji = "🟢" if update["change_pct"] > 0 else "🔴"
                print(f"  [{update['check']}] {emoji} ${update['symbol']}: ${update['price']:.6g} ({update['change_pct']:+.1f}%)")
            
            result = await trader_analyzer.watch_token(mint, args.duration, callback=print_update)
            
            if result and "error" not in result:
                change = result.get("price_change_pct", 0)
                emoji = "🟢" if change > 0 else "🔴"
                print(f"  ✅ Final: {emoji} ${result.get('symbol')}: {change:+.1f}%\n")
    
    elif args.token:
        print(f"👀 Monitoring {args.token[:20]}... for {args.duration}m\n")
        
        def print_update(update):
            emoji = "🟢" if update["change_pct"] > 0 else "🔴"
            print(f"  [{update['check']}] {emoji} ${update['symbol']}: ${update['price']:.6g} ({update['change_pct']:+.1f}%) | 5m: {update['buys_5m']}B/{update['sells_5m']}S")
        
        result = await trader_analyzer.watch_token(args.token, args.duration, callback=print_update)
        
        if result and "error" not in result:
            change = result.get("price_change_pct", 0)
            emoji = "🟢" if change > 0 else "🔴"
            print(f"\n✅ Final: {emoji} ${result.get('symbol')}: {change:+.1f}%")
    
    else:
        print("❌ Please specify --token or --discover")


def main():
    """Main entry point"""
    parser = setup_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Run async commands
    if args.command == "analyze":
        asyncio.run(cmd_analyze(args))
    elif args.command == "discover":
        asyncio.run(cmd_discover(args))
    elif args.command == "report":
        asyncio.run(cmd_report(args))
    elif args.command == "monitor":
        asyncio.run(cmd_monitor(args))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
