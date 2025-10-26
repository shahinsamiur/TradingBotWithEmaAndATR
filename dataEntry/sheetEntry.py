import requests
API_URL = f'https://trading-bot-with-ema-and-atr-p57o.vercel.app/webhook'
localHost=f'http://192.168.68.114:4000/webhook'
def sheetEntryFunction(message):
    payload = {
        "message": message
    }
    print(payload)
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status() 
        result = response.json()

        if result.get("ok"):
            print("data Entred")
        else:
            print(" Telegram API error:", result)
    except requests.exceptions.RequestException as error:
        print(" Error sending message:", error)