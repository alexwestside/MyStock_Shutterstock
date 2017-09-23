from __future__ import print_function
from datetime import date, datetime, timedelta
import requests
import csv
import re
import pandas as pd

urlOrigin = "https://submit.shutterstock.com/earnings/daily?page=1&date=2017-09-01&language=en&category=25_a_day&sort=desc&sorted_by=count&per_page=20"

urlsBase = "https://submit.shutterstock.com/earnings/daily?page="
page = 1
urlDate = "&date="
_date = "2017-09-01"
urlCategory = "&language=en&category="
category = "25_a_day"
urlAppend = "&sort=desc&sorted_by=count&per_page=20"

url = urlsBase + str(page) + urlDate + _date + urlCategory + category + urlAppend

#### GlobalVar ########################################################################################################
MONTH = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
         '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
WEEKDAY = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Fraiday', 5: 'Saturday', 6: 'Sunday'}
ERNINGS_TYPE = ['Subscription', 'Enhanced', 'On demand', 'Videos', 'Single & other']
YEAR = ["2016", "2017"]
DAYS = {"01": "31", "02": "30", "03": "31", "04": "31", "05": "31", "06": "31", "07": "31", "08": "31", "09": "31", "10": "31", "11": "31", "12": "31"}

ernings_type = None
date = None
id = 0
erns = 0
num = 0
#######################################################################################################################


