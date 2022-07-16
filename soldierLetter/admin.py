from telnetlib import GA
from django.contrib import admin
from .models import SportNewsData, FinanceNewsData, FinanceData, Tip, Encourage, Game


# Register your models here.
admin.site.register(SportNewsData)
admin.site.register(FinanceNewsData)
admin.site.register(FinanceData)
admin.site.register(Tip)
admin.site.register(Encourage)
admin.site.register(Game)