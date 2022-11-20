from django.urls import path
from news.views import scrape_latest, scrape_opinion,scrape_local,scrape_politics,scrape_entertainment,scrape_football,scrape_breaking_news,welcome
urlpatterns = [
  path('scrape_latest/', scrape_latest, name="scrape_latest"),
  path('scrape_opinion/', scrape_opinion, name="scrape_opinion"),
  path('scrape_local/', scrape_local, name="scrape_local"),
  path('scrape_politics/', scrape_politics, name="scrape_politics"),
  path('scrape_entertainment/', scrape_entertainment, name="scrape_entertainment"),
  path('scrape_football/', scrape_football, name="scrape_football"),
  path('scrape_breaking_news/', scrape_breaking_news, name="scrape_breaking_news"),
  path('', welcome, name="home"),
]