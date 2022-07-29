from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import SoccerNewsData, WorldSoccerNewsData, BaseballNewsData, WorldBaseballNewsData, BasketballNewsData, EsportsNewsData, FinanceNewsData, FinanceData, Tip, Encourage, Game, Notice, Review
from django.shortcuts import redirect


# Create your views here.
def index(request):
    finance_news = FinanceNewsData.objects.all().order_by('-created_at')[:7]
    finance_data = FinanceData.objects.all().order_by('-created_at')[:3]
    soccer_news = SoccerNewsData.objects.all().order_by('-created_at')[:5]
    worldsoccer_news = WorldSoccerNewsData.objects.all().order_by('-created_at')[:4]
    baseball_news = BaseballNewsData.objects.all().order_by('-created_at')[:5]
    worldbaseball_news = WorldBaseballNewsData.objects.all().order_by('-created_at')[:5]
    basketball_news = BasketballNewsData.objects.all().order_by('-created_at')[:5]
    esports_news = EsportsNewsData.objects.all().order_by('-created_at')[:5]
    tip = Tip.objects
    encourage = Encourage.objects
    game = Game.objects
    notices = Notice.objects.all().order_by('created_at')[:3]
    reviews = Review.objects.all().order_by('-created_at')[:3]
    return render(request, 'soldierLetter/index.html',
     {'finance_news':finance_news, 'finance_data':finance_data, 'soccer_news':soccer_news, 'worldsoccer_news':worldsoccer_news, 'baseball_news':baseball_news,
      'worldbaseball_news':worldbaseball_news, 'basketball_news':basketball_news, 'esports_news':esports_news,
      'tip':tip, 'encourage':encourage, 'game':game, 'notices':notices, 'reviews':reviews})

def notice(request):
    notices = Notice.objects.all().order_by('-created_at')
    context = {'notices': notices}
    return render(request, 'soldierLetter/notice.html', context)

class ReviewView:
    def review_read(request):
        reviews = Review.objects.all().order_by('-created_at')
        content = {'reviews': reviews}
        return render(request, 'soldierLetter/review.html', content)

    def review_new(request):
        if request.method == 'POST':
            content = request.POST['content']
            Review.objects.create(content=content, author=request.user)
            return redirect('/intro/review')
        return render(request, 'soldierLetter/new_review.html')
    
    def review_edit(request, rid):
        if request.method == 'POST':
            review = Review.objects.get(id=rid)
            review.content = request.POST['content']
            review.save()
            return redirect('/intro/review')
        review = Review.objects.get(id=rid)
        return render(request, 'soldierLetter/edit_review.html', {'review':review})

    def review_delete(request, rid):
        review = Review.objects.get(id=rid)
        review.delete()

        return redirect('/intro/review')