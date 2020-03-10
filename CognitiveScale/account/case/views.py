from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Account, Output, Transaction
from .serializer import OutputSerializer, AccountSerializer
from datetime import datetime, timedelta
import json

# Create your views here.


class AccountReg(APIView):

    def post(self, request):
        if request.method == 'POST':
            output = Output()

            if Account.objects.exists():
                account = Account.objects.get()
                serializer = AccountSerializer(account)
                account = serializer.data
                violations = "Account already initialized"
            else:
                account = json.loads(request.body)["account"]
                violations = ""
                acc = Account(**account)
                acc.save()
            output.account.active_card = account['active_card']
            output.account.available_limit = account['available_limit']
            accserailizer = AccountSerializer(output.account)
            output.account = accserailizer.data
            output.violations = violations
            serializer = OutputSerializer(output)


            return Response(serializer.data)


class TransReg(APIView):

    def post(self, request):
        if request.method == 'POST':
            output = Output()
            account = Account()
            transaction = json.loads(request.body)["transaction"]
        if not Account.objects.exists():
            violations = "account not initialized"
        else:
            account = Account.objects.get()
            if account.available_limit < transaction['amount']:
                violations = "insufficient balance"
            else:
                end = datetime.strptime(transaction['time'],
                                        '%Y-%m-%dT%H:%M:%S.%fZ')
                start = end - timedelta(minutes=2)
                if Transaction.objects.filter(merchant=transaction['merchant'],
                                                time__range=[start, end]).\
                        count() >= 1:
                    violations = "doubled transaction"
                elif Transaction.objects.filter(time__range=[start, end]).\
                        count() >= 3:
                    violations = "high-frequency-small-interval"

                else:
                    violations = ""
                    account.available_limit = account.available_limit - \
                        transaction['amount']
                    account.save()
                    tr = Transaction(**transaction)
                    tr.save()
        accserailizer = AccountSerializer(account)
        output.account = accserailizer.data
        output.violations = violations
        serializer = OutputSerializer(output)

        return Response(serializer.data)
