from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory

import threading
from concurrent.futures import ThreadPoolExecutor

import youtube_dl


def show_video_dialog():
    executor = ThreadPoolExecutor(max_workers=8)

    # def start_downloading():
    #     t = threading.Thread(target=download_from_yt)
    #     t.start()

    def download_from_yt():
        if not verify_url():
            return

        if not hasattr(root, 'directory'):
            get_directory()

        executor.submit(download_mp3, entry_url.get(), root.directory)

    def get_directory():
        root.directory = askdirectory()

    def verify_url():
        url = entry_url.get()
        if 'watch?' in url:
            return True
        elif 'playlist?' in url:
            return True
        else:
            link_type.set('Invalid url')
            return False

    def my_hook(hook):
        print(f"Current status: {hook['status']}")
        link_type.set(hook['status'])

    def download_mp3(video_url, save_directory):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{save_directory}/%(title)s.%(ext)s',
            'noplaylist': True,
            'progress_hooks': [my_hook],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'{video_url}'])

    root = Tk()
    root.title('Youtube Downloader')

    # TkInter variables
    link_type = StringVar()
    __download_playlist = BooleanVar()
    __download_playlist.set(True)

    mainframe = ttk.Frame(root)
    mainframe.grid(padx=7, pady=3, sticky=(N, W, E, S))

    mainframe.columnconfigure(0, weight=1, uniform='third')
    mainframe.columnconfigure(1, weight=1, uniform='third')
    mainframe.columnconfigure(2, weight=1, uniform='third')

    lbl_url = ttk.Label(mainframe, text="Youtube url")
    lbl_url.grid(row=0, sticky=W)

    entry_url = ttk.Entry(mainframe)
    entry_url.grid(row=1, columnspan=3, sticky=W + E, pady=(0, 5))

    img_directory = PhotoImage(file="directory.png")
    btn_dir = ttk.Button(mainframe, image=img_directory, command=get_directory)
    btn_dir.grid(row=1, column=4, sticky=N)

    btn_download = ttk.Button(mainframe, text='Download', command=download_from_yt)
    btn_download.grid(row=3, column=0, columnspan=2, sticky=W + E)

    btn_quit = ttk.Button(mainframe, text='Quit', command=root.quit)
    btn_quit.grid(row=3, column=2, columnspan=3, sticky=W + E)

    lbl_current_action = ttk.Label(mainframe, textvariable=link_type)
    lbl_current_action.grid(row=2, column=2, columnspan=2)
    #    lbl_current_action.grid_forget()

    chk_playlist = ttk.Checkbutton(mainframe, text='Download whole playlist',
                                   variable=__download_playlist)

    mainloop()
