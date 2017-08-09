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
import html_txt

#### GlobalVar ########################################################################################################
# MONTH = {'01':'January', '02':'February', '03':'March', '4':'April', '5':'May', '6':'June',
#          '07':'July', '8':'August', '9':'September', '10':'October', '11':'November', '12':'December'}
# WEEKDAY = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday',4:'Fraiday', 5:'Saturday', 6:'Sunday'}
ernings_type = None
date = None
id = 0
erns = 0
num = 0
#######################################################################################################################

file = "../html_txt/ernings_july_2017.txt"
fp = os.path.join(os.path.dirname(os.path.realpath('__file__')), file)
fd = open(fp)
len_lines = len(fd.readlines())
fd.close()
i = 0

##### Connect to DB ##################################
# mySQL_db = MySQLDatabase('db_mystock')
#
# class ernings(Model):
#     month = CharField
#     date = CharField
#     weekday = CharField
#     id = IntegerField
#     ernings = FloatField
#     downloads = IntegerField
#     ernings_type = CharField
#
# mySQL_db.connect()

with open(fp) as f:
    line = f.readlines()
    for i in range(0, len_lines):
        if line[i].find('li role=\"presentation\" class=\"active\"') > 0:
            date = line[i+1].split('=')[2].split('&')[0].split('-')
            date = date[2] + '/' + date[1] + '/' + date[0]
            ernings_type = line[i+2].strip().split(' ')[0]
        if re.findall(r'\$+[0-9]+\.+[0-9]+[0-9]', line[i]):
            id = line[i-1].split('<')[1].split('>')[1]
            erns = float(line[i].split('<')[1].split('$')[1])
            num = int(line[i+1].split('<')[1].split('>')[1])
            month = MONTH.get(date.split('/')[1])
            weekday = WEEKDAY.get(datetime.datetime(int(date.split('/')[2]), int(date.split('/')[1].split('0')[1]), int(date.split('/')[0])).weekday())

            # _ernings = ernings(month=month, date=date, weekday=weekday, id=id, ernings=erns, downloads=num, ernings_type=ernings_type)
            # _ernings.save()

            print(month, end=' ')
            print(date, end=' ')
            print(weekday, end=' ')
            print(id, end=' ')
            print(erns, end=' ')
            print(num, end=' ')
            print(ernings_type, end='\n')



