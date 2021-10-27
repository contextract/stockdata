import csv

with open('hongkong.csv', newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        code = row[0]
        name = row[1]
        if (row[2] == 'Equity'):
            print('{0},{1}'.format(code, name))

