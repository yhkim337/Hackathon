from django.shortcuts import render
from .models import SportNewsData, FinanceNewsData, FinanceData, Tip, Encourage, Game


# Create your views here.
def base(request):
    finance_news = FinanceNewsData.objects
    finance_data = FinanceData.objects.all().order_by('-created_at')[:5]
    sport_news = SportNewsData.objects.all().order_by('-created_at')[:5]
    tip = Tip.objects
    encourage = Encourage.objects
    game = Game.objects
    return render(request, 'soldierLetter/base.html', {'finance_news':finance_news, 'finance_data':finance_data, 'sport_news':sport_news, 'tip':tip, 'encourage':encourage, 'game':game})
