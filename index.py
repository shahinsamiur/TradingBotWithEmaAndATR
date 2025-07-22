from indicatios.ema import ema
from indicatios.atr import atr_stoploss
from getMarketData.getMarketDataFile import getMarketData
from businesslogic.logic import botLogic
from sendMessage.sendMessage import send_message


def bot():
    print("Testing Trend Detection...\n")

    # Fetch full historical market data
    fullData = getMarketData(symbols=['EURUSD'], exchange="OANDA", n_bars=200)
    df = fullData['EURUSD']  # Assuming this is a DataFrame with datetime index

    # Send the full DataFrame to botLogic
    marketDataByPair = {"EURUSD": df}
    signal = botLogic(marketDataByPair)

    # Get the last candle time
    candle_time = df.index[-1]

    if signal:
        # Uncomment to send message
        # send_message(symbol=signal["symbol"], signal=signal["signal"], SL=signal["SL"])
        print(f"Time={candle_time}, Signal={signal['signal']}, SL={signal['SL']}")


bot()
