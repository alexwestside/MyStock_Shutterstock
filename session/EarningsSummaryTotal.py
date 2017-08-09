import sha
import hashlib
from requests import request
from requests import session
from BeautifulSoup import BeautifulSoup


# page=1 (1 of 143)
# category=25_a_day
#   Subscription -> 25_a_day
#   Enhanced -> enhanced
#   On Demand -> on_demand
#   Videos -> video_all
#   Single & other -> single_image_and_other

# Login <a id="login-trigger" href="/login">Sign In</a>
# url = https://contributor-accounts.shutterstock.com/login

# https://submit.shutterstock.com/edit_media.mhtml?type=photos&approved=1&id=508654753

EarningsSummaryPage = "https://submit.shutterstock.com/earnings/details?page=1&language=en&category=25_a_day&sort=desc&sorted_by=count&per_page=20"


# url = 'https://account.socialbakers.com/login'
url = 'https://contributor-accounts.shutterstock.com/login'
# myemail = "yanushkov@gmail.com"
# mypassword = hashlib.sha512(b'328993Standart').hexdigest() #take SHA of password
# payload = {'email':myemail, 'password':mypassword}
# with session() as s:
#     soup = BeautifulSoup(s.get(url).content, 'lxml')
#     p = s.post(url, data=payload, verify=True)
#     print(p.text)


# import mechanize, re
#
# br = mechanize.Browser()
# br.set_handle_robots(False)   # ignore robots
# br.set_handle_refresh(False)  # can sometimes hang without this
# br.addheaders = [('User-agent', 'Firefox')]
# br.open(url)
# br.select_form('f')
# br.form['q'] = 'foo'
# br.submit()
# resp = None
#
# for link in br.links():
#     siteMatch = re.compile( 'www.foofighters.com' ).search( link.url )
#
#     if siteMatch:
#         resp = br.follow_link( link )
#         break
#
# content = resp.get_data()
# print content


# import selenium.webdriver
# driver = selenium.webdriver.PhantomJS()
# driver.get(url)
#
# driver.quit()

# import pandas as pd
# import html5lib
# import lxml
#
# tables = pd.read_html(url)
#
# print(tables[0])


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
#
#
# #replace with your firefox profile
# fp=webdriver.FirefoxProfile('C:/Users/SJ/AppData/Roaming/Mozilla/Firefox/Profiles/hlsfrs2o.scrape')
# #enter your url here
# url1='https://contributor-accounts.shutterstock.com/login'
# driver = webdriver.Firefox(fp)
# driver.get(url1)
#
# html_source = driver.page_source



# import requests
#
# def parse_one():
#     # USERNAME = input('yanushkov@gmail.com')
#     # PASSWORD = input('328993Standart')
#
#     LOGIN_URL = 'https://contributor-accounts.shutterstock.com/login'
#     URL = "https://submit.shutterstock.com/earnings/details?page=1&language=en&category=25_a_day&sort=desc&sorted_by=count&per_page=20"
#
#     session_requests = requests.session()
#
#     payload = {
#         "email": 'yanushkov@gmail.com',
#         "password": '328993Standart'
#     }
#
#     # Perform login
#     result = session_requests.post(LOGIN_URL, data=payload, headers=dict(referer=LOGIN_URL))
#
#     # Scrape journal_url
#     result = session_requests.get(URL, headers=dict(referer=URL))
#     soup = BeautifulSoup(result.content)
#     print(soup)
#
# parse_one()



import sha3
import hashlib
import request

# url = 'https://account.socialbakers.com/login'
myemail = "yanushkov@gmail.com"
mypassword = hashlib.sha512(b"328993Standart").hexdigest() #take SHA3 of password
payload = {'email':myemail, 'password':mypassword}
with session() as s:
    soup = BeautifulSoup(s.get(url).content)
    p = s.post(url, data = payload, verify=True)
    print(p.text)