from pytube import *

# Importing tkinter module
from tkinter import *

<<<<<<< HEAD
# creating root window  for Tkinter
root = Tk() 
  
# adding root window title and dimension for Tkinter
root.title("Python Youtube Video Downloader") 
root.geometry('350x200')
=======
# Passing the url in the pytube function, that is YouTube
yt = YouTube(video_url)
>>>>>>> fd68bc7c7fbf9bb18bf7d27e0955f7784b03dec6

# adding a label to the root window 
lbl = Label(root, text = "Please enter a valid Youtube URL: ") 
lbl.grid() 

<<<<<<< HEAD
# adding Entry Field 
video_url = Entry(root, width=10) 
video_url.grid(column =1, row =0) 

# function to convert the Youtube URL into a .mp4 file in the current directory when button is clicked 
def clicked(): 

    # Passing the url in the pytube function, that is YouTube
    yt = pytube.YouTube(video_url.get())

    # Here you have to choose any one format of the stream (format contains mime_type, resolution, fps, vcodec, acodec). Also, you can change it if you want but I've chosen the first format.
    video = yt.streams.first()

    # Downloads the .mp4 file into the current directory. You can change it if you want.
    video.download()


# button widget with text inside 
btn = Button(root, text = "Start Converting" , 
             fg = "black", command=clicked)

btn.grid(column=2, row=0)


root.mainloop()
=======
# Downloads the .mp4 file into the current directory. You can change it if you want.
video.download()
>>>>>>> fd68bc7c7fbf9bb18bf7d27e0955f7784b03dec6
