import os
import tkinter as tk
from tkinter.filedialog import askdirectory
import pygame as pg

root = tk.Tk()


root.title("Music Gui")


screen_height = 350
screen_width =450
root.minsize(width=screen_width, height=screen_height)


#ask user to select folder that contains mousic
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()


#create a listbox
play_list = tk.Listbox(root,
           font="Helvetica 12 bold",
           bg="silver",
           fg="dark blue",
           selectmode=tk.SINGLE)



pos = 0
for song in song_list:
    play_list.insert(pos, song)
    pos += 1



#initialise the pygame library
pg.init()

music_playing = 1

def play_music():
    pg.mixer.music.load(play_list.get(tk.ACTIVE))
    pg.mixer.music.play()
    music_playing = 0
    print(music_playing)


    return music_playing


def stop_music():
    pg.mixer.music.stop()
    music_playing = 1
    print(music_playing)
    play_button.configure(bg="grey")
    return music_playing

def pause_music():
    pg.mixer.music.pause()
    play_button.configure(bg="grey")

def unpause_music():
    pg.mixer.music.unpause()

def play_on_selection(event):
    play_music()

play_button = tk.Button(root,
                        text="PLAY",
                        height=3,
                        font="Helvetica 12 bold",
                        fg="white",
                        bg="grey",
                        command=play_music)

button_bg_colour = ["grey", "silver"]

if music_playing == 0:

    play_button.configure(bg="silver")
    #print(music_playing)

if music_playing == 1:
    play_button.configure(bg="silver")
    #print(music_playing)


# bg_colour_switch()






#create a a button





stop_button = tk.Button(root,
                        text="STOP",
                        height=3,
                        font="Helvetica 12 bold",
                        fg="white",
                        bg="grey",
                        command=stop_music)



pause_button = tk.Button(root,
                        text="PAUSE",
                        height=3,
                        font="Helvetica 12 bold",
                        fg="white",
                        bg="grey",
                        command=pause_music)



#place the name of the song
song_name = tk.StringVar()
song_title = tk.Label(root,
                      textvariable=song_name,
                      fg="dark blue",
                      bg="grey")

song_title.pack(fill="x")
play_button.pack(fill="x")
stop_button.pack(fill="x")
pause_button.pack(fill="x")
play_list.pack(fill="both")
#play music on selection
#play_list.bind("<<ListboxSelect>>", play_on_selection)







root.mainloop()
