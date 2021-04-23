from random import choice

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    people = [
        {'nickname': "Ruthiness", 'name': 'Ruth Ines Streeter'},
        {'nickname': "GrannyCook", 'name': 'Jane America Streeter'},
        {'nickname': "Neens", 'name': 'Nena Faith Streeter'},
        {'nickname': "Luky", 'name': 'Luke Charles Streeter'},
    ]
    return render(request, "api/index.html", context={"people": people})

def pika(request):
    quality = choice(["smell", "taste", "look", "sound", "feel"])
    qualifier = choice(["trashy", "fat", "beautiful", "tall", "short", "old", "burnt", "young", "medium size", "stinky", "happy"])
    animal = choice(["rat", "snake", "bear", "caterpillar", "baby person", "elephant", "beaver", "giraffe", "principal of a school"])
    name = choice(["Barbara", "Tom", "PikaPika", "Mary had a litle lamb", "Georgey", "Nilsy Poo"])
    return render(request, "poop/index.html", context={"name": name, "animal": animal, "quality": quality, "qualifier": qualifier})

def pikas(request):
    return HttpResponse("<em>World to chus again...</em>")

def sy(request):
    return HttpResponse("<em>World to duck again...</em>")
