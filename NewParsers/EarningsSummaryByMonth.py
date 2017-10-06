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
import xlsxwriter
import string
from UploadedImages import TotalUplodedImages

COOKIES = {"__ssid": "9606bc02-747b-42ef-b851-4e738e7fd1de", "_ga": "GA1.2.1906198584.1505855712",
           "_photo_session_id": "68214e1d41c4266955645373481a5a42", "_session_id": "a8c044ff1ba8114f12f39f2a6024decb",
           "_ym_uid": "1494857922560381083", "accts_contributor": "MyStocks", "accts_customer": "yanushkov",
           "ajs_anonymous_id": "%226ae010e6-859b-484c-b5d9-6221581e51cf%22", "ajs_group_id": "null", "ajs_user_id": "null",
           "did": "a9b91f2e-f3b6-4532-b41e-b34bd7cb67e7",
           "IRF_3": "%7Bvisits%3A21%2Cuser%3A%7Btime%3A1494857922704%2Cref%3A%22direct%22%2Cpv%3A47%2Ccap%3A%7B%7D%2Cv%3A%7B%7D%7D%2Cvisit%3A%7Btime%3A1506455994261%2Cref%3A%22direct%22%2Cpv%3A1%2Ccap%3A%7B47%3A1%7D%2Cv%3A%7B1225%3A%22IR_AN_64%22%7D%7D%2Clp%3A%22https%3A%2F%2Fwww.shutterstock.com%2Fru%2Fimage-illustration%2Fsky-bird-white-macaw-pattern-wildlife-722442694%22%2Cdebug%3A0%2Ca%3A1506455994261%2Cd%3A%22shutterstock.com%22%7D",
           "IRMS_la1305": "1506455994548", "language": "en", "locale": "ru", "optimizelyEndUserId": "oeu1498041993482r0.3441372721886864",
           "optly.pgStore.s.0": "{}", "psst": "115:466,158:572,218:872,332:1160,377:1334,454:1558,530:1787,542:1853,551:1874",
           "urefid": "%7B%22contributor_id%22%3A%22161069038%22%2C%22time%22%3A1505855706%2C%22referrer%22%3A%22https%3A%2F%2Fsubmit.shutterstock.com%2Fdashboard%3Flanguage%3Den%22%2C%22entry_url%22%3A%22%2Fg%2FMyStocks%3Flanguage%3Den%22%7D",
           "visit_id": "16173401993", "visitor_id": "11011468609", "__utma": "265213581.1507426815.1494857922.1506807077.1506887612.40",
           "__utmb": "265213581.3.10.1506887612", "__utmc": "265213581",
           "__utmz": "265213581.1494857970.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)", "__uvt": "", "_ga": "GA1.3.1507426815.1494857922",
           "uvts": "6DIK18ZF738WyVeK", "sbsid": "1822b901c314b74acb7eed69318bfff4",
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
CATEGORYS = {"25_a_day": "subscription", "on_demand": "onDemand", "enhanced": "enhanced", "single_image_and_other": "single&other"}
QUARTER = {"01": "Q1", "02": "Q1", "03": "Q1", "04": "Q2", "05": "Q2", "06": "Q2", "07": "Q3", "08": "Q3", "09": "Q3",
           "10": "Q4", "11": "Q4", "12": "Q4"}
preURLS = []
URLS = []

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


def getMAXpageAndGenerateURLS(URL, file):
    onePage = True
    MAX = 0
    try:
        response = requests.get(URL, cookies=COOKIES)
    except requests.exceptions.ConnectionError as e:
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
        generateURLS(MAX, URL, file)


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
    with open("URLs_EarningsSummaryByMonth.csv", "w") as erningsFile:
        preURLS = [line.rstrip('\n') for line in open("AllStartURLS.csv")]
        threads = [threading.Thread(target=getMAXpageAndGenerateURLS, args=[url.strip(), erningsFile]) for url in preURLS]
        n = 1
        for thread in threads:
            time.sleep(0.07)
            thread.start()
            print("Threads # " + str(n) + " started...")
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
    for category in CATEGORYS.keys():
        if category in url:
            infoData.Category = CATEGORYS.get(category)
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
    with open("DF_EarningsSummaryByMonth.csv", "w") as fileWrite:
        wr = csv.writer(fileWrite)
        csv_header = ["Qurter", "Data", "Day_of_sale", "Day_of_week", "Category", "ID", "Earnings", "Downloads"]
        wr.writerow(csv_header)
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


def writeToExcel():
    workbookName = datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "_" + "MyStocks_analytics_by_set.xlsx"
    # df1 = pd.DataFrame(pd.read_csv("ApprovedPhotosTotalbyBatch.csv"))
    df2 = pd.DataFrame(pd.read_csv("DF_TotalUplodedImages.csv"))
    df3 = pd.DataFrame(pd.read_csv("DF_EarningsSummaryByMonth.csv"))
    writer = pd.ExcelWriter(workbookName, engine='xlsxwriter')
    # df1.to_excel(writer, sheet_name='InfoBatch')
    df2.to_excel(writer, sheet_name='TotalUplodedImages')
    df3.to_excel(writer, sheet_name='EarningsSummaryByMonth')
    writer.save()


def main():
    TotalUplodedImages.uploadImages()
    # generateStartUrls()
    # generateAllUrls()
    # getDataFromURLS()
    # writeToExcel()


main()
