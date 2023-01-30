from rest_framework import serializers
from .models import Transaction
import locale



class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = ('type', 'date', 'amount', 'cpf', 'card', 'hour', 'owner', 'store_name')

    def to_representation(self, instance):
        if instance.type == 2:
            instance.amount = "-" + str(instance.amount)
        return super().to_representation(instance)