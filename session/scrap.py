
import requests

email = 'yanushkov@gmail.com'
password = '328993Standart'


with requests.Session() as session:
    url = "https://contributor-accounts.shutterstock.com/login"
    LOGIN = "username"
    PASSWORD = "password"
    dann = {'username': 'yanushkov@gmail.com', 'pass': '328993Standart'}
    session.get(url)
    session.post(url, dann)
    url2 = "https://submit.shutterstock.com/dashboard?language=en"
    r = session.get(url2)

print(r.text)