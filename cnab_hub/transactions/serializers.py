from rest_framework import serializers
from .models import Transaction
import locale



class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = ('type', 'date', 'amount', 'cpf', 'card', 'hour', 'owner', 'store_name')

    def get_amount(self, obj):
        amount1= amount/ 100
        amount = locale.currency(amount1, grouping=True)
        return amount