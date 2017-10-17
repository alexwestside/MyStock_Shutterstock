from peewee import *
import datetime
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

    def __repr__(self):
        return "{id: " + str(self.id) + " submitted: " + str(self.submitted) + " items: " + str(self.items) + " rejected: " + str(self.rejected_items) + "}"

    class Meta:
        database = batches_db


def get_batches_by_date(date_submitted):
    batches_db.connect()
    query = BatchInfo.select().where(BatchInfo.submitted == date_submitted)
    batches_db.close()
    return query


def main():
    total = 0
    rejected = 0
    filter_date = datetime.datetime.strptime("05/02/2017", '%m/%d/%Y').date()
    batches = get_batches_by_date(filter_date)
    for batch_sh in batches:
        total += batch_sh.items
        rejected += batch_sh.rejected_items

    print "Date:", filter_date, "submitted files:", total, "rejected files:", rejected
    send_email('Upload status illustration Shutterstock: ' + str(filter_date),
               "Illustrations submitted: " + str(total) + " rejected: " + str(rejected),
               TO_EMAIL)

while True:
    t = datetime.datetime.today()
    future = datetime.datetime(t.year, t.month, t.day, 8, 0)
    if t.hour >= 8:
        future += datetime.timedelta(days=1)
    print (future - t).seconds
    time.sleep((future - t).seconds)
    main()