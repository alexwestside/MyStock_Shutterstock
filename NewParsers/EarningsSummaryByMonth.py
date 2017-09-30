from __future__ import print_function
from datetime import date, datetime, timedelta
import requests
import csv
import re
import pandas as pd
import threading
import time
import datetime
import collections
import os

COOKIES = {"__ssid": "9606bc02-747b-42ef-b851-4e738e7fd1de", "_photo_session_id": "68214e1d41c4266955645373481a5a42",
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

urlOrigin = "https://submit.shutterstock.com/earnings/daily?page=1&date=2017-09-01&language=en&category=25_a_day&sort=desc&sorted_by=count&per_page=20"

URLBASE = "https://submit.shutterstock.com/earnings/daily?page="
PAGE = 1
URLDATE = "&date="
DATE = "2017-09-01"
URLCATEGORY = "&language=en&category="
CATEGORY = "25_a_day"
URLAPPEND = "&sort=desc&sorted_by=count&per_page=20"

#### GlobalVar ########################################################################################################
MONTHS = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
          '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
WEEKDAY = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Fraiday', 5: 'Saturday', 6: 'Sunday'}
ERNINGS_TYPE = ['Subscription', 'Enhanced', 'On demand', 'Videos', 'Single & other']
YEARS = ["2016", "2017"]
DAYS = {"01": "31", "02": "30", "03": "31", "04": "31", "05": "31", "06": "31", "07": "31", "08": "31", "09": "31",
        "10": "31", "11": "31", "12": "31"}
CATEGORYS = ['25_a_day', 'on_demand', 'enhanced', 'single_image_and_other']
QUARTER = {"01": "Q1", "02": "Q1", "03": "Q1", "04": "Q2", "05": "Q2", "06": "Q2", "07": "Q3", "08": "Q3", "09": "Q3",
           "10": "Q4", "11": "Q4", "12": "Q4"}
preURLS = []
URLS = []

SETSLIST = ['Abstruct', 'Amarillis', 'Anemone', 'AppleFlower', 'Aquilegia', 'Bird', 'Butterflies', 'Camellia',
            'cannabis', 'Carnation', 'carnegiea', 'CherryFlower', 'Chrysanthemum', 'Chubushnik', 'Clematis',
            'Cornus', 'Crocuses', 'Dahila', 'daisy', 'dandelion', 'Dogwood', 'dragonfly', 'Eustoma', 'ExoticFlower',
            'Feather', 'Fish', 'Forgetmenot', 'frame', 'fresia', 'Fuchsia', 'Gaillardia', 'hibiscus', 'immortelle',
            'Iris', 'Kosmeya', 'Lavender', 'Lily', 'London', 'Love', 'Magnolia', 'Malus', 'Myosotis', 'Narcissus',
            'Olive', 'Orchids', 'other', 'Paintbrush', 'pattern', 'Peony', 'PhotoPromotion', 'Poppy', 'Primula',
            'Rose', 'Sakura', 'Sarracenia', 'Succulentus', 'cactus', 'Tropical Hawaii leaves palm tree', 'Tulip',
            'Viola', 'Weigela']


#######################################################################################################################

def generateURLS(MAX, URL, file):
    baseURL = URL[:URL.index("page=") + len("page=")]
    appendURL = URL[URL.index("&date"):]
    if MAX == 1:
        url = baseURL + str(MAX) + appendURL
        print(url)
        file.write(url + "\n")
        return
    else:
        for page in range(1, int(MAX) + 1):
            url = baseURL + str(page) + appendURL
            print(url)
            file.write(url + "\n")


def getMAXpageAndGenerateURLS(URL, erningsFile, allURLs):
    if URL in allURLs:
        return
    else:
        onePage = True
        MAX = 0
        response = requests.get(URL, cookies=COOKIES)
        dataMass = response.text.split("\n")
        for line in dataMass:
            if "None of your images were downloaded" in line:
                onePage = False
                break
            if "Sorry! We're having some issues loading this data right now." in line:
                onePage = False
                break
            if "max=" in line:
                MAX = re.findall('\d+', line)[0]
                onePage = False
                break
        if onePage == True:
            MAX = 1
        if MAX != 0:
            with open("AllURLS.csv", "a") as allURLSfile:
                allURLSfile.write(URL + '\n')
                allURLSfile.close()
            generateURLS(MAX, URL, erningsFile)


def generateStartUrls():
    with open("AllStartURLS.csv", "w") as allStartURLSfile:
        preURLS = [URLBASE + str(PAGE) + URLDATE + y + "-" + m + "-" + (
            "0" + str(d) if len(str(d)) == 1 else str(d)) + URLCATEGORY + c + URLAPPEND + "\n" for y in YEARS for m in MONTHS.keys() for d in
                   range(1, int(DAYS.get(m)) + 1) for c in CATEGORYS]
        allStartURLSfile.writelines(preURLS)
        allStartURLSfile.close()
        for url in preURLS:
            print(url)


def generateAllUrls():
    with open("URLs_EarningsSummaryByMonth.csv", "a") as erningsFile:
        with open("AllStartURLS.csv", "r") as AllStartURLSfile:
            preURLS = AllStartURLSfile.readlines()
            AllStartURLSfile.close()
            if os.path.exists("AllURLS.csv"):
                allURLs = open("AllURLS.csv", "r").readlines()
            else:
                allURLs = []
            threads = [threading.Thread(target=getMAXpageAndGenerateURLS, args=[url.strip(), erningsFile, allURLs]) for url in
                           preURLS]
            n = 1
            for thread in threads:
                time.sleep(0.07)
                thread.start()
                print("Threads # " + str(n) + " started!")
                n += 1
            for thread in threads:
                n -= 1
                print("Threads # " + str(n) + " joined...")
                time.sleep(0.07)
                thread.join()
    erningsFile.close()


def getInfoData(url, infoData):
    tmpDate = url[url.index("date=") + len("date="):url.index("&language=")]
    tmpDate = tmpDate.split("-")
    for category in CATEGORYS:
        if category in url:
            infoData.Category = category
            break
    infoData.Day_of_sale = tmpDate[1] + "/" + tmpDate[2] + '/' + tmpDate[0]
    infoData.Data = MONTHS.get(str(tmpDate[1])) + "-" + tmpDate[0][2:]
    infoData.Quarter = QUARTER.get(str(tmpDate[1]))
    infoData.Day_of_week = WEEKDAY.get(
        datetime.datetime(int(tmpDate[0]), int(tmpDate[1]), int(tmpDate[2])).weekday())
    return infoData


def getDataFromURLSinThreads(url, wr):
    DF = []
    infoData = collections.namedtuple('infoData', ['Quarter', 'Data', 'Day_of_sale', 'Day_of_week', 'Category'])
    IFD = getInfoData(url, infoData)
    DF.extend([IFD.Quarter, IFD.Data, IFD.Day_of_sale, IFD.Day_of_week, IFD.Category])
    response = requests.get(url, cookies=COOKIES)
    dataMass = response.text.split("\n")
    odd = True
    for i, line in enumerate(dataMass):
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
                print(DF)
                wr.writerow(DF)
                del DF[5:]
        if re.findall(r'<td>[$]\d+.\d+</td>', line):
            Earnings = str(re.findall(r'\d+\.\d+', line)[0])
            DF.append(Earnings)


def getDataFromURLS():
    with open("DF_EarningsSummaryByMonth.csv", "w+") as fileWrite:
        wr = csv.writer(fileWrite)
        with open("URLs_EarningsSummaryByMonth.csv", "r") as fileRead:
            dataFromFile = fileRead.readlines()
            urlsList = [url.strip() for url in dataFromFile]
            threads = [threading.Thread(target=getDataFromURLSinThreads, args=[url, wr]) for url in urlsList]
            n = 1
            for thread in threads:
                time.sleep(0.05)
                thread.start()
                print("Threads # " + str(n) + " started!")
                n += 1
            for thread in threads:
                n -= 1
                time.sleep(0.05)
                thread.join()
                print("Threads # " + str(n) + " joined...")
        fileRead.close()
    fileWrite.close()


def main():
    # print(1)
    generateStartUrls()
    generateAllUrls()
    getDataFromURLS()


main()
