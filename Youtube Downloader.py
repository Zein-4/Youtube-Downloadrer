from __future__ import unicode_literals
from sys import exit
import ffmpeg
import youtube_dl
filetype = input('Would you like video or audio:')
link = input('Youtube Link:')
if filetype == 'audio':
    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': "C:\\Users\\Zein_\\Desktop\\ffmpeg\\bin\\ffmpeg.exe",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }]

        }
       
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print('Thanks for using my service')
    exit()

if filetype =='video':
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print('Thanks for using my service')
    exit()
else:
    filetype = input('Would you like video or audio')

