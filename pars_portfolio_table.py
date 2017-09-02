
import re

with open('pars_portfolio_table.txt', 'r') as f:
    line = f.readlines()
    for l in line:
        l = l.strip().split('. ')[1]
        l = re.split('(\d+)', l)
        print (l[1])
