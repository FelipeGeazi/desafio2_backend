from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import models
from django.core.files.storage import default_storage
from django.contrib import messages
from .models import Transaction
from .forms import UploadFileForm
import pandas as pd 
from dateutil import parser


def lista_operacoes(request):
    operacoes = Transaction.objects.all()
    total_saldo = Transaction.objects.aggregate(models.Sum('amount'))
    return render(request, 'transactions_interface/lista_operacoes.html', {'operacoes': operacoes, 'total_saldo': total_saldo})
   

def upload_file(request):
    if request.method == 'POST':
        cnab_file = request.FILES['file']
        df = pd.read_csv(cnab_file, delimiter=' ', header=None)
        for index, row in df.iterrows():
            print(index)
            print(row)
            row_string = "".join(map(str,row))
            print(row_string)

            type = row_string[0]
            print(type)
            date= row_string[1:9]
            print(date)
            amount = row_string[9:19]
            print(amount)
            cpf = row_string[19:30]
            print(cpf)
            card = row_string[30:42]
            print(card)
            hour = row_string[42:48]
            print(hour)
            owner = row_string[48:63]
            print(owner)
            store_name = row_string[63:]
            print(store_name)

            Transaction.objects.create(
                type = type,
                date= date,
                store_name=store_name,
                amount=amount,
                cpf=cpf,
                card=card,
                hour=hour,
                owner=owner)
        return HttpResponseRedirect('transactions_interface/lista_operacoes/')
    else:
        return render(request, 'transactions_interface/upload.html')    
 


