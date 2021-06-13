from tkinter import*
import random
from tkinter import font
from tkinter.font import Font
droot=Tk()
droot.geometry("400x400")
droot.configure(bg='black')
droot.title("DICE SIMULATOR")
t= Label(droot,text="DICE SIMULATOR",font=("Helvetica",20),fg='White',bg='black')
t.place(x=10,y=10)

image=[]
img=PhotoImage(file="One.png")
image.append(img)
img=PhotoImage(file="Two.png")
image.append(img)
img=PhotoImage(file="three.png")
image.append(img)
img=PhotoImage(file="Four.png")
image.append(img)
img=PhotoImage(file="Five.png")
image.append(img)
img=PhotoImage(file="Six.png")
image.append(img)

lbl=Label(droot,image=img)
lbl.place(x=120,y=70)



def roll():
    num=random.randint(0,5)
    lbl.configure(image=image[num])

rl=Button(droot,text="ROLL",command=roll)
rl.place(x=20,y=40)
droot.mainloop()