from flask import Flask, request, jsonify
import threading
from bot import bot
import os
import sys
import logging

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/runBot', methods=['GET'])
def runBot():
    try:
        # Run bot in a separate thread → async background job
        threading.Thread(target=bot).start()
        
        # Respond immediately
        return jsonify({"status": "ok", "message": "✅ Bot started in background"}), 200

    except Exception as e:
        print("❌ Bot error:", e)
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/coldStart', methods=['GET'])
def coldStart():
    try:
        logging.info("cooled Started")
        sys.stdout.flush()
        return "🌡️ Cold Started"
    
    except Exception as e:
        print(e)
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
