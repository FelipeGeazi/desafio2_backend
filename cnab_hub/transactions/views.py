from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import models
from django.core.files.storage import default_storage
from django.contrib import messages
from .models import Transaction
from .forms import UploadFileForm
from .serializers import TransactionSerializer
import pandas as pd 
import locale
from django.db.models import Sum


""" def lista_operacoes(request):
    data = Transaction.objects.all()
    store_names = Transaction.objects.values_list('store_name', flat=True).distinct()
    operacoes = Transaction.objects.values('store_name').annotate(total_amount=Sum('amount'))
    return render(request, 'transactions_interface/lista_operacoes.html', {'operacoes': operacoes, 'store_names': store_names, 'data': data}) """


def lista_operacoes(request):
    data = Transaction.objects.all()
    store_names = Transaction.objects.values_list('store_name', flat=True).distinct()
    operacoes = Transaction.objects.values('store_name').annotate(total_amount=Sum('amount'))

    for operacao in operacoes:
        operacao['total_amount'] = sum(
            [
                transacao.amount if transacao.type not in [2, 3, 9] else -transacao.amount
                for transacao in data
                if transacao.store_name == operacao['store_name']
            ]
        )

    return render(request, 'transactions_interface/lista_operacoes.html', {'operacoes': operacoes, 'store_names': store_names, 'data': data})
           


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
             

        for row_string in lista_de_listas:       
          
            
            type = row_string[0]
            date= row_string[1:9]
            amount = row_string[9:19]
            cpf = row_string[19:30]
            card = row_string[30:42]
            hour = row_string[42:48]
            owner = row_string[48:62]
            store_name = row_string[62:]

            
            obj = { 'type': type, 'date': date, 'store_name': store_name, 'amount': float(amount)/100, 'cpf': cpf, 'card': card, 'hour': hour, 'owner': owner }

            serializer = TransactionSerializer(data = obj)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return HttpResponseRedirect('lista_operacoes/')
    else:
        return render(request, 'transactions_interface/upload.html')    
 


