from django.shortcuts import render
from django.utils import timezone
from .models import SportNewsData, FinanceNewsData, FinanceData, Tip, Encourage, Game


# Create your views here.
def base(request):
    finance_news = FinanceNewsData.objects.all().order_by('-created_at')[:7]
    finance_data = FinanceData.objects.all().order_by('-created_at')[:5]
    sport_news = SportNewsData.objects.all().order_by('-created_at')[:5]
    tip = Tip.objects
    encourage = Encourage.objects
    game = Game.objects
    return render(request, 'soldierLetter/base.html', {'finance_news':finance_news, 'finance_data':finance_data, 'sport_news':sport_news, 'tip':tip, 'encourage':encourage, 'game':game})

def notice(request):
    return render(request, 'soldierLetter/notice.html')

def review(request):
    return render(request, 'soldierLetter/review.html')