from django.db import models
# Create your models here.
 

class Client(models.Model):
    #CharField <=> String
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',))
    

    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Code_CIN = models.IntegerField(primary_key=True)
    sex = models.CharField(max_length=1,choices=SEX_CHOICES,)
    Adresse = models.CharField(max_length=30)
    Date_of_creation= models.DateField()

    def __str__(self):
        return (self.Last_name)
    



     
 