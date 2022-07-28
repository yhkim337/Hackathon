from telnetlib import GA
from django.contrib import admin
from .models import SoccerNewsData, WorldSoccerNewsData, BaseballNewsData, WorldBaseballNewsData, BasketballNewsData, EsportsNewsData, FinanceNewsData, FinanceData, Tip, Encourage, Game, Notice, Review


# Register your models here.
admin.site.register(SoccerNewsData)
admin.site.register(WorldSoccerNewsData)
admin.site.register(BaseballNewsData)
admin.site.register(WorldBaseballNewsData)
admin.site.register(BasketballNewsData)
admin.site.register(EsportsNewsData)
admin.site.register(FinanceNewsData)
admin.site.register(FinanceData)
admin.site.register(Tip)
admin.site.register(Encourage)
admin.site.register(Game)
admin.site.register(Notice)
admin.site.register(Review)