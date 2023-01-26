from django.db import models

# Create your models here.


class Transaction(models.Model):
    type = models.IntegerField()
    date = models.DateField(max_length=8)
    amount = models.FloatField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField(max_length=6)
    owner = models.CharField(max_length=14)
    store_name= models.CharField(max_length=19)