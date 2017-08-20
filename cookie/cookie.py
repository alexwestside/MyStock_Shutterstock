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
api = 'https://6611f-f9862-5b4d1-b7789-6b2aa-ee745:1f538-1ca8e-8bcb0-7d676-cdff7-08b6b@api.shutterstock.com/v2/images/search?query=donkey'

request = requests.get(api)
print (1)