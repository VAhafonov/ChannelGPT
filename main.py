from flask import Flask, render_template, jsonify, request
import json, os
from telegram_bot import TelegramBot

app = Flask(__name__)
bot = TelegramBot()

def detect_replit():
    try:
        owner = os.environ["REPL_OWNER"]
        return True
    except:
        return False

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        try:
            data = request.get_json()
            text = data["text"]
            bot.send_post(text)
            data = {"success": True}
        except:
            data = {"success": False}
    else:
        data = {"success": False}
    return jsonify(data)

@app.route('/create', methods=['GET'])
def create():
    data = {'text': bot.create_post()}
    return jsonify(data)

if __name__ == '__main__':
    if detect_replit():
        print(f"Hello, {os.environ['REPL_OWNER']}! Your bot is running.")
        app.run(host='0.0.0.0', port=8080, debug=False)
    else:
        app.run(port=8080, debug=False)
