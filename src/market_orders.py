# src/market_orders.py
from binance.client import Client
import logging

MIN_NOTIONAL = 100  # USDT-M Futures minimum

def place_market_order(client, symbol, side, quantity):
    # Validate notional
    ticker = client.futures_symbol_ticker(symbol=symbol)
    market_price = float(ticker['price'])
    notional = quantity * market_price
    if notional < MIN_NOTIONAL:
        print(f"❌ Error: Market order notional too small ({notional} USDT). Minimum is {MIN_NOTIONAL} USDT.")
        return None

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        logging.info(f"Market order successful: {order}")
        print("✅ Market order placed successfully!")
        return order
    except Exception as e:
        logging.error(f"Market order error: {e}")
        print(f"❌ Error: {e}")
        return None
