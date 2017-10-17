import requests
import browsercookie
import datetime
from peewee import *
from bs4 import BeautifulSoup


INIT_APPROVED_PHOTOS_URL = "https://submit.shutterstock.com/review.mhtml?type=photos"
batches_db = SqliteDatabase('batches_statistic.db')


class BatchInfo(Model):
    id = IntegerField(primary_key=True)
    submitted = DateField()
    items = IntegerField()

    def __repr__(self):
        return "{id: " + str(self.id) + " submitted: " + str(self.submitted) + " items: " + str(self.items) + "}"

    class Meta:
        database = batches_db


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

        batches = []

        for tr_search_result in tr_search_results:
            td_search_results = tr_search_result.find_all('td')

            # delete last line in table, because it is paginator
            if len(td_search_results) < 3:
                continue

            id = int(td_search_results[0].get_text())
            submitted = datetime.datetime.strptime(td_search_results[1].get_text(), '%m/%d/%Y').date()
            items = int(td_search_results[2].get_text())
            batches.append(BatchInfo(id=id, submitted=submitted, items=items))

        return batches


def save_to_db(batches):
    batches_db.connect()
    if not BatchInfo.table_exists():
        batches_db.create_table(BatchInfo)

    for batch_sh in batches:
        query = BatchInfo.select().where(BatchInfo.id == batch_sh.id)
        if not query.exists():
            saved = BatchInfo.create(id=batch_sh.id, submitted=batch_sh.submitted, items=batch_sh.items)
            print saved

    batches_db.close()


def get_batches_by_date(date_submitted):
    batches_db.connect()
    query = BatchInfo.select().where(BatchInfo.submitted == date_submitted)
    batches_db.close()
    return query


def main():
    yanushkov_login = LoginCredentials(browsercookie.chrome())
    yanushkov_request_wrapper = BatchesPendingApprovalWrapper(yanushkov_login, INIT_APPROVED_PHOTOS_URL)
    batches = yanushkov_request_wrapper.get_batches()
    save_to_db(batches)

    total = 0
    filter_date = datetime.datetime.strptime("05/02/2017", '%m/%d/%Y').date()
    batches = get_batches_by_date(filter_date)
    for batch_sh in batches:
        total += batch_sh.items
        print batch_sh.id, batch_sh.submitted, batch_sh.items

    print "Date:", filter_date, "submitted files:", total

main()