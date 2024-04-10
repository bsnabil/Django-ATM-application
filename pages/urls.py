

from . import views
from django.urls import path



urlpatterns = [

    path('accounts/', views.accounts,name='pages-accounts'),
    path('login/', views.login,name='pages-login'),
    path('users/', views.users,name='pages-users'),
    path('index/', views.index,name='pages-index'),
    path('addclient/',views.addclient,name='pages-addclient'),
    path('addaccount/',views.addaccount,name='pages-addaccount'),



]