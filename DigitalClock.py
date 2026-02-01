from tkinter import *
import datetime

def set_time():
    time = datetime.datetime.now()
    hr = time.strftime("%H")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    amPm = time.strftime("%p")
    date = time.strftime("%d")
    day = time.strftime("%a")
    month = time.strftime("%m")
    year = time.strftime("%Y")

    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_amPm.config(text=amPm)
    lab_date.config(text=date)
    lab_day.config(text=day)
    lab_month.config(text=month)
    lab_year.config(text=year)
    sp.after(200,set_time)



sp = Tk()
sp.title("DIGITAL CLOCK")
sp.geometry("865x460")
sp.config(bg="#9AFEFF")

lab_hr = Label(sp,text="00",font=("Time New Roman","60","bold"),bg="#9AFEFF")
lab_hr.place(x=80,y=60,height=100,width=100)

lab_hr_txt = Label(sp,text="HOUR",font=("Time New Roman","15","bold"),bg="#9AFEFF")
lab_hr_txt.place(x=80,y=170,height=30,width=100)

lab_date = Label(sp,text="00",font=("Time New Roman","60","bold"),bg="#9AFEFF")
lab_date.place(x=80,y=250,height=100,width=100)

lab_date_txt = Label(sp,text="DATE",font=("Time New Roman","15","bold"),bg="#9AFEFF")
lab_date_txt.place(x=80,y=350,height=30,width=100)

lab_min = Label(sp,text="00",font=("Time New Roman","60","bold"),bg="#9AFEFF")
lab_min.place(x=280,y=60,height=100,width=100)

lab_min_txt = Label(sp,text="MINUTE",font=("Time New Roman","15","bold"),bg="#9AFEFF")
lab_min_txt.place(x=280,y=170,height=30,width=100)

lab_day = Label(sp,text="00",font=("Time New Roman","40","bold"),bg="#9AFEFF")
lab_day.place(x=280,y=250,height=100,width=100)

lab_day_txt = Label(sp,text="DAY",font=("Time New Roman","15","bold"),bg="#9AFEFF")
lab_day_txt.place(x=280,y=350,height=30,width=100)

lab_sec = Label(sp,text="00",font=("Time New Roman","60","bold"),bg="#9AFEFF")
lab_sec.place(x=480,y=60,height=100,width=100)

lab_sec_txt = Label(sp,text="SECOND",font=("Time New Roman","15","bold"),bg="#9AFEFF")
lab_sec_txt.place(x=480,y=170,height=30,width=100)

lab_month = Label(sp,text="00",font=("Time New Roman","60","bold"),bg="#9AFEFF")
lab_month.place(x=480,y=250,height=100,width=100)

lab_month_txt = Label(sp,text="MONTH",font=("Time New Roman","15","bold"),bg="#9AFEFF")
lab_month_txt.place(x=480,y=350,height=30,width=100)

lab_amPm = Label(sp,text="00",font=("Time New Roman","50","bold"),bg="#9AFEFF")
lab_amPm.place(x=680,y=60,height=100,width=100)

lab_amPm_txt = Label(sp,text="AM/PM",font=("Time New Roman","15","bold"),bg="#9AFEFF")
lab_amPm_txt.place(x=680,y=170,height=30,width=100)

lab_year = Label(sp,text="00",font=("Time New Roman","35","bold"),bg="#9AFEFF")
lab_year.place(x=680,y=250,height=100,width=100)

lab_year_txt = Label(sp,text="YEAR",font=("Time New Roman","15","bold"),bg="#9AFEFF")
lab_year_txt.place(x=680,y=350,height=30,width=100)

set_time()
sp.mainloop()