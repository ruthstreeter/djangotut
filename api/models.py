from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)








class Language(models.Model):
    name = models.CharField(max_length=36)
    abbreviated = models.CharField(max_length=3)


class Category(models.Model):
    name = models.CharField(max_length=45)


class Word(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    simile = models.ManyToManyField('Word', related_name="like")


class Translation(models.Model):
    name = models.CharField(max_length=45)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)


class Definition(models.Model):
    word = models.ForeignKey(Translation, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
