#載入LineBot所需要的套件
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('X3H4BMqZpxzTXNbw3XqHHMafRhJhfNnbDznETttFRI19E0N0+7fQ49iR0Jm5iqe2+ruN3xUZiR0bocnX8cFarteBUiKkMmqjWx18yX8WXqP346ozNlnooKXwcuerErUThYzeWxbknd9RdY1MZLRdjgdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('7ebb16631a483de7a45a7256de39310b')

line_bot_api.push_message('U79595215c0522df0d60e603f9bbd925a', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    if re.match('原價屋',message):
        try:
            re_message = ImageSendMessage(
                #base_url="https://i.imgur.com/J90bQis.jpg",
                #base_size=BaseSize(height=1040, width=1040)
                original_content_url="https://i.imgur.com/J90bQis.jpg",
                preview_image_url="https://i.imgur.com/J90bQis.jpg"
            )
            line_bot_api.reply_message(event.reply_token,re_message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('Error!'))
    elif re.match('@Pchome',message):
        try:
            re_message = ImageSendMessage(
                base_url="https://i.imgur.com/b2rFB7q.png",
                base_size=BaseSize(height=1040, width=1040)
            )
            line_bot_api.reply_message(event.reply_token,re_message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('Error!'))
    elif message == '@蝦皮':
        re_message = TextSendMessage(
            text = "我是蝦皮啦!"
        )
        line_bot_api.reply_message(event.reply_token,re_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) #0.0.0.0 all people could connect to this robot