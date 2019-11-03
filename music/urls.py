from django.urls import path, include, re_path
from .views import *


urlpatterns = [
    re_path('^$', home, name='home'),
    #re_path('dinesh/$', dinesh_home, name='dinesh_home'),
    re_path('adv/$', adv, name='adv'),
    re_path('update$', update, name='update'),
    re_path('update/$', update, name='update'),
    re_path('playlist/$', playlist, name='playlist'),
    re_path('song/(?P<videoid>[^/]+)/(?P<title>[^/]+)$', song, name='song'),
    re_path('src/(?P<videoid>[^/]+)/$', get_src, name='get_src'),
]
