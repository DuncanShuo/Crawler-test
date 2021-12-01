import urllib.request as req
#抓取 KKday桃園 的網頁原始碼
url="https://www.kkday.com/zh-tw/product/ajax_get_top_products?areaCode=A01-001-00008&upLimit=10&showLmit=10&csrf_token_name=cee94caceaac73b8e5c6e5b1cb9fc95d"
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

#解析JSON資料
import json
data=json.loads(data)
#取得JSON資料標題
posts=data["data"]
for key in range(10):
    post=posts[key]
    print(post["name"])