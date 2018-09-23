from tkinter import *


def show_video_dialog(on_click):
    def call_function():
        on_click(e1.get())

    window = Tk()
    window.title('Youtube Downloader')
    # window.geometry('300x80')

    Label(window, text="Video Url").grid(row=0, padx=10, pady=(15, 30))

    e1 = Entry(window)
    e1.grid(row=0, column=1, sticky=E + W, padx=10, pady=(15, 30))

    Button(window, text='Show', command=call_function) \
        .grid(row=1, sticky=W + E, columnspan=2, padx=3)
    Button(window, text='Quit', command=window.quit) \
        .grid(row=2, sticky=W + E, columnspan=2, padx=3, pady=5)

    mainloop()
