# 我的LINEBOT 顯卡價格
一個方便我查詢顯卡價格的LINEBOT
## Build Process 
* 加入LINE好友
* ![](https://i.imgur.com/qJvS6Gu.png)
* 利用提供的關鍵字功能，輸入後可得到需要的資訊

![](https://i.imgur.com/LGNnhSQ.png)
* Github連結到Heroku，再由Heroku Server跟Line Developer做溝通

*當30分鐘以上沒使用Linebot，Heroku Server 會進入休眠模式，重啟時需要幾秒的等待時間

## Introduction 
顯卡不但能夠用在遊戲中呈現像是現實生活中的光影，還能用來做研究像是深度學習，甚至日以繼夜的挖礦之途，更不用說那發家致富的可能性，顯卡的珍貴已不用多提，人人都該至少有一張顯卡，如果能有兩張以上，那是多麼令人愉悅的一件事啊，所以時時刻刻了解顯卡的價格是必須的。以下為LINEBOT包含的功能:
1. 查詢2021顯卡的排行榜
2. 查詢顯卡價格
3. 商場連結直接下單
4. 連接到AMD網站，查看最新消息
5. 顯卡介紹


## Details of the approach
* pseudoCode

        connect to http
   
        app.run()
        
        listen the post request from callback's
        
        get input message from user
        if message == 關鍵字
            output all of key words to let user know
        else if message == 設定的關鍵字
            return the information which user need
        else
            return 很抱歉，沒有收尋到所你輸入。\n請善用關鍵字功能，尋找到你需要的資訊
* flow chart
![](https://i.imgur.com/C5qNEC8.png)

## Results 
原始畫面:
> <img src="https://i.imgur.com/8sIW7jW.jpg" width="300" height="600">
點擊下方選單:
>點擊右下的關鍵字那張圖，會出現的所有關鍵字
>> <img src="https://i.imgur.com/jQ1fNCR.jpg" width="300" height="600">
>> <img src="https://i.imgur.com/a8HGJ7i.jpg" width="300" height="600">
>> <img src="https://i.imgur.com/uf9yv05.jpg" width="300" height="600">
>點擊中下選單的最新消息，會出現蘇媽發布會的影片:
>> <img src="https://i.imgur.com/RM7TzeJ.jpg" width="300" height="600">
>點擊左下選單的買顯卡，會出現商場，點擊相對的商場會連結到該網站:
>> <img src="https://i.imgur.com/6QTCdiA.jpg" width="300" height="600">
>> <img src="https://i.imgur.com/oKui4yy.jpg" width="300" height="600">
>點擊選單的2021顯卡天梯，則會連結到顯卡天梯圖的網站:
>> <img src="https://i.imgur.com/ig6OSNt.jpg" width="300" height="600">


## References
* 參考網址
    * https://marketingliveincode.com/?page_id=2532
* API
    *LINEBOT
    *
