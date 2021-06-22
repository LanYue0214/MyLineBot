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

##line_bot_api.push_message('U79595215c0522df0d60e603f9bbd925a', TextSendMessage(text='今天有錢買顯哪了嗎? 今天顯卡價格跌了嗎?'))

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
    elif re.match('關鍵字',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='目前有以下關鍵字\n【關鍵字】所有的關鍵字\n【商場】購買管道在這裡!!\n【介紹】顯卡是啥?能吃嗎?\n【最新消息】蘇媽今天發布了甚麼?\n【天梯圖】2021年度最新顯卡天梯圖\n----開發中，請稍後----'))
    elif re.match('蘇媽今天發布了什麼'or'最新消息',message):
        #video_message = VideoSendMessage(
        #    original_content_url='https://i.imgur.com/9L1opKw.mp4',
        #    preview_image_url='https://i.imgur.com/yebDeyq.png'
        #)
        #line_bot_api.reply_message(event.reply_token, video_message)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='https://youtu.be/xtrhHH0kQI0'))
    elif re.match('test',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='很抱歉，沒有收尋到所你輸入。\n請善用關鍵字功能，尋找到你需要的資訊:)'))

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) #0.0.0.0 all people could connect to this robot