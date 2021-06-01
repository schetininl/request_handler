import os
import json
from flask import Flask, request
import telebot

app = Flask(__name__)


@app.route('/')
def hello_world():
    request_info = dict(
        url=str(request.url),
        headers=dict(request.headers),
        args=dict(request.args),
        data=dict(request.data)
    )
    bot = telebot.TeleBot(app.config['BOT_TOKEN'])
    bot.send_message(app.config['CHAT_ID'], json.dumps(request_info, indent=4))
    return 'OK'


if __name__ == '__main__':
    app.config['BOT_TOKEN'] = os.getenv("BOT_TOKEN")
    app.config['CHAT_ID'] = os.getenv("CHAT_ID")
    port = int(os.getenv('PORT', '8000'))

    app.run(debug=True, port=port)
