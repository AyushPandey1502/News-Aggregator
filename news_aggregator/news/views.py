from django.shortcuts import render
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

# Create your views here.


def scrape(request, name):
    Headline.objects.all().delete()
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = f"https://www.theonion.com/{name}"
    if name.lower() not in ['home', 'latest', 'local', 'politics', 'entertainment', 'sports', 'opinion']:
        url = f"https://www.theonion.com/search?blogId=1636079510&q={name}"
    content = session.get(url).content
    soup = BSoup(content, "html.parser")

    News = soup.find_all("div", {"class": "sc-cw4lnv-13 hHSpAQ"})
    count=0
    for article in News:
        count=count+1

        if count<=20:
            main = article.find_all("a", href=True)

            linkx = article.find("a", {"class": "sc-1out364-0 dPMosf js_link"})
            link = linkx["href"]

            titlex = article.find("h2", {"class": "sc-759qgu-0 cvZkKd sc-cw4lnv-6 TLSoz"})
            title = titlex.text

            imgx = article.find("img")["data-src"]

            new_headline = Headline()
            new_headline.title = title
            new_headline.url = link
            new_headline.image = imgx
            new_headline.save() ##saving each record to news_headline
    return redirect("/news")


def news_list(request):
    headlines = Headline.objects.all()[::-1]
    #to generate current url
    current_url = request.build_absolute_uri()
    #pass current url to template through context
    context = {
        "object_list": headlines,"currenturl":current_url
    }

    return render(request, "home.html", context)

def statichome(request):
     return render(request, "homestatic.html")

def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

# def breakinghome(request):
#     Headline.objects.all().delete()
#     session = requests.Session()
#     session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
#     url = f"https://www.theonion.com/latest"
#     content = session.get(url).content
#     soup = BSoup(content, "html.parser")

#     News = soup.find_all("div", {"class": "sc-cw4lnv-13 hHSpAQ"})
#     count=0
#     for article in News:
#         count=count+1

#         if count<=8:
#             main = article.find_all("a", href=True)

#             linkx = article.find("a", {"class": "sc-1out364-0 dPMosf js_link"})
#             link = linkx["href"]

#             titlex = article.find("h2", {"class": "sc-759qgu-0 cvZkKd sc-cw4lnv-6 TLSoz"})
#             title = titlex.text

#             imgx = article.find("img")["data-src"]

#             new_headline = Headline()
#             new_headline.title = title
#             new_headline.url = link
#             new_headline.image = imgx
#             new_headline.save() ##saving each record to news_headline
    
#     headlines = Headline.objects.all()[::-1]
#     context = {
#         "object_list": headlines,
#     }

#     return render(request, "home.html", context)

