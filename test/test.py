import os
import requests
import time
import datetime

# str = '"Adfghh"'


# a = str.rindex("\"")
# print(a)

# YEARS = ["2016", "2017"]
# DAYS = {"01": "31", "02": "30", "03": "31", "04": "31", "05": "31", "06": "31", "07": "31", "08": "31", "09": "31",
#         "10": "31", "11": "31", "12": "31"}
#
# MONTHS = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
#           '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
# URLBASE = "https://submit.shutterstock.com/earnings/daily?page="
# PAGE = 1
# URLDATE = "&date="
# DATE = "2017-09-01"
# URLCATEGORY = "&language=en&category="
# CATEGORY = "25_a_day"
# URLAPPEND = "&sort=desc&sorted_by=count&per_page=20"
# CATEGORYS = ['25_a_day', 'on_demand', 'enhanced', 'single_image_and_other']
#
# URL = [URLBASE + str(PAGE) + URLDATE + y + "-" + m + "-" + ("0" + str(d) if len(str(d)) == 1 else str(d)) + URLCATEGORY + c + URLAPPEND + "\n" for y in YEARS for m in MONTHS.keys() for d in range(1, int(DAYS.get(m)) + 1) for c in CATEGORYS]

# for u in URL:
#     print(u)

# a = "https://submit.shutterstock.com/earnings/daily?page=1&date=2016-02-15&language=en&category=25_a_day&sort=desc&sorted_by=count&per_page=20\n"


# if not os.path.exists("test.scv"):
#     print(1)
# with open("test.scv", "a") as f:
#     f.close()

# list = []
# list.extend([a, b, c])
# print(list)


# with open("test.scv", "w") as f1:
#     URL1 = f1.readlines()
#     f.close()

# print(URL1)

# COOKIES = {"__ssid": "9606bc02-747b-42ef-b851-4e738e7fd1de", "_photo_session_id": "68214e1d41c4266955645373481a5a42",
#            "_ym_uid": "1494857922560381083", "accts_contributor": "MyStocks", "accts_customer": "yanushkov",
#            "ajs_anonymous_id": "%226ae010e6-859b-484c-b5d9-6221581e51cf%22", "ajs_group_id": "null",
#            "ajs_user_id": "null", "did": "a9b91f2e-f3b6-4532-b41e-b34bd7cb67e7",
#            "IRF_3": "%7Bvisits%3A14%2Cuser%3A%7Btime%3A1494857922704%2Cref%3A%22direct%22%2Cpv%3A39%2Ccap%3A%7B%7D%2Cv%3A%7B%7D%7D%2Cvisit%3A%7Btime%3A1504427803093%2Cref%3A%22https%3A%2F%2Fsubmit.shutterstock.com%2Fearnings%2Fdaily%3Fpage%3D3%26date%3D2017-08-01%26language%3Den%26category%3D25_a_day%26sort%3Ddesc%26sorted_by%3Dcount%26per_page%3D20%22%2Cpv%3A12%2Ccap%3A%7B47%3A1%7D%2Cv%3A%7B1225%3A%22IR_AN_64%22%7D%7D%2Clp%3A%22https%3A%2F%2Fwww.shutterstock.com%2Fru%2Fimage-vector%2Fhand-drawn-botanical-art-isolated-on-687437659%22%2Cdebug%3A0%2Ca%3A1504430191128%2Cd%3A%22shutterstock.com%22%7D",
#            "IRMS_la1305": "1504427803784", "language": "en", "locale": "ru",
#            "optimizelyEndUserId": "oeu1498041993482r0.3441372721886864", "optly.pgStore.s.0": "{}",
#            "psst": "115:466,158:572,218:872,332:1160,377:1334,454:1558,530:1787,542:1853,551:1874",
#            "visit_id": "15831945931", "visitor_id": "11011468609",
#            "__utma": "265213581.1507426815.1494857922.1504638242.1505153117.27", "__utmc": "265213581",
#            "__utmz": "265213581.1494857970.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)", "__uvt": "",
#            "_ga": "GA1.3.1507426815.1494857922", "uvts": "6DIK18ZF738WyVeK",
#            "sbsid": "a8c044ff1ba8114f12f39f2a6024decb",
#            "session": "s%3APOPXQWqr-nYusEExnUPhmPTJ4q76UUXl.iKOHDwAqW8hCq%2FrmqKYBSW8tXwW0Mz45RwTQPe2XW1o", }

# c = {"__ssid": "9606bc02-747b-42ef-b851-4e738e7fd1de", "_photo_session_id": "68214e1d41c4266955645373481a5a42", "_ym_uid": "1494857922560381083",
#      "accts_contributor": "MyStocks", "accts_customer": "yanushkov", "ajs_anonymous_id": "%226ae010e6-859b-484c-b5d9-6221581e51cf%22",
#      "ajs_group_id": "null", "ajs_user_id": "null", "did": "a9b91f2e-f3b6-4532-b41e-b34bd7cb67e7",
#      "IRF_3": "%7Bvisits%3A14%2Cuser%3A%7Btime%3A1494857922704%2Cref%3A%22direct%22%2Cpv%3A39%2Ccap%3A%7B%7D%2Cv%3A%7B%7D%7D%2Cvisit%3A%7Btime%3A1504427803093%2Cref%3A%22https%3A%2F%2Fsubmit.shutterstock.com%2Fearnings%2Fdaily%3Fpage%3D3%26date%3D2017-08-01%26language%3Den%26category%3D25_a_day%26sort%3Ddesc%26sorted_by%3Dcount%26per_page%3D20%22%2Cpv%3A12%2Ccap%3A%7B47%3A1%7D%2Cv%3A%7B1225%3A%22IR_AN_64%22%7D%7D%2Clp%3A%22https%3A%2F%2Fwww.shutterstock.com%2Fru%2Fimage-vector%2Fhand-drawn-botanical-art-isolated-on-687437659%22%2Cdebug%3A0%2Ca%3A1504430191128%2Cd%3A%22shutterstock.com%22%7D",
#      "IRMS_la1305": "1504427803784", "language": "en", "locale": "ru", "optimizelyEndUserId": "oeu1498041993482r0.3441372721886864",
#      "optly.pgStore.p.0": "{"loggedInState":{"value":"Yes","exp":1512206190262},"hasAccount":{"value":"Yes","exp":1512206190800}}",
#      "optly.pgStore.s.0": "{}", "psst": "115:466,158:572,218:872,332:1160,377:1334,454:1558,530:1787,542:1853,551:1874",
#      "visit_id": "15831945931", "visitor_id": "11011468609", "__utma": "265213581.1507426815.1494857922.1504638242.1505153117.27",
#      "__utmc": "265213581", "__utmz": "265213581.1494857970.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)", "__uvt": "",
#      "_ga": "GA1.3.1507426815.1494857922", "uvts": "6DIK18ZF738WyVeK", "sbsid": "a8c044ff1ba8114f12f39f2a6024decb",
#      "session": "s%3APOPXQWqr-nYusEExnUPhmPTJ4q76UUXl.iKOHDwAqW8hCq%2FrmqKYBSW8tXwW0Mz45RwTQPe2XW1o", }

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

url = "https://submit.shutterstock.com/earnings/daily?page=1&date=2016-01-04&language=en&category=25_a_day&sort=desc&sorted_by=count&per_page=20"

a = datetime.datetime.now().microsecond
lines = tuple(open("../NewParsers/AllStartURLS.csv", 'r'))
# lines = [line.rstrip('\n') for line in open('filename')]
b = datetime.datetime.now().microsecond
print(int(b)-int(a))
print(lines)

c = datetime.datetime.now().microsecond
# lines = tuple(open("../NewParsers/AllStartURLS.csv", 'r'))
lines1 = [line.rstrip('\n') for line in open('../NewParsers/AllStartURLS.csv')]
d = datetime.datetime.now().microsecond
print(int(d)-int(c))
print(lines1)

# while True:
#     response = requests.get(url, cookies=COOKIES)
#     dataMass = response.text.split("\n")
#     print(str(dataMass))
# for i, line in enumerate(dataMass):
#     if "img src=" in line:
#         if "465268094" in line:
#             listUploadData = []
#             tmp = line.split("\t\t")
#             end1 = tmp[2].rindex("\"")
#             end2 = tmp[2].rindex(".")
#             Source = str(tmp[0][tmp[0].index("\"") + 1:tmp[0].rindex("\"")])
#             ID = Source[Source.index("photo-") + len("photo-"):Source.index(".jpg")]
#             Title = tmp[2][tmp[2].index("\"") + 1:end1 if end1 > 0 and end1 != tmp[2].index("\"") else end2]
#             print(line)



# PhotosInBatch = 20
# PhotosInBatch1 = 36
# PhotosInBatch2 = 27
# PhotosInBatch3 = 39
#
# pages = int(PhotosInBatch / 20) + 1 if PhotosInBatch % 20 > 0 else int(PhotosInBatch / 20)
# pages1 = int(PhotosInBatch1 / 20) + 1 if (int(PhotosInBatch1 % 20) > 0) else int(PhotosInBatch1 / 20)
# pages2 = int(PhotosInBatch2 / 20) + 1 if PhotosInBatch2 % 20 > 0 else int(PhotosInBatch2 / 20)
# pages3 = int(PhotosInBatch3 / 20) + 1 if PhotosInBatch3 % 20 > 0 else int(PhotosInBatch3 / 20)
# for i in range(1, pages1 + 1):
#     print(i)
#
# print(pages)
# print(pages1)
# print(pages2)
# print(pages3)

# import xlsxwriter
# import time
# import datetime
# import string
#
# list = ["123", "321", "546"]
# workbookName = datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "_" + "MyStocks_analytics_by_set.xlsx"
# workbook = xlsxwriter.Workbook(workbookName, {'default_date_format': 'dd/mm/yy'})
# with xlsxwriter.Workbook(workbookName) as wb:
#     ws1 = wb.add_worksheet("123")
#     ws2 = wb.add_worksheet("1111")
#     ws1.write(list)
# alpha = string.ascii_uppercase
# for a in alpha:
#     for i in range(1, 10):
#         print(a + str(i))
