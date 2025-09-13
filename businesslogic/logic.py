import time
from getMarketData.getMarketDataFile import getMarketData
from indicatios.ema import ema
from indicatios.atr import atr_stoploss
from sendMessage.testSendMessage import send_message  # Use your real send_message import

# Track last signal time for each symbol
last_signal_time = {}


def botLogic(marketData, symbol):

    df = marketData[symbol]

    # Use last fully closed candle (-2) and previous closed candle (-3)
    ema50_prev = ema({symbol: df.iloc[:-2]}, symbol, 'close', 50)
    ema21_prev = ema({symbol: df.iloc[:-2]}, symbol, 'close', 21)

    ema50_curr = ema({symbol: df.iloc[:-1]}, symbol, 'close', 50)
    ema21_curr = ema({symbol: df.iloc[:-1]}, symbol, 'close', 21)

    # Calculate ATR stoploss
    atr_buy = atr_stoploss(data=df, newTrend="buy_signal")
    atr_sell = atr_stoploss(data=df, newTrend="sell_signal")

    # Optional logging
    # message = (
    #     f"📊 *Trend Detection Update:*\n\n"
    #     f"Symbol : `{symbol}`\n"
    #     f"*EMA 21* ➤ Prev: `{ema21_prev:.2f}`, Curr: `{ema21_curr:.2f}`\n"
    #     f"*EMA 50* ➤ Prev: `{ema50_prev:.2f}`, Curr: `{ema50_curr:.2f}`\n\n"
    #     f"🛒 *ATR Stop Loss (Buy)*: `{atr_buy:.2f}`\n"
    #     f"🛑 *ATR Stop Loss (Sell)*: `{atr_sell:.2f}`"
    # )
    # print(message)
    # send_message(message)

    # Determine signal
    signal = None
    if ema21_prev < ema50_prev and ema21_curr > ema50_curr:
        newTrend = "buy_signal"
        SL = atr_stoploss(data=df, newTrend=newTrend)
        signal = {"signal": "buy_signal", "SL": SL, "symbol": symbol}
    elif ema21_prev > ema50_prev and ema21_curr < ema50_curr:
        newTrend = "sell_signal"
        SL = atr_stoploss(data=df, newTrend=newTrend)
        signal = {"signal": "sell_signal", "SL": SL, "symbol": symbol}

    return signal, df.index[-2]  # return last fully closed candle time
