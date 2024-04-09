import requests
import json
import csv

with open('shanghai-src.csv', newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        code = row[0].strip()
        engName = row[4].strip()
        url = 'https://mweb-api.stockplus.com/api/securities/SHANGHAI-%s.json' % (code)
        r = requests.get(url, verify=False)
        data = json.loads(r.content)
        try:
            print("{0},{1}".format(code, data['recentSecurity']['name']))
        except (KeyError, TypeError):
            print("{0},{1}".format(code, engName))

