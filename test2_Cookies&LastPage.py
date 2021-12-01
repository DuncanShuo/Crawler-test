import urllib.request as req
#為了重複執行 建立function
def getData(url):
    #附加 Request Headers & Cookies 資訊
    request=req.Request(url,headers={
        "cookie":"over18=1",
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
    #取得上頁網址
    nextLinlk=root.find("a", string="‹ 上頁")
    return nextLinlk["href"]

#抓取 Gossiping版 的網頁原始碼
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<5:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
    print(count)

getData(pageURL)