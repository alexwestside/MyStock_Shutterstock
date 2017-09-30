
import os
# str = '"Adfghh"'


# a = str.rindex("\"")
# print(a)

YEARS = ["2016", "2017"]
DAYS = {"01": "31", "02": "30", "03": "31", "04": "31", "05": "31", "06": "31", "07": "31", "08": "31", "09": "31",
        "10": "31", "11": "31", "12": "31"}

MONTHS = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
          '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
URLBASE = "https://submit.shutterstock.com/earnings/daily?page="
PAGE = 1
URLDATE = "&date="
DATE = "2017-09-01"
URLCATEGORY = "&language=en&category="
CATEGORY = "25_a_day"
URLAPPEND = "&sort=desc&sorted_by=count&per_page=20"
CATEGORYS = ['25_a_day', 'on_demand', 'enhanced', 'single_image_and_other']

URL = [URLBASE + str(PAGE) + URLDATE + y + "-" + m + "-" + ("0" + str(d) if len(str(d)) == 1 else str(d)) + URLCATEGORY + c + URLAPPEND + "\n" for y in YEARS for m in MONTHS.keys() for d in range(1, int(DAYS.get(m)) + 1) for c in CATEGORYS]

# for u in URL:
#     print(u)

# a = "https://submit.shutterstock.com/earnings/daily?page=1&date=2016-02-15&language=en&category=25_a_day&sort=desc&sorted_by=count&per_page=20\n"


if not os.path.exists("test.scv"):
    print(1)
# with open("test.scv", "a") as f:
#     f.close()






# list = []
# list.extend([a, b, c])
# print(list)


# with open("test.scv", "w") as f1:
#     URL1 = f1.readlines()
#     f.close()

# print(URL1)