from flask import Flask, request, jsonify
import threading
from bot import bot
import os
import sys
import logging
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/runBot', methods=['GET'])
def runBot():
    try:

        threading.Thread(target=bot).start()
        print(" Bot started in background")

        return jsonify({"status": "ok", "message": " Bot started in background"}), 200

    except Exception as e:
        print(" Bot error:", e)
        return jsonify({"status": "error", "message": str(e)}), 500


def trigger_backend():

    try:
        backend_url = "https://trading-bot-with-ema-and-atr-p57o.vercel.app/"
        print("⚙️ Sending request to backend server...")
        response = requests.get(backend_url)
        if response.status_code == 200:
            print(" Backend cold start successful")
        else:
            print(f" Backend responded with {response.status_code}")
    except Exception as e:
        logging.error(f" Backend call failed: {e}")
    finally:
        sys.stdout.flush()


@app.route('/coldStart', methods=['GET'])
def coldStart():
    try:
        logging.info(" Lambda cold start triggered")
        sys.stdout.flush()

  
        threading.Thread(target=trigger_backend).start() 
        return jsonify({"status": "ok", "message": " Cold start accepted"}), 200

    except Exception as e:
        logging.error(f" Cold start error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
