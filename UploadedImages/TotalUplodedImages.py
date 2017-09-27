from __future__ import print_function
import requests
import csv
import re
import threading
import time

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

BaseURL = "https://submit.shutterstock.com/review_batch.mhtml?approved=1&id="
ID = "170355946"
AppendURL = "&type=photos&pg="
Page = 1
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
            start = tmp[0].index("\"")
            end1 = tmp[0].rindex("\"")
            end2 = tmp[0].rindex(".")
            Source = str(tmp[0][start + 1:end1 if end1 > 0 else end2])
            ID = Source[Source.index("photo-") + len("photo-"):Source.index(".jpg")]
            if ID == "465268094":
                print(1)
            Title = tmp[2][tmp[2].index("\"") + 1:tmp[2].rindex("\"")]
            listUploadData.append(UploadData)
            listUploadData.append(ID)
            listUploadData.append(Source)
            listUploadData.append(Title)
            wr.writerow(listUploadData)
            print(listUploadData)


def uploadDataFromURLs():
    with open("DF_TotalUplodedImages.csv", "w") as file:
        wr = csv.writer(file)
        csv_header = ["UploadData", "ID", "Source", "Title"]
        wr.writerow(csv_header)
        threads = [threading.Thread(target=getDataFrame, args=[url, wr]) for url in listURLS]
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
    file.close()


def writeTofileURLS(BatchID, PhotosInBatch):
    pages = int(PhotosInBatch / 20) + (1 if PhotosInBatch % 20 > 0 else 0)
    for n in range(1, pages + 1):
        url = BaseURL + str(BatchID) + AppendURL + str(n)
        listURLS.append(url)


def approvedPhotos():
    url = "https://submit.shutterstock.com/review.mhtml?approved=1&type=photos"
    with open("ApprovedPhotosTotalbyBatch.csv", "w") as file:
        wr = csv.writer(file)
        csv_header = ["BatchID", "DateSubmitted", "PhotosInBatch"]
        wr.writerow(csv_header)
        response = requests.get(url, cookies=cookies)
        dataFrame = response.text.split("\n")
        for i, line in enumerate(dataFrame):
            linetoscv = []
            if "?id=" in line:
                BatchID = re.findall('\d+', line)[0]
                DateSubmitted = dataFrame[i + 3].split(">")[1].split("<")[0]
                PhotosInBatch = re.findall('\d+', dataFrame[i + 4])[0]
                linetoscv.append(str(BatchID))
                linetoscv.append(str(DateSubmitted))
                linetoscv.append(str(PhotosInBatch))
                wr.writerow(linetoscv)
                writeTofileURLS(BatchID, int(PhotosInBatch))
        file.close()


def main():
    approvedPhotos()
    uploadDataFromURLs()


main()
