#
# import requests.cookies
# import os
# import pickle
#
#
# def save_cookies(session, filename):
#     if not os.path.isdir(os.path.dirname(filename)):
#         return False
#     with open(filename, 'w') as f:
#         f.truncate()
#         pickle.dump(session.cookies._cookies, f)
#
#
# def load_cookies(session, filename):
#     if not os.path.isfile(filename):
#         return False
#
#     with open(filename) as f:
#         cookies = pickle.load(f)
#         if cookies:
#             jar = requests.cookies.RequestsCookieJar()
#             jar._cookies = cookies
#             session.cookies = jar
#         else:
#             return False

# from requests import session
#
# url = "https://contributor-accounts.shutterstock.com/login"
#
# payload = {
#     'action': 'login',
#     'username': 'yanushkov@gmail.com',
#     'password': '328993Standart'
# }
#
# with session() as c:
#     s = session()
#     c.post(url, data=payload)
#     response = c.get('http://example.com/protected_page.php')
#     print(response.headers)
#     print(response.text)

# import mechanize
# from urllib2 import urlopen
# from ClientForm import ParseResponse
#
# response = mechanize.urlopen("http://192.168.1.200/login.php")
# #print response.read()
# forms = ParseResponse(response, backwards_compat=False)
# form = forms[0]
# print form
# form["LOGIN_USER"] = "yanushkov@gmail.com"
# form["LOGIN_PASSWD"] = "328993Standart"
# print urlopen(form.click()).read()

# from ghost import Ghost
# import Cookie, LWPCookieJar
#
#
# url = "https://contributor-accounts.shutterstock.com/login"
#
# ghost = Ghost()
# with ghost.start() as session:
#     page, extra_resources = session.open(url)
#     assert page.http_status == 200 and 'jeanphix' in page.content

# from requests import session
# from bs4 import BeautifulSoup
#
#
# url = "https://contributor-accounts.shutterstock.com/login"
#
# data = {
#     'username': 'yanushkov@gmail.com',
#     'password': '328993Standart'
# }
#
# head = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# with  session() as s:
#     soup = BeautifulSoup(s.get("https://contributor-accounts.shutterstock.com/login").content)
#     form_data = soup.select("form[action^=/login?task] input")
#     data.update({inp["name"]: inp["value"] for inp in form_data if inp["name"] not in data})
#     s.post('https://contributor-accounts.shutterstock.com/login?task=user.login', data=data, headers=head)
#     resp = s.get('https://submit.shutterstock.com/dashboard?language=en')
#     print(1)

# import requests
# url1 = "https://contributor-accounts.shutterstock.com/login"
# url12 = 'https://submit.shutterstock.com/dashboard?language=en'
#
# payload = {'user_id': 'yanushkov@gmail.com', 'password': '328993Standart'}
# session = requests.Session() # save an instance of request.Session
# req = session.post(url1, data=payload, verify=False)
# ses = session.get(url12)
# print(1)

import requests
# api = 'https://6611f-f9862-5b4d1-b7789-6b2aa-ee745:1f538-1ca8e-8bcb0-7d676-cdff7-08b6b@api.shutterstock.com/v2/images/search?query=donkey'



#
# pre = 'https://'
# api = '@api.shutterstock.com/v2/images/search?'
# cliendID = '6611f-f9862-5b4d1-b7789-6b2aa-ee745'
# reg = ':'
# clientSecret = '1f538-1ca8e-8bcb0-7d676-cdff7-08b6b'
# type1 = 'added_date_start='
# page = 'page='
#
# _api = pre+cliendID+reg+clientSecret+api+type1+'2017-04-21&'+page+'80&per_page=500'
#
# q = 'https://'+cliendID+':'+clientSecret+'@api.shutterstock.com/v2/images/search?query=donkey'
#
# __api = pre+cliendID+reg+clientSecret+'@api.shutterstock.com/v2/user/subscriptions&scope=purchases.view'
cliendID = '6611f-f9862-5b4d1-b7789-6b2aa-ee745'
clientSecret = '1f538-1ca8e-8bcb0-7d676-cdff7-08b6b'

url='https://api.shutterstock.com/v2/oauth/authorize'
url2='https://api.shutterstock.com/'
scope='scope=licenses.create licenses.view purchases.view'
res_t='response_type=code'
ru='redirect_uri=localhost'

# ast = {"access_token":"1/eyJjbGllbnRfaWQiOiI2NjExZi1mOTg2Mi01YjRkMS1iNzc4OS02YjJhYS1lZTc0NSIsInJlYWxtIjoiY3VzdG9tZXIiLCJzY29wZSI6InVzZXIudmlldyIsInV0diI6IjJlYWQwYzhkNDMiLCJ1c2VybmFtZSI6InlhbnVzaGtvdiIsInVzZXJfaWQiOjExMjQzOTg0NSwib3JnYW5pemF0aW9uX2lkIjpudWxsLCJjdXN0b21lcl9pZCI6NDQ3NjQzMCwiZXhwIjoxNTAzMjU0NTMwfQ.RSiVJeS-vFOl3bQ0rfNyGpap0QSHBi6Tc2jhpV-Oo6KfmwM4yU_hRPszhZ94wNUGcuMjnz-K3RXAeN6A0K0jbA","token_type":"Bearer"}
#
# at='1/eyJjbGllbnRfaWQiOiI2NjExZi1mOTg2Mi01YjRkMS1iNzc4OS02YjJhYS1lZTc0NSIsInJlYWxtIjoiY3VzdG9tZXIiLCJzY29wZSI6InVzZXIudmlldyIsInV0diI6IjJlYWQwYzhkNDMiLCJ1c2VybmFtZSI6InlhbnVzaGtvdiIsInVzZXJfaWQiOjExMjQzOTg0NSwib3JnYW5pemF0aW9uX2lkIjpudWxsLCJjdXN0b21lcl9pZCI6NDQ3NjQzMCwiZXhwIjoxNTAzMjU0NTMwfQ.RSiVJeS-vFOl3bQ0rfNyGpap0QSHBi6Tc2jhpV-Oo6KfmwM4yU_hRPszhZ94wNUGcuMjnz-K3RXAeN6A0K0jbA'
# at2='2/vSrH7JUnbhRIrIPPi0dfm20paLFAQhTRlRYvVkRLkptldy6SvvCRTD1h8mQFrtgwOyQ0-REjVew2wZtiCOH9lOhmW6xE8T6UUIUi2ofAkFy3iMEPEbmbgziA_b08dWHkWQWn4C3x_yPE2_D95UsNIRTVpZtaA_874GygtwmourHe77fYpSgTmGV28jPg6Q0U'
# __api = url+'?'+scope+'&'+res_t+'&'+ru+'&client_id='+cliendID+'&state=lol'
# _api = url2+at+'/earnings'
# api='https://api.shutterstock.com/v2/user?access_token='

q = 'https://'+cliendID+':'+clientSecret+'@api.shutterstock.com/v2/user/subscriptions&scope=purchases.view'

request = requests.post(q, json=)
print (1)