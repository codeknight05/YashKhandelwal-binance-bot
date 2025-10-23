# src/advanced/oco.py
import logging

MIN_NOTIONAL = 100

def place_oco_order(client, symbol, side, quantity, take_profit_price, stop_loss_price):
    notional_tp = quantity * take_profit_price
    notional_sl = quantity * stop_loss_price
    if min(notional_tp, notional_sl) < MIN_NOTIONAL:
        print(f"❌ Error: OCO order notional too small. Minimum is {MIN_NOTIONAL} USDT.")
        return None

    try:
        # Binance USDT-M OCO uses 'futures_create_order' for separate TP/SL with reduceOnly
        tp_order = client.futures_create_order(
            symbol=symbol,
            side='SELL' if side=='BUY' else 'BUY',
            type='LIMIT',
            quantity=quantity,
            price=take_profit_price,
            timeInForce='GTC',
            reduceOnly=True
        )
        sl_order = client.futures_create_order(
            symbol=symbol,
            side='SELL' if side=='BUY' else 'BUY',
            type='STOP_MARKET',
            stopPrice=stop_loss_price,
            quantity=quantity,
            reduceOnly=True
        )
        logging.info(f"OCO orders placed: TP={tp_order}, SL={sl_order}")
        print("✅ OCO orders placed successfully!")
        return tp_order, sl_order
    except Exception as e:
        logging.error(f"OCO order error: {e}")
        print(f"❌ Error: {e}")
        return None
