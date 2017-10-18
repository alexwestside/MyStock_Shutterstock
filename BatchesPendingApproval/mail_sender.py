from peewee import *
import smtplib
import time
import datetime


batches_db = SqliteDatabase('batches_statistic.db')
FROM_EMAIL = "fractal.gen@gmail.com"
FROM_PWD = "fractal123"
TO_EMAIL = "vadimrozov@gmail.com"


def send_email(subject, message, recipient):
    to = recipient if type(recipient) is list else [recipient]

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM_EMAIL, ", ".join(to), subject, message)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(FROM_EMAIL, FROM_PWD)
        server.sendmail(FROM_EMAIL, to, message)
        server.close()
        print("successfully sent the mail to ", recipient)
    except:
        print("failed to send mail to ", recipient)


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


def get_batches_by_date(date_submitted, batch_type):
    batches_db.connect()
    query = BatchInfo.select().where((BatchInfo.submitted == date_submitted) & (BatchInfo.type == batch_type))
    batches_db.close()
    return query


def main():
    filter_date = datetime.date.today() - datetime.timedelta(days=1)

    total = 0
    rejected = 0
    batches = get_batches_by_date(filter_date, 0)
    for batch_sh in batches:
        total += batch_sh.items
        rejected += batch_sh.rejected_items

    illustration_string = "Illustrations Submitted: " + str(total) + " Rejected: " + str(rejected)

    total = 0
    rejected = 0
    batches = get_batches_by_date(filter_date, 1)
    for batch_sh in batches:
        total += batch_sh.items
        rejected += batch_sh.rejected_items

    photos_string = "Photos Submitted: " + str(total) + " Rejected: " + str(rejected)

    print str(filter_date) + "\n" + illustration_string + "\n" + photos_string
    send_email('Upload status Shutterstock: ' + str(filter_date),
               illustration_string + "\n" + photos_string,
               TO_EMAIL)

while True:
    t = datetime.datetime.today()
    future = datetime.datetime(t.year, t.month, t.day, 8, 0)
    if t.hour >= 8:
        future += datetime.timedelta(days=1)
    time.sleep((future - t).seconds)
    main()