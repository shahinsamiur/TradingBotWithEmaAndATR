import time
from getMarketData.getMarketDataFile import getMarketData
from businesslogic.logic import botLogic
from sendMessage.sendMessage import send_message
from sendMessage.errorInformMessageSend import send_error_message

last_signal_time = {}

def bot():
    try:
        symbols = ['EURUSD']

        fullData = getMarketData(symbols=symbols, exchange="OANDA", n_bars=100)

        for idx, symbol in enumerate(symbols):
            try:
                if symbol not in fullData or fullData[symbol] is None:
                    print(f"❌ No data returned for {symbol}. Skipping.")
                    continue

                df = fullData[symbol]

                if df is None or df.empty:
                    print(f"❌ DataFrame is empty for {symbol}. Skipping.")
                    continue

                marketDataByPair = {symbol: df}
                signal, candle_time = botLogic(marketDataByPair, symbol=symbol)

                # Only send signal once per candle
                if signal:
                    if symbol not in last_signal_time or last_signal_time[symbol] != candle_time:
                        send_message(symbol=signal["symbol"], signal=signal["signal"], SL=signal["SL"])
                        last_signal_time[symbol] = candle_time
                        print(f"✅ {symbol} | Time={candle_time}, Signal={signal['signal']}, SL={signal['SL']}")
                    else:
                        print(f"ℹ️ {symbol} | Signal already sent for candle {candle_time}")
                else:
                    print(f"ℹ️ {symbol} | No signal for candle {candle_time}")

                # Sleep only between symbols
                if idx < len(symbols) - 1:
                    time.sleep(5)

            except Exception as e:
                error_message = f"⚠️ Error while processing {symbol}: {str(e)}"
                print(error_message)
                send_error_message(error_message)
                
    except Exception as e:
        error_message = f"❌ Fatal error in bot(): {str(e)}"
        print(error_message)
        send_error_message(error_message)

# Run the bot
# bot()
