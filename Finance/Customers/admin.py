from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Stocks)
admin.site.register(models.Customer)