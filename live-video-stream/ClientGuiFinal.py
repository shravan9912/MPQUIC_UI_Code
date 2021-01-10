import time
import subprocess 
import pathlib
from threading import Thread

from tkinter import *
import os

root=Tk()
def start_capture():
  t1 = Thread(target = lambda: subprocess.call(['python3', 'stream_generator.py']))
  t1.start() 
def send_stream():
 t1 = Thread(target = lambda: subprocess.call(['sh', './sender.sh']))
 t1.start() 
 
myButton1=Button(root,text="Start_Capure",command=start_capture, fg="blue")
myButton1.pack()

myButton2=Button(root,text="send_stream",command=send_stream, fg="blue")
myButton2.pack()

root.mainloop()

