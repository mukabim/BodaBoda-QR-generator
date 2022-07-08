import sqlite3
from tkinter import *
import tkinter.messagebox

import qrcode
from PIL import ImageTk, Image

root = Tk()
root.title("Nachu BodaBoda Co-operative")
root.geometry("786x320")
root.config(bg="#fe6431")
root.iconbitmap("Ndacha Cooperative logo.ico")
root.resizable(False, False)


def create_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS users(id integer primary key, name TEXT, mobile_no integer,number_plate varchar, stage TEXT, StageNo integer, StageChairman TEXT, chairmanTel integer, sqltime TIMESTAMP DEFAULT current_timestamp NOT NULL)")
    conn.commit()
    conn.close()


create_db()


def generate():
    data = (
        f'NACHU BODABODA INFORMATION SYSTEM.',
        f'',
        f'NAME: {fname.get()}',
        f"ID NUMBER: {id_no.get()}",
        f"MOBILE NUMBER: {tel_no.get()}",
        f"NUMBER PLATE: {plate_no.get()}",
        f"STAGE: {stage_name.get()}",
        f"STAGE NUMBER: {stage_no.get()}",
        f"STAGE CHAIRMAN: {stage_chair.get()}",
        f"CHAIRMAN'S NUMBER:{chairtel_no.get()}"
    )

    qr = qrcode.make('\n'.join(data))
    qr.save("Qrcodes/" + str(fname.get()) + ".png")


def save():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(
        'INSERT INTO users(name, id, mobile_no, number_plate, stage, stageNo, StageChairman, chairmanTel) VALUES (?,?,?,?,?,?,?,?)',
        (fname.get(), id_no.get(), tel_no.get(), plate_no.get(), stage_name.get(), stage_no.get(), stage_chair.get(),
         chairtel_no.get()))
    conn.commit()
    conn.close()
    print("Saved Successfully")


def onclick():
    tkinter.messagebox.showinfo("Saved Successfully", "Saved Successfully")


def reset():
    f.set("")
    i.set(0)
    t.set(254)
    p.set("")
    st.set("")
    sta.set(0)
    s.set("")
    ch.set(254)


frame = Frame(root, width=786, height=318)
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("Ndacha Cooperative.png"))

label = Label(frame, image=img)
label.pack()

Label(root, text="NACHU BODABODA CO-OPERATIVE", fg="white", bg="#fe6431", font=15).place(x=330, y=10)


def caps(event):
    f.set(f.get().upper())


f = StringVar()
Label(root, text="Full Name:", fg="white", bg="#fe6431", font=12).place(x=15, y=50)
fname = Entry(root, width=25, font="arial 12", textvariable=f)
fname.place(x=100, y=50)
fname.bind("<KeyRelease>", caps)

i = IntVar()
Label(root, text="ID Number:", fg="white", bg="#fe6431", font=12).place(x=15, y=80)
id_no = Entry(root, width=25, font="arial 12", textvariable=i)
id_no.place(x=100, y=80)

t = IntVar()
Label(root, text="Mobile No:", fg="white", bg="#fe6431", font=12).place(x=15, y=110)
tel_no = Entry(root, width=25, font="arial 12", textvariable=t)
t.set(254)
tel_no.place(x=100, y=110)


def caps(event):
    p.set(p.get().upper())


p = StringVar()
Label(root, text="Plate No:", fg="white", bg="#fe6431", font=12).place(x=15, y=140)
plate_no = Entry(root, width=25, font="arial 12", textvariable=p)
plate_no.place(x=100, y=140)
plate_no.bind("<KeyRelease>", caps)


def caps(event):
    st.set(st.get().upper())


st = StringVar()
Label(root, text="Stage Name:", fg="white", bg="#fe6431", font=12).place(x=15, y=170)
stage_name = Entry(root, width=22, font="arial 12", textvariable=st)
stage_name.place(x=127, y=170)
stage_name.bind("<KeyRelease>", caps)

sta = IntVar()
Label(root, text="Stage No:", fg="white", bg="#fe6431", font=12).place(x=15, y=200)
stage_no = Entry(root, width=22, font="arial 12", textvariable=sta)
stage_no.place(x=127, y=200)


def caps(event):
    s.set(s.get().upper())


s = StringVar()
Label(root, text="Stage Chair:", fg="white", bg="#fe6431", font=12).place(x=15, y=230)
stage_chair = Entry(root, width=22, font="arial 12", textvariable=s)
stage_chair.place(x=127, y=230)
stage_chair.bind("<KeyRelease>", caps)

ch = IntVar()
Label(root, text="Chairman Tel:", fg="white", bg="#fe6431", font=12).place(x=15, y=260)
chairtel_no = Entry(root, width=23, font="arial 12", textvariable=ch)
ch.set(254)
chairtel_no.place(x=120, y=260)

Button(root, text="Generate", width=20, height=1, bg="#fe6431", fg="#ffffff",
       command=lambda: [generate(), save(), onclick(), reset()]).place(
    x=180, y=290)

root.mainloop()
