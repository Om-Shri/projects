from tkinter import *

sp = Tk()
sp.title("ID CARD")
sp.geometry("500x350")
sp.config(bg="#9F0000")

lab_class_name= Label(sp,text="UCC GROUP OF EDUCATION",font=("Time New Roman","25","bold"),bg="#9F0000",fg="Blue")
lab_class_name.place(x=15,y=0,height=40)

lab_add= Label(sp,text="PLACE:AMARPUR(BEHIND POLICE STATION)",font=("Time New Roman","12","bold"),bg="#9F0000",fg="Blue")
lab_add.place(x=50,y=42,height=20,width=400)

lab_contact = Label(sp,text="Mob.-7991132332, 9304299026",font=("Time New Roman","20","bold"),bg="#9F0000",fg="Yellow")
lab_contact.place(x=15,y=62,height=25,width=470)

lab_dash = Label(sp,text="_______________________________________________________________",font=("Time New Roman","12","bold"),bg="#9F0000",fg="Yellow")
lab_dash.place(x=0,y=85,height=20,width=500)

lab_name= Label(sp,text="NAME:",font=("Time New Roman","12","bold"),bg="#9F0000",fg="#05005D")
lab_name.place(x=15,y=120,height=20,width=55)

frame = Frame(sp).pack(side=BOTTOM)

name_comb =Text(frame,font=("Time New Roman",15,"bold"),wrap=WORD)
name_comb.place(x=75,y=117,height=25,width=300)

sp.mainloop()