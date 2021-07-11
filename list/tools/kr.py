import csv
import io
import sys

if len(sys.argv) < 3:
    print('Usage: %s [stock source] [previous data]' % sys.argv[0])
    sys.exit()

corp = {}

with open(sys.argv[2], 'r', encoding='utf-8') as src:
    reader = csv.reader(src)
    for row in reader:
        corp[row[0]] = row[3];

with open(sys.argv[1], 'r', encoding='cp949') as src:
    reader = csv.reader(src)
    for row in reader:
        co = '---------'
        if row[1] in corp:
            co = corp[row[1]]
        print('%s,%s,%s,%s' % (row[1], row[3], row[0], co))
