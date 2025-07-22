from indicatios.ema import ema
from indicatios.atr import atr_stoploss
from getMarketData.getMarketDataFile import getMarketData
from businesslogic.logic import botLogic
from sendMessage.sendMessage import send_message
def bot():
    print("Testing Trend Detection...\n")
    
    # Fetch full historical market data
    fullData = getMarketData(symbols=['EURUSD'], exchange="OANDA", n_bars=100)
    df = fullData['EURUSD']  # Assuming marketData is a dict like {'EURUSD': DataFrame}

    # Loop from index 4000 down to 3500 (simulate sliding window of 500 bars)
    for i in range(4000, 3499, -1):
        window = df[i-500:i]
        marketDataByPair = {"EURUSD": window}
        signal = botLogic(marketDataByPair)
        
        # Get the last candle's datetime
        candle_time = window.index[-1]  # assuming df uses datetime index
        if (signal!=None):
            # send_message(signal=signal["signal"],SL=signal["SL"] , symbol=signal["symbol"])
            print(f"Time={candle_time}, i={i}, Signal={signal["signal"]} , SL={signal["SL"]}")

        


bot()
