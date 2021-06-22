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

line_bot_api.push_message('U79595215c0522df0d60e603f9bbd925a', TextSendMessage(text='今天有錢買顯哪了嗎? 今天顯卡價格跌了嗎?'))

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

#deal with message
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
    elif re.match('蘇媽今天發布了什麼',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='https://youtu.be/xtrhHH0kQI0'))
    elif re.match('最新消息',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='AMD官網。\n'+'https://www.amd.com/zh-hant'))
    elif re.match('介紹',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='前言：\n顯卡不但能夠用在遊戲中呈現像是現實生活中的光影，還能用來做研究像是深度學習，甚至日以繼夜的挖礦之途，更不用說那發家致富的可能性，顯卡的珍貴已不用多提，人人都該至少有一張顯卡，如果能有兩張以上，那是多麼令人愉悅的一件事啊，所以時時刻刻了解顯卡的價格是必須的。\n\n主要：\n顯示卡在電腦中負責了大部分的圖形運算，GPU是他最主要的核心運算。'))
    elif re.match('test',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='很抱歉，沒有收尋到所你輸入。\n請善用關鍵字功能，尋找到你需要的資訊:)'))

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) #0.0.0.0 all people could connect to this robot