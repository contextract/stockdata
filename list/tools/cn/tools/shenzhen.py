import requests
import json
import csv

with open('shenzhen-src.csv', newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        code = row[0].strip()
        engName = row[1].strip()
        url = 'https://polling.finance.naver.com/api/realtime/worldstock/stock/%s.SZ' % (code)
        # print(url)
        r = requests.get(url, verify=False)
        data = json.loads(r.content)
        try:
            print("{0},{1}".format(code, data['datas'][0]['stockName']))
        except IndexError:
            print("{0},{1}".format(code, engName))
