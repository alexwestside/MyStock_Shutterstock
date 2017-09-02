#!/bin/user/python

from __future__ import print_function
import fileinput
import readline
import linecache
import re
import datetime
import os
from peewee import *
from var import *
import csv


#### GlobalVar ########################################################################################################
MONTH = {'01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June',
         '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}
WEEKDAY = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday',4:'Fraiday', 5:'Saturday', 6:'Sunday'}
ERNINGS_TYPE = ['Subscription', 'Enhanced', 'On demand', 'Videos', 'Single & other']
ernings_type = None
date = None
id = 0
erns = 0
num = 0
#######################################################################################################################

file = "../html_txt/html.txt"
fp = os.path.join(os.path.dirname(os.path.realpath('__file__')), file)
fd = open(fp)
len_lines = len(fd.readlines())
fd.close()
i = 0

with open(fp) as f:
    lst = []
    # fp = open('august.csv', 'w')
    fp = open('august.csv', 'w')
    out = csv.writer(fp, delimiter=',', quoting=csv.QUOTE_ALL)
    line = f.readlines()
    for i in range(0, len_lines):
        if line[i].find('li role=\"presentation\" class=\"active\"') > 0:
            date = line[i+1].split('=')[2].split('&')[0].split('-')
            date = date[1] + '/' + date[2] + '/' + date[0]
            for et in ERNINGS_TYPE:
                if et in line[i+2]:
                    ernings_type = et
        if re.findall(r'\$+[0-9]+\.+[0-9]+[0-9]', line[i]):
            id = line[i-1].split('<')[1].split('>')[1]
            erns = float(line[i].split('<')[1].split('$')[1])
            num = int(line[i+1].split('<')[1].split('>')[1])
            month = MONTH.get(date.split('/')[0])
            dateList = date.split('/')


            weekday = WEEKDAY.get(datetime.datetime(int(dateList[2]), int(dateList[0].split('0')[1]), int(dateList[1])).weekday())
            # weekday = WEEKDAY.get(datetime.datetime(int(date.split('/')[2]), int(date.split('/')[0]), int(date.split('/')[1].split('0')[1])).weekday())

            lst.append(month)
            lst.append(date)
            lst.append(weekday)
            lst.append(id)
            lst.append(erns)
            lst.append(num)
            lst.append(ernings_type)
            out.writerow(lst)
            lst = []

            print(month, end=' ')
            print(date, end=' ')
            print(weekday, end=' ')
            print(id, end=' ')
            print(erns, end=' ')
            print(num, end=' ')
            print(ernings_type, end='\n')
    fp.close()



