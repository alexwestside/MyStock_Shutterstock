import os
import requests
import time
import datetime
import pandas as pd
import csv


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

file = "batch.csv"
title = ["BatchID", "MonthSubmitted", "DateSubmitted", "Day_of_week", "PhotosInBatch"]
lists = [["1", "2", "3", "4", "5"], ["4", "5", "6", "7", "8"], ["4", "9", "36", "27", "84"]]

writer = Writer(file, title)
batch = Batch(file)
batch.makeListIDs("BatchID")
a = batch.listBatchIDs
for list in lists:
    l = list[0]
    if batch.checkNewIDinListIDs(list[0]):
        writer.writeTOscv(list)
    else:
        print("!!!!")
