from tkinter import *
import os


def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def log_out():
    os.system("shutdown -l")

def shutdown():
    os.system("shutdown /s /t 1")

sa = Tk()
sa.title("Shutdown App")
sa.geometry("500x500")
sa.config(bg="#9B9B1D")

r_button = Button(sa,text="Restart",font=("Time New Roman",30,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=70,height=50,width=200)

rt_button = Button(sa,text="Restart Time",font=("Time New Roman",25,"bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lo_button = Button(sa,text="Log-Out",font=("Time New Roman",25,"bold"),relief=RAISED,cursor="plus",command=log_out)
lo_button.place(x=150,y=270,height=50,width=200)

sd_button = Button(sa,text="Shutdown",font=("Time New Roman",25,"bold"),relief=RAISED,cursor="plus",command=shutdown)
sd_button.place(x=150,y=370,height=50,width=200)

sa.mainloop()