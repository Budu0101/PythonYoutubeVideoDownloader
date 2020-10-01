from pytube import *

# Inputs the URL
video_url = input("Please enter a valid Youtube URL: ")

# Passing the url in the pytube function, that is YouTube
yt = YouTube(video_url)

# Here you have to choose any one format of the stream (format contains mime_type, resolution, fps, vcodec, acodec). Also, you can change it if you want but I've chosen the first format.
video = yt.streams.first()

# Downloads the .mp4 file into the current directory. You can change it if you want.
video.download()
