import os
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import StreamingHttpResponse
from music import utils
from music.models import *


def home(request):
    network = request.GET.get('network', 'high')
    if request.POST:
        q = request.POST['q']
        q = q.lower()
        if q == 'trending':
            results = utils.get_treding_results()
        else:
            results = utils.get_results(q)
        return render(request, 'music/home.html', {'results': results, 'q': q, 'network': network})
    else:
        return render(request, 'music/search.html', {'network': network})


def adv(request):
    network = request.GET.get('network', 'high')
    if request.POST:
        q = request.POST['q']
        results = utils.get_results(q)
        return render(request, 'music/adv.html', {'results': results, 'q': q, 'network': network})
    else:
        return render(request, 'music/adv.html', {'network': network})


def song(request, videoid, title):
    s, _ = Song.objects.get_or_create(videoid=videoid, title=title)
    flag = request.GET.get('flag')
    if flag:
        if flag == 'like':
            s.liked = True
            s.save()
        else:
            s.liked = False 
            s.save()
    return render(request, 'music/song.html', {'videoid': videoid, 'title': title, 'liked': s.liked})


def playlist(request):
    songs = Song.objects.filter(liked=True)
    return render(request, 'music/playlist.html', {'songs': songs})


def get_src(request, videoid):
    src = utils.get_info(videoid)
    return JsonResponse({'src': src})


def update(request):
    os.system('../env/bin/pip install --upgrade youtube-dl')
    return HttpResponse('updated')
