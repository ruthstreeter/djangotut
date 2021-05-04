from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True)


class Category(models.Model):
    name = models.CharField(max_length=45)


class Language(models.Model):
    name = models.CharField(max_length=36)
    abbreviated = models.CharField(max_length=3)
        

class Topic(models.Model):
    name = models.CharField(max_length=264, unique=True)


class Word(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    simile = models.ManyToManyField("Word", related_name='like')


class Webpage(models.Model):
    name = models.CharField(default=None, max_length=264, null=True)
    url = models.URLField(unique=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


class Translation(models.Model):
    name = models.CharField(max_length=45)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)


class Definition(models.Model):
    content = models.CharField(max_length=255)
    word = models.ForeignKey(Translation, on_delete=models.CASCADE)


class AccessRecord(models.Model):
    date = models.DateField()
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
