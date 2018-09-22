from django.urls import path, include, re_path
from .views import *


urlpatterns = [
    re_path('^$', home, name='home'),
    re_path('^src/(?P<videoid>[^/]+)/$', get_src, name='get_src'),
]
