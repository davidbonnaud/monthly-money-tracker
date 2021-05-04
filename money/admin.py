from django.contrib import admin

from .models import Transaction, Balance

admin.site.register(Balance)
admin.site.register(Transaction)
# Register your models here.
