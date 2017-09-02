
from __future__ import print_function
import re
import csv
from html.parser import HTMLParser
import json

with open('sets.txt', 'r') as f:
    # fp = open('august.csv', 'w')
    # out = csv.writer(fp, delimiter=',', quoting=csv.QUOTE_ALL)
    # f = f.readlines()
    line = f.read()
    line = line[line.index('catalog-store'):]
    line = line[:line.index('</script>')]
    line = line.split('   ')[1]
    # s = json.dumps(line)
    s = json.loads(line)
    df = s['sets']
    for item in df:
        print(item['name'], end='')
        print((item['cover_item'])['item_id'], end='')
        print()


    print(f)