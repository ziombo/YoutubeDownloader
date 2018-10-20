from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory

import youtube_dl


def show_video_dialog(on_click):
    def call_function():
        if hasattr(root, 'directory'):
            on_click(e1.get(), root.directory)
        else:
            on_click(e1.get(), askdirectory())

    def get_directory():
        root.directory = askdirectory()

    root = Tk()
    root.title('Youtube Downloader')

    mainframe = ttk.Frame(root)
    mainframe.grid(padx=7, pady=3, sticky=(N, W, E, S))


    mainframe.columnconfigure(0, weight=1, uniform='third')
    mainframe.columnconfigure(1, weight=1, uniform='third')
    mainframe.columnconfigure(2, weight=1, uniform='third')

    ttk.Label(mainframe, text="Enter valid Youtube url")\
        .grid(row=0)

    e1 = ttk.Entry(mainframe)
    e1.grid(row=1, columnspan=3, sticky=W+E, pady=(0,5))

    btn_dir = ttk.Button(mainframe, text='Select directory', command=get_directory)
    btn_dir.grid(row=2, column=1, sticky=W+E)

    btn_download = ttk.Button(mainframe, text='Download', command=call_function)
    btn_download.grid(row=2, column=2, sticky=W+E)

    btn_quit = ttk.Button(mainframe, text='Quit', command=root.quit)
    btn_quit.grid(row=3, column=2, sticky=W+E)

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
