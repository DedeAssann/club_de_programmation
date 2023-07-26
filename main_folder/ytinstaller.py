"""
_summary_
 
In this module is defined the downloader function, which uses the implementation of the pytube module from python,
to download various type of content from Youtube.
It gives you free management of choosing the folder where to save the downloaded content, naming the file, asks for the URL 
of the youtube content, and also the file type (mp3, mp4, etc...).

_extended_summary_

An exemple of using this functions in the Python CLI would be :
    >>> import downloader
    >>> downloader(url="https://www.youtube.com/watch?v=Q2f9h_-_Fv4", SAVE_PATH="C:/Users/User001/Downloads", filename="Computational Thinking - Harvard Free Course")
The precedent code downloads a video from youtube, about Computational Thinking, a course given by Harvard University.
Not naming the downloaded file during the process won't be fatal to the execution of the program. The file will,
in this case, be named after the title of the downloaded content. While not naming the content is not fatal, the url, 
and the filter are required for the program to be executed. The SAVE_PATH parameter might be fatal for the good execution 
of the program in some cases. Future implementation of the program might propose better handling over this feature.

"""


# importing the module
from pytube import YouTube


def downloader(
    url: str = None,
    filter: str = "mp4",
    SAVE_PATH: str = "C:/Users/dedea/Dropbox/PC/Downloads",
    filename: str = None,
):
    "This function downloads any content from youtube"
    # link of the video to be downloaded
    if url is not None:
        _yt = YouTube(url)
    else:
        link = str(input("Put the youtube link over here : "))
        _yt = YouTube(link)


    # Naming the file
    if filename is None:
        filename = _yt.title

    # get the video with the extension and
    # resolution passed in the get() function
    d_video = _yt.streams.get_by_itag(
        22
    )  # (mp4files[-1].extension, mp4files[-1].resolution)
    try:
        # downloading the video
        d_video.download(filename=filename, output_path=SAVE_PATH, max_retries=5)
    except:
        print("Some Error!")
    print("Task Completed!")


if __name__ == "__main__":
    downloader()
