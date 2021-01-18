from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox

mydb = mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', db='lifechoicesonline', host='127.0.0.1', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

window = tk.Tk()
window.title('Main Login')
window.geometry('450x340')

lblusername = Label(window,text = 'Username:')
lblusername.place(x=30, y=30)
userent = Entry(window)
userent.place(x=150,y=30)

lblpsswrd = Label(text = 'Password:')
lblpsswrd.place(x=30, y=80)
userpsswrd = Entry(window, show= '*')
userpsswrd.place(x=150,y=78)


def registerUser():
    register= Tk()
    register.title('Register User')
    register.geometry('450x230')
    register.resizable(False,False)

    fllname_lbl = Label(register, text="Full name:")
    fllname_ent = Entry(register)
    fllname_lbl.place(x=30, y=30)
    fllname_ent.place(x=150, y=30)

    usrname_lbl = Label(register, text="Username:")
    usrname_ent = Entry(register)
    usrname_lbl.place(x=30, y=70)
    usrname_ent.place(x=150, y=70)

    psswrd_lbl = Label(register, text="Password:")
    pssrwd_ent = Entry(register)
    psswrd_lbl.place(x=30, y=110)
    pssrwd_ent.place(x=150, y=110)

    def createUser():
        try:
            credentials = fllname_ent.get(), usrname_ent.get(), pssrwd_ent.get()
            usertbl = "INSERT INTO Users (Full_name, Username, Password) VALUES(%s, %s, %s)"
            mycursor.execute(usertbl, credentials)
            mydb.commit()
            messagebox.showinfo("Message", "User successfully created!")
        except:
            messagebox.showerror("ERROR", "User already exists")

    createusrbtn = Button(register, text="Create user", command=createUser)
    createusrbtn.place(x=120, y=170)


def login():
    try:
        loginsql = "select * from Users where Username = %s and Password=%s"
        mycursor.execute(loginsql,[(userent.get()), (userpsswrd.get())])

        usersdb = mycursor.fetchall()
        if usersdb:
            messagebox.showinfo('Message','Logged in successfully')
            master = Tk()
            master.mainloop()
    except:
        pass
lgnbtn = Button(window, text="Login" ,command=login)
lgnbtn.place(x=160, y=140)
rgstbtn = Button(window, text="Register", command=registerUser)
rgstbtn.place(x=260, y=140)

window.mainloop()
