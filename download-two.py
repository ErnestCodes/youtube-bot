import pytube
from pytube import YouTube
video_url = "https://www.youtube.com/watch?v=1ZdFJ0701QI"
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('C:/Users/Hp/Downloads/')