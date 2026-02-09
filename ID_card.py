from tkinter import *

sp = Tk()
sp.title("ID CARD")
sp.geometry("500x350")
sp.config(bg="#9F0000")

frame = Frame(sp).pack(side=BOTTOM)

lab_class_name= Label(sp,text="UCC GROUP OF EDUCATION",font=("Time New Roman","25","bold"),bg="#9F0000",fg="Blue")
lab_class_name.place(x=15,y=0,height=40)

lab_add= Label(sp,text="PLACE:AMARPUR(BEHIND POLICE STATION)",font=("Time New Roman","12","bold"),bg="#9F0000",fg="Blue")
lab_add.place(x=50,y=42,height=20,width=400)

lab_dash = Label(sp,text="_______________________________________________________________",font=("Time New Roman","12","bold"),bg="#9F0000",fg="Yellow")
lab_dash.place(x=0,y=85,height=20,width=500)

lab_contact = Label(sp,text="Mob.-7991132332, 9304299026",font=("Time New Roman","20","bold"),bg="#9F0000",fg="Yellow")
lab_contact.place(x=15,y=70,height=25,width=470)

lab_name= Label(sp,text="NAME:",font=("Time New Roman","12","bold"),bg="#9F0000",fg="#05005D")
lab_name.place(x=15,y=120,height=20,width=55)

name_comb =Text(frame,font=("Time New Roman",15,"bold"),wrap=WORD)
name_comb.place(x=75,y=117,height=25,width=300)

lab_mob= Label(sp,text="MOB.",font=("Time New Roman","12","bold"),bg="#9F0000",fg="#05005D")
lab_mob.place(x=10,y=160,height=20,width=55)

mob_comb =Text(frame,font=("Time New Roman",15,"bold"),wrap=WORD)
mob_comb.place(x=75,y=155,height=25,width=300)

lab_shift= Label(sp,text="SHIFT TIME/CLASS:",font=("Time New Roman","12","bold"),bg="#9F0000",fg="#05005D")
lab_shift.place(x=11,y=200,height=20,width=160)

shift_comb =Text(frame,font=("Time New Roman",15,"bold"),wrap=WORD)
shift_comb.place(x=175,y=195,height=25,width=300)

lab_address= Label(sp,text="ADDRESS",font=("Time New Roman","12","bold"),bg="#9F0000",fg="#05005D")
lab_address.place(x=15,y=240,height=20,width=80)

address_comb =Text(frame,font=("Time New Roman",15,"bold"),wrap=WORD)
address_comb.place(x=105,y=235,height=25,width=370)

lab_st_Sign= Label(sp,text="Student's Signature",font=("Time New Roman","10","bold"),bg="#9F0000",fg="#05005D")
lab_st_Sign.place(x=30,y=300,height=17,width=123)

st_sign_comb =Text(frame,font=("Time New Roman",10,"bold"),wrap=WORD)
st_sign_comb.place(x=15,y=280,height=20,width=150)

dir_sign= Label(sp,text="Director's Signature",font=("Time New Roman","10","bold"),bg="#9F0000",fg="#05005D")
dir_sign.place(x=340,y=300,height=17,width=123)

dir_sign_comb =Text(frame,font=("Time New Roman",10,"bold"),wrap=WORD)
dir_sign_comb.place(x=325,y=280,height=20,width=150)

classes= Label(sp,text="CLASS",font=("Time New Roman","10","bold"),fg="#05005D")
classes.place(x=380,y=110,height=20,width=110)

classes_comb =Text(frame,font=("Time New Roman",10,"bold"),wrap=WORD)
classes_comb.place(x=380,y=130,height=20,width=110)

roll_no= Label(sp,text="ROLL NO.",font=("Time New Roman","10","bold"),fg="#05005D")
roll_no.place(x=380,y=150,height=20,width=110)

roll_no_comb =Text(frame,font=("Time New Roman",10,"bold"),wrap=WORD)
roll_no_comb.place(x=380,y=170,height=20,width=110)



sp.mainloop()