from django.urls import path
from news.views import scrape, news_list,statichome,about,contact, home, service
urlpatterns = [
  path('scrape/<str:name>', scrape, name="scrape"),
  path('news/', news_list, name="home"),
  path('home/',home, name="home"),
  path('about/',about, name="about"),
  path('service/',service, name="service"),
  path('contact/',contact, name="contact"),
  path('', statichome, name="breakinghome"),
]