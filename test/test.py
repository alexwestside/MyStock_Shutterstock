import os
import requests
import time
import datetime
import pandas as pd
import csv
import smtplib

# class Writer:
#     def __init__(self, file, title):
#         self.file = file
#         self.title = title
#     def writeTOscv(self, data):
#         if not os.path.isfile(self.file):
#             csv.writer(open(self.file, "w")).writerow(self.title)
#         csv.writer(open(self.file, "a")).writerow(data)
#
# class Batch:
#     def __init__(self, file):
#         self.file = file
#         self.listBatchIDs = []
#     def makeListIDs(self, columne):
#         if os.path.isfile(self.file):
#             [self.listBatchIDs.append(val[0]) for val in pd.read_csv(self.file, usecols=[columne]).values.tolist()]
#     def checkNewIDinListIDs(self, data):
#         return False if data in self.listBatchIDs else True
#
# file = "batch.csv"
# title = ["BatchID", "MonthSubmitted", "DateSubmitted", "Day_of_week", "PhotosInBatch"]
# lists = [["1", "2", "3", "4", "5"], ["4", "5", "6", "7", "8"], ["4", "9", "36", "27", "84"]]
#
# writer = Writer(file, title)
# batch = Batch(file)
# batch.makeListIDs("BatchID")
# a = batch.listBatchIDs
# for list in lists:
#     l = list[0]
#     if batch.checkNewIDinListIDs(list[0]):
#         writer.writeTOscv(list)
#     else:
#         print("!!!!")



fromUser = "sklif.85@gmail.com"
fromUserPassword = "1XyUNnz_"
toUser = "olexandr.rizhiy@gmail.com"
subject = "TEST"
message = "Hello!!!"



class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        # session.ehlo()
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, subject, body, toUser):
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + toUser,
            "MIME-Version: 1.0",
           "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.email,
            self.email,
            headers + "\r\n\r\n" + body)


gm = Gmail(fromUser, fromUserPassword)

gm.send_message('TEST', 'Hello!!!')

