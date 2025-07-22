from indicatios.atr import atr_stoploss
from indicatios.ema import ema

def botLogic(marketData):
    symbol = "EURUSD"
    
    # Get last two EMA values for both 21 and 50
    ema50_prev = ema({"EURUSD": marketData[symbol].iloc[:-2]}, symbol, 'close', 50)
    ema21_prev = ema({"EURUSD": marketData[symbol].iloc[:-2]}, symbol, 'close', 21)

    ema50_curr =ema({"EURUSD": marketData[symbol].iloc[:-1]}, symbol, 'close', 50)
    ema21_curr = ema({"EURUSD": marketData[symbol].iloc[:-1]}, symbol, 'close', 21)





    # print("ema21 : ",ema21_curr , ema21_prev)
    # print("ema50 : ",ema50_curr ,ema50_prev)
    # print(atr_stoploss(data=marketData[symbol] , newTrend="buy_signal"))
    # print(atr_stoploss(data=marketData[symbol] , newTrend="sell_signal"))





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
