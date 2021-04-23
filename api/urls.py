from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pika$', views.pika, name='index'),
    url(r'^pikas$', views.pikas, name='index'),
    url(r'^sy$', views.sy, name='index'),
]
