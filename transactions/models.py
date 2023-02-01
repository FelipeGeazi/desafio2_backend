from django.db import models
from babel.numbers import format_currency

# Create your models here.


class Transaction(models.Model):
    type = models.IntegerField()
    date = models.DateField(max_length=8)
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField(max_length=6)
    owner = models.CharField(max_length=14)
    store_name= models.CharField(max_length=19)

    
    def __str__(self):
        return format_currency(self.amount, 'BRL', locale='pt_BR')