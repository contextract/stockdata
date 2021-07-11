import requests
import json

for market in [ "NYSE", "NASDAQ", "AMEX" ]:
    page = 1
    while 1:
        url = "https://api.stock.naver.com/stock/exchange/%s/marketValue?page=%d&pageSize=60" % (market, page)
        response = requests.get(url)
        data = json.loads(response.text)
        if len(data["stocks"]) <= 0:
            break
        page = page + 1
        for stock in data["stocks"]:
            print(stock["reutersCode"] + "," + stock["symbolCode"].replace(' PR ', '$').replace(' PR', '$').replace(' U', '.U').replace(' RT', '.R').replace(' WI', 'V'))
