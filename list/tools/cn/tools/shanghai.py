import requests
import json
import csv

with open('shanghai-src.csv', newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        code = row[0].strip()
        r = requests.get("https://asp.edaily.co.kr/shb/shinhaninvest//module/json_check.php?exid=16&symbol=" + code, verify=False)
        data = json.loads(r.content)
        print("{0},{1}".format(code, data['hname']))
