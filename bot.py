from indicatios.ema import ema
from indicatios.atr import atr_stoploss
from getMarketData.getMarketDataFile import getMarketData
from businesslogic.logic import botLogic
from sendMessage.sendMessage import send_message


def bot():
    # print("Testing Trend Detection...\n")

    # Fetch full historical market data
    fullData = getMarketData(symbols=['EURUSD'], exchange="OANDA", n_bars=100)

    if 'EURUSD' not in fullData or fullData['EURUSD'] is None:
        print("❌ No data returned for EURUSD. Skipping logic.")
        return

    df = fullData['EURUSD']

    if df.empty:
        print("❌ DataFrame is empty for EURUSD.")
        return

    # Send the full DataFrame to botLogic
    marketDataByPair = {"EURUSD": df}
    signal = botLogic(marketDataByPair)

    candle_time = df.index[-1]

    if signal:
        send_message(symbol=signal["symbol"], signal=signal["signal"], SL=signal["SL"])
        print(f"Time={candle_time}, Signal={signal['signal']}, SL={signal['SL']}")

