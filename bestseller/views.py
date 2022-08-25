from datetime import datetime
from django.shortcuts import render
from common.decorators import login_required
from .models import *
import requests
from bs4 import BeautifulSoup
# Create your views here.


@login_required
def bestSellerList(request, **kwargs):
    
    from datetime import timedelta, date
    def get_week_no():
        today = date.today()
        firstday = today.replace(day=1)
        
        if firstday.weekday() == 6:
            origin = firstday
        elif firstday.weekday() < 3:
            origin = firstday - timedelta(days=firstday.weekday() + 1)
        else:
            origin = firstday + timedelta(days=6-firstday.weekday())
        
        stdweek = str(today.year) + str(today.month) + str((today - origin).days // 7 + 1)
        url = 'https://www.aladin.co.kr/shop/common/wbest.aspx?Year=%YEAR%&Month=%MONTH%&Week=%WEEK%'.replace('%YEAR%', str(today.year)).replace('%MONTH%', str(today.month)).replace('%WEEK%', str((today - origin).days // 7 + 1))
        
        return stdweek, url
    
    def crawling(stdweek, url):
    
        # pip install requests 를 사용한다.
        req = requests.get(url)
        
        # 전체 페이지 html 가지고 오기
        soup = BeautifulSoup(req.text, 'lxml')
        booklist = soup.select('.ss_book_box')
        bestbook = []

        for book in booklist:
            if book.select_one(".ss_ht1"):
                book.select_one(".ss_ht1").parent.decompose()
                
            rank = book.select_one("td").get_text().replace('.', '').strip()
            title = book.select_one(".bo3").get_text()
            author = book.select("li")[1].get_text().split("|")
            author = author[0]
            price = book.select("li")[2].get_text().split("원")
            price = int(price[0].replace(",", ""))
            pubdate = book.select("li")[1].get_text().split("|")
            pubdate = pubdate[-1].strip()
            bookcover = book.select_one(".front_cover")['src']
            
            bestbook.append(Bestseller(rank=rank, title=title, author=author, price=price, pub_date=pubdate, bookcover=bookcover, standard_week=stdweek))
            
        Bestseller.objects.bulk_create(bestbook)

    context = {}
    context['login_session'] = kwargs.get("login_session")

    stdweek, url = get_week_no()

    # db에서 당일기준 지난주 베스트셀러 데이터가 있는지 조회
    bestseller = Bestseller.objects.filter(standard_week=stdweek)
    
    # 있으면 그대로 뿌려주기
    if bestseller:
        context['bestseller'] = bestseller
        return render(request, "bestseller.html", context)
    # 없을 시에는 데이터 크롤링하고 db에 저장하고 뿌려주기
    else:
        context['bestseller'] = bestseller
        crawling(stdweek, url)
        return render(request, "bestseller.html", context)

    
    


