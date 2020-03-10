from rest_framework import serializers
from .models import Account, Output


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['active_card', 'available_limit']


class OutputSerializer(serializers.ModelSerializer):


    class Meta:
        model = Output
        fields = ['account', 'violations']

