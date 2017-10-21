from UploadedImages.TotalUplodedImages import *
import requests
import browsercookie
import os
import pandas as pd
import smtplib
import browser_cookie3
import itertools


# url = "https://submit.shutterstock.com/earnings/daily?category=25_a_day&language=en&date=2017-10-15"
#
# cj = browser_cookie3.chrome(domain_name='submit.shutterstock.com')
# print(cj)
# r = requests.get(url, cookies=cj)
# print(r.text)

c = ["a", "b", "c", "d"]

print(c)
# a = str(itertools.chain.from_iterable(c))
print(', '.join(c))