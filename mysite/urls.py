from django.contrib import admin
from django.http import HttpResponse
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/',include('pages.urls')),
   # path('clients/',include('clients.urls')),

    #path('*', welcome),

]
