from flask import Flask, render_template, jsonify, request
import json
from telegram_bot import TelegramBot

app = Flask(__name__)
bot = TelegramBot()

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
    app.run(host='0.0.0.0', port=8080)
