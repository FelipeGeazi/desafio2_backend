from rest_framework import serializers
from .models import Transaction
import locale



class TransactionSerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField()
    class Meta:
        model = Transaction
        fields = ('type', 'date', 'amount', 'cpf', 'card', 'hour', 'owner', 'store_name')

    def get_amount(self, obj):
        amount = obj.amount / 100
        amount_formated = locale.currency(amount, grouping=True)
        return amount_formated