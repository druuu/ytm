from __future__ import unicode_literals
import json
import youtube_dl
import pafy

import asyncio
import datetime
import random
import websockets


async def time(websocket, path):
    qs = {'q': 'hello', 'maxResults': 10, 'part': 'id,snippet'}
    gdata = pafy.call_gdata('search', qs)
    with youtube_dl.YoutubeDL({'format': 'bestaudio/best'}) as ydl:
        for item in gdata['items']:
            result = {'extracted': False, 'id': item['id']['videoId'], 'title': item['snippet']['title']}
            await websocket.send(json.dumps(result))
        for item in gdata['items']:
            url = "https://www.youtube.com/watch?v=" + item['id']['videoId']
            info_dict = ydl.extract_info(url, download=False)
            result = {'extracted': True, 'id': item['id']['videoId'], 'url': info_dict.get('url', '#'), 'title': item['snippet']['title']}
            await websocket.send(json.dumps(result))

start_server = websockets.serve(time, '0.0.0.0', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
