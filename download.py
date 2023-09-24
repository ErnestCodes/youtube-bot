from pytube import YouTube
link = "https://www.youtube.com/watch?v=1ZdFJ0701QI"
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download('C:/Users/Hp/Downloads/')