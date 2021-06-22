# 我的LINEBOT 顯卡價格
一個方便我查詢顯卡價格的LINEBOT
## Build Process 
* 加入LINE好友
* ![](https://i.imgur.com/qJvS6Gu.png)

## Introduction 
顯卡不但能夠用在遊戲中呈現像是現實生活中的光影，還能用來做研究像是深度學習，甚至日以繼夜的挖礦之途，更不用說那發家致富的可能性，顯卡的珍貴已不用多提，人人都該至少有一張顯卡，如果能有兩張以上，那是多麼令人愉悅的一件事啊，所以時時刻刻了解顯卡的價格是必須的。以下為LINEBOT包含的功能:
1. 查詢2021顯卡的排行榜
2. 查詢顯卡價格
3. 商場連結直接下單
## Methods 



## Code
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

## Results 
<img src="https://i.imgur.com/8sIW7jW.jpg" width="300" height="600">
<img src="https://i.imgur.com/a8HGJ7i.jpg" width="300" height="600">
<img src="https://i.imgur.com/uf9yv05.jpg" width="300" height="600">
<img src="https://i.imgur.com/jQ1fNCR.jpg" width="300" height="600">
<img src="https://i.imgur.com/RM7TzeJ.jpg" width="300" height="600">
## References
* 參考網址
    * https://marketingliveincode.com/?page_id=2532

