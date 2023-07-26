from pytube import YouTube 

yt = YouTube("https://www.youtube.com/watch?v=V89ZjRwMlvM&pp=ygUVbGF1cnluIGhpbGwgZXggZmFjdG9y")
video = yt.streams.filter(file_extension="mp4", resolution="720p").first()
video.download()

