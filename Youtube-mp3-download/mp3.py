import youtube_dl
import sys
from colorama import Fore

#print(f"uzunluk {len(sys.argv[1:])}")

while (len(sys.argv[1:]) == 1):
    if len(sys.argv[1:]) == 1:
        params={
                'format':'bestaudio/best',
                'postprocessors':[{
                    'key':'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                    }],
                }
        youtube=youtube_dl.YoutubeDL(params)
        youtube.download(sys.argv[1:])
        break
while (len(sys.argv[1:]) == 0):
    print(f"\n{Fore.RED}It also supports Youtube music and playlists.{Fore.GREEN}\
          \nUsage: youtube_mp3.py <link>\n\
        or: youtube_mp3.py <https://www.youtube.com/watch?v=...>\n\
        or: youtube_mp3.py <https://music.youtube.com/watch?v=...>\n\
        or: youtube_mp3.py <https://www.youtube.com/watch?v=...&list=...>")
    break
    
