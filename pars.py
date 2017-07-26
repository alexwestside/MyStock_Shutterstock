# bin/user/python

from __future__ import print_function
import fileinput
import readline
import linecache
import re

####GlobalVar
ernings_type = None
data = None
_len = 0
id = 0
erns = 0
num = 0
##############

fp = "/Users/alex/PycharmProjects/untitled1/ernings_july_2017.txt"
fd = open(fp, mode='r')
len_lines = len(fd.readlines())
fd.close()
i = 0
with open(fp, mode='r') as f:
    line = f.readlines()
    for i in range(0, len_lines):
        if re.findall(r'[January|February|March|April|May|June|July|August|September|October|November|December]+\s[\d]+\,\s+[0-9]+', line[i]):
            data = line[i]
        if line[i].find('li role=\"presentation\" class=\"active\"') > 0:
            ernings_type = line[i+2].strip().split(' ')[0]
            _len = int(line[i+2].strip().split(' ')[1].strip('(').strip(')'))
        if re.findall(r'\$+[0-9]+\.+[0-9]+[0-9]', line[i]):
            id = line[i-1].split('<')[1].split('>')[1]
            erns = float(line[i].split('<')[1].split('$')[1])
            num = int(line[i+1].split('<')[1].split('>')[1])
            print(ernings_type, end=' ')
            print(id, end=' ')
            print(erns, end=' ')
            print(num, end='\n')

# &gt