from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from datetime import *

mydb = mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', db='lifechoicesonline', host='127.0.0.1', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

window = tk.Tk()
window.title('Life Choices online')
window.geometry('450x220')
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
            register.destroy()
        except:
            messagebox.showerror("ERROR", "User already exists")

    createusrbtn = Button(register, text="Create user", command=createUser, bg="green", fg="white")
    createusrbtn.place(x=120, y=170)


def login():
    try:
        loginsql = "select * from Users where Username = %s and Password=%s"
        mycursor.execute(loginsql,[(userent.get()), (userpsswrd.get())])

        usersdb = mycursor.fetchall()
        if usersdb:
            messagebox.showinfo('Message','Logged in successfully')
            master = Tk()
            master.title("Sign-in Sign-out")
            master.geometry("250x100")
            timeIn = datetime.now()
            x = timeIn.strftime("%H:%M:%S")
            def signout():
                timeout = datetime.now()
                y = timeout.strftime("%H:%M:%S")
                z = userent.get()

                infoTime = z, x, y

                timeComm = "INSERT INTO Time_Register(Username, Sign_in, Sign_out) VALUES(%s, %s, %s)"

                mycursor.execute(timeComm, infoTime)

                mydb.commit()
                messagebox.showinfo('Message','Signed out!')
                master.destroy()
            sign_outbtn= Button(master, text="Sign out", command=signout ,bg="green", fg="white")
            sign_outbtn.place(x=90, y=30)
            master.mainloop()
    except:
        pass
def createAdmin():
    root=Tk()
    root.title("Create Admin/User")
    root.geometry('450x230')


    fllname_lbl = Label(root, text="Full name:")
    fllname_ent = Entry(root)
    fllname_lbl.place(x=30, y=30)
    fllname_ent.place(x=150, y=30)

    usrname_lbl = Label(root, text="Username:")
    usrname_ent = Entry(root)
    usrname_lbl.place(x=30, y=70)
    usrname_ent.place(x=150, y=70)

    psswrd_lbl = Label(root, text="Password:")
    pssrwd_ent = Entry(root, show="*")
    psswrd_lbl.place(x=30, y=110)
    pssrwd_ent.place(x=150, y=110)

    def createSuperUser():
        try:
            credentials = fllname_ent.get(), pssrwd_ent.get(), usrname_ent.get()
            admintbl = "INSERT INTO Admin (full_name, password, username) VALUES(%s, %s, %s)"
            mycursor.execute(admintbl, credentials)
            mydb.commit()
            messagebox.showinfo("Message", "User successfully created!")
            root.destroy()
        except:
            messagebox.showerror("ERROR", "User already exists")

    createadminusrbtn = Button(root, text="Create user", command=createSuperUser, bg="green", fg="white")
    createadminusrbtn.place(x=120, y=170)

lgnbtn = Button(window, text="Login" ,command=login , bg="green", fg="white")
lgnbtn.place(x=160, y=140)
rgstbtn = Button(window, text="Register", command=registerUser, bg="green", fg="white")
rgstbtn.place(x=260, y=140)
admin_btn = Button(window, text="Create admin/user", bg="grey", fg="white" , command=createAdmin)
admin_btn.place(x=160, y=180)
window.mainloop()
