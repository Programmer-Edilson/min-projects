from pygame import mixer
from tkinter import *
import os

global song_pointer
song_pointer = 1

def playsong():
    current_song.set(listbox.get(ACTIVE))
    current_song_index.set(listbox.index(ACTIVE))

    mixer.music.load(current_song.get())
    mixer.music.play()
    playerstatus.set("Playing")
    print("Playing, index: ", current_song_index.get(), "title ", current_song.get())

def pausesong():
    mixer.music.pause()
    playerstatus.set("Paused")
    print("Paused, index: ", current_song_index.get(), "title ", current_song.get())

def resumisong():
    mixer.music.unpause()
    playerstatus.set("Resuming")
    print("Resuming, index: ", current_song_index.get(), "title ", current_song.get())

def resetsong():
    mixer.music.play()
    playerstatus.set("Reseting")
    print("Reseting, index: ", current_song_index.get(), "title ", current_song.get())

def nextsong():
    global song_pointer
    if current_song_index.get() <= listbox.size() - 4:
        try:
            current_song_indexN = current_song_index.get()

            next_song_index = current_song_indexN + song_pointer
            current_song.set(listbox.get(next_song_index))
            current_song_index.set(next_song_index) 

            mixer.music.load(current_song.get())
            mixer.music.play()
            playerstatus.set("Nexting")
        
            print("Nexting, index: ", current_song_index.get(), "title ", current_song.get())
        except:
            pass

def prevsong():
    if current_song_index.get() > 0:
        try:
            current_song_indexP = current_song_index.get()
            prev_song_index = current_song_indexP - 1

            current_song_index.set(prev_song_index)
            current_song.set(listbox.get(current_song_index.get()))
            mixer.music.load(current_song.get())
            mixer.music.play()

            playerstatus.set("Previous")
            print("Previous, index: ", current_song_index.get(), "title ", current_song.get())
        except:
            pass

root = Tk()
root.title("Player v1.0")
root['bg'] = "DodgerBlue2"

os.chdir(r"E:\Music\Gota D'Espaço [2020]")
songs = os.listdir()
listbox = Listbox(root, selectmode=SINGLE, bg="DodgerBlue2", fg="white", font=('arial',15))
for song in songs:
    listbox.insert(END, song)

mixer.init()

#global variables
playerstatus = StringVar()
current_song = StringVar()
current_song_index = IntVar()


#assigning global variables
playerstatus.set("Choosing")

label = Label(root, text = "Music Player", bg="DodgerBlue2", fg="white", font=('arial',9))
labelplaylist = Label(root, text = "Playlist one", bg="DodgerBlue2", fg="white", font=('arial',9))
button = Button(root, text = "Play", command = playsong, bg="DodgerBlue2", fg="white", font=('arial',9))
button1 = Button(root, text = "Pause",  width = 32,command = pausesong, bg="DodgerBlue2", fg="white", font=('arial',9))
button2 = Button(root, text = "Continue", command = resumisong, bg="DodgerBlue2", fg="white", font=('arial',9))
button3 = Button(root, text = "Reset", command = resetsong, bg="DodgerBlue2", fg="white", font=('arial',9))
button5 = Button(root, text = "Next", command = nextsong, bg="DodgerBlue2", fg="white", font=('arial',9))
button4 = Button(root, text = "Previous", command = prevsong, bg="DodgerBlue2", fg="white", font=('arial',9))


button.grid(row = 0, column = 0, sticky = W+E)
button1.grid(row = 1, column = 0, sticky = W+E)
button2.grid(row = 2, column = 0, sticky = W+E)
button5.grid(row = 3, column = 0, sticky = W+E)
button4.grid(row = 4, column = 0, sticky = W+E)
button3.grid(row = 5, column = 0, sticky = W+E)
labelplaylist.grid(row = 6, column = 0, pady = 10, sticky = W)
listbox.grid(row = 7, column = 0, sticky = W+E)

root.mainloop()
