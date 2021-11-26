from tkinter import *
import winsound
from functools import partial
import scroll_bar
import tkinter.ttk
import time
import threading
from tkinter.font import Font
songs = ['0','ts.wav','shape.wav','ot.wav','a','b','c','d','f','g','h']
col = 'black'
fg = 'white'



def play(ind):
    now_playing_l = Label(now_playing_frame, text='Now Playing:',bg = col,fg = fg,font = ('Comic Sans MS',17))
    now_playing_l.place(x=0, y=0)
    s = Label(now_playing_frame,text = songs[ind]+'         ',bg = col,fg = fg,font = ('Comic Sans MS',17))
    s.place(x = 200, y = 30)
    winsound.PlaySound(songs[ind],winsound.SND_ASYNC)

def stop():
    winsound.PlaySound(None,winsound.SND_PURGE)



root = Tk()

root.geometry('500x500')
root.config(bg = col)
tf = Frame(root,height = 100, width = 500,bg = col)
tf.pack()

logo = PhotoImage(file = 'spotify.png')
logo_i = logo.subsample(15,15)
logo_l = Label(tf, image = logo_i,bg = col)
logo_l.pack(side = LEFT)

title = Label(tf, text = 'ADITYA MUSIC PLAYER',font = ('Comic Sans MS',20),bg = col, fg = fg)
title.pack(side = LEFT)

list_frame = Frame(root,height = 400, width = 500,bg =col)
list_frame.pack(pady = 30)

p = PhotoImage(file = 'play.png')
pi = p.subsample(25,25)

s = PhotoImage(file = 'stop.png')
st_i =s.subsample(25,25)



for i in range(1,len(songs)):

    s1 = Label(list_frame,text = songs[i],bg = col,fg = fg,font = ('Comic Sans MS',20))
    s1.grid(row = i, column = 1,padx = 100)

    play_with_args = partial(play, i)
    b1 = Button(list_frame,image = pi,command = play_with_args,activebackground = 'white',bg = col)
    b1.grid(row = i, column = 2)

scroll_bar.ScrollFrame(list_frame)
list_frame.pack(pady = 30)

now_playing_frame = Frame(root, height = 100, width = 500,bg = col,highlightbackground = 'white',highlightthickness = 1)
now_playing_frame.pack(side = BOTTOM)



b2 = Button(now_playing_frame,image = st_i,command = stop,bg = col)
b2.place(x = 225, y = 70)


root.mainloop()