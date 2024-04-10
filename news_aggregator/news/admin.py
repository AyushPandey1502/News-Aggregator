from django.contrib import admin
from news.models import Headline
# Register your models here.

#adding our model to the admin dashboard
admin.site.register(Headline)
