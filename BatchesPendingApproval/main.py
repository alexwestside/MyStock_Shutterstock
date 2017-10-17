import requests
import browsercookie
import datetime
import time
from time import gmtime, strftime
import sys
from peewee import *
from bs4 import BeautifulSoup


APPROVED_PHOTOS_URL = "https://submit.shutterstock.com/review.mhtml?type=photos"
REJECTED_PHOTOS_URL = "https://submit.shutterstock.com/review.mhtml?approved=-1&type=photos"
batches_db = SqliteDatabase('batches_statistic.db')


def printer(data):
    sys.stdout.write("\r")
    sys.stdout.write(data)
    sys.stdout.flush()


class BatchInfo(Model):
    id = IntegerField(primary_key=True)
    submitted = DateField()
    items = IntegerField()
    rejected_items = IntegerField()
    # 0 - illustrations, 1 - photos
    type = IntegerField(default=0)

    def __repr__(self):
        return "{id: " + str(self.id) + " submitted: " + str(self.submitted) + " items: " + str(self.items) + " rejected: " + str(self.rejected_items) + " type: "+ str(self.type) + "}"

    class Meta:
        database = batches_db


class LoginCredentials:
    def __init__(self, cookies, type):
        self.cookies = cookies
        self.type = type


class BatchesPendingApprovalWrapper:
    def __init__(self, login_credentials, url):
        self.login_credentials = login_credentials
        self.url = url

    def get_response(self):
        return requests.get(self.url, cookies=self.login_credentials.cookies)

    def get_batches(self):
        html = self.get_response().text
        soup_talbe = BeautifulSoup(html, 'html.parser')
        table = soup_talbe.find('table', class_="table")
        if table is None:
            return []

        tr_search_results = table.find_all('tr');

        batches = []

        for tr_search_result in tr_search_results:
            td_search_results = tr_search_result.find_all('td')

            # delete last line in table, because it is paginator
            if len(td_search_results) < 3:
                continue

            id = int(td_search_results[0].get_text())
            submitted = datetime.datetime.strptime(td_search_results[1].get_text(), '%m/%d/%Y').date()
            items = int(td_search_results[2].get_text())
            batches.append(BatchInfo(id=id, submitted=submitted, items=items, type=self.login_credentials.type))

        return batches


class BatchesRejectedWrapper:
    def __init__(self, login_credentials, url):
        self.url = url
        self.login_credentials = login_credentials

    def get_response(self):
        return requests.get(self.url, cookies=self.login_credentials.cookies)

    def get_batches(self):
        html = self.get_response().text
        soup_talbe = BeautifulSoup(html, 'html.parser')
        table = soup_talbe.find('table', class_="table")
        if table is None:
            return []

        tr_search_results = table.find_all('tr');

        batches = []

        for tr_search_result in tr_search_results:
            td_search_results = tr_search_result.find_all('td')

            # delete last line in table, because it is paginator
            if len(td_search_results) < 3:
                continue

            id = int(td_search_results[0].get_text())
            submitted = datetime.datetime.strptime(td_search_results[1].get_text(), '%m/%d/%Y').date()
            rejected_items = int(td_search_results[2].get_text())
            batches.append(BatchInfo(id=id, submitted=submitted, rejected_items=rejected_items, type=self.login_credentials.type))

        return batches


def save_rejected_to_db(batches):
    batches_db.connect()
    if not BatchInfo.table_exists():
        batches_db.close()
        return

    for batch_sh in batches:
        batch_db = BatchInfo.select().where(BatchInfo.id == batch_sh.id)
        if batch_db.exists():
            res = batch_db.get()
            res.rejected_items = batch_sh.rejected_items
            saved = res.save()
            print saved, batch_sh.id, "updated with rejections"

    batches_db.close()


def save_to_db(batches):
    batches_db.connect()
    if not BatchInfo.table_exists():
        batches_db.create_table(BatchInfo)

    for batch_sh in batches:
        query = BatchInfo.select().where(BatchInfo.id == batch_sh.id)
        if not query.exists():
            saved = BatchInfo.create(id=batch_sh.id, submitted=batch_sh.submitted, items=batch_sh.items, rejected_items=0, type=batch_sh.type)
            print saved, "added to db"

    batches_db.close()


def main():
    credentials = [ LoginCredentials(browsercookie.chrome(), 0), LoginCredentials(browsercookie.firefox(), 1)]
    for credential in credentials:
        pending_wrapper = BatchesPendingApprovalWrapper(credential, APPROVED_PHOTOS_URL)
        batches = pending_wrapper.get_batches()
        save_to_db(batches)

        rejected_wrapper = BatchesRejectedWrapper(credential, REJECTED_PHOTOS_URL)
        batches = rejected_wrapper.get_batches()
        save_rejected_to_db(batches)


while True:
    printer(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " getting latest batches:")
    main()
    time.sleep(3600)
