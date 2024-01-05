from django.contrib import admin

from debtsApp.models import Debtor, Debt

# Register your models here.
admin.site.register(Debtor)
admin.site.register(Debt)