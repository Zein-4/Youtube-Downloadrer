# Youtube-Downloadrer
Download Youtube Videos as mp4 or mp3
# Tutorial
1) First you need Python (idk if u need the newest version but u can try)

2) U need FFmpeg

**Install FFmpeg on Mac:**

Either type in terminal: 
```
brew install ffmpeg
```
If that doesnt work download it form the official website: https://ffmpeg.org/

**Install ffmpeg on Windows:**

https://www.youtube.com/watch?v=a_KqycyErd8

**Linux:**

I dont think anyone here is using Linux

3) U need pip so here

**Windows:**

https://phoenixnap.com/kb/install-pip-windows

**Mac:**

https://ahmadawais.com/install-pip-macos-os-x-python/

4) Now download python modules
```
pip install ffmpeg
pip install youtube-dl
```

5) Now open it in you python editor and on line 25 put your ffmpeg location (make sure its not in some kind of root location)
```
'ffmpeg_location': "path//to//ffmpeg//bin",
```
6) Now you can download any youtube video as mp3 or mp4 as long as you run it from a python editor or terminal/cmd
