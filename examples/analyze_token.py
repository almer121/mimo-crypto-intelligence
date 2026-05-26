"""
Example: Analyze a token for risks

Usage:
  python examples/analyze_token.py <mint_address>
"""

import asyncio
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.analyzers import RiskAnalyzer


async def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_token.py <mint_address>")
        return
    
    mint = sys.argv[1]
    analyzer = RiskAnalyzer()
    
    print(f"🔍 Analyzing {mint[:20]}...\n")
    result = await analyzer.analyze_token(mint)
    print(analyzer.format_report(result))


if __name__ == "__main__":
    asyncio.run(main())
