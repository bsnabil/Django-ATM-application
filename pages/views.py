from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def login(request):

    return render(request,'pages/login.html')
def users(request):

    return render(request,'pages/users.html')

def index(request):

    return render(request,'pages/index.html')

def accounts(request):
    return render(request ,'pages/accounts.html')

def addclient(request):
    return render(request,'pages/addclient.html')

def addaccount(request):
    return render(request,'pages/addaccount.html')







 
