from django.shortcuts import render
from api.models import User
# Create your views here.

def index(request):
    users = User.objects.all()
    return render(request,'api/index.html', context={ "people": users })

def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request,'api/users.html',context=user_dict)
