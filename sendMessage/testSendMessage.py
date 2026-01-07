import requests
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()
# === Configuration ===


BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'


def send_message(Message) -> None:

    # message_data = f"Pair: {symbol}\nSide: {signal}\nSL: {SL}"

    payload = {
        'chat_id': CHAT_ID,
        'text': Message,
        'disable_notification': False
    }

    try:
        response = requests.post(API_URL, data=payload)
        response.raise_for_status()  # Raise exception for HTTP errors
        result = response.json()

        if result.get("ok"):
            print("✅ Message sent:", result["result"]["text"])
        else:
            print("⚠️ Telegram API error:", result)
    except requests.exceptions.RequestException as error:
        print("❌ Error sending message:", error)


# send_message("Test Message")