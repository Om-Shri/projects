from tkinter import *
from tkinter import ttk
import requests

def get_info():
    city = city_name.get()
    api_key = ""
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15))+"°C")
    pre_label1.config(text=str(data["main"]["pressure"])+" hPa")


win = Tk()
win.title("WEATHER APP")
win.geometry("500x500")
win.config(bg="#D17E31")

name_label = Label(win,text="WEATHER APP",font=("Time New Roman",35,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

state_list = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa",
              "Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka",
              "Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland",
              "Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura",
              "Uttar Pradesh","Uttarakhand","West Bengal"]

city_name = StringVar()
comb = ttk.Combobox(win,values=state_list,font=("Time New Roman",20,"bold"),textvariable=city_name)
comb.place(x=50,y=120,height=40,width=400)

search_button = Button(win,text="Search",font=("Time New Roman",20,"bold"),command=get_info)
search_button.place(x=200,y=170,height=30,width=100)

w_label = Label(win,text="Weather Climate",font=("Time New Roman",20),bg="#D17E31")
w_label.place(x=25,y=220,height=30,width=210)
w_label1 = Label(win,text="",font=("Time New Roman",20),bg="#D17E31")
w_label1.place(x=255,y=220,height=30,width=210)

wd_label = Label(win,text="Weather Discription",font=("Time New Roman",17),bg="#D17E31")
wd_label.place(x=25,y=270,height=30,width=210)
wd_label1 = Label(win,text="",font=("Time New Roman",17),bg="#D17E31")
wd_label1.place(x=255,y=270,height=30,width=210)

temp_label = Label(win,text="Temprature",font=("Time New Roman",20),bg="#D17E31")
temp_label.place(x=25,y=320,height=30,width=150)
temp_label1 = Label(win,text="",font=("Time New Roman",20),bg="#D17E31")
temp_label1.place(x=195,y=320,height=30,width=150)

pre_label = Label(win,text="Pressure",font=("Time New Roman",20),bg="#D17E31")
pre_label.place(x=25,y=370,height=30,width=150)
pre_label1 = Label(win,text="",font=("Time New Roman",20),bg="#D17E31")
pre_label1.place(x=195,y=370,height=30,width=150)



win.mainloop()