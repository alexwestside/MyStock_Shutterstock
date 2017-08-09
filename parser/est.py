


from __future__ import print_function
import fileinput
import readline
import re
import datetime
from var import *

url = 'https://submit.shutterstock.com/earnings/details?page=1&language=en&category=25_a_day&sort=desc&sorted_by=count&per_page=20'

test1 = 'https://submit.shutterstock.com/earnings/details?page=1&language=en&category=25_a_day&sort=desc&sorted_by=count&per_page=20'
test2 = 'https://submit.shutterstock.com/earnings/details?page=1&language=en&category=25_a_day&sort=desc&sorted_by=count&per_page=20'


type = None
ernings_type = None
curr_page = 0
caunt_page = 0
id = None
link = None

with open('../html_txt/test1.txt', mode='r') as file:
    line = file.readlines()
    for i in range(len(line)):
        if line[i].find('li role=\"presentation\" class=\"active\"') > 0:
            ernings_type = line[i+2].strip().split(' ')[0]
        if line[i].find('src=\"//image.shutterstock.com') > 0:
            link = line[i]
            id = link.strip().split('/')[6].split('.')[0]
            i+=1
        if line[i].find(str(id)) > 0:
            totalErningById = re.findall(r'\d+\.+\d+', line[i + 1])[0]
            totalDownloadsById = re.findall(r'\d+', line[i + 2])[0]
            dateUploadedById = line[i + 4].strip().split('/')
            month = MONTH.get(dateUploadedById[0])
            weekday = WEEKDAY.get(datetime.datetime(int(dateUploadedById[2]), int(dateUploadedById[0]), int(dateUploadedById[1])).weekday())
            dateUploadedById = dateUploadedById[1] + '/' + dateUploadedById[0] + '/' + dateUploadedById[2]

            print(month, end=' ')
            print(dateUploadedById, end=' ')
            print(weekday, end=' ')
            print(id, end=' ')
            print(totalErningById, end=' ')
            print(totalDownloadsById, end=' ')
            print(ernings_type, end='\n')



