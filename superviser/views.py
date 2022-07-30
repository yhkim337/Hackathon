from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from soldierLetter.models import SoccerNewsData, WorldSoccerNewsData, BaseballNewsData, WorldBaseballNewsData, BasketballNewsData, EsportsNewsData, FinanceNewsData, FinanceData
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from django.shortcuts import redirect
from django.contrib.auth.models import User
import os

# Create your views here.
def soccer_news_crawling():
    result = {}
    rank_url = 'https://sports.daum.net/soccer'
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
        
        SoccerNewsData(index=index, title=head, summary=body).save()
        
    return result

def worldsoccer_news_crawling():
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
        
        WorldSoccerNewsData(index=index, title=head, summary=body).save()
        
    return result

def baseball_news_crawling():
    result = {}
    rank_url = 'https://sports.daum.net/baseball'
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
        
        BaseballNewsData(index=index, title=head, summary=body).save()
        
    return result

def worldbaseball_news_crawling():
    result = {}
    rank_url = 'https://sports.daum.net/worldbaseball'
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
        
        WorldBaseballNewsData(index=index, title=head, summary=body).save()
        
    return result

def basketball_news_crawling():
    result = {}
    rank_url = 'https://sports.daum.net/basketball'
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
        
        BasketballNewsData(index=index, title=head, summary=body).save()
        
    return result

def esports_news_crawling():
    result = {}
    rank_url = 'https://sports.daum.net/esports'
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
        
        EsportsNewsData(index=index, title=head, summary=body).save()
        
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

def index(request):
    if request.method == "POST":
        financenews_data_dict = financenews_crawling()
        financedata_crawling()
        # soccer_news_crawling()
        worldsoccer_news_crawling()
        # baseball_news_crawling()
        # worldbaseball_news_crawling()
        # basketball_news_crawling()
        # esports_news_crawling()
        for m in financenews_data_dict:
            FinanceNewsData(title=m).save()
        return redirect('superviser')
    
    date = WorldSoccerNewsData.objects.all().order_by('-created_at')[:1]
    final_date = date[0]

    return render(request, 'superviser/superviser.html', {'final_date':final_date})


def send_letter(request):
    users = User.objects.all()
    address = "서울대학교"
    address_detail = "인대전"
    sendername = "인대전"
    relation = "서비스"
    password = "1234"
    for user in users:
        if user.profile.army_type == "공군":
            name = user.profile.name
            birthYear = user.profile.birthday[0:4]
            birthMonth = user.profile.birthday[5:7]
            birthDay = user.profile.birthday[8:10]
            title = "오늘의 뉴스"
            content = ""
            if user.profile.sub_type1 == "국내축구":
                content1 = SoccerNewsData.objects.all().order_by('-created_at')[:5]
                for news in content1:
                    content = content + news.title + "\n" + news.summary + "\n"
            elif user.profile.sub_type1 == "해외축구":
                content1 = WorldSoccerNewsData.objects.all().order_by('-created_at')[:5]
                for news in content1:
                    content = content + news.title + "\n" + news.summary + "\n"
            elif user.profile.sub_type1 == "국내야구":
                content1 = BaseballNewsData.objects.all().order_by('-created_at')[:5]
                for news in content1:
                    content = content + news.title + "\n" + news.summary + "\n"
            elif user.profile.sub_type1 == "해외야구":
                content1 = WorldBaseballNewsData.objects.all().order_by('-created_at')[:5]
                for news in content1:
                    content = content + news.title + "\n" + news.summary + "\n"
            elif user.profile.sub_type1 == "농구":
                content1 = BasketballNewsData.objects.all().order_by('-created_at')[:5]
                for news in content1:
                    content = content + news.title + "\n" + news.summary + "\n"
            elif user.profile.sub_type1 == "이스포츠":
                content1 = EsportsNewsData.objects.all().order_by('-created_at')[:5]
                for news in content1:
                    content = content + news.title + "\n" + news.summary + "\n"
            elif user.profile.sub_type1 == "주식":
                content1 = FinanceNewsData.objects.all().order_by('-created_at')[:7]
                content2 = FinanceData.objects.get(name=user.profile.stock_type)
                content = content + content2.name + ":" + content2.price + "\n"
                for news in content1:
                    content = content + news.title + "\n"
            
            content = content + " " + "\n"

            if user.profile.sub_type2 == "국내축구":
                content1 = SoccerNewsData.objects.all().order_by('-created_at')[:5]
                for news in content1:
                    content = content + news.title + "\n" + news.summary + "\n"
            elif user.profile.sub_type2 == "해외축구":
                content1 = WorldSoccerNewsData.objects.all().order_by('-created_at')[:5]
                for news in content1:
                    content = content + news.title + "\n" + news.summary + "\n"
            elif user.profile.sub_type2 == "국내야구":
                content1 = BaseballNewsData.objects.all().order_by('-created_at')[:5]
                for news in content1:
                    content = content + news.title + "\n" + news.summary + "\n"
            elif user.profile.sub_type2 == "해외야구":
                content1 = WorldBaseballNewsData.objects.all().order_by('-created_at')[:5]
                for news in content1:
                    content = content + news.title + "\n" + news.summary + "\n"
            elif user.profile.sub_type2 == "농구":
                content1 = BasketballNewsData.objects.all().order_by('-created_at')[:5]
                for news in content1:
                    content = content + news.title + "\n" + news.summary + "\n"
            elif user.profile.sub_type2 == "이스포츠":
                content1 = EsportsNewsData.objects.all().order_by('-created_at')[:5]
                for news in content1:
                    content = content + news.title + "\n" + news.summary + "\n"
            elif user.profile.sub_type2 == "주식":
                content1 = FinanceNewsData.objects.all().order_by('-created_at')[:7]
                content2 = FinanceData.objects.get(name=user.profile.stock_type)
                content = content + content2.name + ":" + content2.price + "\n"
                for news in content1:
                    content = content + news.title + "\n"

            print(content)
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")

            options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            s = Service(executable_path=os.environ.get("CHROMEDRIVER_PATH"))
            driver = webdriver.Chrome(service=s, options=options)
            driver.implicitly_wait(2)
            driver.get('https://www.airforce.mil.kr/user/indexSub.action?codyMenuSeq=156893223&siteId=last2&menuUIType=sub')
            driver.find_element(By.CSS_SELECTOR, "#searchName").send_keys(name)
            driver.find_element(By.CSS_SELECTOR, "#birthYear").send_keys(birthYear)
            driver.find_element(By.CSS_SELECTOR, "#birthMonth").send_keys(birthMonth)
            driver.find_element(By.CSS_SELECTOR, "#birthDay").send_keys(birthDay)
            driver.implicitly_wait(1)
            driver.find_element(By.CSS_SELECTOR, "#btnNext").click()

            driver.implicitly_wait(1)
            driver.switch_to.window(driver.window_handles[1])

            driver.find_element(By.CSS_SELECTOR, "#emailPic-container > ul > li > input").click()

            driver.switch_to.window(driver.window_handles[0])
            driver.find_element(By.CSS_SELECTOR, "#btnNext").click()

            driver.implicitly_wait(1)

            driver.find_element(By.CSS_SELECTOR, "#emailPic-container > div.UIbtn > span > input[type=button]").click()
            driver.find_element(By.CSS_SELECTOR, "#emailPic-container > form > div.UIview > table > tbody > tr:nth-child(3) > td > div:nth-child(1) > span > input").click()

            driver.implicitly_wait(5)

            # driver.switch_to.window(driver.window_handles[1])

            # driver.find_element(By.CSS_SELECTOR, "#proceed-button").click()
            # driver.find_element(By.CSS_SELECTOR, "#keyword").send_keys(address)
            # driver.find_element(By.CSS_SELECTOR, "#searchContentBox > div.search-wrap > fieldset > span > input[type=button]:nth-child(2)").click()
            # driver.find_element(By.CSS_SELECTOR, "#roadAddrTd1 > a").click()
            # driver.find_element(By.CSS_SELECTOR, "#rtAddrDetail").send_keys(address_detail)
            # driver.find_element(By.CSS_SELECTOR, "#resultData > div > a").click()

            # driver.switch_to.window(driver.window_handles[0])

            # driver.find_element(By.CSS_SELECTOR, "#senderName").send_keys(sendername)
            # driver.find_element(By.CSS_SELECTOR, "#relationship").send_keys(relation)
            # driver.find_element(By.CSS_SELECTOR, "#title").send_keys(title)
            # driver.find_element(By.CSS_SELECTOR, "#contents").send_keys(content)
            # driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)

            driver.close()
    date = WorldSoccerNewsData.objects.all().order_by('-created_at')[:1]
    final_date = date[0]
    send = True
    return render(request, 'superviser/superviser.html', {'final_date':final_date, 'send':send})