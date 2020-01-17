import tkinter as tk
from tkinter import messagebox

# creating action function
def area():
    'to execute action when button is clicked'
    len=float(tfLen.get())
    wid=float(tfWid.get())
    areaR=len*wid
    tfArea.insert(0,areaR)
    # show message box
    messagebox.showinfo("INFO BOX","Area is:"+str(areaR)+"CM")
# creating a frame
frame=tk.Tk()
frame.geometry("1000x800")
# creating controls
tfLen=tk.Entry(frame)
tfWid=tk.Entry(frame)
tfArea=tk.Entry(frame)
btn=tk.Button(frame,text="GET AREA",command=area)
# adding controls as frame
tfLen.pack()
tfWid.pack()
tfArea.pack()
btn.pack()
# showing frame
frame.mainloop()