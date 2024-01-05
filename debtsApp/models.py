from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Debtor(models.Model):
    SEX_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    sex = models.CharField(max_length=1, choices=SEX_CHOICE)
    address = models.CharField(max_length=100)
    
    def total_debt(self):
        if(self.debts.aggregate(Sum('amount'))['amount__sum'] != None):
            return self.debts.aggregate(Sum('amount'))['amount__sum']
        else:
            return 0

    def __str__(self):
        return self.surname

class Debt(models.Model):
    reason = models.CharField(max_length=200)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE, null=False, related_name='debts')

    def __str__(self):
        return "Reason: "+self.reason+", ammount: "+str(self.amount)
    