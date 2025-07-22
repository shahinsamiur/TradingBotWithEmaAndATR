from flask import Flask, request, jsonify, g
from bot import bot

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://neondb_owner:npg_yuFa31xvZgfU@ep-shy-pine-a8d70zrz-pooler.eastus2.azure.neon.tech/neondb?sslmode=require'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
        return "🌡️ Cold Started"
    except Exception as e:
        print(e)
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
