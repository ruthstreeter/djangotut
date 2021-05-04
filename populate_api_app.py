import os 
import random


from faker import Faker
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from api.models import AccessRecord,Webpage,Topic, User

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(name=random.choice(topics))[0]
    t.save()
    return t 

def populate_webpages(n):
    print("populating webpages")
    webpages = []
    for entry in range(n):

        # get the topic for the entry
        top = add_topic()

        # Create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpages.append(
            Webpage.objects.get_or_create(
                topic=top,
                url=fake_url,
                name=fake_name)[0]
        )
    return webpages


def populate_access_records(webpages):
    print("populating access records")
    access_records = []
    for webpg in webpages:
        # create a fake access record for that webpage
        fake_date = fakegen.date()
        access_records.append(
            AccessRecord.objects.get_or_create(
                name=webpg,
                date=fake_date)[0]
        )
    return access_records


def populate_users(n=10):
    print("populating users")
    users = []
    for entry in range(n):
        fake_first = fakegen.first_name()
        fake_last = fakegen.last_name()
        fake_email = fakegen.email()
        users.append(
            User.objects.create(
                first_name=fake_first,
                last_name=fake_last,
                email=fake_email,
            )
        )
    return users

def populate(n=5):
    webpages = populate_webpages(n=n)
    access_records = populate_access_records(webpages=webpages)
    users = populate_users()


def main():
    print("populating script!")
    populate(20)
    print("Populating complete!")

if __name__ == '__main__':
    main()


