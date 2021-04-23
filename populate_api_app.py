import os 
import random


from faker import Faker
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from api.models import AccessRecord,Webpage,Topic

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t 


def populate(N=5):

    for entry in range(N):

        # get the topic for the entry
        top = add_topic()

        # Create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]



def main():
    print("populating script!")
    populate(20)
    print("Populating complete!")

if __name__ == '__main__':
    main()


