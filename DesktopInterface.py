from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import youtube_dl


def show_video_dialog(on_click):
    def call_function():
        if hasattr(window, 'directory'):
            on_click(e1.get(), window.directory)
        else:
            on_click(e1.get(), askdirectory())

    def get_directory():
        window.directory = askdirectory()

    window = Tk()
    window.title('Youtube Downloader')
    # window.geometry('300x80')

    Label(window, text="Enter valid Youtube url").grid(row=0, padx=10)

    e1 = Entry(window)
    e1.grid(row=1, column=0, sticky=E + W, padx=10, pady=(0, 15))

    Button(window, text='Select directory', command=get_directory) \
        .grid(row=2, sticky=E + W, columnspan=2, padx=3, pady=3)
    Button(window, text='Download', command=call_function) \
        .grid(row=3, sticky=W + E, columnspan=2, padx=3)
    Button(window, text='Quit', command=window.quit) \
        .grid(row=4, sticky=W + E, columnspan=2, padx=3, pady=5)

    mainloop()


def download_mp3(video_url, save_directory):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{save_directory}/%(title)s.%(ext)s',

    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'{video_url}'])
