from multiprocessing import connection
from django.contrib import admin
from .models import accounts

# Register your models here.


#display list all fields in admin panel
 
class AccountAdmin(admin.ModelAdmin):

      list_display = ('Id','Amount','Date_of_creation')
      


admin.site.register(accounts,AccountAdmin)

