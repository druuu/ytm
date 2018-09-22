from django.urls import path, include, re_path
from .views import *


urlpatterns = [
    re_path('^$', home, name='home'),
    re_path('^search/$', search, name='search'),
]
