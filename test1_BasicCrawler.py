import urllib.request as req
#抓取 C_Chat版 的網頁原始碼
url="https://www.ptt.cc/bbs/C_Chat/index.html"
#建立一個request物件 附加 Request Headers 資訊
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

#解析HTML資料
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
#取得標題
titles=root.find_all("div", class_="title")
for title in titles:
    if title.a !=None:
        print(title.a.string)