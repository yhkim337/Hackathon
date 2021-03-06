from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import SportNewsData, FinanceNewsData, FinanceData, Tip, Encourage, Game, Notice


# Create your views here.
def index(request):
    finance_news = FinanceNewsData.objects.all().order_by('-created_at')[:7]
    finance_data = FinanceData.objects.all().order_by('-created_at')[:5]
    sport_news = SportNewsData.objects.all().order_by('-created_at')[:5]
    tip = Tip.objects
    encourage = Encourage.objects
    game = Game.objects
    notices = Notice.objects.all().order_by('created_at')[:3]
    return render(request, 'soldierLetter/index.html', {'finance_news':finance_news, 'finance_data':finance_data, 'sport_news':sport_news, 'tip':tip, 'encourage':encourage, 'game':game, 'notices':notices})

def notice(request):
    notices = Notice.objects.all()
    context = {'notices': notices}
    return render(request, 'soldierLetter/notice.html', context)

def review(request):
    return render(request, 'soldierLetter/review.html')