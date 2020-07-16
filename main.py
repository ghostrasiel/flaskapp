from flask import Flask, request, abort
from linebot import ( LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)
app = Flask(__name__)
line_bot_api = LineBotApi('K6amaYqMI/DaMOJn7TRifGTsGybXxf2prf9jjLgAIC2hmPEV+k936CKue0tpZV1m3EWEKgV0mpV7zoA9CzwcREyujiqWzoj/QDqFhgonjI4Gtgj1ZkZQ4DShjIx9wsMYh7hf04ifKAokDahl5aktrQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('96d19ee3824377a76b1533dec7a9d75c')
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        # print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()