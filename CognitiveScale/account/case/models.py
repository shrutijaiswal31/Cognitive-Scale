from django.db import models

# Create your models here.


class Account(models.Model):
    active_card = models.BooleanField()
    available_limit = models.FloatField()

    def __str__(self):
        return str(self.available_limit)


class Transaction(models.Model):
    merchant = models.CharField(max_length=20)
    amount = models.FloatField()
    time = models.DateTimeField()

    def __str__(self):
        return self.merchant


class Output(Account, models.Model):
    account = Account()
    violations = models.CharField(max_length=50)

    def __str__(self):
        return self.violations

