from rest_framework import serializers
from .models import Transaction



class TransationUpload(serializers.Serializer):
    type = serializers.IntegerField()
    date = serializers.DateField(max_length=8)
    amount = serializers.FloatField(max_length=10)
    cpf = serializers.CharField(max_length=11)
    card = serializers.CharField(max_length=12)
    hour = serializers.DateTimeField(max_length=6)
    owner = serializers.CharField(max_length=14)
    store_name= serializers.CharField(max_length=19)  

    def validate_date(self, value):
        print(value)
        return value