# Generated by Django 3.2 on 2021-04-29 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210429_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpage',
            name='name',
        ),
    ]
