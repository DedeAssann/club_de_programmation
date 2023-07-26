from pytube import YouTube

yt = YouTube(
    "https://www.youtube.com/watch?v=V89ZjRwMlvM&pp=ygUVbGF1cnluIGhpbGwgZXggZmFjdG9y"
)
file = yt.streams.filter(file file_extension="mp4", resolution="720p").first()
video.download()
