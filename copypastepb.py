import tkinter as tk
import tkinter import ttk
from tkinter import messagebox
import os

# finding file size
def copy():
    'to copy paste'
    sfpath=tfsf.get()
    dfpath=tfdf.get()
    # finding file size
    fs=os.stat(sfpath).st_size
    pbar["maximum"]=fs
    fr=open(sfpath,"rb")
    fw=open(dfpath,"wb")
    for i in range(fs+1):
        fw.write(fr.read())
        pbar["value"]=i
        lbl["text"]=str((i/1024)+"kb"
        pbar.update()

    
root=tk.Tk()
root.geometry("400x500")

lbl=tk.Label(root,text="Bytes")
ttk.Progressbar(root,orient=)