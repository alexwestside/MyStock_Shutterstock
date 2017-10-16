from UploadedImages.TotalUplodedImages import *
import requests
import browsercookie
import os
import pandas as pd
import smtplib

InitApprovedPhotosURLs = "https://submit.shutterstock.com/review.mhtml?approved=1&type=photos"
a = "https://submit.shutterstock.com/review_batch.mhtml?id=174048139&approved=1&type=photos"

class Login:
    def __init__(self):
        self.url = "https://submit.shutterstock.com/earnings?language=en"
        self.cookies = browsercookie.chrome()
    def getCookies(self):
        return requests.get(self.url, cookies=self.cookies).cookies

class Response:
    def __init__(self, cookies, url):
        self.url = url
        self.cookies = cookies
    def getResponse(self):
        return requests.get(self.url, cookies=self.cookies).text

class Batch:
    def __init__(self, file):
        self.write = "w"
        self.append = "a"
        self.file = file
        self.fd = ""
        self.csv_header = ["BatchID", "MonthSubmitted", "DateSubmitted", "Day_of_week", "PhotosInBatch"]
    def writeAppend(self):
        if os.path.isfile(self.file):
            self.fd = open(self.file, self.append)
        else:
            self.fd = open(self.file, self.write)
            self.scvWriter().writerow(self.csv_header)
    def scvWriter(self):
        return csv.writer(self.fd)

class Checker:
    def __init__(self, columne, file):
        self.getAllBatchesID = pd.read_csv(file, usecols=[columne])
    def check(self, data):
        if data in self.getAllBatchesID:
            return True
        else:
            return False


def main():
    a = pd.read_csv("batch.csv", usecols=["BatchID"])




    batchFile = "batch.csv"
    batchObj = Batch(batchFile)
    batchObj.writeAppend()
    checkerObj = Checker(batchObj.csv_header[0], batchObj.fd)
    if checkerObj.check("12345"):
        print(1)
    else:
        print(2)



    # url = "https://submit.shutterstock.com/earnings/daily?category=25_a_day&language=en&date=2017-10-15"
    # response = Response(Login().cookies, url).getResponse()
    # print(response)

main()
