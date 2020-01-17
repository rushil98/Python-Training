import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# creating frame
frame=tk.Tk()
frame.geometry("700x500")

# event function
def progress():
    'to update progress'
    for i in range(5001):
        # update progress value
        pbar["value"]=i
        lbl["text"]=i
        pbar.update()
    else:
        messagebox.showinfo("INFO","Loop Completed")

lbl=tk.Label(frame,text="Progress Bar")
# creating  progressbar
pbar=ttk.Progressbar(frame,orient="horizontal",length=400,mode="determinate")
# setting max value
pbar["maximum"]=5000
btn=tk.Button(frame,text="START",command=progress) 
# adding controls on frame
lbl.pack()
pbar.pack()
btn.pack()
frame.mainloop()
