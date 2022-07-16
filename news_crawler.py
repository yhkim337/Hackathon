import requests
from bs4 import BeautifulSoup

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hackathon.settings")

import django
django.setup()

from soldierLetter.models import SportNewsData, FinanceNewsData, FinanceData

def sportnews_crawling():
    result = {}
    rank_url = 'https://sports.daum.net/worldsoccer'
    req = requests.get(rank_url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    list = soup.find("ol", {"class":"list_rank"}).findAll("li")
    sports_urls = []
    for li in list:
        link = li.find("strong")
        if len(sports_urls) < 5:
            sports_urls.append((link.find("a")['href']))

    for i in sports_urls:
        index = sports_urls.index(i) + 1
        url = '%s' % i
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('#cSub > div > h3')
        summary = soup.select_one('#cSub > div > div > div.btn_util.util_summary > div')
        if summary != None:
            summary_text = summary.select('div > p')
            head = title.get_text()
            for text in summary_text:
                body = text.get_text()
        else:
            head = title.get_text()
            body = ' '
        
        SportNewsData(index=index, title=head, summary=body).save()
        
    
    return result

def financenews_crawling():
    rank_url = 'https://finance.naver.com/news/mainnews.naver'
    req = requests.get(rank_url)

    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    list1 = soup.findAll("dt", {"class":"articleSubject"})
    list2 = soup.findAll("dd", {"class":"articleSubject"})
    title = []
    for a in list1:
        title.append(a.get_text())
    for a in list2:
        title.append(a.get_text())
    titles = []
    for i in title:
        temp = i.replace('\n', '')
        temp = temp[1:]
        titles.append(temp)
        
    return titles

def financedata_crawling():
    result = []
    rank_url = 'https://finance.naver.com/sise/sise_market_sum.naver'
    req = requests.get(rank_url)

    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    list = soup.find("tbody")
    items = list.findAll('tr', onmouseover="mouseOver(this)")
    for item in items :
        if len(result) < 5:
            basic_info = item.get_text()
            sinfo = basic_info.split("\n")
            index = sinfo[1]
            name = sinfo[2]
            price = sinfo[3]
            result.append(index)
            FinanceData(index=index, name=name, price=price).save()
    
    return result


if __name__=='__main__':
    financenews_data_dict = financenews_crawling()
    financedata_crawling()
    sportnews_crawling()
    for m in financenews_data_dict:
        FinanceNewsData(title=m).save()
