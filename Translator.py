from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES
import asyncio

def change(text="type", src="en", dest="hi"):
    async def _translate():
        trans = Translator()
        result = await trans.translate(text, src=src, dest=dest)
        return result.text

    return asyncio.run(_translate())

def data():
    s = sor_combo.get()
    d = dest_combo.get()
    msg = sor_txt.get(1.0,END)

    textget = change(text=msg,src=s,dest=d)

    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)


root = Tk()
root.title("TRANSLATOR")
root.geometry("600x700")
root.config(bg="Gray")

lab_txt = Label(root,text="Translator",font=("Time New Roman",40,"bold"),bg="Gray")
lab_txt.pack()

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root,text="Source Text",font=("Time New Roman",20,"bold"),fg="Black",bg="Gray")
lab_txt.place(x=150,y=90,height=30,width=300)

sor_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
sor_txt.place(x=10,y=120,height=200,width=580)

list_text = list(LANGUAGES.values())

sor_combo = ttk.Combobox(frame,value=list_text,state="readonly")
sor_combo.place(x=10,y=322,height=25,width=100)
sor_combo.set("English")

button_change = Button(frame,text="Translate To",relief=RAISED,command=data)
button_change.place(x=115,y=322,height=25,width=100)

dest_combo = ttk.Combobox(frame,value=list_text,state="readonly")
dest_combo.place(x=218,y=322,height=25,width=100)
dest_combo.set("Hindi")

dest_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=390,height=200,width=580)

lab_txt = Label(root,text="Translated Text",font=("Time New Roman",20,"bold"),fg="Black",bg="Gray")
lab_txt.place(x=150,y=360,height=30,width=300)

root.mainloop()