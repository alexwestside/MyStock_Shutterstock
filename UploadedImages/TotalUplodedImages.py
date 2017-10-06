from __future__ import print_function
import requests
import csv
import re
import threading
import time
import pandas as pd
import xlsxwriter
import datetime
import string

cookies = {"__ssid": "9606bc02-747b-42ef-b851-4e738e7fd1de", "_ga": "GA1.2.1906198584.1505855712",
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

BaseURL = "https://submit.shutterstock.com/review_batch.mhtml?approved=1&id="
ID = "170355946"
AppendURL = "&type=photos&pg="
Page = 1

MONTHS = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
          '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
WEEKDAY = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Fraiday', 5: 'Saturday', 6: 'Sunday'}

listURLS = []


def getDataFrame(url, wr):
    UploadData = None
    response = requests.get(url, cookies=cookies)
    dataFrame = response.text.split("\n")
    for i, line in enumerate(dataFrame):
        if "Batch ID:" in line:
            UploadData = line.split("(")[1].split(")")[0]
        if "img src=" in line:
            listUploadData = []
            tmp = line.split("\t\t")
            try:
                end1 = tmp[2].rindex("\"")
            except:
                print("substring not found", tmp[0])
            try:
                end2 = tmp[2].index(".")
            except:
                print("substring not found", tmp[0])
            Source = str(tmp[0][tmp[0].index("\"") + 1:tmp[0].rindex("\"")])
            ID = Source[Source.index("photo-") + len("photo-"):Source.index(".jpg")]
            Title = tmp[2][tmp[2].index("\"") + 1:end2 if end2 > 0 else end1]
            # Title = tmp[2][tmp[2].index("\"") + 1:end1 if end1 > 0 and end1 != tmp[2].index("\"") else end2]
            splitDate = UploadData.split("/")
            listUploadData.append(MONTHS.get(splitDate[0]) + "-" + splitDate[2])
            listUploadData.append(UploadData)
            listUploadData.append(str(WEEKDAY.get(datetime.datetime(int(splitDate[2]), int(splitDate[0]), int(splitDate[1])).weekday())))
            listUploadData.append(ID)
            listUploadData.append(Source)
            listUploadData.append(Title)
            wr.writerow(listUploadData)
            print(listUploadData)


def uploadDataFromURLs():
    with open("DF_TotalUplodedImages.csv", "w") as file:
        wr = csv.writer(file)
        csv_header = ["MonthUpload", "UploadData", "Day_of_week", "ID", "Source", "Title"]
        wr.writerow(csv_header)
        URLSlist = [line.rstrip('\n') for line in open("BatchURLSfile.csv")]
        threads = [threading.Thread(target=getDataFrame, args=[url, wr]) for url in URLSlist]
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
    file.close()


def writeTofileURLS(BatchID, PhotosInBatch, BatchURLSfile):
    pages = int(PhotosInBatch / 20) + 1 if PhotosInBatch % 20 > 0 else int(PhotosInBatch / 20)
    listURLS = [BaseURL + str(BatchID) + AppendURL + str(n) + "\n" for n in range(1, pages + 1)]
    BatchURLSfile.writelines(listURLS)


def approvedPhotos():
    url = "https://submit.shutterstock.com/review.mhtml?approved=1&type=photos"
    with open("ApprovedPhotosTotalbyBatch.csv", "w") as file:
        with open("BatchURLSfile.csv", "w") as BatchURLSfile:
            wr = csv.writer(file)
            csv_header = ["BatchID", "MonthSubmitted", "DateSubmitted", "Day_of_week", "PhotosInBatch"]
            wr.writerow(csv_header)
            response = requests.get(url, cookies=cookies)
            dataFrame = response.text.split("\n")
            for i, line in enumerate(dataFrame):
                linetoscv = []
                if "?id=" in line:
                    BatchID = re.findall('\d+', line)[0]
                    DateSubmitted = dataFrame[i + 3].split(">")[1].split("<")[0]
                    PhotosInBatch = re.findall('\d+', dataFrame[i + 4])[0]
                    dateSplit = DateSubmitted.split("/")
                    linetoscv.append(str(BatchID))
                    linetoscv.append(str(MONTHS.get(dateSplit[0])) + "-" + dateSplit[2])
                    linetoscv.append(str(DateSubmitted))
                    linetoscv.append(str(WEEKDAY.get(datetime.datetime(int(dateSplit[2]), int(dateSplit[0]), int(dateSplit[1])).weekday())))
                    linetoscv.append(str(PhotosInBatch))
                    wr.writerow(linetoscv)
                    writeTofileURLS(BatchID, int(PhotosInBatch), BatchURLSfile)
        file.close()


def uploadImages():
    approvedPhotos()
    uploadDataFromURLs()
    # writeToExcel()
