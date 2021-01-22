# ZOE ANNASTASIA ENGEL
# CLASS 1

# TO ACCESS ADMIN PAGE PRESS CNTRL+a KEYS
from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from datetime import *

# IMPORTING THE MYSQL DATABASE
mydb = mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', db='lifechoicesonline', host='127.0.0.1',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

# CREATING MAIN LOGIN WINDOW
window = tk.Tk()
window.title('Life Choices online')
window.geometry('460x230')
window.resizable(False, False)
lblusername = Label(window, text='Username:')
lblusername.place(x=30, y=30)
userent = Entry(window)
userent.place(x=150, y=30)

lblpsswrd = Label(text='Password:')
lblpsswrd.place(x=30, y=80)
userpsswrd = Entry(window, show='*')
userpsswrd.place(x=150, y=78)


# QUIT WINDOW FUNCTION
def exit():
    ex = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?', icon='warning')
    if ex == 'yes':
        window.destroy()
    else:
        pass


# NEW TKINTER PAGE TO REGISTER A NEW USER/VISITOR
def registerUser():
    register = Tk()
    register.title('Register User')
    register.geometry('450x230')
    register.resizable(False, False)

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

    # FUNCTION TO CREATE THE NEW USER/VISITOR
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


# LOGIN FUNCTION WHICH TRACKS THE SIGN-IN/SIGN-OUT TIME
def login():
    try:
        loginsql = "select * from Users where Username = %s and Password=%s"
        mycursor.execute(loginsql, [(userent.get()), (userpsswrd.get())])

        usersdb = mycursor.fetchall()
        if usersdb:
            messagebox.showinfo('Message', 'Logged in successfully')
            master = Tk()
            master.title("Sign-in Sign-out")
            master.geometry("250x100")
            timeIn = datetime.now()
            x = timeIn.strftime("%H:%M:%S")


            # POPS UP THE SIGN UP PAGE WITH THE SIGN OUT BUTTON
            def signout():
                timeout = datetime.now()
                y = timeout.strftime("%H:%M:%S")
                z = userent.get()
                infoTime = z, x, y
                timeComm = "INSERT INTO Time_Register(Username, Sign_in, Sign_out) VALUES(%s, %s, %s)"

                mycursor.execute(timeComm, infoTime)
                mydb.commit()
                messagebox.showinfo('Message', 'Signed out!')
                master.destroy()

            sign_outbtn = Button(master, text="Sign out", command=signout, bg="green", fg="white")
            sign_outbtn.place(x=90, y=30)
            master.mainloop()
    except:
        pass


# ADMINS LOGIN PAGE
def createAdmin():
    root = Tk()
    root.title("Admin login")
    root.geometry('450x230')
    root.resizable(False, False)

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

    def loginAdmin():
        try:
            adminlgn= "select * from Admin where Username = %s and Password=%s"
            mycursor.execute(adminlgn, [(usrname_ent.get()), (pssrwd_ent.get())])
            usersdb = mycursor.fetchall()
            if usersdb:
                messagebox.showinfo('Message', 'Logged in successfully')
                table = Tk()
                table.title("Database tables")
                table.geometry("880x500")
                table.resizable(False,False)

                # SHOWING USERS IN A LIST BOX
                ID = Label(table, text="ID")
                Fulln = Label(table, text="Full name")
                Usernm = Label(table, text="Username")
                Passwrd = Label(table, text="Password")

                IDList = Listbox(table, width=25)
                FullnmList = Listbox(table, width=25)
                UsernmList = Listbox(table, width=25)
                PasswrdList = Listbox(table, width=25)

                # SHOWING SIGN IN/SIGN OUT TIMES IN A LIST BOX
                Username = Label(table, text="Username")
                Signin = Label(table, text="Sign in")
                Signout = Label(table, text="Sign out")

                Usernamelist = Listbox(table, width=25)
                Signlist = Listbox(table, width=25)
                Signoutlist = Listbox(table, width=25)

                # FOR LOOPS (USERS LIST BOX)
                mycursor.execute("SELECT ID from Users")
                tab = mycursor.fetchall()

                for i in tab:
                    IDList.insert(END, i)

                mycursor.execute("SELECT Full_name from Users")
                tab = mycursor.fetchall()

                for i in tab:
                    FullnmList.insert(END, i)

                mycursor.execute("SELECT Username from Users")
                tab = mycursor.fetchall()

                for i in tab:
                    PasswrdList.insert(END, i)

                mycursor.execute("SELECT Password from Users")
                tab = mycursor.fetchall()

                for i in tab:
                    UsernmList.insert(END, i)

                # FOR LOOPS FOR TIME REGISTER
                mycursor.execute("SELECT Username from Time_Register")
                tab = mycursor.fetchall()

                for i in tab:
                    Usernamelist.insert(END, i)

                mycursor.execute("SELECT Sign_in from Time_Register")
                tab = mycursor.fetchall()

                for i in tab:
                    Signlist.insert(END, i)

                mycursor.execute("SELECT Sign_out from Time_Register")
                tab = mycursor.fetchall()

                for i in tab:
                    Signoutlist.insert(END, i)

                ID.place(x=5, y=4)
                IDList.place(x=5,y=20)
                Fulln.place(x=225, y=4)
                FullnmList.place(x=225, y=20)
                Usernm.place(x=445, y=4)
                UsernmList.place(x=445, y=20)
                Passwrd.place(x=670, y=4)
                PasswrdList.place(x=670, y=20)

                Username.place(x=5, y=210)
                Usernamelist.place(x=5, y=230)
                Signin.place(x=225, y=210)
                Signlist.place(x=225, y=230)
                Signout.place(x=445, y=210)
                Signoutlist.place(x=445, y=230)

                table.mainloop()
            else:
                messagebox.showinfo('Error', 'Incorrect Password/Username')
                quit()
        except:
            pass

    createadminusrbtn = Button(root, text="Create user", command=createSuperUser, bg="green", fg="white")
    createadminusrbtn.place(x=125, y=170)
    # LOGIN BUTTON
    admin_login = Button(root, text="Login", command=loginAdmin)
    admin_login.place(x=50, y=170)


# CREAING A HOT KEY (PRESS Cntrl+a)
def key():
    createAdmin()
window.bind("<Control-a>", lambda x: key())

lgnbtn = Button(window, text="Login", command=login, bg="green", fg="white")
lgnbtn.place(x=160, y=140)
rgstbtn = Button(window, text="Register New User", command=registerUser, bg="green", fg="white")
rgstbtn.place(x=260, y=140)
close_btn = Button(window, text='Quit', bg='red', command=exit)
close_btn.place(x=396, y=190)
window.mainloop()

# GRANT PRIVILAGES TO ADMIN USER, MUST VIEW DATABASE TABLES, CREATE/DELETE USER FROM USERS TABLE
# Login As admin and view tables
