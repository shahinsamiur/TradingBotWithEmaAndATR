from indicatios.atr import atr_stoploss
from indicatios.ema import ema
import sys
import logging
def botLogic(marketData):
    symbol = "BTCUSDT"
    # logging.info(marketData)
    # Get last two EMA values for both 21 and 50
    ema50_prev = ema({symbol: marketData[symbol].iloc[:-2]}, symbol, 'close', 50)
    ema21_prev = ema({symbol: marketData[symbol].iloc[:-2]}, symbol, 'close', 21)

    ema50_curr =ema({symbol: marketData[symbol].iloc[:-1]}, symbol, 'close', 50)
    ema21_curr = ema({symbol: marketData[symbol].iloc[:-1]}, symbol, 'close', 21)

    logging.info(f"ema21: curr={ema21_curr}, prev={ema21_prev}")
    logging.info(f"ema50: curr={ema50_curr}, prev={ema50_prev}")

    buy_sl = atr_stoploss(data=marketData[symbol], newTrend="buy_signal")
    logging.info(f"Buy SL: {buy_sl}")

    sell_sl = atr_stoploss(data=marketData[symbol], newTrend="sell_signal")
    logging.info(f"Sell SL: {sell_sl}")






    # Detect trend change
    if ema21_prev < ema50_prev and ema21_curr > ema50_curr:
        newTrend =  "buy_signal"
        SL=atr_stoploss(data=marketData[symbol] , newTrend=newTrend)
        return {"signal":"buy_signal" , "SL":SL , "symbol":symbol}
    elif ema21_prev > ema50_prev and ema21_curr < ema50_curr:
        newTrend =  "sell_signal"
        SL=atr_stoploss(data=marketData[symbol] , newTrend=newTrend)
        return {"signal":"sell_signal" , "SL":SL ,  "symbol":symbol}
    else:
        return None
