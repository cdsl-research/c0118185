import urequests
import ujson
import timer

count = 0
while count < 100:
    #送信先のURLの指定
    url = 'http://192.168.100.181/test.php'
    
    a = timer.get_time()
    #データをDICT型で宣言
    powerdata = {
        "value" : a,
        "text" : "Hello World!"
    }
    
    #jsonデータで送信するという事を明示的に宣言
    header = {
        'Content-Type' : 'application/json'
    }
    
    #HTTPリクエストをPOSTとして送信
    res = urequests.post(
        url,
        data = ujson.dumps(powerdata).encode("utf-8"),
        headers = header
    )
    
    #サーバ側からのレスポンスを受け取って表示(jsonのデコードも一緒にしている)
    print (res.json())
    
    #終了
    res.close()
    count += 1