# 我的LINE BOT 顯卡價格
一個方便我差看顯卡的LINE BOT

*加入好友

![](https://i.imgur.com/qJvS6Gu.png)



#Code
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

line_bot_api = LineBotApi('你自己的token')
handler = WebhookHandler('你自己的secret')

line_bot_api.push_message('你自己的ID', TextSendMessage(text='今天有錢買顯哪了嗎? 今天顯卡價格跌了嗎?'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    
    signature = request.headers['X-Line-Signature'] # get X-Line-Signature header value

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
    if re.match('商場',message):
            buttons_template_message = TemplateSendMessage(
            alt_text='顯卡好貴，沒錢QQ',#cannot be see
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/siRPgJZ.jpg',
                title='顯卡買起來啦',
                text='GTX3090值得你擁有',
                actions=[
                    URIAction(
                        label='原價屋',
                        uri='https://www.coolpc.com.tw/tw/product-category/gpu/'
                    ),
                    URIAction(
                        label='Pchome',
                        uri='https://24h.pchome.com.tw/region/DRAD'
                    ),
                    URIAction(
                        label='蝦皮',
                        uri='https://shopee.tw/search?keyword=%E9%A1%AF%E7%A4%BA%E5%8D%A1'
                    )
                ]
            )
        )
            line_bot_api.reply_message(event.reply_token, buttons_template_message)
    elif re.match('Pchome',message):
        try:
            re_message = ImageSendMessage(
                original_content_url="https://i.imgur.com/b2rFB7q.png",
                preview_image_url="https://i.imgur.com/b2rFB7q.png"
            )
            line_bot_api.reply_message(event.reply_token,re_message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('Error!'))
    elif message == '蝦皮':
        re_message = TextSendMessage(
            text = "我是蝦皮啦!"
        )
        line_bot_api.reply_message(event.reply_token,re_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) #0.0.0.0 all people could connect to this robot


#References
*參考網址
