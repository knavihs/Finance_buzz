from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Stocks(models.Model):
    Stock_name_symbol=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.Stock_name_symbol
    class Meta:
        verbose_name_plural = "Stocks"

class Customer(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="customer")
    companies_invested=models.ForeignKey(to=Stocks,on_delete=models.CASCADE,related_name='company_name')

