# Generated by Django 3.2 on 2021-04-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_webpage_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='name',
            field=models.CharField(default=None, max_length=264, null=True),
        ),
    ]
