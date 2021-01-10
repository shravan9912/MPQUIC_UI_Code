import time
import subprocess 
import pathlib
from threading import Thread
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib.image as img
from tkinter import *
import os

root=Tk()
def Play_stream():
  t1 = Thread(target = lambda: subprocess.call(['python3', 'stream_viewer.py']))
  t1.start() 
def RecieveStream():
 t1 = Thread(target = lambda: subprocess.call(['sh', './startreceiver.sh']))
 t1.start() 
 
myButton1=Button(root,text="Start_Stream_server",command=RecieveStream, fg="blue")
myButton1.pack()

myButton2=Button(root,text="Play_stream",command=Play_stream, fg="blue")
myButton2.pack()

root.mainloop()

