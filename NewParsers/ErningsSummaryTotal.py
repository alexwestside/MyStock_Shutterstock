from __future__ import print_function
from datetime import date, datetime, timedelta
import requests
import csv
import re
import pandas as pd
import threading

cookies = {"__ssid": "9606bc02-747b-42ef-b851-4e738e7fd1de", "_photo_session_id": "68214e1d41c4266955645373481a5a42",
           "_ym_uid": "1494857922560381083", "accts_contributor": "MyStocks", "accts_customer": "yanushkov",
           "ajs_anonymous_id": "%226ae010e6-859b-484c-b5d9-6221581e51cf%22", "ajs_group_id": "null",
           "ajs_user_id": "null", "did": "a9b91f2e-f3b6-4532-b41e-b34bd7cb67e7",
           "IRF_3": "%7Bvisits%3A14%2Cuser%3A%7Btime%3A1494857922704%2Cref%3A%22direct%22%2Cpv%3A39%2Ccap%3A%7B%7D%2Cv%3A%7B%7D%7D%2Cvisit%3A%7Btime%3A1504427803093%2Cref%3A%22https%3A%2F%2Fsubmit.shutterstock.com%2Fearnings%2Fdaily%3Fpage%3D3%26date%3D2017-08-01%26language%3Den%26category%3D25_a_day%26sort%3Ddesc%26sorted_by%3Dcount%26per_page%3D20%22%2Cpv%3A12%2Ccap%3A%7B47%3A1%7D%2Cv%3A%7B1225%3A%22IR_AN_64%22%7D%7D%2Clp%3A%22https%3A%2F%2Fwww.shutterstock.com%2Fru%2Fimage-vector%2Fhand-drawn-botanical-art-isolated-on-687437659%22%2Cdebug%3A0%2Ca%3A1504430191128%2Cd%3A%22shutterstock.com%22%7D",
           "IRMS_la1305": "1504427803784", "language": "en", "locale": "ru",
           "optimizelyEndUserId": "oeu1498041993482r0.3441372721886864", "optly.pgStore.s.0": "{}",
           "psst": "115:466,158:572,218:872,332:1160,377:1334,454:1558,530:1787,542:1853,551:1874",
           "visit_id": "15831945931", "visitor_id": "11011468609",
           "__utma": "265213581.1507426815.1494857922.1504638242.1505153117.27", "__utmc": "265213581",
           "__utmz": "265213581.1494857970.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)", "__uvt": "",
           "_ga": "GA1.3.1507426815.1494857922", "uvts": "6DIK18ZF738WyVeK",
           "sbsid": "a8c044ff1ba8114f12f39f2a6024decb",
           "session": "s%3APOPXQWqr-nYusEExnUPhmPTJ4q76UUXl.iKOHDwAqW8hCq%2FrmqKYBSW8tXwW0Mz45RwTQPe2XW1o", }

YEARS = ["2016", "2017"]
MONTHS = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
          '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}

AYS = {"01": "31", "02": "30", "03": "31", "04": "31", "05": "31", "06": "31", "07": "31", "08": "31", "09": "31",
       "10": "31", "11": "31", "12": "31"}

CATEGORYS = ['25_a_day', 'on_demand', 'enhanced', 'single_image_and_other']

urlOrigin = "https://submit.shutterstock.com/earnings/details?page=1&language=en&category=25_a_day&sort=desc&sorted_by=count&per_page=20"

urlBase = "https://submit.shutterstock.com/earnings/details?page="
page = "1"
urlCategory = "&language=en&category="
category = "25_a_day"
urlAppend = "&sort=desc&sorted_by=count&per_page=20"

URLS = []


# 2017-09-01

def getData(url):
    DF = []
    # print(url)
    try:
        response = requests.get(url, cookies=cookies)
        dataFrame = response.text.split("\n")
    except ConnectionRefusedError:
        print("ERRRRR")
    odd = True
    for i, line in enumerate(dataFrame):
        if re.findall(r'<td>\d+</td>', line):
            res = re.findall(r'\d+', line)[0]
            if odd:
                ID = str(res)
                odd = False
                DF.append(ID)
            else:
                Downloads = str(res)
                odd = True
                DF.append(Downloads)
                Uploaded = str(dataFrame[i+2]).strip()
                DF.append(Uploaded)
                print(DF)
                DF = []
        if re.findall(r'<td>[$]\d+.\d+</td>', line):
            # ?????????????????????????????????
            Earnings = str(re.findall(r'\d+', line)[0])
            # ?????????????????????????????????
            DF.append(Earnings)
        # if re.findall(r'\d+\/\d+\/\d+', line):
        #     Uploaded = str(line)
        #     DF.append(Uploaded)

for category in CATEGORYS:
    page = 1
    max = 0
    URL = urlBase + str(page) + urlCategory + category + urlAppend
    response = requests.get(URL, cookies=cookies)
    dataFrame = response.text.split("\n")
    for line in dataFrame:
        if "max=" in line:
            # print(line)
            if max == 0:
                max = int(re.findall(r'\d+', line)[0])
                break
    while page <= max:
        URL = urlBase + str(page) + urlCategory + category + urlAppend
        URLS.append(URL)
        page += 1
# for url in URLS:
#     getData(url)


threads = [threading.Thread(target=getData, args=[url]) for url in URLS]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# https://submit.shutterstock.com/earnings/details?page=1&language=en&category=25_a_day&sort=desc&sorted_by=count&per_page=20
