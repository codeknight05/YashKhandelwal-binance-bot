# src/advanced/stop_limit.py
import logging

MIN_NOTIONAL = 100

def place_stop_limit_order(client, symbol, side, quantity, stop_price, limit_price):
    notional = quantity * limit_price
    if notional < MIN_NOTIONAL:
        print(f"❌ Error: Stop-Limit order notional too small ({notional} USDT). Minimum is {MIN_NOTIONAL} USDT.")
        return None

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='STOP_MARKET',
            stopPrice=stop_price,
            quantity=quantity
        )
        logging.info(f"Stop-Limit order successful: {order}")
        print("✅ Stop-Limit order placed successfully!")
        return order
    except Exception as e:
        logging.error(f"Stop-Limit order error: {e}")
        print(f"❌ Error: {e}")
        return None
