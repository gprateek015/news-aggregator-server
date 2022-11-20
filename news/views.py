from turtle import tilt
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup 
from news.models import Headline
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def scrape_latest(request):
  Headline.objects.all().delete()
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.theonion.com/latest"
  content = session.get(url).content
  soup = BeautifulSoup(content, "html.parser")
  News = soup.find_all('div', {"class":"cw4lnv-13 ljLQgi"})
  data = []
  for article in News:
    try :
      main = article.find_all('a',href=True)
      linkx = article.find('a', {"class":"sc-1out364-0 hMndXN js_link"})
      link=linkx['href']
      imgx=main[0].find('img',src=True)
      image_src=imgx['data-srcset'].split(" ")[-4]
      titlex = article.find('h2', {"class":"sc-759qgu-0 iRbzKE cw4lnv-6 bnjwdx"})
      title = titlex.text
      data.append({'title': title, 'link': link, 'img_src': image_src})
      new_headline = Headline()
      new_headline.title = title
      new_headline.url = link
      new_headline.image = image_src
      new_headline.save()
    except :
      continue
  return Response(data, 200)

@api_view(['GET'])
def scrape_opinion(request):
  Headline.objects.all().delete()
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.theonion.com/opinion/roundtable"
  content = session.get(url).content
  soup = BeautifulSoup(content, "html.parser")
  News = soup.find_all('div', {"class":"cw4lnv-13 ljLQgi"})
  data = []
  for article in News:
    try :
      main = article.find_all('a',href=True)
      linkx = article.find('a', {"class":"sc-1out364-0 hMndXN js_link"})
      link=linkx['href']
      imgx=main[0].find('img',src=True)
      image_src=imgx['data-srcset'].split(" ")[-4]
      titlex = article.find('h2', {"class":"sc-759qgu-0 iRbzKE cw4lnv-6 bnjwdx"})
      title = titlex.text
      data.append({'title': title, 'link': link, 'img_src': image_src})
      new_headline = Headline()
      new_headline.title = title
      new_headline.url = link
      new_headline.image = image_src
      new_headline.save()
    except :
      continue
  return Response(data, 200)
  
@api_view(['GET'])
def scrape_local(request):
  Headline.objects.all().delete()
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.theonion.com/local/news-in-brief"
  content = session.get(url).content
  soup = BeautifulSoup(content, "html.parser")
  News = soup.find_all('div', {"class":"cw4lnv-13 ljLQgi"})
  data = []
  for article in News:
    try :
      main = article.find_all('a',href=True)
      linkx = article.find('a', {"class":"sc-1out364-0 hMndXN js_link"})
      link=linkx['href']
      imgx=main[0].find('img',src=True)
      image_src=imgx['data-srcset'].split(" ")[-4]
      titlex = article.find('h2', {"class":"sc-759qgu-0 iRbzKE cw4lnv-6 bnjwdx"})
      title = titlex.text
      data.append({'title': title, 'link': link, 'img_src': image_src})
      new_headline = Headline()
      new_headline.title = title
      new_headline.url = link
      new_headline.image = image_src
      new_headline.save()
    except :
      continue
  return Response(data, 200)
  
@api_view(['GET'])
def scrape_politics(request):
  Headline.objects.all().delete()
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.theonion.com/politics/news-in-brief"
  content = session.get(url).content
  soup = BeautifulSoup(content, "html.parser")
  News = soup.find_all('div', {"class":"cw4lnv-13 ljLQgi"})
  data = []
  for article in News:
    try :
      main = article.find_all('a',href=True)
      linkx = article.find('a', {"class":"sc-1out364-0 hMndXN js_link"})
      link=linkx['href']
      imgx=main[0].find('img',src=True)
      image_src=imgx['data-srcset'].split(" ")[-4]
      titlex = article.find('h2', {"class":"sc-759qgu-0 iRbzKE cw4lnv-6 bnjwdx"})
      title = titlex.text
      data.append({'title': title, 'link': link, 'img_src': image_src})
      new_headline = Headline()
      new_headline.title = title
      new_headline.url = link
      new_headline.image = image_src
      new_headline.save()
    except :
      continue
  return Response(data, 200)
  
@api_view(['GET'])
def scrape_entertainment(request):
  Headline.objects.all().delete()
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.theonion.com/entertainment/news-in-brief"
  content = session.get(url).content
  soup = BeautifulSoup(content, "html.parser")
  News = soup.find_all('div', {"class":"cw4lnv-13 ljLQgi"})
  data = []
  for article in News:
    try :
      main = article.find_all('a',href=True)
      linkx = article.find('a', {"class":"sc-1out364-0 hMndXN js_link"})
      link=linkx['href']
      imgx=main[0].find('img',src=True)
      image_src=imgx['data-srcset'].split(" ")[-4]
      titlex = article.find('h2', {"class":"sc-759qgu-0 iRbzKE cw4lnv-6 bnjwdx"})
      title = titlex.text
      data.append({'title': title, 'link': link, 'img_src': image_src})
      new_headline = Headline()
      new_headline.title = title
      new_headline.url = link
      new_headline.image = image_src
      new_headline.save()
    except :
      continue
  return Response(data, 200)
  
@api_view(['GET'])
def scrape_football(request):
  Headline.objects.all().delete()
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.theonion.com/sports/football"
  content = session.get(url).content
  soup = BeautifulSoup(content, "html.parser")
  News = soup.find_all('div', {"class":"cw4lnv-13 ljLQgi"})
  data = []
  for article in News:
    try :
      main = article.find_all('a',href=True)
      linkx = article.find('a', {"class":"sc-1out364-0 hMndXN js_link"})
      link=linkx['href']
      imgx=main[0].find('img',src=True)
      image_src=imgx['data-srcset'].split(" ")[-4]
      titlex = article.find('h2', {"class":"sc-759qgu-0 iRbzKE cw4lnv-6 bnjwdx"})
      title = titlex.text
      data.append({'title': title, 'link': link, 'img_src': image_src})
      new_headline = Headline()
      new_headline.title = title
      new_headline.url = link
      new_headline.image = image_src
      new_headline.save()
    except :
      continue
  return Response(data, 200)

@api_view(['GET'])
def scrape_breaking_news(request):
  Headline.objects.all().delete()
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.theonion.com/breaking-news/news-in-brief"
  content = session.get(url).content
  soup = BeautifulSoup(content, "html.parser")
  News = soup.find_all('div', {"class":"cw4lnv-13 ljLQgi"})
  data = []
  for article in News:
    try :
      main = article.find_all('a',href=True)
      linkx = article.find('a', {"class":"sc-1out364-0 hMndXN js_link"})
      link=linkx['href']
      imgx=main[0].find('img',src=True)
      image_src=imgx['data-srcset'].split(" ")[-4]
      titlex = article.find('h2', {"class":"sc-759qgu-0 iRbzKE cw4lnv-6 bnjwdx"})
      title = titlex.text
      data.append({'title': title, 'link': link, 'img_src': image_src})
      new_headline = Headline()
      new_headline.title = title
      new_headline.url = link
      new_headline.image = image_src
      new_headline.save()
    except :
      continue
  return Response(data, 200)


@api_view(['GET'])
def welcome(request):
  return Response('We welcome you to use our web scraping api, send GET request to /scrape', 200)
