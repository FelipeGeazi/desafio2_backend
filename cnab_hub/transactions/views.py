from django.shortcuts import render, HttpResponse
from django.db import models
import pandas as pd
from .models import Transaction
from .forms import UploadFileForm
from django.http import HttpResponseRedirect



#from somewhere import handle_uploaded_file



def upload_file(request):
    if request.method == 'POST':
        cnab_file = request.FILES['file']
        df = pd.read_csv(cnab_file, delimiter=' ', header=None)
        for index, row in df.iterrows():
            type = row[1][0]
            date= row[1:98]
            amount = float(row[24:40])
            cpf = row[19:29]
            card = row[30:41]
            hour = row[42:47]
            owner = row[48:61]
            store_name = row[62:80]

            Transaction.objects.create(
                type = type,
                date=date,
                store_name=store_name,
                amount=amount,
                cpf=cpf,
                card=card,
                hour=hour,
                owner=owner)
        return HttpResponseRedirect('transactions/lista_operacoes/')
    else:
        return render(request, 'transactions/upload.html')    

def upload(request):
    return render(request, 'upload.html')


def lista_operacoes(request):
    operacoes = Transaction.objects.all()
    total_saldo = Transaction.objects.aggregate(models.Sum('saldo_conta'))
    return render(request, 'transactions/lista_operacoes.html', {'operacoes': operacoes, 'total_saldo': total_saldo})
   


""" def transactions(request):
    transactions = Transaction.objects.all()
    transactions_data = []
    for transaction in transactions:
        transactions_data.append({'store_name': transaction.store_name, 'amount': transaction.amount, 'date': transaction.date})
    return JsonResponse({'transactions': transactions_data}) """