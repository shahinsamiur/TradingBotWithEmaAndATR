from indicatios.ema import ema
from indicatios.atr import atr_stoploss
from getMarketData.getMarketDataFile import getMarketData
from businesslogic.logic import botLogic
from sendMessage.sendMessage import send_message


def bot():
    print("🚀 Testing Trend Detection...\n")

    # Fetch full historical market data
    fullData = getMarketData(symbols=['BTCUSDT'], exchange="BINANCE", n_bars=4500)
    print(fullData)
    # Check if data exists
    if 'BTCUSDT' not in fullData or fullData['BTCUSDT'] is None:
        return

    df = fullData['BTCUSDT']

    # Check if DataFrame is valid
    if df is None or df.empty:
        return

    # Ensure enough data exists for the loop
    if len(df) < 4000:
        print(f"❌ Not enough data: only {len(df)} rows, need at least 4000.")
        return

    # Loop from index 4000 down to 3500 (simulate sliding window of 500 bars)
    for i in range(len(df), 3499, -1):
        window = df[i-500:i]

        marketDataByPair = {"BTCUSDT": window}
        # print(marketDataByPair)
        # Skip if window is empty or malformed
        if window.empty or len(window) < 500:
            print(f"⚠️ Skipping i={i}, not enough candles in window.")
            continue

        marketDataByPair = {"BTCUSDT": window}
        signal = botLogic(marketDataByPair)

        # Get candle time
        candle_time = window.index[-1] if not window.empty else "N/A"

        if signal is not None:
            # send_message(symbol=signal["symbol"], signal=signal["signal"], SL=signal["SL"])
            print(f"✅ Time={candle_time}, i={i}, Signal={signal['signal']} , SL={signal['SL']}")
        else:
            continue

bot()
