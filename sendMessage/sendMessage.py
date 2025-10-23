import requests
from dataEntry.sheetEntry import sheetEntryFunction 
# === Configuration ===
BOT_TOKEN = '8100528566:AAG1B8WC_BgD2yN3t7U8NFeuMJDvcLp4mak'
CHAT_ID = '5834307479'
API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'


def send_message(symbol: str, signal: str, SL: float , entry: float) -> None:

    message_data = f"Pair: {symbol} \nSide: {signal} \nSL: {SL} \nEntry: {entry} "

    payload = {
        'chat_id': CHAT_ID,
        'text': message_data,
        'disable_notification': False
    }

    try:
        response = requests.post(API_URL, data=payload)
        response.raise_for_status() 
        result = response.json()
        sheetEntryFunction(message_data)
        if result.get("ok"):
            print("✅ Message sent:", result["result"]["text"])
        else:
            print("⚠️ Telegram API error:", result)
    except requests.exceptions.RequestException as error:
        print("❌ Error sending message:", error)

# payload='Pair: EURUSD Side: sell_signal SL: 1.160831512763423 Entry: 1.15996'
# sheetEntryFunction(payload)