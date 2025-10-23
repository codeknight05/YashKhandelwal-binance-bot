# src/limit_orders.py
from binance.client import Client
import logging

MIN_NOTIONAL = 100  # USDT-M Futures minimum

def place_limit_order(client, symbol, side, quantity, price):
    notional = quantity * price
    if notional < MIN_NOTIONAL:
        print(f"❌ Error: Limit order notional too small ({notional} USDT). Minimum is {MIN_NOTIONAL} USDT.")
        return None

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            quantity=quantity,
            price=price,
            timeInForce='GTC'
        )
        logging.info(f"Limit order successful: {order}")
        print("✅ Limit order placed successfully!")
        return order
    except Exception as e:
        logging.error(f"Limit order error: {e}")
        print(f"❌ Error: {e}")
        return None
