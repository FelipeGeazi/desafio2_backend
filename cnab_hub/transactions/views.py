from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import models
from django.core.files.storage import default_storage
from django.contrib import messages
from .models import Transaction
from .forms import UploadFileForm
from .serializers import TransactionSerializer
import pandas as pd 



def lista_operacoes(request):
    operacoes = Transaction.objects.all()
    total_saldo = Transaction.objects.aggregate(models.Sum('amount'))
    return render(request, 'transactions_interface/lista_operacoes.html', {'operacoes': operacoes, 'total_saldo': total_saldo})
   

def upload_file(request):
   
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        
        with open('transactions/arquivos/cnab.txt', 'wb+') as destination:
            for chunk in request.FILES['file'].chunks():
                destination.write(chunk)
        with open('transactions/arquivos/cnab.txt', 'r') as f:
            lista_de_listas = []
            for linha in f.read().split("\n"):
                lista_de_listas.append(linha) 
            print(lista_de_listas)   

        for row_string in lista_de_listas:       
            print(row_string)    
            print(lista_de_listas)
            
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
            owner = row_string[48:62]
            print(owner)
            store_name = row_string[62:]
            print(store_name)
            
            obj = { 'type': type, 'date': date, 'store_name': store_name, 'amount': amount, 'cpf': cpf, 'card': card, 'hour': hour, 'owner': owner }

            serializer = TransactionSerializer(data = obj)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return HttpResponseRedirect('lista_operacoes/')
    else:
        return render(request, 'transactions_interface/upload.html')    
 


