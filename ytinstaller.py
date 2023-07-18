# importing the module
from pytube import YouTube

# from tqdm import tqdm
# from pytube.cli import on_progress

# where to save
SAVE_PATH = "C:/Users/dedea/Dropbox/PC/Downloads"  # to_do


# link of the video to be downloaded
link = str(input("Put the youtube link over here : "))
yt = YouTube(link)  # , on_complete_callback=progress_function)

# filters out all the files with "mp4" extension
mp4files = yt.streams.filter(file_extension="mp4", progressive=True)

# to set the name of the file
filename = yt.title

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.streams.get_by_itag(
    22
)  # (mp4files[-1].extension, mp4files[-1].resolution)
try:
    # downloading the video
    d_video.download(filename=filename, output_path=SAVE_PATH)
except:
    print("Some Error!")
print("Task Completed!")
