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
    bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
    bot.send_message(os.getenv("CHAT_ID"), json.dumps(request_info, indent=4))
    return 'OK'


if __name__ == '__main__':
    print(os.getenv("BOT_TOKEN"))
    print(os.getenv("CHAT_ID"))
    port = int(os.getenv('PORT', '5000'))

    app.run(threaded=True, port=port)
