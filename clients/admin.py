from django.contrib import admin
from .models import Client
 
# Register your models here.


#display list all fields in admin panel
class ClientAdmin(admin.ModelAdmin):
    list_display = ('First_name','Last_name','Code_CIN','Adresse','sex','Date_of_creation')
    
admin.site.register(Client,ClientAdmin)
