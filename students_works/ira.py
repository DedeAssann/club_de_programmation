from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=4l6UrAhTvxE")
video = yt.streams.filter(file_extension="mp4", resolution="720p").first()
video.download()
