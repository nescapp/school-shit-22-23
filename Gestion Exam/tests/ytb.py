from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from tkinter import filedialog
import requests
from PIL import ImageTk, Image
from pytube import YouTube
import time


root = Tk()
root.title("YouTube Downloader")
# root.iconbitmap("icon.ico")
root.geometry("400x100")
# root.resizable(width=False, height=False)
# example link : https://youtu.be/Bk_z96dHSPw
r = ""
url = ""
video = ""


def submit():

    global r, url
    url = entry_link.get()

    if url != "":
        try:
            r = requests.get(url)
        except requests.exceptions.MissingSchema:
            messagebox.showerror("Error", "Not a valid url")
            pass
        else:
            if "Video unavailable" in r.text:
                messagebox.showinfo("Error", "Video unavailable")
            else:
                settings()
    else:
        print("empty")


def file_save():
    f = filedialog.askdirectory()
    print(f)


def settings():
    global frame_submit, video, thumbnail_source
    video = YouTube(url)
    frame_submit.pack_forget()
    root.geometry("400x400")
    # frame
    frame_settings = Frame(root)
    frame_settings.pack()
    # thumbnail
    thumbnail_url = video.thumbnail_url
    img_data = requests.get(thumbnail_url).content
    with open('temp_thumbnails/test.jpg', 'wb') as handler:
        handler.write(img_data)

    thumbnail_frame = Frame(frame_settings)
    thumbnail_frame.pack()
    thumbnail_source = Image.open("temp_thumbnails/test.jpg")
    thumbnail_source = thumbnail_source.resize((300, 205), Image.ANTIALIAS)
    thumbnail_source = ImageTk.PhotoImage(thumbnail_source)

    thumbnail = Label(frame_settings, image=thumbnail_source)
    thumbnail.pack()

    # controls frame
    controls_settings = LabelFrame(frame_settings)
    controls_settings.pack()
    # controls
    button_saveas = Button(controls_settings, text="save as", command=file_save, state=DISABLED)
    button_download = Button(controls_settings, text="download", command=download)

    button_saveas.grid(column=0, row=0)
    button_download.grid(column=1, row=0)

    Label(frame_settings, text=video.title, font=("Arial", 8, "bold")).pack()
    Label(frame_settings, text=f"views: {'{:,}'.format(video.views)}").pack()
    Label(frame_settings, text=f"author: {video.author}").pack()
    Label(frame_settings, text=f"age restricted: {video.age_restricted}").pack()
    Label(frame_settings, text=f"lenght: {time.strftime('%H:%M:%S', time.gmtime(video.length))}").pack()

def clear():
    entry_link.delete(0, END)


def paste():
    clear()
    clipboard = str(root.clipboard_get())
    entry_link.insert(0, clipboard)


def download():
    global video
    stream = video.streams.get_highest_resolution()
    stream.download()


def cancel():
    root.quit()


# frame
frame_submit = Frame(root)
frame_submit.pack()
# entry
Label(frame_submit, text="Enter link here :").pack()
entry_link = Entry(frame_submit, width=50)
entry_link.pack(pady=10)
entry_link.insert(0, "https://www.youtube.com/watch?v=GZvSYJDk-us")

# controls frame
controls_submit = LabelFrame(frame_submit)
controls_submit.pack()
# controls
button_clear = Button(controls_submit, text="Clear", command=clear)
button_paste = Button(controls_submit, text="Paste clipboard", command=paste)
button_submit = Button(controls_submit, text="Submit", command=submit)
button_cancel = Button(controls_submit, text="Cancel", command=cancel)

# adding everything to interface
button_clear.grid(column=0, row=0)
button_paste.grid(column=1, row=0)
button_submit.grid(column=2, row=0)
button_cancel.grid(column=3, row=0)

root.mainloop()