from UploadedImages.TotalUplodedImages import *
import requests
import browsercookie
import os
import pandas as pd
import smtplib
import browser_cookie3

InitApprovedPhotosURLs = "https://submit.shutterstock.com/review.mhtml?type=photos"


class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.login(self.email, self.password)
        self.session = session

    def send(self, subject, body, to_user):
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + to_user,
            "MIME-Version: 1.0",
            "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.session.sendmail(self.email, self.email, headers + "\r\n\r\n" + body)
        self.session.close()


class Login:
    def __init__(self):
        self.cookies = browsercookie.chrome()
        # self.cookies = browser_cookie3.chrome(domain_name='submit.shutterstock.com')

class Response:
    def __init__(self, cookies, url):
        self.url = url
        self.cookies = cookies

    def getResponse(self):
        return requests.get(self.url, cookies=self.cookies).text.split("\n")


class Writer:
    def __init__(self, file, title):
        self.file = file
        self.title = title

    def writeTOscv(self, data):
        if not os.path.isfile(self.file):
            csv.writer(open(self.file, "w")).writerow(self.title)
        csv.writer(open(self.file, "a")).writerow(data)


class Batch:
    def __init__(self, file):
        self.file = file
        self.listBatchIDs = []

    def makeListIDs(self, columne):
        if os.path.isfile(self.file):
            [self.listBatchIDs.append(val[0]) for val in pd.read_csv(self.file, usecols=[columne]).values.tolist()]

    def checkNewIDinListIDs(self, data):
        return False if data in self.listBatchIDs else True


def main():
    batchFile = "batch.csv"
    title = ["BatchID", "MonthSubmitted", "DateSubmitted", "Day_of_week", "PhotosInBatch"]
    print(Login().cookies)
    dataFrame = Response(Login().cookies, InitApprovedPhotosURLs).getResponse()
    writer = Writer(batchFile, title)
    batch = Batch(batchFile)
    batch.makeListIDs("BatchID")
    boby = []
    for i, line in enumerate(dataFrame):
        lineTOscv = []
        if "?id=" in line:
            BatchID = re.findall('\d+', line)[0]
            if batch.checkNewIDinListIDs(BatchID):
                DateSubmitted = dataFrame[i + 3].split(">")[1].split("<")[0]
                PhotosInBatch = re.findall('\d+', dataFrame[i + 4])[0]
                dateSplit = DateSubmitted.split("/")
                lineTOscv.extend([str(BatchID), str(MONTHS.get(dateSplit[0])) + "-" + dateSplit[2], str(DateSubmitted),
                                  str(WEEKDAY.get(datetime.datetime(int(dateSplit[2]), int(dateSplit[0]), int(dateSplit[1])).weekday())),
                                  str(PhotosInBatch)])
                writer.writeTOscv(lineTOscv)
                # boby.append(lineTOscv)
                boby = ', '.join(lineTOscv).join("\n")
                print(lineTOscv)
    print(boby)
    if len(boby) != 0:
        user = "sklif.85@gmail.com"
        password = "1XyUNnz_"
        touser = "olexandr.rizhiy@gmail.com"
        subject = "subject"

        # TODO need test for sending email.....
        mail = Gmail(user, password)
        mail.send(subject, boby, touser)


main()
