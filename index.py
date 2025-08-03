from flask import Flask, request, jsonify, g
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
        bot()
        return "✅ Bot executed successfully"
    except Exception as e:
        print("❌ Bot error:", e)
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/coldStart', methods=['GET'])
def coldStart():
    try:
        logging.info("cooled Stared")
        sys.stdout.flush()
        return "🌡️ Cold Started"
    
    except Exception as e:
        print(e)
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
