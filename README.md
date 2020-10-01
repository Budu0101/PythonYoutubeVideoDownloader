# Python Youtube Video Downloader

Python Youtube Video Downloader is a script that downloads the .mp4 file from a given Youtube URL.


## Installation

Use the package manager [pip]
(https://pip.pypa.io/en/stable/) to install the necessary library called [pytube]
(https://pypi.org/project/pytube/).

```bash
pip install pytube3
```


## Usage

```python
from pytube import *

# Importing tkinter module
from tkinter import *

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


```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## Licence

MIT License

Copyright (c) 2020 Stan Andrei

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
