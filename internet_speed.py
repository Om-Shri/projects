from tkinter import *
import speedtest
import time
import threading

def run_test():
    button.config(state=DISABLED)
    lab3.config(text="Testing...")
    lab5.config(text="Testing...")
    threading.Thread(target=speed_check, daemon=True).start()

def speed_check():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        down = round(st.download() / 10**6, 2)
        up = round(st.upload() / 10**6, 2)

        sp.after(0, update_labels, down, up)

    except Exception:
        sp.after(0, update_error)

def update_labels(down, up):
    lab3.config(text=f"{down} Mb/s")
    lab5.config(text=f"{up} Mb/s")
    button.config(state=NORMAL)

def update_error():
    lab3.config(text="Error")
    lab5.config(text="Error")
    button.config(state=NORMAL)


sp = Tk()
sp.title("INTERNET SPEED TEST")
sp.geometry("500x400")
sp.config(bg="Blue")

lab1 = Label(sp,text="INTERNET SPEED TEST",font=("Time New Roman",20,"bold"),bg="Blue",fg="White")
lab1.place(x=90,y=10,height=50)

lab2 = Label(sp,text="Downloding speed",font=("Time New Roman",20,"bold"),bg="Blue",fg="White")
lab2.place(x=125,y=90,height=30)

lab3 = Label(sp,text="00",font=("Time New Roman",20,"bold"),bg="Blue",fg="White")
lab3.place(x=225,y=130)

lab4 = Label(sp,text="Uploding Speed",font=("Time New Roman",20,"bold"),bg="Blue",fg="White")
lab4.place(x=140,y=180,height=30)

lab5 = Label(sp,text="00",font=("Time New Roman",20,"bold"),bg="Blue",fg="White")
lab5.place(x=225,y=220)

button = Button(sp,text="RUN TEST",font=("Time New Roman",13,"bold"),relief=RAISED,command=run_test)
button.place(x=195,y=300)

sp.mainloop()