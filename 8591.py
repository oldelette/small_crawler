import urllib.request as req
import bs4


url="https://www.8591.com.tw/orders-orderList.html"

request=req.Request(url,headers={
    "cookie":"PHPSESSID=b72effbaa4c974437d9493fa66e4537ecf7e0da8; _ga=GA1.3.1467406418.1590642649; is_support_webp=1; delHistory=1; history=%5B%7B%22gn%22%3A%22%E6%96%B0%E6%A5%93%E4%B9%8B%E8%B0%B7%22%2C%22gid%22%3A%22859%22%2C%22check%22%3A%22859--%22%2C%22sn%22%3A-1%2C%22sid%22%3A-1%2C%22tn%22%3A-1%2C%22tid%22%3A-1%7D%5D; recent_Records=%E6%96%B0%E6%A5%93%E4%B9%8B%E8%B0%B7%3A%3A859; mallList-game=1; _gid=GA1.3.1102242928.1591062411; login_name=m-0983736339; t=2ef2e06da809ca5ae288c72875777c8a; _gat=1; isOnlineware=1; abc=EgO2%2BLeAwTK0QNSHj835%2BQ458GnNcf5fnYM; _gat_UA-1901986-1=1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    })



with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

print(data)
