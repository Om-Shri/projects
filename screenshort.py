import pyautogui
import PIL
from tkinter import *

def work():
    file = entry.get()
    button.config(state=DISABLED)
    ss = pyautogui.screenshot()
    ss.save(f"{file}.png")
    button.config(state=NORMAL)

ss_app = Tk()
ss_app.title("SCREENShORT")
ss_app.geometry("300x200")
ss_app.resizable(False,False)
ss_app.config(bg="lime")

lab_txt = Label(ss_app,text="Type File name",font=("Time New Roman",15,"bold"),bg="lime")
lab_txt.place(x=50,y=5,height=30,width=200)

entry = Entry(ss_app,font=("Time New Roman",20,"bold"))
entry.place(x=50,y=40,height=50,width=200)

button = Button(ss_app,text="Screenshort",font=("Time New Roman",20,"bold"),command=work)
button.place(x= 50,y=100,height=50,width=200)
ss_app.mainloop()