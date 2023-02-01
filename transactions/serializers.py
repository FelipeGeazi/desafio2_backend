from rest_framework import serializers
from .models import Transaction
import locale



class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = ('type', 'date', 'amount', 'cpf', 'card', 'hour', 'owner', 'store_name')

    def to_representation(self, instance):
        if instance.type in [2, 3, 9]:
            instance.amount = instance.amount * -1
        return super().to_representation(instance)