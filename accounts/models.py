import random
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from clients.models import Client

 # Create your models here.




class accounts(models.Model):
    
    Id= models.IntegerField(Client,
            default=random. randint(1000, 20000),validators=[MaxValueValidator(9999999),
                                               MinValueValidator(1000000)],on_delete=models.CASCADE)
    Amount = models.IntegerField(default='250',validators=[MinValueValidator(250)])
    Date_of_creation= models.DateField()

    

     

 