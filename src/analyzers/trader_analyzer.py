"""
Real-time trader pattern analyzer.

Monitors graduated tokens for actual buy/sell trades.
Tracks wallet patterns, win rates, entry/exit timing.
Data used to upgrade scalper analysis.
"""

import asyncio
import json
import os
import time
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any

import httpx


class TraderAnalyzer:
    """Real-time trader pattern analyzer"""
    
    PUMP_API = "https://frontend-api-v3.pump.fun"
    DEX_API = "https://api.dexscreener.com/tokens/v1/solana"
    
    def __init__(self, data_dir: str = "data/trader-data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        self.wallet_db_path = os.path.join(data_dir, "wallet-db.json")
        self.wallet_db = self._load_json(self.wallet_db_path, {})
    
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
    
    async def get_recent_graduated(self, limit: int = 20) -> List[Dict]:
        """Get recently graduated tokens from Pump.fun"""
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
    
    async def watch_token(self, mint: str, duration_min: int = 30, callback=None) -> Dict:
        """Watch a specific token for trading patterns
        
        Args:
            mint: Token mint address
            duration_min: Watch duration in minutes
            callback: Optional callback function called with each update
            
        Returns:
            Final analysis result
        """
        pair = await self.get_token_info(mint)
        if not pair:
            return {"error": "Token not found"}
        
        symbol = pair.get("baseToken", {}).get("symbol", "?")
        initial_price = float(pair.get("priceUsd", 0) or 0)
        liquidity = float(pair.get("liquidity", {}).get("usd", 0) or 0)
        volume = float(pair.get("volume", {}).get("h24", 0) or 0)
        
        start_time = time.time()
        check_count = 0
        
        while time.time() - start_time < duration_min * 60:
            check_count += 1
            current_pair = await self.get_token_info(mint)
            
            if current_pair:
                current_price = float(current_pair.get("priceUsd", 0) or 0)
                price_change = ((current_price - initial_price) / initial_price * 100) if initial_price > 0 else 0
                
                txns = current_pair.get("txns", {})
                m5 = txns.get("m5", {})
                h1 = txns.get("h1", {})
                
                update = {
                    "symbol": symbol,
                    "mint": mint,
                    "price": current_price,
                    "change_pct": price_change,
                    "buys_5m": m5.get("buys", 0),
                    "sells_5m": m5.get("sells", 0),
                    "buys_1h": h1.get("buys", 0),
                    "sells_1h": h1.get("sells", 0),
                    "check": check_count,
                }
                
                if callback:
                    callback(update)
            
            await asyncio.sleep(30)
        
        # Final result
        final_pair = await self.get_token_info(mint)
        final_price = float(final_pair.get("priceUsd", 0) or 0) if final_pair else 0
        price_change = ((final_price - initial_price) / initial_price * 100) if initial_price > 0 else 0
        
        result = {
            "symbol": symbol,
            "mint": mint,
            "initial_price": initial_price,
            "final_price": final_price,
            "price_change_pct": price_change,
            "duration_min": duration_min,
            "checks": check_count,
            "liquidity": liquidity,
            "volume_24h": volume,
            "analyzed_at": datetime.now(timezone.utc).isoformat(),
        }
        
        # Save
        safe_symbol = symbol.replace(" ", "_").replace("/", "_")
        data_path = os.path.join(self.data_dir, f"{safe_symbol}_{int(time.time())}.json")
        self._save_json(data_path, result)
        
        return result
    
    async def discover_active(self, limit: int = 30, min_txns: int = 20, min_liq: float = 3000) -> List[Dict]:
        """Discover active graduated tokens"""
        tokens = await self.get_recent_graduated(limit)
        active = []
        
        for token in tokens:
            mint = token.get("mint", "")
            symbol = token.get("symbol", "?")
            mcap = token.get("usd_market_cap", 0)
            
            pair = await self.get_token_info(mint)
            if not pair:
                continue
            
            liquidity = float(pair.get("liquidity", {}).get("usd", 0) or 0)
            volume = float(pair.get("volume", {}).get("h24", 0) or 0)
            txns = pair.get("txns", {})
            h1 = txns.get("h1", {})
            buys_1h = h1.get("buys", 0)
            sells_1h = h1.get("sells", 0)
            total_1h = buys_1h + sells_1h
            
            if total_1h >= min_txns and liquidity >= min_liq:
                active.append({
                    "mint": mint,
                    "symbol": symbol,
                    "mcap": mcap,
                    "liquidity": liquidity,
                    "volume": volume,
                    "txns_1h": total_1h,
                    "buy_ratio": buys_1h / total_1h if total_1h > 0 else 0,
                })
            
            await asyncio.sleep(0.5)
        
        active.sort(key=lambda x: x["txns_1h"], reverse=True)
        return active


# CLI interface
async def main():
    import argparse
    parser = argparse.ArgumentParser(description="Trader Pattern Analyzer")
    parser.add_argument("--discover", action="store_true", help="Discover active tokens")
    parser.add_argument("--watch", type=str, help="Watch specific mint")
    parser.add_argument("--duration", type=int, default=15, help="Watch duration in minutes")
    args = parser.parse_args()
    
    analyzer = TraderAnalyzer()
    
    if args.discover:
        print("🔍 Discovering active tokens...")
        active = await analyzer.discover_active()
        print(f"\n📊 Found {len(active)} active tokens:")
        for t in active[:5]:
            print(f"  ${t['symbol']}: {t['txns_1h']} txns/h | Liq: ${t['liquidity']:,.0f} | Buy: {t['buy_ratio']:.0%}")
    
    elif args.watch:
        print(f"👀 Watching {args.watch[:20]}... for {args.duration}m")
        
        def print_update(update):
            emoji = "🟢" if update["change_pct"] > 0 else "🔴"
            print(f"  [{update['check']}] {emoji} ${update['symbol']}: ${update['price']:.6g} ({update['change_pct']:+.1f}%) | 5m: {update['buys_5m']}B/{update['sells_5m']}S")
        
        result = await analyzer.watch_token(args.watch, args.duration, callback=print_update)
        print(f"\n📊 Final: {result.get('symbol')}: {result.get('price_change_pct', 0):+.1f}%")

if __name__ == "__main__":
    asyncio.run(main())
