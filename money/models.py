from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator

class Balance(models.Model):
  total = models.FloatField(default = 0.00)

class Transaction(models.Model):
  balance = models.ForeignKey(Balance, on_delete = models.CASCADE)
  amount = MoneyField(max_digits=14, 
                      decimal_places=2, 
                      default_currency='USD',
                      validators=[
                        MinMoneyValidator(0),
                        MaxMoneyValidator(100000),
                        MinMoneyValidator({'USD': 0}),
                        MaxMoneyValidator({'USD': 100000}),
                      ])
  details = models.CharField(max_length = 50)
  date_time = models.DateTimeField(auto_now=True)