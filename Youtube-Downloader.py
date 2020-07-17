from __future__ import unicode_literals
from sys import exit
import os
import ffmpeg
import youtube_dl
print(r"""\
                     
        
                    \ \ / /__  _   _| |_ _   _| |__   ___
                     \ V / _ \| | | | __| | | | '_ \ / _ \
                      | | (_) | |_| | |_| |_| | |_) |  __/
                      |_|\___/ \__,_|\__|\__,_|_.__/ \___|

                     ____                      _                 _
                    |  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __
                    | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
                    | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |
                    |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|
                    """)
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
    os.system('clear')
    os.system('cls')
    print(r"""\
                     
        
                    \ \ / /__  _   _| |_ _   _| |__   ___
                     \ V / _ \| | | | __| | | | '_ \ / _ \
                      | | (_) | |_| | |_| |_| | |_) |  __/
                      |_|\___/ \__,_|\__|\__,_|_.__/ \___|

                     ____                      _                 _
                    |  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __
                    | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
                    | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |
                    |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|
                    """)
    

if filetype =='video':
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print('Thanks for using my service')
    os.system('clear')
    os.system('cls')
    print(r"""\
                     
        
                    \ \ / /__  _   _| |_ _   _| |__   ___
                     \ V / _ \| | | | __| | | | '_ \ / _ \
                      | | (_) | |_| | |_| |_| | |_) |  __/
                      |_|\___/ \__,_|\__|\__,_|_.__/ \___|

                     ____                      _                 _
                    |  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __
                    | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
                    | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |
                    |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|
                    """)
else:
    filetype = input('Would you like video or audio')

