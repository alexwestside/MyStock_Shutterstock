import requests
import browsercookie
import datetime
from bs4 import BeautifulSoup


INIT_APPROVED_PHOTOS_URL = "https://submit.shutterstock.com/review.mhtml?type=photos"


class LoginCredentials:
    def __init__(self, cookies):
        self.cookies = cookies


class BatchesPendingApprovalWrapper:
    def __init__(self, login_credentials, url):
        self.url = url
        self.login_credentials = login_credentials

    def get_response(self):
        return requests.get(self.url, cookies=self.login_credentials.cookies)

    def get_batches(self):
        html = self.get_response().text
        soup_talbe = BeautifulSoup(html, 'html.parser')
        tr_search_results = soup_talbe.find('table', class_="table").find_all('tr');
        for tr_search_result in tr_search_results:
            td_search_results = tr_search_result.find_all('td')

            # удаляем последнюю строчку в таблице, так как это пейджинатор
            if len(td_search_results) < 3:
                continue

            print(int(td_search_results[0].get_text()))
            print(datetime.datetime.strptime(td_search_results[1].get_text(), '%m/%d/%Y').date())
            print(int(td_search_results[2].get_text()))


def main():
    yanushkov_login = LoginCredentials(browsercookie.chrome())
    yanushkov_request_wrapper = BatchesPendingApprovalWrapper(yanushkov_login, INIT_APPROVED_PHOTOS_URL)
    yanushkov_request_wrapper.get_batches()
    # print yanushkov_request_wrapper.get_response().text

main()