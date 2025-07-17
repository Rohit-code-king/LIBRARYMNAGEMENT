#*********************************imported modules*********************************************************
import os
import smtplib
import random
import mysql.connector as sql
from tkinter import *
from tkinter import PhotoImage
from login import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext
from datetime import timedelta
from datetime import date
from datetime import datetime
from email.mime.text import MIMEText
#*********************************imported modules*********************************************************

#***************************************mysql connections***************************************************
mysql_passcode=os.environ.get('Mysql_passcode') # the environmental variable - 'Mysql_passcode' stores the passcode
mysql_database=os.environ.get('database_mysql_for_library_project')
# database must also be variablised
mycon=sql.connect(host='localhost',user='root',passwd=mysql_passcode,database=mysql_database)
cursor_mysql=mycon.cursor()
#***************************************mysql connections***************************************************

#**************************User Variables************************************************#
'''
user_first_name
user_last_name
user_email_id
user_name
user_username           #not safe to store password
user_gender
user_phone_no
user_country
user_account
'''
#*********************************************************User Variables***************



#Function Definitions********************************************************************************************


#*********************************imported modules*********************************************************
import os
import smtplib
import random
import mysql.connector as sql
from tkinter import *
from tkinter import PhotoImage
from login import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext
from datetime import timedelta
from datetime import date
from datetime import datetime
from email.mime.text import MIMEText
#*********************************imported modules*********************************************************

#***************************************mysql connections***************************************************
mysql_passcode=os.environ.get('Mysql_passcode') # the environmental variable - 'Mysql_passcode' stores the passcode
mysql_database=os.environ.get('database_mysql_for_library_project')
# database must also be variablised
mycon=sql.connect(host='localhost',user='root',passwd=mysql_passcode,database=mysql_database)
cursor_mysql=mycon.cursor()
#***************************************mysql connections***************************************************

#**************************User Variables************************************************#
'''
user_first_name
user_last_name
user_email_id
user_name
user_username           #not safe to store password
user_gender
user_phone_no
user_country
user_account
'''
#*********************************************************User Variables***************



#Function Definitions********************************************************************************************



def librarymang_home_page_student():
    global librarymang_home_page_student_root
    login_screen.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)

def force_exit_from_borrow_due_to_more_than_3_issue_to_librarymang_home_page_student():
    global librarymang_home_page_student_root
    book_issue_verification_tkinter_page_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)


def librarymang_home_page_student_from_the_borrow_book_page():
    global librarymang_home_page_student_root
    borrow_books_student_page_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)


def librarymang_home_page_student_from_book_issue_verification_tkinter_page():
    global librarymang_home_page_student_root
    book_issue_verification_tkinter_page_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)

def librarymang_home_page_student_after_issue_of_book():
    global librarymang_home_page_student_root
    book_issue_verification_tkinter_page_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)



def librarymang_home_page_student_from_return_of_book():
    global librarymang_home_page_student_root
    return_books_student_page_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)



def librarymang_home_page_student_after_return_of_book():
    global librarymang_home_page_student_root
    book_return_verification_tkinter_page_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)


def librarymang_home_page_student_from_view_borrowed_of_book():
    global librarymang_home_page_student_root
    view_borrowed_books_page_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)



def librarymang_home_page_student_after_viewing_of_book():
    global librarymang_home_page_student_root
    book_view_verification_tkinter_page_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)

def librarymang_home_page_student_after_profile():
    global librarymang_home_page_student_root
    profile_student_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)


def librarymang_home_page_student_after_profile_edit():
    global librarymang_home_page_student_root
    profile_student_root_edit.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)



#*********************************************************************************************************************************************************************************





def profile_page_student():
    global profile_student_root
    librarymang_home_page_student_root.destroy()
    profile_student_root=Tk()
    profile_student_root.title('Profile')
    profile_student_root.state("zoomed")
    profile_student_root.config(background = "black", pady=10)
    Label(profile_student_root, text="Profile",width=100, font=("freestyle script", 70)).pack()
    Label(profile_student_root,text="Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(profile_student_root,text="Username:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(profile_student_root,text="Email-Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=350)
    Label(profile_student_root,text="Gender:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=350)
    Label(profile_student_root,text="Country:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=600)
    Label(profile_student_root,text="Account Type:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=600)



    Label(profile_student_root,text=user_name,font=("verdana", 20),width=30,anchor='w').place(x=250,y=150)
    Label(profile_student_root,text=user_username,font=("verdana", 20),width=20,anchor='w').place(x=1225,y=150)
    Label(profile_student_root,text=user_email_id,font=("verdana", 20),width=30,anchor='w').place(x=310,y=350)
    Label(profile_student_root,text=user_gender,font=("verdana", 20),width=20,anchor='w').place(x=1185,y=350)
    Label(profile_student_root,text=user_country,font=("verdana", 20),width=20,anchor='w').place(x=300,y=600)
    Label(profile_student_root,text=user_account,font=("verdana", 20),width=20,anchor='w').place(x=1300,y=600)

    Button(profile_student_root,text='Edit',font=('verdana',25),cursor='hand2',bg='green',width=10,command=profile_page_student_edit).place(x=850,y=800)
    Button(profile_student_root,text='Go Back',font=('verdana',25),cursor='hand2',width=10,command=librarymang_home_page_student_after_profile).place(x=500,y=800)
    Button(profile_student_root,text='Log Out',font=('verdana',25),cursor='hand2',bg='red',width=10,command=log_out_from_profile).place(x=1200,y=800)
    photo = PhotoImage(file = "e.png")
    profile_student_root.iconphoto(False, photo)

def profile_page_student_edit():
    global profile_student_root_edit
    global edit_profile_first_name_var
    global edit_profile_last_name_var
    global edit_profile_username_var
    global edit_profile_gender_var
    global edit_profile_country_var
    global edit_profile_phone_no_var
    if user_phone_no==None:
        phoneno=''
    else:
        phoneno=str(user_phone_no)
    profile_student_root.destroy()
    profile_student_root_edit=Tk()
    profile_student_root_edit.title("Edit")
    profile_student_root_edit.state("zoomed")
    profile_student_root_edit.config(background = "black", pady=10)
    Label(profile_student_root_edit, text="Profile",width=100, font=("freestyle script", 70)).pack()
    Label(profile_student_root_edit,text="First Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(profile_student_root_edit,text="Last Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(profile_student_root_edit,text="Username:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=350)
    Label(profile_student_root_edit,text="Email-Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=350)
    Label(profile_student_root_edit,text="Gender:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=600)
    Label(profile_student_root_edit,text="Country:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=600)
    Label(profile_student_root_edit,text="Phone No:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=850)

    edit_profile_first_name_var=StringVar()
    edit_profile_last_name_var=StringVar()
    edit_profile_username_var=StringVar()
    edit_profile_gender_var=StringVar()
    edit_profile_country_var=StringVar()
    edit_profile_phone_no_var=StringVar()

    edit_profile_first_name_var.set(user_first_name)
    edit_profile_last_name_var.set(user_last_name)
    edit_profile_username_var.set(user_username)
    edit_profile_gender_var.set(user_gender)
    edit_profile_country_var.set(user_country)
    edit_profile_phone_no_var.set(phoneno)


    e1=Entry(profile_student_root_edit,textvariable=edit_profile_first_name_var,font=("verdana", 20),width=30)
    e2=Entry(profile_student_root_edit,textvariable=edit_profile_last_name_var,font=("verdana", 20),width=20)
    e3=Entry(profile_student_root_edit,textvariable=edit_profile_username_var,font=("verdana", 20),width=20)
    e4=Label(profile_student_root_edit,text=user_email_id,font=("verdana", 20),width=30,anchor='w')

    edit_profile_gender_list=[ 'male','female']
    edit_profile_gender_droplist=OptionMenu(profile_student_root_edit, edit_profile_gender_var, *edit_profile_gender_list)
    edit_profile_gender_droplist.config(font=("verdana", 20),width=20)

    edit_profile_country_list=[ 'India' ,'US' , 'UK' ,'Australia' ,'Canada']
    edit_profile_country_droplist=OptionMenu(profile_student_root_edit, edit_profile_country_var, *edit_profile_country_list)
    edit_profile_country_droplist.config(font=("verdana", 20),width=20)
    edit_profile_country_droplist.place(x=1250,y=250)

    e7=Entry(profile_student_root_edit,textvariable=edit_profile_phone_no_var,font=("verdana", 20),width=20)

    e1.place(x=350,y=150)
    e2.place(x=1235,y=150)
    e3.place(x=350,y=350)
    e4.place(x=1245,y=350)
    edit_profile_gender_droplist.place(x=300,y=600)
    edit_profile_country_droplist.place(x=1200,y=600)
    e7.place(x=310,y=850)

    Button(profile_student_root_edit,text='Edit',font=('verdana',25),cursor='hand2',bg='green',width=10,command=check_edit_profile_info_student).place(x=1350,y=750)
    Button(profile_student_root_edit,text='Go Back',font=('verdana',25),cursor='hand2',width=10,command=librarymang_home_page_student_after_profile_edit).place(x=1350,y=900)
    photo = PhotoImage(file = "e.png")
    profile_student_root_edit.iconphoto(False, photo)


def check_edit_profile_info_student():
    edit_profile_first_name=edit_profile_first_name_var.get()
    edit_profile_last_name=edit_profile_last_name_var.get()
    edit_profile_username=edit_profile_username_var.get()
    edit_profile_gender=edit_profile_gender_var.get()
    edit_profile_country=edit_profile_country_var.get()
    edit_profile_phone_no=edit_profile_phone_no_var.get()
    ref_for_edit_verify=0
    query_edit_info="select username from logindata where emailid!='{0}';"      #We are creating 2 lists of already eisting username and emails from testlogin
    cursor_mysql.execute(query_edit_info.format(user_email_id))
    output1=cursor_mysql.fetchall()
    list_of_usernames=[]
    for username_tuple in output1:
        list_of_usernames.append(username_tuple[0])
  
    if edit_profile_username=='' and ref_for_edit_verify==0:
        messagebox.showerror('username error','please enter username')
        ref_for_edit_verify=2
    elif len(edit_profile_username)<6 and len(edit_profile_username)>=20 and ref_for_edit_verify==0:
        messagebox.showerror('username error','username must have atleast 6 char')
        ref_for_edit_verify=2
    elif edit_profile_username[0].isdigit() and ref_for_edit_verify==0:
        messagebox.showerror('username error','username cant start with numbers')
        ref_for_edit_verify=2
    elif edit_profile_username in list_of_usernames:   #checking for duplicates of username
        messagebox.showerror('username error','Username is taken')
        ref_for_edit_verify=2
    else:
        pass
    
    if ref_for_edit_verify==0:
        if edit_profile_phone_no=='':
            pass
        elif not edit_profile_phone_no.isdigit():
            messagebox.showerror('phone no','invaid phone no')
            ref_for_edit_verify=4
        elif len(str(edit_profile_phone_no))!=10:
            messagebox.showerror('phone no','invaid phone no')
            ref_for_edit_verify=4
        else:
            pass
    else:
        pass
    if len(edit_profile_first_name)==0 and ref_for_edit_verify==0:
        messagebox.showerror('error','please enter name')
        ref_for_edit_verify=5
    elif len(edit_profile_last_name)==0 and ref_for_edit_verify==0:
        messagebox.showerror('error','please enter last name')
        ref_for_edit_verify=5
    elif len(edit_profile_first_name)>20 and ref_for_edit_verify==0:
        messagebox.showerror('error','name should be less than 21 charcters')
        ref_for_edit_verify=5
    elif len(edit_profile_last_name)>20 and ref_for_edit_verify==0:
        messagebox.showerror('error','last name should be less than 21 charcters')
        ref_for_edit_verify=5
    else:
        pass

    if edit_profile_gender=='' and ref_for_edit_verify==0:
        messagebox.showerror('error','please enter your gender')
        ref_for_edit_verify=6
    elif edit_profile_gender not in ['male','female']:
        messagebox.showerror('error','please enter your gender')
        ref_for_edit_verify=6
    else:
        pass
    if ref_for_edit_verify==0 and edit_profile_country=='':
        messagebox.showerror('error','please enter country')
        ref_for_edit_verify=7
    elif ref_for_edit_verify==0 and (edit_profile_country not in [ 'India' ,'US' , 'UK' ,'Australia' ,'Canada']):
        messagebox.showerror('error','cant verify your country')
        ref_for_edit_verify=7
    else:
        pass


    if (('\'' in edit_profile_username) or ('\"' in edit_profile_username) or ('\'' in edit_profile_first_name) or ('\"' in edit_profile_first_name) or ('\'' in edit_profile_last_name) or ('\"' in edit_profile_last_name)) and  ref_for_edit_verify==0:
        messagebox.showinfo('error','Dnot use \' or \" in any field')
        ref_for_edit_verify=9
    if ref_for_edit_verify==0:
        updating_profile_student(edit_profile_username,edit_profile_phone_no,edit_profile_first_name,edit_profile_last_name,edit_profile_gender,edit_profile_country)  # True and False returned is just for reference. In the main program define a global variable using 'global' and assign true and false to that. if the variable is true follow on with the sign up and then break out of while loop int new page but if false reload page using while loop.
    else:
        pass

def updating_profile_student(username,phoneno,firstname,lastname,gender,country):
    global user_username
    global user_name
    global user_gender
    global user_phone_no
    global user_first_name
    global user_last_name
    global user_country
    try:
        if phoneno=='':
            query1="update logindata set username='{0}',phoneno=Null,firstname='{1}',lastname='{2}',gender='{3}',country='{4}' where emailid='{5}';"
            query2="update loginissue set username='{0}' where username='{1}';"
            query3="update bookissue set username='{0}' where username='{1}';"
            cursor_mysql.execute(query1.format(username,firstname,lastname,gender,country,user_email_id))
            mycon.commit()
            a=2
            cursor_mysql.execute(query2.format(username,user_username))
            mycon.commit()
            a=3
            cursor_mysql.execute(query3.format(username,user_username))
            mycon.commit()
        else:
            query1="update logindata set username='{0}',phoneno='{1}',firstname='{2}',lastname='{3}',gender='{4}',country='{5}' where emailid='{6}';"
            query2="update loginissue set username='{0}' where username='{1}';"
            query3="update bookissue set username='{0}' where username='{1}';"
            cursor_mysql.execute(query1.format(username,phoneno,firstname,lastname,gender,country,user_email_id))
            mycon.commit()
            a=2
            cursor_mysql.execute(query2.format(username,user_username))
            mycon.commit()
            a=3
            cursor_mysql.execute(query3.format(username,user_username))
            mycon.commit()
        ref=1
    except:
        messagebox.showinfo('oops','something went wrong')
        ref=2
        librarymang_home_page_student_after_profile_edit()
    if ref==1:
        messagebox.showinfo('success','Profile Updated')

        user_username=username
        user_name=firstname+' '+lastname
        user_gender=gender
        user_phone_no=phoneno
        user_first_name=firstname
        user_last_name=lastname
        user_country=country
        librarymang_home_page_student_after_profile_edit()









def log_out_from_profile():
    global user_email_id
    global user_name
    global user_username           
    global user_gender
    global user_phone_no
    global user_country
    global user_account
    user_email_id=''
    user_name=''
    user_username=''
    user_phone_no=None
    user_gender=''
    user_country=''
    user_account=''
    profile_student_root.destroy()
    login_screen_from_student_profile()











#************************************************************************************************************************************************************************************




def view_borrowed_books():
    global view_borrowed_books_page_root
    librarymang_home_page_student_root.destroy()
    view_borrowed_books_page_root=Tk()
    view_borrowed_books_page_root.title('View Borrowed Books')
    view_borrowed_books_page_root.config(bg='black',pady=10)
    view_borrowed_books_page_root.state('zoomed')
    Label(view_borrowed_books_page_root, text="View Borrowed book",width=100, font=("freestyle script", 70)).pack()
    count_of_borrowed_books_for_view()

    Button(view_borrowed_books_page_root,text='Go Back',font=('verdana',25),cursor='hand2',command=librarymang_home_page_student_from_view_borrowed_of_book).place(x=1070,y=800)
    Button(view_borrowed_books_page_root,text='Show Book Info',font=('verdana',25),cursor='hand2',command=clicking_proceed_in_view_fn,).place(x=700,y=800)
    photo = PhotoImage(file = "e.png")
    view_borrowed_books_page_root.iconphoto(False, photo)


def count_of_borrowed_books_for_view():
    global no_of_borrowed_books_for_view
    global list_of_books_for_view
    global dict_of_books_for_view
    dict_of_books_for_view={}
    list_of_books_for_view=[]
    query="select * from loginissue where username='{0}'"
    cursor_mysql.execute(query.format(user_username))
    output=cursor_mysql.fetchall()
    no_of_borrowed_books_for_view=0
    tup_of_borrowed_books_for_view=output[0]
    if tup_of_borrowed_books_for_view[1]==None:
        no_of_borrowed_books_for_view=0
    else:
        if tup_of_borrowed_books_for_view[2]==None:
            no_of_borrowed_books_for_view=1
        else:
            if tup_of_borrowed_books_for_view[3]==None:
                no_of_borrowed_books_for_view=2
            else:
                no_of_borrowed_books_for_view=3

    if no_of_borrowed_books_for_view==0:
        nothing_to_view_fn()
    elif no_of_borrowed_books_for_view==1:
        query1="select book_id2,date_of_issue,date_of_return from bookissue where username='{0}';"
        cursor_mysql.execute(query1.format(user_username))
        out1=cursor_mysql.fetchall()
        bookid=out1[0][0]
        query12="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query12.format(bookid))
        out12=cursor_mysql.fetchall()
        dict_of_books_for_view[1]=[bookid,out12[0][0],out12[0][1],str(out1[0][1]),str(out1[0][2])]
        list_of_books_for_view.append([bookid,out12[0][0],out12[0][1],str(out1[0][1]),str(out1[0][2]),1])
        one_book_to_view()
    elif no_of_borrowed_books_for_view==2:
        query2="select book_id2,date_of_issue,date_of_return from bookissue where username='{0}';"
        cursor_mysql.execute(query2.format(user_username))
        out2=cursor_mysql.fetchall()
        bookid21=out2[0][0]
        bookid22=out2[1][0]
        
        query21="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query21.format(bookid21))
        out22=cursor_mysql.fetchall()
        dict_of_books_for_view[1]=[bookid21,out22[0][0],out22[0][1],str(out2[0][1]),str(out2[0][2])]
        list_of_books_for_view.append([bookid21,out22[0][0],out22[0][1],str(out2[0][1]),str(out2[0][2]),1])
        
        query23="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query23.format(bookid22))
        out23=cursor_mysql.fetchall()
        dict_of_books_for_view[2]=[bookid22,out23[0][0],out23[0][1],str(out2[1][1]),str(out2[1][2])]
        list_of_books_for_view.append([bookid22,out23[0][0],out23[0][1],str(out2[1][1]),str(out2[1][2]),2])
        two_books_to_view()
    else:
        query3="select book_id2,date_of_issue,date_of_return from bookissue where username='{0}';"
        cursor_mysql.execute(query3.format(user_username))
        out3=cursor_mysql.fetchall()
        bookid31=out3[0][0]
        bookid32=out3[1][0]
        bookid33=out3[2][0]

        query31="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query31.format(bookid31))
        out32=cursor_mysql.fetchall()
        dict_of_books_for_view[1]=[bookid31,out32[0][0],out32[0][1],str(out3[0][1]),str(out3[0][2])]
        list_of_books_for_view.append([bookid31,out32[0][0],out32[0][1],str(out3[0][1]),str(out3[0][2]),1])

        query32="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query32.format(bookid32))
        out33=cursor_mysql.fetchall()
        dict_of_books_for_view[2]=[bookid32,out33[0][0],out33[0][1],str(out3[1][1]),str(out3[1][2])]
        list_of_books_for_view.append([bookid32,out33[0][0],out33[0][1],str(out3[1][1]),str(out3[1][2]),2])

        query33="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query33.format(bookid33))
        out34=cursor_mysql.fetchall()
        dict_of_books_for_view[3]=[bookid33,out34[0][0],out34[0][1],str(out3[2][1]),str(out3[2][2])]
        list_of_books_for_view.append([bookid33,out34[0][0],out34[0][1],str(out3[2][1]),str(out3[2][2]),3])
        three_books_to_view()

def obtaining_month_day_year_of_view(due_date):

    list_of_day_month_year=due_date.split('-')
    year_of_view=int(list_of_day_month_year[0])
    month_of_view=int(list_of_day_month_year[1])
    day_of_view=int(list_of_day_month_year[2])
    bool_val_for_date=(datetime.now()>datetime(year_of_view,month_of_view,day_of_view))
    return bool_val_for_date



def nothing_to_view_fn():
    global book_name_select_for_view
    global book_name_select_for_view_var
    book_name_select_for_view_var=book_name_select_for_view='chumma'
    Label(view_borrowed_books_page_root,text="You Have Not Borrowed Any Book",font=("lucida handwriting", 30),bg='black',fg='white').place(x=600,y=300)


def one_book_to_view():
    global book_name_select_for_view_var
    global main_frame6
    innerframe6=LabelFrame(view_borrowed_books_page_root,text='books',bd=15,width=1000)
    innerframe6.place(x=300,y=300)

    #Creating Main fram:
    main_frame6=Frame(innerframe6,width=1000)
    main_frame6.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_view_var=IntVar()
    if obtaining_month_day_year_of_view(dict_of_books_for_view[1][4]):
        radiobutton_color_if_due_date_is_past_view(list_of_books_for_view[0][5],list_of_books_for_view[0][1],list_of_books_for_view[0][2],list_of_books_for_view[0][4])
    else:
        radiobutton_color_if_due_date_is_only_coming_view(list_of_books_for_view[0][5],list_of_books_for_view[0][1],list_of_books_for_view[0][2],list_of_books_for_view[0][4])



def two_books_to_view():
    global book_name_select_for_view_var
    global main_frame6
    innerframe6=LabelFrame(view_borrowed_books_page_root,text='books',bd=15,width=1000)
    innerframe6.place(x=300,y=300)

    #Creating Main fram:
    main_frame6=Frame(innerframe6,width=1000)
    main_frame6.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_view_var=IntVar()
    if obtaining_month_day_year_of_view(dict_of_books_for_view[1][4]):
        radiobutton_color_if_due_date_is_past_view(list_of_books_for_view[0][5],list_of_books_for_view[0][1],list_of_books_for_view[0][2],list_of_books_for_view[0][4])
    else:
        radiobutton_color_if_due_date_is_only_coming_view(list_of_books_for_view[0][5],list_of_books_for_view[0][1],list_of_books_for_view[0][2],list_of_books_for_view[0][4])

    if obtaining_month_day_year_of_view(dict_of_books_for_view[2][4]):
        radiobutton_color_if_due_date_is_past_view(list_of_books_for_view[1][5],list_of_books_for_view[1][1],list_of_books_for_view[1][2],list_of_books_for_view[1][4])
    else:
        radiobutton_color_if_due_date_is_only_coming_view(list_of_books_for_view[1][5],list_of_books_for_view[1][1],list_of_books_for_view[1][2],list_of_books_for_view[1][4],)

def three_books_to_view():
    global book_name_select_for_view_var
    global main_frame6
    innerframe6=LabelFrame(view_borrowed_books_page_root,text='books',bd=15,width=1000)
    innerframe6.place(x=300,y=300)

    #Creating Main fram:
    main_frame6=Frame(innerframe6,width=1000)
    main_frame6.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_view_var=IntVar()
    if obtaining_month_day_year_of_view(dict_of_books_for_view[1][4]):
        radiobutton_color_if_due_date_is_past_view(list_of_books_for_view[0][5],list_of_books_for_view[0][1],list_of_books_for_view[0][2],list_of_books_for_view[0][4])
    else:
        radiobutton_color_if_due_date_is_only_coming_view(list_of_books_for_view[0][5],list_of_books_for_view[0][1],list_of_books_for_view[0][2],list_of_books_for_view[0][4])

    if obtaining_month_day_year_of_view(dict_of_books_for_view[2][4]):
        radiobutton_color_if_due_date_is_past_view(list_of_books_for_view[1][5],list_of_books_for_view[1][1],list_of_books_for_view[1][2],list_of_books_for_view[1][4])
    else:
        radiobutton_color_if_due_date_is_only_coming_view(list_of_books_for_view[1][5],list_of_books_for_view[1][1],list_of_books_for_view[1][2],list_of_books_for_view[1][4],)
    
    if obtaining_month_day_year_of_view(dict_of_books_for_view[3][4]):
        radiobutton_color_if_due_date_is_past_view(list_of_books_for_view[2][5],list_of_books_for_view[2][1],list_of_books_for_view[2][2],list_of_books_for_view[2][4])
    else:
        radiobutton_color_if_due_date_is_only_coming_view(list_of_books_for_view[2][5],list_of_books_for_view[2][1],list_of_books_for_view[2][2],list_of_books_for_view[2][4])
    
    

def radiobutton_color_if_due_date_is_only_coming_view(ival,bookname,bookauthor,duedate):
    global book_name_select_for_view_var
    Radiobutton(main_frame6,text=bookname+'        (   by  '+bookauthor+' )\n(   Due On '+duedate+'   )',font=("lucida handwriting", 30),indicator=0,variable=book_name_select_for_view_var,value=ival,width=50,bg='cyan',fg='black',padx=10,anchor='w').pack()
def radiobutton_color_if_due_date_is_past_view(ival,bookname,bookauthor,duedate):
    global book_name_select_for_view_var
    Radiobutton(main_frame6,text=bookname+'        (   by  '+bookauthor+' )\n(   Book Due    )',font=("lucida handwriting", 30),indicator=0,variable=book_name_select_for_view_var,value=ival,width=50,bg='red',fg='black',padx=10,anchor='w').pack()




def clicking_proceed_in_view_fn():
    global book_name_select_for_view_var
    global main_list_regarding_book_and_author_info_for_view
    global dict_of_books_for_view

    try:
        book_name_select_for_view=book_name_select_for_view_var.get()
    except:
        book_name_select_for_view='chumma'
    main_list_regarding_book_and_author_info_for_view=[]
    if book_name_select_for_view==0:
        messagebox.showerror('view book','please select a book')
        ref=1
    elif book_name_select_for_view=='chumma' or book_name_select_for_view_var=='chumma':
        messagebox.showinfo('oops','You have not borrwed any book')
        librarymang_home_page_student_from_view_borrowed_of_book()
        ref=1
    else:
        main_list_regarding_book_and_author_info_for_view=dict_of_books_for_view[book_name_select_for_view][0:5]   #just so that the 4th column is taken
        book_view_verification_tkinter_page()







def book_view_verification_tkinter_page():
    global main_list_regarding_book_and_author_info_for_view
    global book_view_verification_tkinter_page_root

    view_borrowed_books_page_root.destroy()

    book_view_verification_tkinter_page_root=Tk()
    book_view_verification_tkinter_page_root.title('View Books')
    book_view_verification_tkinter_page_root.state("zoomed")

    book_view_verification_tkinter_page_root.config(background = "black", pady=10)

    obtaining_book_info_for_view(main_list_regarding_book_and_author_info_for_view)

    Label(book_view_verification_tkinter_page_root,text="Book Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=700,y=20)
    Label(book_view_verification_tkinter_page_root,text="Book Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(book_view_verification_tkinter_page_root,text="Book Author:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(book_view_verification_tkinter_page_root,text="Number Of Pages:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=250)
    Label(book_view_verification_tkinter_page_root,text="Book Cover:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=250)
    Label(book_view_verification_tkinter_page_root,text="Book Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=400)
    Label(book_view_verification_tkinter_page_root,text="Author Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=400)
    Label(book_view_verification_tkinter_page_root,text="Issue Date:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=680)
    Label(book_view_verification_tkinter_page_root,text="Return Date:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=680)

    Label(book_view_verification_tkinter_page_root,text=main_book_id_for_showing_in_book_view,font=("verdana", 20),width=20,anchor='w').place(x=890,y=20)
    Label(book_view_verification_tkinter_page_root,text=main_bookname_for_showing_in_book_view,font=("verdana", 20),width=30,anchor='w').place(x=350,y=150)
    Label(book_view_verification_tkinter_page_root,text=main_bookauthor_for_showing_in_book_view,font=("verdana", 20),width=30,anchor='w').place(x=1275,y=150)
    Label(book_view_verification_tkinter_page_root,text=str(main_number_of_pages_for_showing_in_book_view),font=("verdana", 20),width=20,anchor='w').place(x=460,y=250)
    Label(book_view_verification_tkinter_page_root,text=main_book_cover_for_showing_in_book_view,font=("verdana", 20),width=20,anchor='w').place(x=1245,y=250)
    Label(book_view_verification_tkinter_page_root,text=main_issue_date_for_showing_in_book_view,font=("verdana", 20),width=20,anchor='w').place(x=340,y=680)
    Label(book_view_verification_tkinter_page_root,text=main_return_date_for_showing_in_book_view,font=("verdana", 20),width=20,anchor='w').place(x=1270,y=680)

    first_scroll_for_view=scrolledtext.ScrolledText(book_view_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    second_scroll_for_view=scrolledtext.ScrolledText(book_view_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    first_scroll_for_view.insert(END,main_bookinfo_for_showing_in_book_view)
    second_scroll_for_view.insert(END,main_author_info_for_showing_in_book_view)
    first_scroll_for_view.place(x=330,y=400)
    second_scroll_for_view.place(x=1270,y=400)

    Button(book_view_verification_tkinter_page_root,text='Go Back',font=('verdana',25),cursor='hand2',command=librarymang_home_page_student_after_viewing_of_book).place(x=800,y=800)
    photo = PhotoImage(file = "e.png")
    book_view_verification_tkinter_page_root.iconphoto(False, photo)
    


def obtaining_book_info_for_view(list_to_regard):
    global main_book_id_for_showing_in_book_view
    global main_bookname_for_showing_in_book_view
    global main_bookauthor_for_showing_in_book_view
    global main_bookinfo_for_showing_in_book_view
    global main_number_of_pages_for_showing_in_book_view
    global main_book_cover_for_showing_in_book_view
    global main_author_info_for_showing_in_book_view
    global main_issue_date_for_showing_in_book_view
    global main_return_date_for_showing_in_book_view

    query_for_book_last_view='''select * from bookdata where book_id='{0}';'''
    cursor_mysql.execute(query_for_book_last_view.format(list_to_regard[0]))
    new_list5=cursor_mysql.fetchall()


    main_book_id_for_showing_in_book_view=new_list5[0][0]
    main_bookname_for_showing_in_book_view=new_list5[0][1]
    main_bookauthor_for_showing_in_book_view=new_list5[0][2]
    main_number_of_pages_for_showing_in_book_view=new_list5[0][3]
    main_book_cover_for_showing_in_book_view=new_list5[0][6]
    main_bookinfo_for_showing_in_book_view=new_list5[0][4]
    if new_list5[0][5]==None:
        main_author_info_for_showing_in_book_view='No Information Available'
    else:
        main_author_info_for_showing_in_book_view=new_list5[0][5]

    query_for_books_view_2="select * from bookissue where book_id2='{0}';"
    cursor_mysql.execute(query_for_books_view_2.format(main_book_id_for_showing_in_book_view))
    newlist6=cursor_mysql.fetchall()
    list_local_issuedateview=(str(newlist6[0][2])).split('-')
    list_local_returndateview=(str(newlist6[0][3])).split('-')
    yearissueview=list_local_issuedateview[0]
    monthissueview=list_local_issuedateview[1]
    dayissueview=list_local_issuedateview[2]
    yearreturnview=list_local_returndateview[0]
    monthreturnview=list_local_returndateview[1]
    dayreturnview=list_local_returndateview[2]
    main_issue_date_for_showing_in_book_view=dayissueview+'-'+monthissueview+'-'+yearissueview
    main_return_date_for_showing_in_book_view=dayreturnview+'-'+monthreturnview+'-'+yearreturnview






#************************************************************************************************************************************************************************************


def return_books_student_page():
    global return_books_student_page_root
    librarymang_home_page_student_root.destroy()
    return_books_student_page_root=Tk()
    return_books_student_page_root.title('Return Books')
    return_books_student_page_root.config(bg='black',pady=10)
    return_books_student_page_root.state('zoomed')
    Label(return_books_student_page_root, text="Return book",width=100, font=("freestyle script", 70)).pack()
    count_of_borrowed_books()

    Button(return_books_student_page_root,text='Cancel',font=('verdana',25),cursor='hand2',command=librarymang_home_page_student_from_return_of_book).place(x=1000,y=800)
    Button(return_books_student_page_root,text='Proceed',font=('verdana',25),cursor='hand2',command=clicking_proceed_in_return_fn,).place(x=700,y=800)
    photo = PhotoImage(file = "e.png")
    return_books_student_page_root.iconphoto(False, photo)

def count_of_borrowed_books():
    global no_of_borrowed_books_for_return
    global list_of_books_for_return
    global dict_of_books_for_return
    dict_of_books_for_return={}
    list_of_books_for_return=[]
    query="select * from loginissue where username='{0}'"
    cursor_mysql.execute(query.format(user_username))
    output=cursor_mysql.fetchall()
    no_of_borrowed_books_for_return=0
    tup_of_borrowed_books_for_return=output[0]
    if tup_of_borrowed_books_for_return[1]==None:
        no_of_borrowed_books_for_return=0
    else:
        if tup_of_borrowed_books_for_return[2]==None:
            no_of_borrowed_books_for_return=1
        else:
            if tup_of_borrowed_books_for_return[3]==None:
                no_of_borrowed_books_for_return=2
            else:
                no_of_borrowed_books_for_return=3

    if no_of_borrowed_books_for_return==0:
        nothing_to_return_fn()
    elif no_of_borrowed_books_for_return==1:
        query1="select book_id2,date_of_issue,date_of_return from bookissue where username='{0}';"
        cursor_mysql.execute(query1.format(user_username))
        out1=cursor_mysql.fetchall()
        bookid=out1[0][0]
        query12="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query12.format(bookid))
        out12=cursor_mysql.fetchall()
        dict_of_books_for_return[1]=[bookid,out12[0][0],out12[0][1],str(out1[0][1]),str(out1[0][2])]
        list_of_books_for_return.append([bookid,out12[0][0],out12[0][1],str(out1[0][1]),str(out1[0][2]),1])
        one_book_to_return()
    elif no_of_borrowed_books_for_return==2:
        query2="select book_id2,date_of_issue,date_of_return from bookissue where username='{0}';"
        cursor_mysql.execute(query2.format(user_username))
        out2=cursor_mysql.fetchall()
        bookid21=out2[0][0]
        bookid22=out2[1][0]
        
        query21="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query21.format(bookid21))
        out22=cursor_mysql.fetchall()
        dict_of_books_for_return[1]=[bookid21,out22[0][0],out22[0][1],str(out2[0][1]),str(out2[0][2])]
        list_of_books_for_return.append([bookid21,out22[0][0],out22[0][1],str(out2[0][1]),str(out2[0][2]),1])
        
        query23="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query23.format(bookid22))
        out23=cursor_mysql.fetchall()
        dict_of_books_for_return[2]=[bookid22,out23[0][0],out23[0][1],str(out2[1][1]),str(out2[1][2])]
        list_of_books_for_return.append([bookid22,out23[0][0],out23[0][1],str(out2[1][1]),str(out2[1][2]),2])
        two_books_to_return()
    else:
        query3="select book_id2,date_of_issue,date_of_return from bookissue where username='{0}';"
        cursor_mysql.execute(query3.format(user_username))
        out3=cursor_mysql.fetchall()
        bookid31=out3[0][0]
        bookid32=out3[1][0]
        bookid33=out3[2][0]

        query31="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query31.format(bookid31))
        out32=cursor_mysql.fetchall()
        dict_of_books_for_return[1]=[bookid31,out32[0][0],out32[0][1],str(out3[0][1]),str(out3[0][2])]
        list_of_books_for_return.append([bookid31,out32[0][0],out32[0][1],str(out3[0][1]),str(out3[0][2]),1])

        query32="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query32.format(bookid32))
        out33=cursor_mysql.fetchall()
        dict_of_books_for_return[2]=[bookid32,out33[0][0],out33[0][1],str(out3[1][1]),str(out3[1][2])]
        list_of_books_for_return.append([bookid32,out33[0][0],out33[0][1],str(out3[1][1]),str(out3[1][2]),2])

        query33="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query33.format(bookid33))
        out34=cursor_mysql.fetchall()
        dict_of_books_for_return[3]=[bookid33,out34[0][0],out34[0][1],str(out3[2][1]),str(out3[2][2])]
        list_of_books_for_return.append([bookid33,out34[0][0],out34[0][1],str(out3[2][1]),str(out3[2][2]),3])
        three_books_to_return()

def obtaining_month_day_year_of_return(due_date):

    list_of_day_month_year=due_date.split('-')
    year_of_return=int(list_of_day_month_year[0])
    month_of_return=int(list_of_day_month_year[1])
    day_of_return=int(list_of_day_month_year[2])
    bool_val_for_date=(datetime.now()>datetime(year_of_return,month_of_return,day_of_return))
    return bool_val_for_date

def nothing_to_return_fn():
    global book_name_select_for_return
    global book_name_select_for_return_var
    book_name_select_for_return_var=book_name_select_for_return='chumma'
    Label(return_books_student_page_root,text="No Books To Return",font=("lucida handwriting", 30),bg='black',fg='white').place(x=700,y=300)


def one_book_to_return():
    global book_name_select_for_return_var
    global main_frame5
    innerframe5=LabelFrame(return_books_student_page_root,text='books',bd=15,width=1000)
    innerframe5.place(x=300,y=300)

    #Creating Main fram:
    main_frame5=Frame(innerframe5,width=1000)
    main_frame5.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_return_var=IntVar()
    if obtaining_month_day_year_of_return(dict_of_books_for_return[1][4]):
        radiobutton_color_if_due_date_is_past(list_of_books_for_return[0][5],list_of_books_for_return[0][1],list_of_books_for_return[0][2],list_of_books_for_return[0][4])
    else:
        radiobutton_color_if_due_date_is_only_coming(list_of_books_for_return[0][5],list_of_books_for_return[0][1],list_of_books_for_return[0][2],list_of_books_for_return[0][4])



def two_books_to_return():
    global book_name_select_for_return_var
    global main_frame5
    innerframe5=LabelFrame(return_books_student_page_root,text='books',bd=15,width=1000)
    innerframe5.place(x=300,y=300)

    #Creating Main fram:
    main_frame5=Frame(innerframe5,width=1000)
    main_frame5.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_return_var=IntVar()
    if obtaining_month_day_year_of_return(dict_of_books_for_return[1][4]):
        radiobutton_color_if_due_date_is_past(list_of_books_for_return[0][5],list_of_books_for_return[0][1],list_of_books_for_return[0][2],list_of_books_for_return[0][4])
    else:
        radiobutton_color_if_due_date_is_only_coming(list_of_books_for_return[0][5],list_of_books_for_return[0][1],list_of_books_for_return[0][2],list_of_books_for_return[0][4])

    if obtaining_month_day_year_of_return(dict_of_books_for_return[2][4]):
        radiobutton_color_if_due_date_is_past(list_of_books_for_return[1][5],list_of_books_for_return[1][1],list_of_books_for_return[1][2],list_of_books_for_return[1][4])
    else:
        radiobutton_color_if_due_date_is_only_coming(list_of_books_for_return[1][5],list_of_books_for_return[1][1],list_of_books_for_return[1][2],list_of_books_for_return[1][4],)

def three_books_to_return():
    global book_name_select_for_return_var
    global main_frame5
    innerframe5=LabelFrame(return_books_student_page_root,text='books',bd=15,width=1000)
    innerframe5.place(x=300,y=300)

    #Creating Main fram:
    main_frame5=Frame(innerframe5,width=1000)
    main_frame5.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_return_var=IntVar()
    if obtaining_month_day_year_of_return(dict_of_books_for_return[1][4]):
        radiobutton_color_if_due_date_is_past(list_of_books_for_return[0][5],list_of_books_for_return[0][1],list_of_books_for_return[0][2],list_of_books_for_return[0][4])
    else:
        radiobutton_color_if_due_date_is_only_coming(list_of_books_for_return[0][5],list_of_books_for_return[0][1],list_of_books_for_return[0][2],list_of_books_for_return[0][4])

    if obtaining_month_day_year_of_return(dict_of_books_for_return[2][4]):
        radiobutton_color_if_due_date_is_past(list_of_books_for_return[1][5],list_of_books_for_return[1][1],list_of_books_for_return[1][2],list_of_books_for_return[1][4])
    else:
        radiobutton_color_if_due_date_is_only_coming(list_of_books_for_return[1][5],list_of_books_for_return[1][1],list_of_books_for_return[1][2],list_of_books_for_return[1][4],)
    
    if obtaining_month_day_year_of_return(dict_of_books_for_return[3][4]):
        radiobutton_color_if_due_date_is_past(list_of_books_for_return[2][5],list_of_books_for_return[2][1],list_of_books_for_return[2][2],list_of_books_for_return[2][4])
    else:
        radiobutton_color_if_due_date_is_only_coming(list_of_books_for_return[2][5],list_of_books_for_return[2][1],list_of_books_for_return[2][2],list_of_books_for_return[2][4])
    
    

def radiobutton_color_if_due_date_is_only_coming(ival,bookname,bookauthor,duedate):
    global book_name_select_for_return_var
    Radiobutton(main_frame5,text=bookname+'        (   by  '+bookauthor+' )\n(   Due On '+duedate+'   )',font=("lucida handwriting", 30),indicator=0,variable=book_name_select_for_return_var,value=ival,width=50,bg='cyan',fg='black',padx=10,anchor='w').pack()
def radiobutton_color_if_due_date_is_past(ival,bookname,bookauthor,duedate):
    global book_name_select_for_return_var
    Radiobutton(main_frame5,text=bookname+'        (   by  '+bookauthor+' )\n(   Book Due    )',font=("lucida handwriting", 30),indicator=0,variable=book_name_select_for_return_var,value=ival,width=50,bg='red',fg='black',padx=10,anchor='w').pack()


def clicking_proceed_in_return_fn():
    global book_name_select_for_return_var
    global main_list_regarding_book_and_author_info_for_return
    global dict_of_books_for_return

    try:
        book_name_select_for_return=book_name_select_for_return_var.get()
    except:
        book_name_select_for_return='chumma'
    main_list_regarding_book_and_author_info_for_return=[]
    if book_name_select_for_return==0:
        messagebox.showerror('return book','please select a book')
        ref=1
    elif book_name_select_for_return=='chumma' or book_name_select_for_return_var=='chumma':
        messagebox.showinfo('oops','You have not borrwed any book')
        librarymang_home_page_student_from_return_of_book()
        ref=1
    else:
        main_list_regarding_book_and_author_info_for_return=dict_of_books_for_return[book_name_select_for_return][0:5]   #just so that the 4th column is taken
        book_return_verification_tkinter_page()



def book_return_verification_tkinter_page():
    global main_list_regarding_book_and_author_info_for_return
    global book_return_verification_tkinter_page_root

    return_books_student_page_root.destroy()

    book_return_verification_tkinter_page_root=Tk()
    book_return_verification_tkinter_page_root.title('Return Books')
    book_return_verification_tkinter_page_root.state("zoomed")

    book_return_verification_tkinter_page_root.config(background = "black", pady=10)

    obtaining_book_info_for_return(main_list_regarding_book_and_author_info_for_return)

    Label(book_return_verification_tkinter_page_root,text="Book Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=700,y=20)
    Label(book_return_verification_tkinter_page_root,text="Book Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(book_return_verification_tkinter_page_root,text="Book Author:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(book_return_verification_tkinter_page_root,text="Number Of Pages:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=250)
    Label(book_return_verification_tkinter_page_root,text="Book Cover:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=250)
    Label(book_return_verification_tkinter_page_root,text="Book Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=400)
    Label(book_return_verification_tkinter_page_root,text="Author Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=400)
    Label(book_return_verification_tkinter_page_root,text="Issue Date:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=680)
    Label(book_return_verification_tkinter_page_root,text="Return Date:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=680)

    Label(book_return_verification_tkinter_page_root,text=main_book_id_for_showing_in_book_return,font=("verdana", 20),width=20,anchor='w').place(x=890,y=20)
    Label(book_return_verification_tkinter_page_root,text=main_bookname_for_showing_in_book_return,font=("verdana", 20),width=30,anchor='w').place(x=350,y=150)
    Label(book_return_verification_tkinter_page_root,text=main_bookauthor_for_showing_in_book_return,font=("verdana", 20),width=30,anchor='w').place(x=1275,y=150)
    Label(book_return_verification_tkinter_page_root,text=str(main_number_of_pages_for_showing_in_book_return),font=("verdana", 20),width=20,anchor='w').place(x=460,y=250)
    Label(book_return_verification_tkinter_page_root,text=main_book_cover_for_showing_in_book_return,font=("verdana", 20),width=20,anchor='w').place(x=1245,y=250)
    Label(book_return_verification_tkinter_page_root,text=main_issue_date_for_showing_in_book_return,font=("verdana", 20),width=20,anchor='w').place(x=340,y=680)
    Label(book_return_verification_tkinter_page_root,text=main_return_date_for_showing_in_book_return,font=("verdana", 20),width=20,anchor='w').place(x=1270,y=680)

    first_scroll_for_return=scrolledtext.ScrolledText(book_return_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    second_scroll_for_return=scrolledtext.ScrolledText(book_return_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    first_scroll_for_return.insert(END,main_bookinfo_for_showing_in_book_return)
    second_scroll_for_return.insert(END,main_author_info_for_showing_in_book_return)
    first_scroll_for_return.place(x=330,y=400)
    second_scroll_for_return.place(x=1270,y=400)

    Button(book_return_verification_tkinter_page_root,text='Cancel',font=('verdana',25),cursor='hand2',command=librarymang_home_page_student_after_return_of_book).place(x=1000,y=800)
    Button(book_return_verification_tkinter_page_root,text='Return Book',font=('verdana',25),cursor='hand2',bg='red',command=returning_book_fn).place(x=700,y=800)
    photo = PhotoImage(file = "e.png")
    book_return_verification_tkinter_page_root.iconphoto(False, photo)


def obtaining_book_info_for_return(list_to_regard):
    global main_book_id_for_showing_in_book_return
    global main_bookname_for_showing_in_book_return
    global main_bookauthor_for_showing_in_book_return
    global main_bookinfo_for_showing_in_book_return
    global main_number_of_pages_for_showing_in_book_return
    global main_book_cover_for_showing_in_book_return
    global main_author_info_for_showing_in_book_return
    global main_issue_date_for_showing_in_book_return
    global main_return_date_for_showing_in_book_return

    query_for_book_last_return='''select * from bookdata where book_id='{0}';'''
    cursor_mysql.execute(query_for_book_last_return.format(list_to_regard[0]))
    new_list3=cursor_mysql.fetchall()


    main_book_id_for_showing_in_book_return=new_list3[0][0]
    main_bookname_for_showing_in_book_return=new_list3[0][1]
    main_bookauthor_for_showing_in_book_return=new_list3[0][2]
    main_number_of_pages_for_showing_in_book_return=new_list3[0][3]
    main_book_cover_for_showing_in_book_return=new_list3[0][6]
    main_bookinfo_for_showing_in_book_return=new_list3[0][4]
    if new_list3[0][5]==None:
        main_author_info_for_showing_in_book_return='No Information Available'
    else:
        main_author_info_for_showing_in_book_return=new_list3[0][5]

    query_for_books_return_2="select * from bookissue where book_id2='{0}';"
    cursor_mysql.execute(query_for_books_return_2.format(main_book_id_for_showing_in_book_return))
    newlist4=cursor_mysql.fetchall()
    list_local_issuedate=(str(newlist4[0][2])).split('-')
    list_local_returndate=(str(newlist4[0][3])).split('-')
    yearissue=list_local_issuedate[0]
    monthissue=list_local_issuedate[1]
    dayissue=list_local_issuedate[2]
    yearreturn=list_local_returndate[0]
    monthreturn=list_local_returndate[1]
    dayreturn=list_local_returndate[2]
    main_issue_date_for_showing_in_book_return=dayissue+'-'+monthissue+'-'+yearissue
    main_return_date_for_showing_in_book_return=dayreturn+'-'+monthreturn+'-'+yearreturn


def returning_book_fn():
    query1="select * from bookissue where book_id2='{0}';"
    cursor_mysql.execute(query1.format(main_book_id_for_showing_in_book_return))
    out1=cursor_mysql.fetchall()
    bookid=main_book_id_for_showing_in_book_return
    query2="select * from loginissue where username='{0}';"
    cursor_mysql.execute(query2.format(user_username))
    out2=cursor_mysql.fetchall()
    user=out2[0][0]
    i1=out2[0][1]
    i2=out2[0][2]
    i3=out2[0][3]
    ref=0
    if (i1==bookid) and i2==None and i3==None:
        query="update loginissue set book_id1=Null where username='{0}';"
        query0="update bookissue set username=Null,date_of_issue=Null,date_of_return=Null where book_id2='{0}';"
        cursor_mysql.execute(query.format(user_username))
        mycon.commit()
        a=1
        cursor_mysql.execute(query0.format(main_book_id_for_showing_in_book_return))
        mycon.commit()
        ref=1

    elif (i1==bookid) and i3==None and i2!=None:
        query="update loginissue set book_id1='{0}',book_id2=Null where username='{1}';"
        query0="update bookissue set username=Null,date_of_issue=Null,date_of_return=Null where book_id2='{0}';"
        cursor_mysql.execute(query.format(i2,user_username))
        mycon.commit()
        a=1
        cursor_mysql.execute(query0.format(main_book_id_for_showing_in_book_return))
        mycon.commit()
        ref=1

    elif (i1==bookid) and i2!=None and i3!=None:
        query="update loginissue set book_id1='{0}',book_id2='{1}',book_id3=Null where username='{2}';"
        query0="update bookissue set username=Null,date_of_issue=Null,date_of_return=Null where book_id2='{0}';"
        cursor_mysql.execute(query.format(i2,i3,user_username))
        mycon.commit()
        a=1
        cursor_mysql.execute(query0.format(main_book_id_for_showing_in_book_return))
        mycon.commit()
        ref=1

    elif (i2==bookid) and i3==None and i1!=None:
        query="update loginissue set book_id2=Null where username='{0}';"
        query0="update bookissue set username=Null,date_of_issue=Null,date_of_return=Null where book_id2='{0}';"
        cursor_mysql.execute(query.format(user_username))
        mycon.commit()
        a=1
        cursor_mysql.execute(query0.format(main_book_id_for_showing_in_book_return))
        mycon.commit()
        ref=1
    elif (i2==bookid) and i3!=None and i1!=None:
        query="update loginissue set book_id2='{0}',book_id3=Null where username='{1}';"
        query0="update bookissue set username=Null,date_of_issue=Null,date_of_return=Null where book_id2='{0}';"
        cursor_mysql.execute(query.format(i3,user_username))
        mycon.commit()
        a=1
        cursor_mysql.execute(query0.format(main_book_id_for_showing_in_book_return))
        mycon.commit()
        ref=1
    elif (i3==bookid) and i1!=None and i2!=None:
        query="update loginissue set book_id3=Null where username='{0}';"
        query0="update bookissue set username=Null,date_of_issue=Null,date_of_return=Null where book_id2='{0}';"
        cursor_mysql.execute(query.format(user_username))
        mycon.commit()
        a=1
        cursor_mysql.execute(query0.format(main_book_id_for_showing_in_book_return))
        mycon.commit()
        ref=1

    if ref==1:
        messagebox.showinfo('success','You have returned The book : '+main_bookname_for_showing_in_book_return)
        librarymang_home_page_student_after_return_of_book()
    else:
        messagebox.showinfo('oops','Something Went Wrong')
        librarymang_home_page_student_after_return_of_book()


#***********************************************************************************************************************************************************************************

def searcher_bar_mid_fn():
    global search_bar_borrow_books_student_page_var
    global search_bar_borrow_books_student_page
    global dict_of_non_issued_books
    global count_of_books_for_non_issued
    search_bar_borrow_books_student_page_1=search_bar_borrow_books_student_page_var.get()
    search_bar_borrow_books_student_page=search_bar_borrow_books_student_page_1.lower()
    if count_of_books_for_non_issued==0:
        if_no_books_to_borrow()
    elif count_of_books_for_non_issued<=12:
        if_there_is_no_scroll_from_mifn()
    else:
        if_there_is_scroll_in_issue_from_mifn()


def if_there_is_scroll_in_issue_from_mifn():
    global count_of_books_for_non_issued
    global dict_of_non_issued_books
    global list_of_non_issued_books
    global search_bar_borrow_books_student_page
    global variable_list_order_2
    variable_list_order_2=[]

    #search bar

    if search_bar_borrow_books_student_page=='':
        searaching_and_reodering_radiobutton_of_issue_page_for_scroll(list_of_non_issued_books)
    else:
        pass
        for sample in list_of_non_issued_books:
            if (sample[0].lower()==search_bar_borrow_books_student_page) and (sample[1].lower()==search_bar_borrow_books_student_page) and (sample[2].lower()==search_bar_borrow_books_student_page) and ((sample[1].lower()).startswith(search_bar_borrow_books_student_page)) and ((sample[2].lower()).startswith(search_bar_borrow_books_student_page)) and ((sample[1].lower()).endswith(search_bar_borrow_books_student_page)) and ((sample[2].lower()).endswith(search_bar_borrow_books_student_page)) and (search_bar_borrow_books_student_page in sample[1].lower()) and (search_bar_borrow_books_student_page in sample[2].lower()):
                variable_list_order_2.append(sample)
            else:
                continue
        for sample2 in list_of_non_issued_books:
            if (sample2 not in variable_list_order_2) and (sample2[0].lower()==search_bar_borrow_books_student_page):
                variable_list_order_2.append(sample2)
            else:
                continue
        for sample3 in list_of_non_issued_books:
            if (sample3 not in variable_list_order_2) and (sample3[1].lower()==search_bar_borrow_books_student_page):
                variable_list_order_2.append(sample3)
            else:
                continue
        for sample4 in list_of_non_issued_books:
            if (sample4 not in variable_list_order_2) and (sample4[2].lower()==search_bar_borrow_books_student_page):
                variable_list_order_2.append(sample4)
            else:
                continue
        for sample5 in list_of_non_issued_books:
            if (sample5 not in variable_list_order_2) and ((sample5[1].lower()).startswith(search_bar_borrow_books_student_page)):
                variable_list_order_2.append(sample5)
            else:
                continue
        for sample6 in list_of_non_issued_books:
            if (sample6 not in variable_list_order_2) and ((sample6[2].lower()).startswith(search_bar_borrow_books_student_page)):
                variable_list_order_2.append(sample6)
            else:
                continue
        for sample7 in list_of_non_issued_books:
            if (sample7 not in variable_list_order_2) and ((sample7[1].lower()).endswith(search_bar_borrow_books_student_page)):
                variable_list_order_2.append(sample7)
            else:
                continue
        for sample8 in list_of_non_issued_books:
            if (sample8 not in variable_list_order_2) and ((sample8[2].lower()).endswith(search_bar_borrow_books_student_page)):
                variable_list_order_2.append(sample8)
            else:
                continue
        for sample9 in list_of_non_issued_books:
            if (sample9 not in variable_list_order_2) and (search_bar_borrow_books_student_page in sample9[1].lower()):
                variable_list_order_2.append(sample9)
            else:
                continue
        for sample10 in list_of_non_issued_books:
            if (sample10 not in variable_list_order_2) and (search_bar_borrow_books_student_page in sample10[2].lower()):
                variable_list_order_2.append(sample10)
            else:
                continue 
        for sample11 in list_of_non_issued_books:
            if sample11 not in variable_list_order_2:
                variable_list_order_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_issue_page_for_scroll(variable_list_order_2)



def searaching_and_reodering_radiobutton_of_issue_page_for_scroll(list_ordered):
    global book_name_select_for_issue_var
    global count_of_books_for_non_issued
    global dict_of_non_issued_books
    global list_of_non_issued_books
    global search_bar_borrow_books_student_page
    global variable_list_order_2

    innerframe=LabelFrame(borrow_books_student_page_root,text='books',bd=15,width=1000)
    innerframe.place(x=600,y=300)

    #Creating Main fram:
    main_frame=Frame(innerframe,width=1000)
    main_frame.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva=Canvas(main_frame,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll=ttk.Scrollbar(main_frame,orient=VERTICAL,command=canva.yview) 
    scroll.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva.configure(yscrollcommand=scroll.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva.bind('<Configure>', lambda e: canva.configure(scrollregion=canva.bbox("all")))
    #Creating another frame inside canvas
    second_frame=Frame(canva,width=1000)
    #placing the second frame inside canva
    canva.create_window((0,0),window=second_frame,anchor='nw',)#nw means on the top right corner


    book_name_select_for_issue_var=IntVar()

    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(second_frame,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_issue_var,value=i[3],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_issue_var,value=i[3],width=50,bg='cyan',padx=10,anchor='w').pack()




def if_there_is_no_scroll_from_mifn():
    global count_of_books_for_non_issued
    global dict_of_non_issued_books
    global list_of_non_issued_books
    global search_bar_borrow_books_student_page
    global variable_list_order
    global variable_list_order_2
    variable_list_order=[]
    variable_list_order_2=[]


    #search Bar operation

    if search_bar_borrow_books_student_page=='':
        searaching_and_reodering_radiobutton_of_issue_page_for_no_scroll(list_of_non_issued_books)
    else:        
        for sample in list_of_non_issued_books:
            if (sample[0].lower()==search_bar_borrow_books_student_page) and (sample[1].lower()==search_bar_borrow_books_student_page) and (sample[2].lower()==search_bar_borrow_books_student_page) and ((sample[1].lower()).startswith(search_bar_borrow_books_student_page)) and ((sample[2].lower()).startswith(search_bar_borrow_books_student_page)) and ((sample[1].lower()).endswith(search_bar_borrow_books_student_page)) and ((sample[2].lower()).endswith(search_bar_borrow_books_student_page)) and (search_bar_borrow_books_student_page in sample[1].lower()) and (search_bar_borrow_books_student_page in sample[2].lower()):
                variable_list_order_2.append(sample)
            else:
                continue
        for sample2 in list_of_non_issued_books:
            if (sample2 not in variable_list_order_2) and (sample2[0].lower()==search_bar_borrow_books_student_page):
                variable_list_order_2.append(sample2)
            else:
                continue
        for sample3 in list_of_non_issued_books:
            if (sample3 not in variable_list_order_2) and (sample3[1].lower()==search_bar_borrow_books_student_page):
                variable_list_order_2.append(sample3)
            else:
                continue
        for sample4 in list_of_non_issued_books:
            if (sample4 not in variable_list_order_2) and (sample4[2].lower()==search_bar_borrow_books_student_page):
                variable_list_order_2.append(sample4)
            else:
                continue
        for sample5 in list_of_non_issued_books:
            if (sample5 not in variable_list_order_2) and ((sample5[1].lower()).startswith(search_bar_borrow_books_student_page)):
                variable_list_order_2.append(sample5)
            else:
                continue
        for sample6 in list_of_non_issued_books:
            if (sample6 not in variable_list_order_2) and ((sample6[2].lower()).startswith(search_bar_borrow_books_student_page)):
                variable_list_order_2.append(sample6)
            else:
                continue
        for sample7 in list_of_non_issued_books:
            if (sample7 not in variable_list_order_2) and ((sample7[1].lower()).endswith(search_bar_borrow_books_student_page)):
                variable_list_order_2.append(sample7)
            else:
                continue
        for sample8 in list_of_non_issued_books:
            if (sample8 not in variable_list_order_2) and ((sample8[2].lower()).endswith(search_bar_borrow_books_student_page)):
                variable_list_order_2.append(sample8)
            else:
                continue
        for sample9 in list_of_non_issued_books:
            if (sample9 not in variable_list_order_2) and (search_bar_borrow_books_student_page in sample9[1].lower()):
                variable_list_order_2.append(sample9)
            else:
                continue
        for sample10 in list_of_non_issued_books:
            if (sample10 not in variable_list_order_2) and (search_bar_borrow_books_student_page in sample10[2].lower()):
                variable_list_order_2.append(sample10)
            else:
                continue
        for sample11 in list_of_non_issued_books:
            if sample11 not in variable_list_order_2:
                variable_list_order_2.append(sample11)
            else:
                pass
        searaching_and_reodering_radiobutton_of_issue_page_for_no_scroll(variable_list_order_2)




def searaching_and_reodering_radiobutton_of_issue_page_for_no_scroll(list_ordered):
    global book_name_select_for_issue_var
    global count_of_books_for_non_issued
    global dict_of_non_issued_books
    global list_of_non_issued_books
    global search_bar_borrow_books_student_page
    global variable_list_order
    variable_list_order=[]
    innerframe=LabelFrame(borrow_books_student_page_root,text='books',bd=15,width=1000)
    innerframe.place(x=600,y=300)

    #Creating Main fram:
    main_frame=Frame(innerframe,width=1000)
    main_frame.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_issue_var=IntVar()
    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(main_frame,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_issue_var,value=i[3],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_issue_var,value=i[3],width=50,bg='cyan',padx=10,anchor='w').pack()



def if_there_is_scroll_in_issue():
    global borrow_books_student_page_root
    global dict_of_non_issued_books
    innerframe=LabelFrame(borrow_books_student_page_root,text='books',bd=15,width=1000)
    innerframe.place(x=600,y=300)

    #Creating Main fram:
    main_frame=Frame(innerframe,width=1000)
    main_frame.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva=Canvas(main_frame,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll=ttk.Scrollbar(main_frame,orient=VERTICAL,command=canva.yview) 
    scroll.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva.configure(yscrollcommand=scroll.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva.bind('<Configure>', lambda e: canva.configure(scrollregion=canva.bbox("all")))
    #Creating another frame inside canvas
    second_frame=Frame(canva,width=1000)
    #placing the second frame inside canva
    canva.create_window((0,0),window=second_frame,anchor='nw',)#nw means on the top right corner
    global book_name_select_for_issue_var
    book_name_select_for_issue_var=IntVar()
    for i in range(1,count_of_books_for_non_issued+1):
        if i%2==0:
            Radiobutton(second_frame,text=dict_of_non_issued_books[i][1]+'        (   by  '+dict_of_non_issued_books[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_issue_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame,text=dict_of_non_issued_books[i][1]+'        (   by  '+dict_of_non_issued_books[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_issue_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()


def if_there_is_no_scroll():
    global dict_of_non_issued_books
    global count_of_books_for_non_issued

    innerframe=LabelFrame(borrow_books_student_page_root,text='books',bd=15,width=1000,)
    innerframe.place(x=600,y=300)

    #Creating Main fram:
    main_frame=Frame(innerframe,width=1000)
    main_frame.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    global book_name_select_for_issue_var
    book_name_select_for_issue_var=IntVar()
    for i in range(1,count_of_books_for_non_issued+1):
        if i%2==0:
            Radiobutton(main_frame,text=dict_of_non_issued_books[i][1]+'        (   by  '+dict_of_non_issued_books[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_issue_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame,text=dict_of_non_issued_books[i][1]+'        (   by  '+dict_of_non_issued_books[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_issue_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()

def if_no_books_to_borrow():
    global book_name_select_for_issue
    global book_name_select_for_issue_var
    book_name_select_for_issue_var=book_name_select_for_issue='chumma'
    Label(borrow_books_student_page_root,text="There are no books available right now",font=("lucida handwriting", 30),bg='black',fg='white').place(x=500,y=500)



def creating_dict_table_for_issue():

    global count_of_books_for_non_issued
    global dict_of_non_issued_books
    global list_of_non_issued_books
    list_of_non_issued_books=[]
    dict_of_non_issued_books={}

    query1="select book_id2 from bookissue;"
    cursor_mysql.execute(query1)
    out3_1=cursor_mysql.fetchall()
    query2="select book_id,bookname,bookauthor from bookdata;"
    cursor_mysql.execute(query2)
    out3_2=cursor_mysql.fetchall()
    if out3_1==[]:
        for tups3_1 in out3_2:
            list_of_non_issued_books.append([tups3_1[0],tups3_1[1],tups3_1[2]])
        count_of_books_for_non_issued=len(list_of_non_issued_books)
        if count_of_books_for_non_issued==0:
            dict_of_non_issued_books={}
            list_of_non_issued_books=[]
        else:
            for i in range(1,count_of_books_for_non_issued+1):
                dict_of_non_issued_books[i]=list_of_non_issued_books[i-1]
                list_of_non_issued_books[i-1].append(i)
    else:
        query="select book_id2,username from bookissue;"
        cursor_mysql.execute(query)
        out3=cursor_mysql.fetchall()
        query122="select book_id,bookname,bookauthor from bookdata;"
        cursor_mysql.execute(query122)
        out322=cursor_mysql.fetchall()
        dict1={}
        dict2={}
        for p in out322:
            dict1[p[0]]=[p[1],p[2]]
        for t in out3:
            dict2[t[0]]=[t[1],]
        for q in dict1:
            if dict2[q][0]==None:
                list_of_non_issued_books.append([q,dict1[q][0],dict1[q][1]])
            else:
                continue
        count_of_books_for_non_issued=len(list_of_non_issued_books)
        if count_of_books_for_non_issued==0:
            dict_of_non_issued_books={}
            list_of_non_issued_books=[]
        else:
            for i in range(1,count_of_books_for_non_issued+1):
                dict_of_non_issued_books[i]=list_of_non_issued_books[i-1]
                list_of_non_issued_books[i-1].append(i)



def clicking_proceed_in_borrow_fn():
    global book_name_select_for_issue_var
    global main_list_regarding_book_and_author_info
    global dict_of_non_issued_books

    try:
        book_name_select_for_issue=book_name_select_for_issue_var.get()
    except:
        book_name_select_for_issue='chumma'
    main_list_regarding_book_and_author_info=[]
    if book_name_select_for_issue==0:
        messagebox.showerror('issue book','please select a book to borrow')
    elif book_name_select_for_issue=='chumma' or book_name_select_for_issue_var=='chumma':
        messagebox.showinfo('oops','There are no books availiable right now')
        librarymang_home_page_student_from_the_borrow_book_page()
    else:
        main_list_regarding_book_and_author_info=dict_of_non_issued_books[book_name_select_for_issue][0:3]   #just so that the 4th column is taken
        book_issue_verification_tkinter_page()






def return_date_findding_fn(daystoadd):
    today_date=date.today()
    ret_date=today_date+timedelta(days=daystoadd)
    return str(ret_date)




def check_for_issue_period_and_mid_fn():
    global period_of_issue_var
    global period_of_issue_list
    global period_of_issue
    query="select * from loginissue;"
    cursor_mysql.execute(query)
    out=cursor_mysql.fetchall()
    for tups_dup in out:
        if tups_dup[0]==user_username:
            issue1=tups_dup[1]
            issue2=tups_dup[2]
            issue3=tups_dup[3]
        else:
            continue
    period_of_issue=period_of_issue_var.get()
    ref=0
    if issue3!=None:
        messagebox.showerror('issue books','You Have Already Issued 3 Books Please Return Them to Borrow More')
        ref=1
    elif period_of_issue not in period_of_issue_list:
        messagebox.showerror('issue books','please enter period of issue')
        ref=2
    else:
        if period_of_issue=='3 days':
            date_of_return=return_date_findding_fn(3)
        elif period_of_issue=='7 days':
            date_of_return=return_date_findding_fn(7)
        elif period_of_issue=='14 days':
            date_of_return=return_date_findding_fn(14)
        elif period_of_issue=='28 days':
            date_of_return=return_date_findding_fn(28)
        else:
            date_of_return=return_date_findding_fn(56)

    if ref==1:
        force_exit_from_borrow_due_to_more_than_3_issue_to_librarymang_home_page_student()
        
    elif ref==2:
        pass

    else:
        issuing_books_fn(issue1,issue2,issue3,date_of_return)
        messagebox.showinfo('success','Book has been Succesfully Issued')
        librarymang_home_page_student_after_issue_of_book()

def issuing_books_fn(i1,i2,i3,dateret):
    global user_username
    global main_book_id_for_showing_in_book_issue
    dateissue=str(date.today())
    datereturn=dateret
    bookId=main_book_id_for_showing_in_book_issue
    if i1==None:
        query1='''update bookissue set username="{0}",date_of_issue="{1}",date_of_return="{2}" where book_id2="{3}";'''
        cursor_mysql.execute(query1.format(user_username,dateissue,datereturn,bookId))
        mycon.commit()
        username=user_username
        query2='''update loginissue set book_id1="{0}" where username="{1}";'''
        cursor_mysql.execute(query2.format(bookId,username))
        mycon.commit()
    elif i2==None:
        query1='''update bookissue set username="{0}",date_of_issue="{1}",date_of_return="{2}" where book_id2="{3}";'''
        cursor_mysql.execute(query1.format(user_username,dateissue,datereturn,bookId))
        mycon.commit()
        username=user_username
        query2='''update loginissue set book_id2="{0}" where username="{1}";'''
        cursor_mysql.execute(query2.format(bookId,username))
        mycon.commit()
    elif i3==None:
        query1='''update bookissue set username="{0}",date_of_issue="{1}",date_of_return="{2}" where book_id2="{3}";'''
        cursor_mysql.execute(query1.format(user_username,dateissue,datereturn,bookId))
        mycon.commit()
        username=user_username
        query2='''update loginissue set book_id3="{0}" where username="{1}";'''
        cursor_mysql.execute(query2.format(bookId,username))
        mycon.commit()
    else:
        messagebox.showerror('issue books','You Have Already Issued 3 Books Please Return Them to Borrow More')
        force_exit_from_borrow_due_to_more_than_3_issue_to_librarymang_home_page_student()


def obtaining_book_info(list_to_regard):
    global main_book_id_for_showing_in_book_issue
    global main_bookname_for_showing_in_book_issue
    global main_bookauthor_for_showing_in_book_issue
    global main_number_of_pages_for_showing_in_book_issue
    global main_book_cover_for_showing_in_book_issue
    global main_bookinfo_for_showing_in_book_issue
    global main_author_info_for_showing_in_book_issue

    query_for_book_last_issue='''select * from bookdata where book_id='{0}';'''
    cursor_mysql.execute(query_for_book_last_issue.format(list_to_regard[0]))
    new_list=cursor_mysql.fetchall()

    main_book_id_for_showing_in_book_issue=new_list[0][0]
    main_bookname_for_showing_in_book_issue=new_list[0][1]
    main_bookauthor_for_showing_in_book_issue=new_list[0][2]
    main_number_of_pages_for_showing_in_book_issue=new_list[0][3]
    main_book_cover_for_showing_in_book_issue=new_list[0][6]
    main_bookinfo_for_showing_in_book_issue=new_list[0][4]
    if new_list[0][5]==None:
        main_author_info_for_showing_in_book_issue='No Information Available'
    else:
        main_author_info_for_showing_in_book_issue=new_list[0][5]






def book_issue_verification_tkinter_page():
    global main_list_regarding_book_and_author_info
    global book_issue_verification_tkinter_page_root
    global period_of_issue_list
    global period_of_issue_var

    borrow_books_student_page_root.destroy()

    book_issue_verification_tkinter_page_root=Tk()
    book_issue_verification_tkinter_page_root.title('Borrow Books')
    book_issue_verification_tkinter_page_root.state("zoomed")

    book_issue_verification_tkinter_page_root.config(background = "black", pady=10)

    obtaining_book_info(main_list_regarding_book_and_author_info)

    Label(book_issue_verification_tkinter_page_root,text="Book Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=700,y=20)
    Label(book_issue_verification_tkinter_page_root,text="Book Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(book_issue_verification_tkinter_page_root,text="Book Author:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(book_issue_verification_tkinter_page_root,text="Number Of Pages:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=250)
    Label(book_issue_verification_tkinter_page_root,text="Book Cover:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=250)
    Label(book_issue_verification_tkinter_page_root,text="Book Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=400)
    Label(book_issue_verification_tkinter_page_root,text="Author Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=400)

    Label(book_issue_verification_tkinter_page_root,text=main_book_id_for_showing_in_book_issue,font=("verdana", 20),width=20,anchor='w').place(x=890,y=20)
    Label(book_issue_verification_tkinter_page_root,text=main_bookname_for_showing_in_book_issue,font=("verdana", 20),width=30,anchor='w').place(x=350,y=150)
    Label(book_issue_verification_tkinter_page_root,text=main_bookauthor_for_showing_in_book_issue,font=("verdana", 20),width=30,anchor='w').place(x=1275,y=150)
    Label(book_issue_verification_tkinter_page_root,text=main_number_of_pages_for_showing_in_book_issue,font=("verdana", 20),width=20,anchor='w').place(x=460,y=250)
    Label(book_issue_verification_tkinter_page_root,text=main_book_cover_for_showing_in_book_issue,font=("verdana", 20),width=20,anchor='w').place(x=1245,y=250)

    first_scroll=scrolledtext.ScrolledText(book_issue_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    second_scroll=scrolledtext.ScrolledText(book_issue_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    first_scroll.insert(END,main_bookinfo_for_showing_in_book_issue)
    second_scroll.insert(END,main_author_info_for_showing_in_book_issue)
    first_scroll.place(x=330,y=400)
    second_scroll.place(x=1270,y=400)
    global period_of_issue_list
    period_of_issue_list=['3 days','7 days','14 days','28 days','56 days']
    period_of_issue_var=StringVar()
    droplist_for_period_issue=OptionMenu(book_issue_verification_tkinter_page_root, period_of_issue_var, *period_of_issue_list)
    droplist_for_period_issue.config(width=30,font=("verdana", 10))
    period_of_issue_var.set('Select Period Of Issue')
    droplist_for_period_issue.place(x=800,y=700)

    Button(book_issue_verification_tkinter_page_root,text='Cancel',font=('verdana',25),cursor='hand2',command=librarymang_home_page_student_from_book_issue_verification_tkinter_page).place(x=1000,y=800)
    Button(book_issue_verification_tkinter_page_root,text='Issue Book',font=('verdana',25),cursor='hand2',bg='blue',command=check_for_issue_period_and_mid_fn).place(x=700,y=800)
    photo = PhotoImage(file = "e.png")
    book_issue_verification_tkinter_page_root.iconphoto(False, photo)


def borrow_books_student_page_fn():
    librarymang_home_page_student_root.destroy()
    global borrow_books_student_page_root
    global search_bar_borrow_books_student_page_var
    global search_bar_borrow_books_student_page
    global dict_of_non_issued_books
    global count_of_books_for_non_issued
    global search_bar_borrow_books_student_page_var

    borrow_books_student_page_root=Tk()
    borrow_books_student_page_root.title('Borrow books')
    borrow_books_student_page_root.state('zoomed')

    search_bar_borrow_books_student_page_var=StringVar()

    borrow_books_student_page_root.config(background = "black", pady=10)
    Label(borrow_books_student_page_root, text="Select Books to borrow",width=100, font=("freestyle script", 70)).pack()
    try:
        Entry(borrow_books_student_page_root, font=('verdana',30),textvariable=search_bar_borrow_books_student_page_var,width=50).place(x=250,y=200)
    except:
        messagebox.showinfo('error',"Dont type \" or  in any of the fields")
    Button(borrow_books_student_page_root,text='Search',cursor='hand2',font=('verdana',30),bg='grey',command=searcher_bar_mid_fn).place(x=1600,y=180)
    Button(borrow_books_student_page_root,text='Go Back',cursor='hand2',font=('verdana',30),command=librarymang_home_page_student_from_the_borrow_book_page).place(x=1050,y=900)
    Button(borrow_books_student_page_root,text='Proceed',cursor='hand2',font=('verdana',30),command=clicking_proceed_in_borrow_fn).place(x=750,y=900)
    photo = PhotoImage(file = "e.png")
    borrow_books_student_page_root.iconphoto(False, photo)


    #checking for issued books

    creating_dict_table_for_issue()


    if count_of_books_for_non_issued==0:
        if_no_books_to_borrow()
    elif count_of_books_for_non_issued<=12:
        if_there_is_no_scroll()
    else:
        if_there_is_scroll_in_issue()






#***********************************************************************************************************************************************************************************









def verification_for_add_books():
    global book_info_add_books_admin_page_text_var
    global author_info_add_books_admin_page_text_var
    global book_name_for_add_books_admin_page_var
    global author_name_for_add_books_admin_page_var
    global number_of_pages_add_books_admin_page_var
    global book_cover_type_for_add_books_admin_page_var
    global add_books_admin_page_root

    global book_name_for_add_books_admin_page
    global author_name_for_add_books_admin_page
    global number_of_pages_add_books_admin_page
    global book_cover_type_for_add_books_admin_page
    global book_info_add_books_admin_page_text
    global author_info_add_books_admin_page_text
    global bookid_for_add_books_admin_page

    book_name_for_add_books_admin_page=book_name_for_add_books_admin_page_var.get()
    author_name_for_add_books_admin_page=author_name_for_add_books_admin_page_var.get()
    number_of_pages_add_books_admin_page=number_of_pages_add_books_admin_page_var.get()
    book_cover_type_for_add_books_admin_page=book_cover_type_for_add_books_admin_page_var.get()
    book_info_add_books_admin_page_text=book_info_add_books_admin_page_text_var.get(1.0,'end-1c')
    author_info_add_books_admin_page_text=author_info_add_books_admin_page_text_var.get(1.0,'end-1c')
    
    query_for_bookid_for_add_books_admin_page='select book_id from bookdata;'
    cursor_mysql.execute(query_for_bookid_for_add_books_admin_page)
    output_for_add_books_admin_page=cursor_mysql.fetchall()
    newl=[]
    for tups in output_for_add_books_admin_page:
        newl.append(tups[0])

    while True:
        alphabet_part_of_bookid_for_add_books_admin_page=''
        alphas='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(4):
            alphabet_part_of_bookid_for_add_books_admin_page+=alphas[(random.randint(0,51))]
        numberpart_part_of_bookid_for_add_books_admin_page=random.randint(10000000,99999999)
        bookid_for_add_books_admin_page=alphabet_part_of_bookid_for_add_books_admin_page+str(numberpart_part_of_bookid_for_add_books_admin_page)
        if bookid_for_add_books_admin_page in newl:
            continue
        else:
            break

    ref_for_add_books_admin_page=0
    if book_name_for_add_books_admin_page=='':
        messagebox.showerror('error','please enter book name')
        ref_for_add_books_admin_page=1
    elif len(book_name_for_add_books_admin_page)>50:
        messagebox.showerror('error','Book name should be less than 51 characters')
        ref_for_add_books_admin_page=1
    else:
        pass
    if ref_for_add_books_admin_page==0 and author_name_for_add_books_admin_page=='':
        messagebox.showerror('error','please enter Authors name')
        ref_for_add_books_admin_page=2
    elif ref_for_add_books_admin_page==0 and len(author_name_for_add_books_admin_page)>50:
        messagebox.showerror('error','Author name cannot be more than 51 characters')
        ref_for_add_books_admin_page=2
    else:
        pass
    if ref_for_add_books_admin_page==0 and number_of_pages_add_books_admin_page=='':
        messagebox.showerror('error','please enter the number of pages')
        ref_for_add_books_admin_page=3
    elif ref_for_add_books_admin_page==0 and (not number_of_pages_add_books_admin_page.isdigit()):
        messagebox.showerror('error','number of pages must only contain numbers')
        ref_for_add_books_admin_page=3
    else:
        pass
    if ref_for_add_books_admin_page==0 and book_cover_type_for_add_books_admin_page==0:
        messagebox.showerror('error','please enter the book cover type')
        ref_for_add_books_admin_page=4
    else:
        pass
    if ref_for_add_books_admin_page==0 and book_info_add_books_admin_page_text=='':
        messagebox.showerror('error','please enter the book description')
        ref_for_add_books_admin_page=5
    elif ref_for_add_books_admin_page==0 and len(book_info_add_books_admin_page_text)>6000:
        messagebox.showerror('error','book info must be less than 6001 characters')
        ref_for_add_books_admin_page=5
    else:
        pass
    if ref_for_add_books_admin_page==0 and len(author_info_add_books_admin_page_text)>6000:
        messagebox.showerror('error','author info must be less than 6001 characters')
        ref_for_add_books_admin_page=6
    else:
        pass
    if ref_for_add_books_admin_page==0 and (('\'' in book_name_for_add_books_admin_page) or ('\"' in book_name_for_add_books_admin_page) or ('\'' in author_name_for_add_books_admin_page) or ('\"' in author_name_for_add_books_admin_page) or ('\'' in book_info_add_books_admin_page_text) or ('\"' in book_info_add_books_admin_page_text) or ('\'' in author_info_add_books_admin_page_text) or ('\"' in author_info_add_books_admin_page_text)):
        messagebox.showinfo('error','Dnot use \' or \" in any field')
        ref_for_add_books_admin_page=7
    if ref_for_add_books_admin_page==0:
        mid_for_add_fns()
    else:
        pass

def add_books_fn(local_book_id,local_book_name,local_book_author,local_book_number_pages,local_bookinfo,local_book_cover,local_authorinfo=0):

    
    if local_authorinfo==0:
        query='''insert into bookdata(book_id,bookname,bookauthor,number_of_pages,bookinfo,bookcover) values("{0}","{1}","{2}",{3},"{4}","{5}");'''
        cursor_mysql.execute(query.format(local_book_id,local_book_name,local_book_author,local_book_number_pages,local_bookinfo,local_book_cover))
        mycon.commit()
        bookid=local_book_id
        query_2="insert into bookissue(book_id2) values('{0}');"
        cursor_mysql.execute(query_2.format(bookid))
        mycon.commit()
        aftereadding()

    
    else:
        query='''insert into bookdata(book_id,bookname,bookauthor,number_of_pages,bookinfo,authorinfo,bookcover) values("{0}","{1}","{2}",{3},"{4}","{5}","{6}");'''
        cursor_mysql.execute(query.format(local_book_id,local_book_name,local_book_author,local_book_number_pages,local_bookinfo,local_authorinfo,local_book_cover))
        mycon.commit()
        bookid=local_book_id
        query_2="insert into bookissue(book_id2) values('{0}');"
        cursor_mysql.execute(query_2.format(bookid))
        mycon.commit()
        aftereadding()

def aftereadding():
    messagebox.showinfo('success','Book successfully added')
    librarymang_home_page_admin_after_adding()



def mid_for_add_fns():
    global book_name_for_add_books_admin_page
    global author_name_for_add_books_admin_page
    global number_of_pages_add_books_admin_page
    global book_cover_type_for_add_books_admin_page
    global book_info_add_books_admin_page_text
    global author_info_add_books_admin_page_text
    global real_book_cover_type_for_add_books_admin_page
    global real_number_of_pages_add_books_admin_page
    global bookid_for_add_books_admin_page

    if book_cover_type_for_add_books_admin_page==1:
        real_book_cover_type_for_add_books_admin_page='paperback'
    else:
        real_book_cover_type_for_add_books_admin_page='hardcover'

    real_number_of_pages_add_books_admin_page=int(number_of_pages_add_books_admin_page)

    if author_info_add_books_admin_page_text=='':
        add_books_fn(bookid_for_add_books_admin_page,book_name_for_add_books_admin_page,author_name_for_add_books_admin_page,real_number_of_pages_add_books_admin_page,book_info_add_books_admin_page_text,real_book_cover_type_for_add_books_admin_page)
    else:
        add_books_fn(bookid_for_add_books_admin_page,book_name_for_add_books_admin_page,author_name_for_add_books_admin_page,real_number_of_pages_add_books_admin_page,book_info_add_books_admin_page_text,real_book_cover_type_for_add_books_admin_page,author_info_add_books_admin_page_text)





def add_books_admin_page():
    librarymang_home_page_admin_root.destroy()
    global book_info_add_books_admin_page_text_var
    global author_info_add_books_admin_page_text_var
    global book_name_for_add_books_admin_page_var
    global author_name_for_add_books_admin_page_var
    global number_of_pages_add_books_admin_page_var
    global book_cover_type_for_add_books_admin_page_var
    global add_books_admin_page_root

    add_books_admin_page_root=Tk()
    add_books_admin_page_root.title('Add Book')
    add_books_admin_page_root.state('zoomed')
    add_books_admin_page_root.config(bg='black',pady=10)


    Label(add_books_admin_page_root, text="Add Books",width=100, font=("freestyle script", 70)).pack()
    Label(add_books_admin_page_root,text='Book name : ',font=("lucida handwriting", 30),bg='black',fg='white').place(x=50,y=200)
    Label(add_books_admin_page_root,text='Book Author : ',font=("lucida handwriting", 30),bg='black',fg='white').place(x=50,y=350)
    Label(add_books_admin_page_root,text='Author info : ',font=("lucida handwriting", 30),bg='black',fg='white').place(x=900,y=550)
    Label(add_books_admin_page_root,text='*optional',font=("lucida handwriting", 12),bg='black',fg='red').place(x=900,y=600)
    Label(add_books_admin_page_root,text='Book info   :',font=("lucida handwriting", 30),bg='black',fg='white').place(x=900,y=200)
    Label(add_books_admin_page_root,text='Number of pages :',font=("lucida handwriting", 30),bg='black',fg='white').place(x=50,y=550)
    Label(add_books_admin_page_root,text='Book Cover : ',font=("lucida handwriting", 30),bg='black',fg='white').place(x=50,y=750)
    
    book_info_add_books_admin_page_text_var=scrolledtext.ScrolledText(add_books_admin_page_root,wrap=WORD,bg='white',width=30,height=7,font=('verdana',20))
    author_info_add_books_admin_page_text_var=scrolledtext.ScrolledText(add_books_admin_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))

    book_name_for_add_books_admin_page_var=StringVar()
    author_name_for_add_books_admin_page_var=StringVar()
    number_of_pages_add_books_admin_page_var=StringVar()
    book_cover_type_for_add_books_admin_page_var=StringVar()
    
    Entry(add_books_admin_page_root,font=('verdana',20),textvariable=book_name_for_add_books_admin_page_var).place(x=370,y=210)
    Entry(add_books_admin_page_root,font=('verdana',20),textvariable=author_name_for_add_books_admin_page_var).place(x=400,y=360)
    Entry(add_books_admin_page_root,font=('verdana',20),width=5,textvariable=number_of_pages_add_books_admin_page_var).place(x=485,y=560)
    book_info_add_books_admin_page_text_var.place(x=1230,y=200)
    author_info_add_books_admin_page_text_var.place(x=1230,y=550)

    book_cover_type_for_add_books_admin_page_var=IntVar()
    Radiobutton(add_books_admin_page_root,text="Paperback",padx= 10,variable= book_cover_type_for_add_books_admin_page_var, value=1,font=('verdana',17)).place(x=370,y=760)
    Radiobutton(add_books_admin_page_root,text="Hardcover",padx= 10, variable= book_cover_type_for_add_books_admin_page_var, value=2,font=('verdana',17)).place(x=530,y=760)

    Button(add_books_admin_page_root,text='Add Book',font=('verdana',25),command=verification_for_add_books,cursor='hand2').place(x=800,y=800)
    Button(add_books_admin_page_root,text='Go Back',font=('verdana',25),command=librarymang_home_page_admin_after_adding,cursor='hand2').place(x=810,y=900)
    photo = PhotoImage(file = "e.png")
    add_books_admin_page_root.iconphoto(False, photo)






#***********************************************************************************************************************************************************************************






def searcher_bar_mid_fn_for_delete():
    global search_bar_delete_books_student_page_var
    global search_bar_delete_books_student_page
    global dict_of_books_for_delete
    global count_of_books_for_delete
    search_bar_delete_books_student_page_2=search_bar_delete_books_student_page_var.get()
    search_bar_delete_books_student_page=search_bar_delete_books_student_page_2.lower()
    if count_of_books_for_delete==0:
        no_books_to_delete()
    elif count_of_books_for_delete<=12:
        no_scroll_for_delete_mid_fn()
    else:
        if_is_scroll_for_delete_for_mid_fn()





def if_is_scroll_for_delete_for_mid_fn():
    global count_of_books_for_delete
    global dict_of_books_for_delete
    global list_of_books_for_delete
    global search_bar_delete_books_student_page
    global variable_list_order_for_delete_2
    variable_list_order_for_delete_2=[]

    #search bar

    if search_bar_delete_books_student_page=='':
        searaching_and_reodering_radiobutton_of_delete_page_for_scroll(list_of_books_for_delete)
    else:
        pass
        for sample in list_of_books_for_delete:
            if (sample[0].lower()==search_bar_delete_books_student_page) and (sample[1].lower()==search_bar_delete_books_student_page) and (sample[2].lower()==search_bar_delete_books_student_page) and ((sample[1].lower()).startswith(search_bar_delete_books_student_page)) and ((sample[2].lower()).startswith(search_bar_delete_books_student_page)) and ((sample[1].lower()).endswith(search_bar_delete_books_student_page)) and ((sample[2].lower()).endswith(search_bar_delete_books_student_page)) and (search_bar_delete_books_student_page in sample[1].lower()) and (search_bar_delete_books_student_page in sample[2].lower()):
                variable_list_order_for_delete_2.append(sample)
            else:
                continue
        for sample2 in list_of_books_for_delete:
            if (sample2 not in variable_list_order_for_delete_2) and (sample2[0].lower()==search_bar_delete_books_student_page):
                variable_list_order_for_delete_2.append(sample2)
            else:
                continue
        for sample3 in list_of_books_for_delete:
            if (sample3 not in variable_list_order_for_delete_2) and (sample3[1].lower()==search_bar_delete_books_student_page):
                variable_list_order_for_delete_2.append(sample3)
            else:
                continue
        for sample4 in list_of_books_for_delete:
            if (sample4 not in variable_list_order_for_delete_2) and (sample4[2].lower()==search_bar_delete_books_student_page):
                variable_list_order_for_delete_2.append(sample4)
            else:
                continue
        for sample5 in list_of_books_for_delete:
            if (sample5 not in variable_list_order_for_delete_2) and ((sample5[1].lower()).startswith(search_bar_delete_books_student_page)):
                variable_list_order_for_delete_2.append(sample5)
            else:
                continue
        for sample6 in list_of_books_for_delete:
            if (sample6 not in variable_list_order_for_delete_2) and ((sample6[2].lower()).startswith(search_bar_delete_books_student_page)):
                variable_list_order_for_delete_2.append(sample6)
            else:
                continue
        for sample7 in list_of_books_for_delete:
            if (sample7 not in variable_list_order_for_delete_2) and ((sample7[1].lower()).endswith(search_bar_delete_books_student_page)):
                variable_list_order_for_delete_2.append(sample7)
            else:
                continue
        for sample8 in list_of_books_for_delete:
            if (sample8 not in variable_list_order_for_delete_2) and ((sample8[2].lower()).endswith(search_bar_delete_books_student_page)):
                variable_list_order_for_delete_2.append(sample8)
            else:
                continue
        for sample9 in list_of_books_for_delete:
            if (sample9 not in variable_list_order_for_delete_2) and (search_bar_delete_books_student_page in sample9[1].lower()):
                variable_list_order_for_delete_2.append(sample9)
            else:
                continue
        for sample10 in list_of_books_for_delete:
            if (sample10 not in variable_list_order_for_delete_2) and (search_bar_delete_books_student_page in sample10[2].lower()):
                variable_list_order_for_delete_2.append(sample10)
            else:
                continue
        for sample11 in list_of_books_for_delete:
            if sample11 not in variable_list_order_for_delete_2:
                variable_list_order_for_delete_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_delete_page_for_scroll(variable_list_order_for_delete_2)





def searaching_and_reodering_radiobutton_of_delete_page_for_scroll(list_ordered):
    global book_name_select_for_delete_var
    global count_of_books_for_delete
    global dict_of_books_for_delete
    global list_of_books_for_delete
    global search_bar_delete_books_student_page
    global variable_list_order_for_delete_2
    variable_list_order_for_delete_2=[]



    innerframe2=LabelFrame(delete_books_admin_page_root,text='books',bd=15,width=1000)
    innerframe2.place(x=600,y=300)

    #Creating Main fram:
    main_frame2=Frame(innerframe2,width=1000)
    main_frame2.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva2=Canvas(main_frame2,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva2.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll2=ttk.Scrollbar(main_frame2,orient=VERTICAL,command=canva2.yview) 
    scroll2.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva2.configure(yscrollcommand=scroll2.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva2.bind('<Configure>', lambda e: canva2.configure(scrollregion=canva2.bbox("all")))
    #Creating another frame inside canvas
    second_frame2=Frame(canva2,width=1000)
    #placing the second frame inside canva
    canva2.create_window((0,0),window=second_frame2,anchor='nw',)#nw means on the top right corner


    book_name_select_for_delete_var=IntVar()

    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(second_frame2,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_delete_var,value=i[3],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame2,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_delete_var,value=i[3],width=50,bg='cyan',padx=10,anchor='w').pack()














def no_scroll_for_delete_mid_fn():
    global count_of_books_for_delete
    global dict_of_books_for_delete
    global list_of_books_for_delete
    global search_bar_delete_books_student_page
    global variable_list_order_for_delete_2
    variable_list_order_for_delete_2=[]


    #search Bar operation

    if search_bar_delete_books_student_page=='':
        searaching_and_reodering_radiobutton_of_delete_page_for_no_scroll(list_of_books_for_delete)
    else:
        pass
        for sample in list_of_books_for_delete:
            if (sample[0].lower()==search_bar_delete_books_student_page) and (sample[1].lower()==search_bar_delete_books_student_page) and (sample[2].lower()==search_bar_delete_books_student_page) and ((sample[1].lower()).startswith(search_bar_delete_books_student_page)) and ((sample[2].lower()).startswith(search_bar_delete_books_student_page)) and ((sample[1].lower()).endswith(search_bar_delete_books_student_page)) and ((sample[2].lower()).endswith(search_bar_delete_books_student_page)) and (search_bar_delete_books_student_page in sample[1].lower()) and (search_bar_delete_books_student_page in sample[2].lower()):
                variable_list_order_for_delete_2.append(sample)
            else:
                continue
        for sample2 in list_of_books_for_delete:
            if (sample2 not in variable_list_order_for_delete_2) and (sample2[0].lower()==search_bar_delete_books_student_page):
                variable_list_order_for_delete_2.append(sample2)
            else:
                continue
        for sample3 in list_of_books_for_delete:
            if (sample3 not in variable_list_order_for_delete_2) and (sample3[1].lower()==search_bar_delete_books_student_page):
                variable_list_order_for_delete_2.append(sample3)
            else:
                continue
        for sample4 in list_of_books_for_delete:
            if (sample4 not in variable_list_order_for_delete_2) and (sample4[2].lower()==search_bar_delete_books_student_page):
                variable_list_order_for_delete_2.append(sample4)
            else:
                continue
        for sample5 in list_of_books_for_delete:
            if (sample5 not in variable_list_order_for_delete_2) and ((sample5[1].lower()).startswith(search_bar_delete_books_student_page)):
                variable_list_order_for_delete_2.append(sample5)
            else:
                continue
        for sample6 in list_of_books_for_delete:
            if (sample6 not in variable_list_order_for_delete_2) and ((sample6[2].lower()).startswith(search_bar_delete_books_student_page)):
                variable_list_order_for_delete_2.append(sample6)
            else:
                continue
        for sample7 in list_of_books_for_delete:
            if (sample7 not in variable_list_order_for_delete_2) and ((sample7[1].lower()).endswith(search_bar_delete_books_student_page)):
                variable_list_order_for_delete_2.append(sample7)
            else:
                continue
        for sample8 in list_of_books_for_delete:
            if (sample8 not in variable_list_order_for_delete_2) and ((sample8[2].lower()).endswith(search_bar_delete_books_student_page)):
                variable_list_order_for_delete_2.append(sample8)
            else:
                continue
        for sample9 in list_of_books_for_delete:
            if (sample9 not in variable_list_order_for_delete_2) and (search_bar_delete_books_student_page in sample9[1].lower()):
                variable_list_order_for_delete_2.append(sample9)
            else:
                continue
        for sample10 in list_of_books_for_delete:
            if (sample10 not in variable_list_order_for_delete_2) and (search_bar_delete_books_student_page in sample10[2].lower()):
                variable_list_order_for_delete_2.append(sample10)
            else:
                continue
        for sample11 in list_of_books_for_delete:
            if sample11 not in variable_list_order_for_delete_2:
                variable_list_order_for_delete_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_delete_page_for_no_scroll(variable_list_order_for_delete_2)


def searaching_and_reodering_radiobutton_of_delete_page_for_no_scroll(list_ordered):
    global book_name_select_for_delete_var
    global count_of_books_for_delete
    global dict_of_books_for_delete
    global list_of_books_for_delete
    global search_bar_delete_books_student_page
    global variable_list_order_for_delete_2
    variable_list_order_for_delete_2=[]
    innerframe2=LabelFrame(delete_books_admin_page_root,text='books',bd=15,width=1000)
    innerframe2.place(x=600,y=300)

    #Creating Main fram:
    main_frame2=Frame(innerframe2,width=1000)
    main_frame2.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_delete_var=IntVar()
    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(main_frame2,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_delete_var,value=i[3],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame2,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_delete_var,value=i[3],width=50,bg='cyan',padx=10,anchor='w').pack()








def if_is_scroll_for_delete_fn():

    global delete_books_admin_page_root
    global dict_of_books_for_delete
    innerframe2=LabelFrame(delete_books_admin_page_root,text='books',bd=15,width=1000)
    innerframe2.place(x=600,y=300)

    #Creating Main fram:
    main_frame2=Frame(innerframe2,width=1000)
    main_frame2.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva2=Canvas(main_frame2,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva2.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll2=ttk.Scrollbar(main_frame2,orient=VERTICAL,command=canva2.yview) 
    scroll2.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva2.configure(yscrollcommand=scroll2.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva2.bind('<Configure>', lambda e: canva2.configure(scrollregion=canva2.bbox("all")))
    #Creating another frame inside canvas
    second_frame2=Frame(canva2,width=1000)
    #placing the second frame inside canva
    canva2.create_window((0,0),window=second_frame2,anchor='nw',)#nw means on the top right corner
    global book_name_select_for_delete_var
    book_name_select_for_delete_var=IntVar()
    for i in range(1,count_of_books_for_delete+1):
        if i%2==0:
            Radiobutton(second_frame2,text=dict_of_books_for_delete[i][1]+'        (   by  '+dict_of_books_for_delete[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_delete_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame2,text=dict_of_books_for_delete[i][1]+'        (   by  '+dict_of_books_for_delete[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_delete_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()








def no_scroll_for_delete_fn():
    global dict_of_books_for_delete
    global count_of_books_for_delete

    innerframe2=LabelFrame(delete_books_admin_page_root,text='books',bd=15,width=1000,)
    innerframe2.place(x=600,y=300)

    #Creating Main fram:
    main_frame2=Frame(innerframe2,width=1000)
    main_frame2.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    global book_name_select_for_delete_var
    book_name_select_for_delete_var=IntVar()
    for i in range(1,count_of_books_for_delete+1):
        if i%2==0:
            Radiobutton(main_frame2,text=dict_of_books_for_delete[i][1]+'        (   by  '+dict_of_books_for_delete[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_delete_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame2,text=dict_of_books_for_delete[i][1]+'        (   by  '+dict_of_books_for_delete[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_delete_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()


def no_books_to_delete():
    global book_name_select_for_delete_var
    global book_name_select_for_delete_var

    book_name_select_for_delete=book_name_select_for_delete_var='chumma'
    Label(delete_books_admin_page_root,text="There are no books available right now",font=("lucida handwriting", 30),bg='black',fg='white').place(x=500,y=500)




def creating_dict_table_for_delete():
    global count_of_books_for_delete
    global list_of_books_for_delete  
    global dict_of_books_for_delete

    list_of_books_for_delete=[]
    dict_of_books_for_delete={}

    query1="select book_id,bookname,bookauthor from bookdata;"
    cursor_mysql.execute(query1)
    output=cursor_mysql.fetchall()

    if output==[]:
        list_of_books_for_delete=[]
        dict_of_books_for_delete={}
        count_of_books_for_delete=0
    else:
        for i in range(len(output)):
            dict_of_books_for_delete[i+1]=[output[i][0],output[i][1],output[i][2]]
            list_of_books_for_delete.append([output[i][0],output[i][1],output[i][2],(i+1)])
            count_of_books_for_delete=len(list_of_books_for_delete)



def clicking_proceed_in_delete_fn():
    global book_name_select_for_delete_var
    global main_list_regarding_book_and_author_info_for_delete
    global dict_of_books_for_delete

    try:
        book_name_select_for_delete=book_name_select_for_delete_var.get()
    except:
        book_name_select_for_delete='chumma'
    main_list_regarding_book_and_author_info_for_delete=[]
    if book_name_select_for_delete==0:
        messagebox.showerror('delete book','please select a book to delete')
    elif book_name_select_for_delete=='chumma' or book_name_select_for_delete_var=='chumma':
        messagebox.showinfo('oops','there are no books to delete right now')
        librarymang_home_page_admin_from_book_selecting_from_delete_page()
    else:
        main_list_regarding_book_and_author_info_for_delete=dict_of_books_for_delete[book_name_select_for_delete][0:3]   #just so that the 4th column is taken
        book_delete_verification_tkinter_page()






def checking_if_selected_book_is_issued_or_not_delete():
    global main_book_id_for_showing_in_book_delete
    
    query="select book_id2,username from bookissue where book_id2='{0}';"
    cursor_mysql.execute(query.format(main_book_id_for_showing_in_book_delete))
    out=cursor_mysql.fetchall()
    book_id_local=out[0][0]
    book_username_local=out[0][1]

    if book_username_local==None:
        delete_books_fn(main_book_id_for_showing_in_book_delete)
        messagebox.showinfo('success','Book has been successfully Deleted')
        librarymang_home_page_admin_from_deleting_confirmation_page()



    else:
        messagebox.showinfo('unsuccessful','Cannot Delete Books which have been issued')
        librarymang_home_page_admin_from_deleting_confirmation_page()




def delete_books_fn(book_to_delete):
    query1="delete from bookdata where book_id='{0}';"
    query2="delete from bookissue where book_id2='{0}';"
    cursor_mysql.execute(query1.format(book_to_delete))
    mycon.commit()
    bookidtodel=book_to_delete
    cursor_mysql.execute(query2.format(bookidtodel))
    mycon.commit()





def obtaining_book_info_for_delete(list_to_regard):
    global main_book_id_for_showing_in_book_delete
    global main_bookname_for_showing_in_book_delete
    global main_bookauthor_for_showing_in_book_delete
    global main_number_of_pages_for_showing_in_book_delete
    global main_book_cover_for_showing_in_book_delete
    global main_bookinfo_for_showing_in_book_delete
    global main_author_info_for_showing_in_book_delete

    query_for_book_last_delete='''select * from bookdata where book_id='{0}';'''
    cursor_mysql.execute(query_for_book_last_delete.format(list_to_regard[0]))
    new_list2=cursor_mysql.fetchall()

    main_book_id_for_showing_in_book_delete=new_list2[0][0]
    main_bookname_for_showing_in_book_delete=new_list2[0][1]
    main_bookauthor_for_showing_in_book_delete=new_list2[0][2]
    main_number_of_pages_for_showing_in_book_delete=new_list2[0][3]
    main_book_cover_for_showing_in_book_delete=new_list2[0][6]
    main_bookinfo_for_showing_in_book_delete=new_list2[0][4]
    if new_list2[0][5]==None:
        main_author_info_for_showing_in_book_delete='No Information Available'
    else:
        main_author_info_for_showing_in_book_delete=new_list2[0][5]















def book_delete_verification_tkinter_page():
    global main_list_regarding_book_and_author_info_for_delete
    global book_delete_verification_tkinter_page_root

    delete_books_admin_page_root.destroy()

    book_delete_verification_tkinter_page_root=Tk()
    book_delete_verification_tkinter_page_root.title('Delete Books')
    book_delete_verification_tkinter_page_root.state("zoomed")

    book_delete_verification_tkinter_page_root.config(background = "black", pady=10)

    obtaining_book_info_for_delete(main_list_regarding_book_and_author_info_for_delete)

    Label(book_delete_verification_tkinter_page_root,text="Book Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=700,y=20)
    Label(book_delete_verification_tkinter_page_root,text="Book Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(book_delete_verification_tkinter_page_root,text="Book Author:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(book_delete_verification_tkinter_page_root,text="Number Of Pages:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=250)
    Label(book_delete_verification_tkinter_page_root,text="Book Cover:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=250)
    Label(book_delete_verification_tkinter_page_root,text="Book Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=400)
    Label(book_delete_verification_tkinter_page_root,text="Author Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=400)

    Label(book_delete_verification_tkinter_page_root,text=main_book_id_for_showing_in_book_delete,font=("verdana", 20),width=20,anchor='w').place(x=890,y=20)
    Label(book_delete_verification_tkinter_page_root,text=main_bookname_for_showing_in_book_delete,font=("verdana", 20),width=30,anchor='w').place(x=350,y=150)
    Label(book_delete_verification_tkinter_page_root,text=main_bookauthor_for_showing_in_book_delete,font=("verdana", 20),width=30,anchor='w').place(x=1275,y=150)
    Label(book_delete_verification_tkinter_page_root,text=main_number_of_pages_for_showing_in_book_delete,font=("verdana", 20),width=20,anchor='w').place(x=460,y=250)
    Label(book_delete_verification_tkinter_page_root,text=main_book_cover_for_showing_in_book_delete,font=("verdana", 20),width=20,anchor='w').place(x=1245,y=250)

    first_scroll_for_delete=scrolledtext.ScrolledText(book_delete_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    second_scroll_for_delete=scrolledtext.ScrolledText(book_delete_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    first_scroll_for_delete.insert(END,main_bookinfo_for_showing_in_book_delete)
    second_scroll_for_delete.insert(END,main_author_info_for_showing_in_book_delete)
    first_scroll_for_delete.place(x=330,y=400)
    second_scroll_for_delete.place(x=1270,y=400)

    Button(book_delete_verification_tkinter_page_root,text='Cancel',font=('verdana',25),cursor='hand2',command=librarymang_home_page_admin_from_deleting_confirmation_page).place(x=1000,y=800)
    Button(book_delete_verification_tkinter_page_root,text='Delete Book',font=('verdana',25),cursor='hand2',bg='red',command=checking_if_selected_book_is_issued_or_not_delete).place(x=700,y=800)
    photo = PhotoImage(file = "e.png")
    book_delete_verification_tkinter_page_root.iconphoto(False, photo)





def delete_books_admin_page():

    global delete_books_admin_page_root
    global count_of_books_for_delete
    global list_of_books_for_delete
    global dict_of_books_for_delete
    global search_bar_delete_books_student_page_var

    librarymang_home_page_admin_root.destroy()

    delete_books_admin_page_root=Tk()
    delete_books_admin_page_root.title("Delete Books")
    delete_books_admin_page_root.state("zoomed")
    delete_books_admin_page_root.config(background = "black", pady=10)
    Label(delete_books_admin_page_root, text="Select Book to Delete",width=100, font=("freestyle script", 70)).pack()
    search_bar_delete_books_student_page_var=StringVar()
    Entry(delete_books_admin_page_root, font=('verdana',30),textvariable=search_bar_delete_books_student_page_var,width=50).place(x=250,y=200)
    Button(delete_books_admin_page_root,text='Search',cursor='hand2',font=('verdana',30),bg='grey',command=searcher_bar_mid_fn_for_delete).place(x=1600,y=180)
    Button(delete_books_admin_page_root,text='Go Back',cursor='hand2',font=('verdana',30),command=librarymang_home_page_admin_from_book_selecting_from_delete_page).place(x=1050,y=900)
    Button(delete_books_admin_page_root,text='Proceed',cursor='hand2',font=('verdana',30),command=clicking_proceed_in_delete_fn).place(x=750,y=900)
    photo = PhotoImage(file = "e.png")
    delete_books_admin_page_root.iconphoto(False, photo)
    

    creating_dict_table_for_delete()    # creating dictionary and list

    if count_of_books_for_delete==0:
        no_books_to_delete()
    elif count_of_books_for_delete<=12:
        no_scroll_for_delete_fn()
    else:
        if_is_scroll_for_delete_fn()




#***********************************************************************************************************************************************************************************



def searcher_bar_mid_fn_for_update():
    global search_bar_update_books_student_page_var
    global search_bar_update_books_student_page
    global dict_of_books_for_update
    global count_of_books_for_update
    search_bar_update_books_student_page_2=search_bar_update_books_student_page_var.get()
    search_bar_update_books_student_page=search_bar_update_books_student_page_2.lower()
    if count_of_books_for_update==0:
        no_books_to_update()
    elif count_of_books_for_update<=12:
        no_scroll_for_update_mid_fn()
    else:
        if_is_scroll_for_update_for_mid_fn()








def if_is_scroll_for_update_for_mid_fn():
    global count_of_books_for_update
    global dict_of_books_for_update
    global list_of_books_for_update
    global search_bar_update_books_student_page
    global variable_list_order_for_update_2
    variable_list_order_for_update_2=[]

    #search bar

    if search_bar_update_books_student_page=='':
        searaching_and_reodering_radiobutton_of_update_page_for_scroll(list_of_books_for_update)
    else:
        pass
        for sample in list_of_books_for_update:
            if (sample[0].lower()==search_bar_update_books_student_page) and (sample[1].lower()==search_bar_update_books_student_page) and (sample[2].lower()==search_bar_update_books_student_page) and ((sample[1].lower()).startswith(search_bar_update_books_student_page)) and ((sample[2].lower()).startswith(search_bar_update_books_student_page)) and ((sample[1].lower()).endswith(search_bar_update_books_student_page)) and ((sample[2].lower()).endswith(search_bar_update_books_student_page)) and (search_bar_update_books_student_page in sample[1].lower()) and (search_bar_update_books_student_page in sample[2].lower()):
                variable_list_order_for_update_2.append(sample)
            else:
                continue
        for sample2 in list_of_books_for_update:
            if (sample2 not in variable_list_order_for_update_2) and (sample2[0].lower()==search_bar_update_books_student_page):
                variable_list_order_for_update_2.append(sample2)
            else:
                continue
        for sample3 in list_of_books_for_update:
            if (sample3 not in variable_list_order_for_update_2) and (sample3[1].lower()==search_bar_update_books_student_page):
                variable_list_order_for_update_2.append(sample3)
            else:
                continue
        for sample4 in list_of_books_for_update:
            if (sample4 not in variable_list_order_for_update_2) and (sample4[2].lower()==search_bar_update_books_student_page):
                variable_list_order_for_update_2.append(sample4)
            else:
                continue
        for sample5 in list_of_books_for_update:
            if (sample5 not in variable_list_order_for_update_2) and ((sample5[1].lower()).startswith(search_bar_update_books_student_page)):
                variable_list_order_for_update_2.append(sample5)
            else:
                continue
        for sample6 in list_of_books_for_update:
            if (sample6 not in variable_list_order_for_update_2) and ((sample6[2].lower()).startswith(search_bar_update_books_student_page)):
                variable_list_order_for_update_2.append(sample6)
            else:
                continue
        for sample7 in list_of_books_for_update:
            if (sample7 not in variable_list_order_for_update_2) and ((sample7[1].lower()).endswith(search_bar_update_books_student_page)):
                variable_list_order_for_update_2.append(sample7)
            else:
                continue
        for sample8 in list_of_books_for_update:
            if (sample8 not in variable_list_order_for_update_2) and ((sample8[2].lower()).endswith(search_bar_update_books_student_page)):
                variable_list_order_for_update_2.append(sample8)
            else:
                continue
        for sample9 in list_of_books_for_update:
            if (sample9 not in variable_list_order_for_update_2) and (search_bar_update_books_student_page in sample9[1].lower()):
                variable_list_order_for_update_2.append(sample9)
            else:
                continue
        for sample10 in list_of_books_for_update:
            if (sample10 not in variable_list_order_for_update_2) and (search_bar_update_books_student_page in sample10[2].lower()):
                variable_list_order_for_update_2.append(sample10)
            else:
                continue
        for sample11 in list_of_books_for_update:
            if sample11 not in variable_list_order_for_update_2:
                variable_list_order_for_update_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_update_page_for_scroll(variable_list_order_for_update_2)







def searaching_and_reodering_radiobutton_of_update_page_for_scroll(list_ordered):
    global book_name_select_for_update_var
    global count_of_books_for_update
    global dict_of_books_for_update
    global list_of_books_for_update
    global search_bar_update_books_student_page
    global variable_list_order_for_update_2
    variable_list_order_for_update_2=[]



    innerframe3=LabelFrame(update_books_admin_page_root,text='books',bd=15,width=1000)
    innerframe3.place(x=600,y=300)

    #Creating Main fram:
    main_frame3=Frame(innerframe3,width=1000)
    main_frame3.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva3=Canvas(main_frame3,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva3.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll3=ttk.Scrollbar(main_frame3,orient=VERTICAL,command=canva3.yview) 
    scroll3.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva3.configure(yscrollcommand=scroll3.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva3.bind('<Configure>', lambda e: canva3.configure(scrollregion=canva3.bbox("all")))
    #Creating another frame inside canvas
    second_frame3=Frame(canva3,width=1000)
    #placing the second frame inside canva
    canva3.create_window((0,0),window=second_frame3,anchor='nw',)#nw means on the top right corner


    book_name_select_for_update_var=IntVar()

    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(second_frame3,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_update_var,value=i[3],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame3,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_update_var,value=i[3],width=50,bg='cyan',padx=10,anchor='w').pack()






def no_scroll_for_update_mid_fn():
    global count_of_books_for_update
    global dict_of_books_for_update
    global list_of_books_for_update
    global search_bar_update_books_student_page
    global variable_list_order_for_update_2
    variable_list_order_for_update_2=[]


    #search Bar operation

    if search_bar_update_books_student_page=='':
        searaching_and_reodering_radiobutton_of_update_page_for_no_scroll(list_of_books_for_update)
    else:
        pass
        for sample in list_of_books_for_update:
            if (sample[0].lower()==search_bar_update_books_student_page) and (sample[1].lower()==search_bar_update_books_student_page) and (sample[2].lower()==search_bar_update_books_student_page) and ((sample[1].lower()).startswith(search_bar_update_books_student_page)) and ((sample[2].lower()).startswith(search_bar_update_books_student_page)) and ((sample[1].lower()).endswith(search_bar_update_books_student_page)) and ((sample[2].lower()).endswith(search_bar_update_books_student_page)) and (search_bar_update_books_student_page in sample[1].lower()) and (search_bar_update_books_student_page in sample[2].lower()):
                variable_list_order_for_update_2.append(sample)
            else:
                continue
        for sample2 in list_of_books_for_update:
            if (sample2 not in variable_list_order_for_update_2) and (sample2[0].lower()==search_bar_update_books_student_page):
                variable_list_order_for_update_2.append(sample2)
            else:
                continue
        for sample3 in list_of_books_for_update:
            if (sample3 not in variable_list_order_for_update_2) and (sample3[1].lower()==search_bar_update_books_student_page):
                variable_list_order_for_update_2.append(sample3)
            else:
                continue
        for sample4 in list_of_books_for_update:
            if (sample4 not in variable_list_order_for_update_2) and (sample4[2].lower()==search_bar_update_books_student_page):
                variable_list_order_for_update_2.append(sample4)
            else:
                continue
        for sample5 in list_of_books_for_update:
            if (sample5 not in variable_list_order_for_update_2) and ((sample5[1].lower()).startswith(search_bar_update_books_student_page)):
                variable_list_order_for_update_2.append(sample5)
            else:
                continue
        for sample6 in list_of_books_for_update:
            if (sample6 not in variable_list_order_for_update_2) and ((sample6[2].lower()).startswith(search_bar_update_books_student_page)):
                variable_list_order_for_update_2.append(sample6)
            else:
                continue
        for sample7 in list_of_books_for_update:
            if (sample7 not in variable_list_order_for_update_2) and ((sample7[1].lower()).endswith(search_bar_update_books_student_page)):
                variable_list_order_for_update_2.append(sample7)
            else:
                continue
        for sample8 in list_of_books_for_update:
            if (sample8 not in variable_list_order_for_update_2) and ((sample8[2].lower()).endswith(search_bar_update_books_student_page)):
                variable_list_order_for_update_2.append(sample8)
            else:
                continue
        for sample9 in list_of_books_for_update:
            if (sample9 not in variable_list_order_for_update_2) and (search_bar_update_books_student_page in sample9[1].lower()):
                variable_list_order_for_update_2.append(sample9)
            else:
                continue
        for sample10 in list_of_books_for_update:
            if (sample10 not in variable_list_order_for_update_2) and (search_bar_update_books_student_page in sample10[2].lower()):
                variable_list_order_for_update_2.append(sample10)
            else:
                continue
        for sample11 in list_of_books_for_update:
            if sample11 not in variable_list_order_for_update_2:
                variable_list_order_for_update_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_update_page_for_no_scroll(variable_list_order_for_update_2)


def searaching_and_reodering_radiobutton_of_update_page_for_no_scroll(list_ordered):
    global book_name_select_for_update_var
    global count_of_books_for_update
    global dict_of_books_for_update
    global list_of_books_for_update
    global search_bar_update_books_student_page
    global variable_list_order_for_update_2
    variable_list_order_for_update_2=[]
    innerframe3=LabelFrame(update_books_admin_page_root,text='books',bd=15,width=1000)
    innerframe3.place(x=600,y=300)

    #Creating Main fram:
    main_frame3=Frame(innerframe3,width=1000)
    main_frame3.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_update_var=IntVar()
    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(main_frame3,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_update_var,value=i[3],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame3,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_update_var,value=i[3],width=50,bg='cyan',padx=10,anchor='w').pack()








def if_is_scroll_for_update_fn():

    global update_books_admin_page_root
    global dict_of_books_for_update
    innerframe3=LabelFrame(update_books_admin_page_root,text='books',bd=15,width=1000)
    innerframe3.place(x=600,y=300)

    #Creating Main fram:
    main_frame3=Frame(innerframe3,width=1000)
    main_frame3.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva3=Canvas(main_frame3,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva3.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll3=ttk.Scrollbar(main_frame3,orient=VERTICAL,command=canva3.yview) 
    scroll3.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva3.configure(yscrollcommand=scroll3.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva3.bind('<Configure>', lambda e: canva3.configure(scrollregion=canva3.bbox("all")))
    #Creating another frame inside canvas
    second_frame3=Frame(canva3,width=1000)
    #placing the second frame inside canva
    canva3.create_window((0,0),window=second_frame3,anchor='nw',)#nw means on the top right corner
    global book_name_select_for_update_var
    book_name_select_for_update_var=IntVar()
    for i in range(1,count_of_books_for_update+1):
        if i%2==0:
            Radiobutton(second_frame3,text=dict_of_books_for_update[i][1]+'        (   by  '+dict_of_books_for_update[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_update_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame3,text=dict_of_books_for_update[i][1]+'        (   by  '+dict_of_books_for_update[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_update_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()









def no_scroll_for_update_fn():
    global dict_of_books_for_update
    global count_of_books_for_update

    innerframe3=LabelFrame(update_books_admin_page_root,text='books',bd=15,width=1000,)
    innerframe3.place(x=600,y=300)

    #Creating Main fram:
    main_frame3=Frame(innerframe3,width=1000)
    main_frame3.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    global book_name_select_for_update_var
    book_name_select_for_update_var=IntVar()
    for i in range(1,count_of_books_for_update+1):
        if i%2==0:
            Radiobutton(main_frame3,text=dict_of_books_for_update[i][1]+'        (   by  '+dict_of_books_for_update[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_update_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame3,text=dict_of_books_for_update[i][1]+'        (   by  '+dict_of_books_for_update[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_update_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()





def no_books_to_update():
    global book_name_select_for_update_var
    global book_name_select_for_update
    book_name_select_for_update=book_name_select_for_update_var='chumma'
    Label(update_books_admin_page_root,text="There are no books available right now",font=("lucida handwriting", 30),bg='black',fg='white').place(x=500,y=500)






def creating_dict_table_for_update():
    global count_of_books_for_update
    global list_of_books_for_update 
    global dict_of_books_for_update

    list_of_books_for_update=[]
    dict_of_books_for_update={}

    query1="select book_id,bookname,bookauthor from bookdata;"
    cursor_mysql.execute(query1)
    output=cursor_mysql.fetchall()

    if output==[]:
        list_of_books_for_update=[]
        dict_of_books_for_update={}
        count_of_books_for_update=0
    else:
        for i in range(len(output)):
            dict_of_books_for_update[i+1]=[output[i][0],output[i][1],output[i][2]]
            list_of_books_for_update.append([output[i][0],output[i][1],output[i][2],(i+1)])
            count_of_books_for_update=len(list_of_books_for_update)





def clicking_proceed_in_update_fn():
    global book_name_select_for_update_var
    global main_list_regarding_book_and_author_info_for_update
    global dict_of_books_for_update

    try:
        book_name_select_for_update=book_name_select_for_update_var.get()
    except:
        book_name_select_for_update='chumma'
    main_list_regarding_book_and_author_info_for_update=[]
    if book_name_select_for_update==0:
        messagebox.showerror('update book','please select a book to update')
    elif book_name_select_for_update=='chumma' or book_name_select_for_update_var=='chumma':
        messagebox.showinfo('oops','there are no books to update right now')
        librarymanag_from_update_search_page()
    else:
        main_list_regarding_book_and_author_info_for_update=dict_of_books_for_update[book_name_select_for_update][0:3]   #just so that the 4th column is taken
        book_update_verification_tkinter_page()






def obtaining_book_info_for_update(list_to_regard):
    global main_book_id_for_showing_in_book_update
    global main_bookname_for_showing_in_book_update
    global main_bookauthor_for_showing_in_book_update
    global main_number_of_pages_for_showing_in_book_update
    global main_book_cover_for_showing_in_book_update
    global main_bookinfo_for_showing_in_book_update
    global main_author_info_for_showing_in_book_update

    query_for_book_last_update='''select * from bookdata where book_id='{0}';'''
    cursor_mysql.execute(query_for_book_last_update.format(list_to_regard[0]))
    new_list3=cursor_mysql.fetchall()

    main_book_id_for_showing_in_book_update=new_list3[0][0]
    main_bookname_for_showing_in_book_update=new_list3[0][1]
    main_bookauthor_for_showing_in_book_update=new_list3[0][2]
    main_number_of_pages_for_showing_in_book_update=new_list3[0][3]
    main_book_cover_for_showing_in_book_update=new_list3[0][6]
    main_bookinfo_for_showing_in_book_update=new_list3[0][4]
    if new_list3[0][5]==None:
        main_author_info_for_showing_in_book_update=''
    else:
        main_author_info_for_showing_in_book_update=new_list3[0][5]






def mid_for_update_fns():
    global main_book_id_for_showing_in_book_update
    global bookname_for_verification_update
    global bookauthor_for_verification_update
    global number_of_pages_for_verification_update
    global book_cover_for_verification_update
    global book_info_for_verification_update
    global authorinfo_for_verification_update
    global real_no_of_pages_for_update

    real_no_of_pages_for_update=int(number_of_pages_for_verification_update)

    
    query="select book_id2,username from bookissue where book_id2='{0}';"
    cursor_mysql.execute(query.format(main_book_id_for_showing_in_book_update))
    out=cursor_mysql.fetchall()
    book_id_local=out[0][0]
    book_username_local=out[0][1]

    if book_username_local==None:

        updating_data_fn()
        messagebox.showinfo('hooray','updation successful')
        librarymanag_from_update_verification()


    else:
        messagebox.showinfo('unsuccessful','Cannot Update Books which have been issued')
        librarymanag_from_update_verification()

def updating_data_fn():
    global main_book_id_for_showing_in_book_update
    global bookname_for_verification_update
    global bookauthor_for_verification_update
    global book_cover_for_verification_update
    global book_info_for_verification_update
    global authorinfo_for_verification_update
    global real_no_of_pages_for_update


    if authorinfo_for_verification_update=='':
        query_of_updation="update bookdata set bookname='{0}',bookauthor='{1}',number_of_pages={2},bookinfo='{3}',authorinfo=Null,bookcover='{4}' where book_id='{5}';"
        cursor_mysql.execute(query_of_updation.format(bookname_for_verification_update,bookauthor_for_verification_update,real_no_of_pages_for_update,book_info_for_verification_update,book_cover_for_verification_update,main_book_id_for_showing_in_book_update))
        mycon.commit()
    else:
        query_of_updation="update bookdata set bookname='{0}',bookauthor='{1}',number_of_pages={2},bookinfo='{3}',authorinfo='{4}',bookcover='{5}' where book_id='{6}';"
        cursor_mysql.execute(query_of_updation.format(bookname_for_verification_update,bookauthor_for_verification_update,real_no_of_pages_for_update,book_info_for_verification_update,authorinfo_for_verification_update,book_cover_for_verification_update,main_book_id_for_showing_in_book_update))
        mycon.commit()





def checking_updation_data():
    global main_list_regarding_book_and_author_info_for_update
    global book_update_verification_tkinter_page_root

    global bookname_for_verification_update_var
    global bookauthor_for_verification_update_var
    global number_of_pages_for_verification_update_var
    global book_cover_for_verification_update_var
    global book_info_for_verification_update_var
    global authorinfo_for_verification_update_var

    global main_book_id_for_showing_in_book_update
    global bookname_for_verification_update
    global bookauthor_for_verification_update
    global number_of_pages_for_verification_update
    global book_cover_for_verification_update
    global book_info_for_verification_update
    global authorinfo_for_verification_update

    bookname_for_verification_update=bookname_for_verification_update_var.get()
    bookauthor_for_verification_update=bookauthor_for_verification_update_var.get()
    number_of_pages_for_verification_update=number_of_pages_for_verification_update_var.get()
    book_cover_for_verification_update=book_cover_for_verification_update_var.get()
    book_info_for_verification_update=book_info_for_verification_update_var.get(1.0,'end-1c')
    authorinfo_for_verification_update=authorinfo_for_verification_update_var.get(1.0,'end-1c')


    ref_for_update_books_admin_page=0
    if bookname_for_verification_update=='':
        messagebox.showerror('error','please enter book name')
        ref_for_update_books_admin_page=1
    elif len(bookname_for_verification_update)>50:
        messagebox.showerror('error','Book name should be less than 51 characters')
        ref_for_update_books_admin_page=1
    else:
        pass
    if ref_for_update_books_admin_page==0 and bookauthor_for_verification_update=='':
        messagebox.showerror('error','please enter Authors name')
        ref_for_update_books_admin_page=2
    elif ref_for_update_books_admin_page==0 and len(bookauthor_for_verification_update)>50:
        messagebox.showerror('error','Author name cannot be more than 51 characters')
        ref_for_update_books_admin_page=2
    else:
        pass
    if ref_for_update_books_admin_page==0 and number_of_pages_for_verification_update=='':
        messagebox.showerror('error','please enter the number of pages')
        ref_for_update_books_admin_page=3
    elif ref_for_update_books_admin_page==0 and (not number_of_pages_for_verification_update.isdigit()):
        messagebox.showerror('error','number of pages must only contain numbers')
        ref_for_update_books_admin_page=3
    else:
        pass
    if ref_for_update_books_admin_page==0 and (book_cover_for_verification_update not in book_cover_for_verification_update_list):
        messagebox.showerror('error','please enter the book cover type')
        ref_for_update_books_admin_page=4
    else:
        pass
    if ref_for_update_books_admin_page==0 and book_info_for_verification_update=='':
        messagebox.showerror('error','please enter the book description')
        ref_for_update_books_admin_page=5
    elif ref_for_update_books_admin_page==0 and len(book_info_for_verification_update)>6000:
        messagebox.showerror('error','book info must be less than 6001 characters')
        ref_for_update_books_admin_page=5
    else:
        pass
    if ref_for_update_books_admin_page==0 and len(authorinfo_for_verification_update)>6000:
        messagebox.showerror('error','author info must be less than 6001 characters')
        ref_for_update_books_admin_page=6
    else:
        pass
    if ref_for_update_books_admin_page==0 and (('\"' in bookname_for_verification_update) or ('\"' in bookauthor_for_verification_update) or ('\"' in book_info_for_verification_update) or ('\"' in authorinfo_for_verification_update) or ('\'' in bookname_for_verification_update) or ('\'' in bookauthor_for_verification_update) or ('\'' in book_info_for_verification_update) or ('\'' in authorinfo_for_verification_update)):
        messagebox.showinfo('error','Dnot use \' or \" in any field')
        ref_for_update_books_admin_page=7
    if ref_for_update_books_admin_page==0:
        mid_for_update_fns()
    else:
        pass




def book_update_verification_tkinter_page():
    global main_list_regarding_book_and_author_info_for_update
    global book_update_verification_tkinter_page_root

    global main_book_id_for_showing_in_book_update
    global bookname_for_verification_update_var
    global bookauthor_for_verification_update_var
    global number_of_pages_for_verification_update_var
    global book_cover_for_verification_update_var
    global book_info_for_verification_update_var
    global authorinfo_for_verification_update_var
    global book_cover_for_verification_update_list

    update_books_admin_page_root.destroy()

    book_update_verification_tkinter_page_root=Tk()
    book_update_verification_tkinter_page_root.title('Delete Books')
    book_update_verification_tkinter_page_root.state("zoomed")

    book_update_verification_tkinter_page_root.config(background = "black", pady=10)

    obtaining_book_info_for_update(main_list_regarding_book_and_author_info_for_update)

    Label(book_update_verification_tkinter_page_root,text="Book Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=700,y=20)
    Label(book_update_verification_tkinter_page_root,text="Book Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(book_update_verification_tkinter_page_root,text="Book Author:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(book_update_verification_tkinter_page_root,text="Number Of Pages:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=250)
    Label(book_update_verification_tkinter_page_root,text="Book Cover:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=250)
    Label(book_update_verification_tkinter_page_root,text="Book Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=400)
    Label(book_update_verification_tkinter_page_root,text="Author Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=400)

    bookname_for_verification_update_var=StringVar()
    bookauthor_for_verification_update_var=StringVar()
    number_of_pages_for_verification_update_var=StringVar()
    book_cover_for_verification_update_var=StringVar()

    bookname_for_verification_update_var.set(main_bookname_for_showing_in_book_update)
    bookauthor_for_verification_update_var.set(main_bookauthor_for_showing_in_book_update)
    number_of_pages_for_verification_update_var.set(main_number_of_pages_for_showing_in_book_update)
    book_cover_for_verification_update_var.set(main_book_cover_for_showing_in_book_update)

    label_for_book_id=Label(book_update_verification_tkinter_page_root,text=main_book_id_for_showing_in_book_update,font=("verdana", 20),width=20)
    entry_for_bookname=Entry(book_update_verification_tkinter_page_root,textvariable=bookname_for_verification_update_var,font=("verdana", 20),width=30)
    entry_for_bookauthor=Entry(book_update_verification_tkinter_page_root,textvariable=bookauthor_for_verification_update_var,font=("verdana", 20),width=30)
    entry_for_number_of_pages=Entry(book_update_verification_tkinter_page_root,textvariable=number_of_pages_for_verification_update_var,font=("verdana", 20),width=20,)


    book_cover_for_verification_update_list=[ 'paperback','hardcover']
    book_cover_for_verification_update_droplist=OptionMenu(book_update_verification_tkinter_page_root, book_cover_for_verification_update_var, *book_cover_for_verification_update_list)
    book_cover_for_verification_update_droplist.config(font=("verdana", 20),width=20)
    book_cover_for_verification_update_droplist.place(x=1250,y=250)

    book_info_for_verification_update_var=scrolledtext.ScrolledText(book_update_verification_tkinter_page_root,wrap=WORD,bg='white',width=30,height=7,font=('verdana',20))
    authorinfo_for_verification_update_var=scrolledtext.ScrolledText(book_update_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))

    book_info_for_verification_update_var.insert(END,main_bookinfo_for_showing_in_book_update)
    authorinfo_for_verification_update_var.insert(END,main_author_info_for_showing_in_book_update)
    
    label_for_book_id.place(x=890,y=20)
    entry_for_bookname.place(x=350,y=150)
    entry_for_bookauthor.place(x=1275,y=150)
    entry_for_number_of_pages.place(x=460,y=250)
    book_info_for_verification_update_var.place(x=330,y=400)
    authorinfo_for_verification_update_var.place(x=1270,y=400)

    Button(book_update_verification_tkinter_page_root,text='Cancel',font=('verdana',25),cursor='hand2',command=librarymanag_from_update_verification).place(x=1000,y=800)
    Button(book_update_verification_tkinter_page_root,text='Update Book',font=('verdana',25),cursor='hand2',bg='green',command=checking_updation_data).place(x=700,y=800)
    photo = PhotoImage(file = "e.png")
    book_update_verification_tkinter_page_root.iconphoto(False, photo)





def update_books_admin_page():

    global update_books_admin_page_root
    global count_of_books_for_update
    global list_of_books_for_update
    global dict_of_books_for_update
    global search_bar_update_books_student_page_var

    librarymang_home_page_admin_root.destroy()

    update_books_admin_page_root=Tk()
    update_books_admin_page_root.title("Update Books")
    update_books_admin_page_root.state("zoomed")
    update_books_admin_page_root.config(background = "black", pady=10)
    Label(update_books_admin_page_root, text="Select Book to Update",width=100, font=("freestyle script", 70)).pack()
    search_bar_update_books_student_page_var=StringVar()
    Entry(update_books_admin_page_root, font=('verdana',30),textvariable=search_bar_update_books_student_page_var,width=50).place(x=250,y=200)
    Button(update_books_admin_page_root,text='Search',cursor='hand2',font=('verdana',30),bg='grey',command=searcher_bar_mid_fn_for_update).place(x=1600,y=180)
    Button(update_books_admin_page_root,text='Go Back',cursor='hand2',font=('verdana',30),command=librarymanag_from_update_search_page).place(x=1050,y=900)
    Button(update_books_admin_page_root,text='Proceed',cursor='hand2',font=('verdana',30),command=clicking_proceed_in_update_fn).place(x=750,y=900)
    photo = PhotoImage(file = "e.png")
    update_books_admin_page_root.iconphoto(False, photo)
    

    creating_dict_table_for_update()    # creating dictionary and list

    if count_of_books_for_update==0:
        no_books_to_update()
    elif count_of_books_for_update<=12:
        no_scroll_for_update_fn()
    else:
        if_is_scroll_for_update_fn()




#***********************************************************************************************************************************************************************************
def view_books_admin_page():

    global view_books_admin_page_root
    global count_of_view_books_admin
    global list_of_view_books_admin
    global dict_of_view_books_admin
    global search_bar_view_books_for_admin_var

    librarymang_home_page_admin_root.destroy()

    view_books_admin_page_root=Tk()
    view_books_admin_page_root.title("View Books")
    view_books_admin_page_root.state("zoomed")
    view_books_admin_page_root.config(background = "black", pady=10)
    Label(view_books_admin_page_root, text="Select Book to View",width=100, font=("freestyle script", 70)).pack()
    search_bar_view_books_for_admin_var=StringVar()
    Entry(view_books_admin_page_root, font=('verdana',30),textvariable=search_bar_view_books_for_admin_var,width=50).place(x=250,y=200)
    Button(view_books_admin_page_root,text='Search',cursor='hand2',font=('verdana',30),bg='grey',command=searcher_bar_mid_fn_for_view_books_admin).place(x=1600,y=180)
    Button(view_books_admin_page_root,text='Go Back',cursor='hand2',font=('verdana',30),command=librarymanag_from_view_books_admin).place(x=1050,y=900)
    Button(view_books_admin_page_root,text='Book info',cursor='hand2',font=('verdana',30),command=clicking_proceed_in_view_books_admin).place(x=700,y=900)
    photo = PhotoImage(file = "e.png")
    view_books_admin_page_root.iconphoto(False, photo)
    

    creating_dict_table_for_view_books_admin()    # creating dictionary and list

    if count_of_view_books_admin==0:
        no_books_to_view_admin()
    elif count_of_view_books_admin<=12:
        no_scroll_for_view_books_admin()
    else:
        if_is_scroll_for_view_books_admin()



def no_books_to_view_admin():
    global book_name_select_for_view_books_admin_var
    global book_name_select_for_view_books_admin
    book_name_select_for_view_books_admin=book_name_select_for_view_books_admin_var='chumma'
    Label(view_books_admin_page_root,text="There are no books available right now",font=("lucida handwriting", 30),bg='black',fg='white').place(x=500,y=500)


def if_is_scroll_for_view_books_admin():

    global view_books_admin_page_root
    global dict_of_view_books_admin
    innerframe7=LabelFrame(view_books_admin_page_root,text='books',bd=15,width=1000)
    innerframe7.place(x=600,y=300)

    #Creating Main fram:
    main_frame7=Frame(innerframe7,width=1000)
    main_frame7.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva7=Canvas(main_frame7,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva7.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll7=ttk.Scrollbar(main_frame7,orient=VERTICAL,command=canva7.yview) 
    scroll7.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva7.configure(yscrollcommand=scroll7.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva7.bind('<Configure>', lambda e: canva7.configure(scrollregion=canva7.bbox("all")))
    #Creating another frame inside canvas
    second_frame7=Frame(canva7,width=1000)
    #placing the second frame inside canva
    canva7.create_window((0,0),window=second_frame7,anchor='nw',)#nw means on the top right corner
    global book_name_select_for_view_books_admin_var
    book_name_select_for_view_books_admin_var=IntVar()
    for i in range(1,count_of_view_books_admin+1):
        if i%2==0:
            Radiobutton(second_frame7,text=dict_of_view_books_admin[i][1]+'        (   by  '+dict_of_view_books_admin[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_view_books_admin_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame7,text=dict_of_view_books_admin[i][1]+'        (   by  '+dict_of_view_books_admin[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_view_books_admin_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()







def no_scroll_for_view_books_admin():
    global dict_of_view_books_admin
    global count_of_view_books_admin

    innerframe7=LabelFrame(view_books_admin_page_root,text='books',bd=15,width=1000,)
    innerframe7.place(x=600,y=300)

    #Creating Main fram:
    main_frame7=Frame(innerframe7,width=1000)
    main_frame7.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    global book_name_select_for_view_books_admin_var
    book_name_select_for_view_books_admin_var=IntVar()
    for i in range(1,count_of_view_books_admin+1):
        if i%2==0:
            Radiobutton(main_frame7,text=dict_of_view_books_admin[i][1]+'        (   by  '+dict_of_view_books_admin[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_view_books_admin_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame7,text=dict_of_view_books_admin[i][1]+'        (   by  '+dict_of_view_books_admin[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_view_books_admin_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()



def searcher_bar_mid_fn_for_view_books_admin():
    global search_bar_view_books_for_admin_var
    global search_bar_view_books_for_admin
    global dict_of_view_books_admin
    global count_of_view_books_admin
    search_bar_view_books_for_admin_2=search_bar_view_books_for_admin_var.get()
    search_bar_view_books_for_admin=search_bar_view_books_for_admin_2.lower()
    if count_of_view_books_admin==0:
        no_books_to_view_admin()
    elif count_of_view_books_admin<=12:
        no_scroll_for_view_books_admin_mid_fn()
    else:
        if_is_scroll_for_view_books_admin_for_mid_fn()



def if_is_scroll_for_view_books_admin_for_mid_fn():
    global count_of_view_books_admin
    global dict_of_view_books_admin
    global list_of_view_books_admin
    global search_bar_view_books_for_admin
    global variable_list_order_for_view_books_admin_2
    variable_list_order_for_view_books_admin_2=[]

    #search bar

    if search_bar_view_books_for_admin=='':
        searaching_and_reodering_radiobutton_of_view_books_admin_page_for_scroll(list_of_view_books_admin)
    else:
        pass
        for sample in list_of_view_books_admin:
            if (sample[0].lower()==search_bar_view_books_for_admin) and (sample[1].lower()==search_bar_view_books_for_admin) and (sample[2].lower()==search_bar_view_books_for_admin) and ((sample[1].lower()).startswith(search_bar_view_books_for_admin)) and ((sample[2].lower()).startswith(search_bar_view_books_for_admin)) and ((sample[1].lower()).endswith(search_bar_view_books_for_admin)) and ((sample[2].lower()).endswith(search_bar_view_books_for_admin)) and (search_bar_view_books_for_admin in sample[1].lower()) and (search_bar_view_books_for_admin in sample[2].lower()):
                variable_list_order_for_view_books_admin_2.append(sample)
            else:
                continue
        for sample2 in list_of_view_books_admin:
            if (sample2 not in variable_list_order_for_view_books_admin_2) and (sample2[0].lower()==search_bar_view_books_for_admin):
                variable_list_order_for_view_books_admin_2.append(sample2)
            else:
                continue
        for sample3 in list_of_view_books_admin:
            if (sample3 not in variable_list_order_for_view_books_admin_2) and (sample3[1].lower()==search_bar_view_books_for_admin):
                variable_list_order_for_view_books_admin_2.append(sample3)
            else:
                continue
        for sample4 in list_of_view_books_admin:
            if (sample4 not in variable_list_order_for_view_books_admin_2) and (sample4[2].lower()==search_bar_view_books_for_admin):
                variable_list_order_for_view_books_admin_2.append(sample4)
            else:
                continue
        for sample5 in list_of_view_books_admin:
            if (sample5 not in variable_list_order_for_view_books_admin_2) and ((sample5[1].lower()).startswith(search_bar_view_books_for_admin)):
                variable_list_order_for_view_books_admin_2.append(sample5)
            else:
                continue
        for sample6 in list_of_view_books_admin:
            if (sample6 not in variable_list_order_for_view_books_admin_2) and ((sample6[2].lower()).startswith(search_bar_view_books_for_admin)):
                variable_list_order_for_view_books_admin_2.append(sample6)
            else:
                continue
        for sample7 in list_of_view_books_admin:
            if (sample7 not in variable_list_order_for_view_books_admin_2) and ((sample7[1].lower()).endswith(search_bar_view_books_for_admin)):
                variable_list_order_for_view_books_admin_2.append(sample7)
            else:
                continue
        for sample8 in list_of_view_books_admin:
            if (sample8 not in variable_list_order_for_view_books_admin_2) and ((sample8[2].lower()).endswith(search_bar_view_books_for_admin)):
                variable_list_order_for_view_books_admin_2.append(sample8)
            else:
                continue
        for sample9 in list_of_view_books_admin:
            if (sample9 not in variable_list_order_for_view_books_admin_2) and (search_bar_view_books_for_admin in sample9[1].lower()):
                variable_list_order_for_view_books_admin_2.append(sample9)
            else:
                continue
        for sample10 in list_of_view_books_admin:
            if (sample10 not in variable_list_order_for_view_books_admin_2) and (search_bar_view_books_for_admin in sample10[2].lower()):
                variable_list_order_for_view_books_admin_2.append(sample10)
            else:
                continue
        for sample11 in list_of_view_books_admin:
            if sample11 not in variable_list_order_for_view_books_admin_2:
                variable_list_order_for_view_books_admin_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_view_books_admin_page_for_scroll(variable_list_order_for_view_books_admin_2)







def searaching_and_reodering_radiobutton_of_view_books_admin_page_for_scroll(list_ordered):
    global book_name_select_for_view_books_admin_var
    global count_of_view_books_admin
    global dict_of_view_books_admin
    global list_of_view_books_admin
    global search_bar_view_books_for_admin
    global variable_list_order_for_view_books_admin_2
    variable_list_order_for_view_books_admin_2=[]



    innerframe7=LabelFrame(view_books_admin_page_root,text='books',bd=15,width=1000)
    innerframe7.place(x=600,y=300)

    #Creating Main fram:
    main_frame7=Frame(innerframe7,width=1000)
    main_frame7.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva7=Canvas(main_frame7,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva7.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll7=ttk.Scrollbar(main_frame7,orient=VERTICAL,command=canva7.yview) 
    scroll7.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva7.configure(yscrollcommand=scroll7.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva7.bind('<Configure>', lambda e: canva7.configure(scrollregion=canva7.bbox("all")))
    #Creating another frame inside canvas
    second_frame7=Frame(canva7,width=1000)
    #placing the second frame inside canva
    canva7.create_window((0,0),window=second_frame7,anchor='nw',)#nw means on the top right corner


    book_name_select_for_view_books_admin_var=IntVar()

    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(second_frame7,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_view_books_admin_var,value=i[3],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame7,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_view_books_admin_var,value=i[3],width=50,bg='cyan',padx=10,anchor='w').pack()






def no_scroll_for_view_books_admin_mid_fn():
    global count_of_view_books_admin
    global dict_of_view_books_admin
    global list_of_view_books_admin
    global search_bar_view_books_for_admin
    global variable_list_order_for_view_books_admin_2
    variable_list_order_for_view_books_admin_2=[]



    #search Bar operation

    if search_bar_view_books_for_admin=='':
        searaching_and_reodering_radiobutton_of_view_books_admin_page_for_no_scroll(list_of_view_books_admin)
    else:
        pass
        for sample in list_of_view_books_admin:
            if (sample[0].lower()==search_bar_view_books_for_admin) and (sample[1].lower()==search_bar_view_books_for_admin) and (sample[2].lower()==search_bar_view_books_for_admin) and ((sample[1].lower()).startswith(search_bar_view_books_for_admin)) and ((sample[2].lower()).startswith(search_bar_view_books_for_admin)) and ((sample[1].lower()).endswith(search_bar_view_books_for_admin)) and ((sample[2].lower()).endswith(search_bar_view_books_for_admin)) and (search_bar_view_books_for_admin in sample[1].lower()) and (search_bar_view_books_for_admin in sample[2].lower()):
                variable_list_order_for_view_books_admin_2.append(sample)
            else:
                continue
        for sample2 in list_of_view_books_admin:
            if (sample2 not in variable_list_order_for_view_books_admin_2) and (sample2[0].lower()==search_bar_view_books_for_admin):
                variable_list_order_for_view_books_admin_2.append(sample2)
            else:
                continue
        for sample3 in list_of_view_books_admin:
            if (sample3 not in variable_list_order_for_view_books_admin_2) and (sample3[1].lower()==search_bar_view_books_for_admin):
                variable_list_order_for_view_books_admin_2.append(sample3)
            else:
                continue
        for sample4 in list_of_view_books_admin:
            if (sample4 not in variable_list_order_for_view_books_admin_2) and (sample4[2].lower()==search_bar_view_books_for_admin):
                variable_list_order_for_view_books_admin_2.append(sample4)
            else:
                continue
        for sample5 in list_of_view_books_admin:
            if (sample5 not in variable_list_order_for_view_books_admin_2) and ((sample5[1].lower()).startswith(search_bar_view_books_for_admin)):
                variable_list_order_for_view_books_admin_2.append(sample5)
            else:
                continue
        for sample6 in list_of_view_books_admin:
            if (sample6 not in variable_list_order_for_view_books_admin_2) and ((sample6[2].lower()).startswith(search_bar_view_books_for_admin)):
                variable_list_order_for_view_books_admin_2.append(sample6)
            else:
                continue
        for sample7 in list_of_view_books_admin:
            if (sample7 not in variable_list_order_for_view_books_admin_2) and ((sample7[1].lower()).endswith(search_bar_view_books_for_admin)):
                variable_list_order_for_view_books_admin_2.append(sample7)
            else:
                continue
        for sample8 in list_of_view_books_admin:
            if (sample8 not in variable_list_order_for_view_books_admin_2) and ((sample8[2].lower()).endswith(search_bar_view_books_for_admin)):
                variable_list_order_for_view_books_admin_2.append(sample8)
            else:
                continue
        for sample9 in list_of_view_books_admin:
            if (sample9 not in variable_list_order_for_view_books_admin_2) and (search_bar_view_books_for_admin in sample9[1].lower()):
                variable_list_order_for_view_books_admin_2.append(sample9)
            else:
                continue
        for sample10 in list_of_view_books_admin:
            if (sample10 not in variable_list_order_for_view_books_admin_2) and (search_bar_view_books_for_admin in sample10[2].lower()):
                variable_list_order_for_view_books_admin_2.append(sample10)
            else:
                continue
        for sample11 in list_of_view_books_admin:
            if sample11 not in variable_list_order_for_view_books_admin_2:
                variable_list_order_for_view_books_admin_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_view_books_admin_page_for_no_scroll(variable_list_order_for_view_books_admin_2)


def searaching_and_reodering_radiobutton_of_view_books_admin_page_for_no_scroll(list_ordered):
    global book_name_select_for_view_books_admin_var
    global count_of_view_books_admin
    global dict_of_view_books_admin
    global list_of_view_books_admin
    global search_bar_view_books_for_admin
    global variable_list_order_for_view_books_admin_2
    variable_list_order_for_view_books_admin_2=[]

    innerframe7=LabelFrame(view_books_admin_page_root,text='books',bd=15,width=1000,)
    innerframe7.place(x=600,y=300)

    #Creating Main fram:
    main_frame7=Frame(innerframe7,width=1000)
    main_frame7.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_view_books_admin_var=IntVar()
    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(main_frame7,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_view_books_admin_var,value=i[3],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame7,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_view_books_admin_var,value=i[3],width=50,bg='cyan',padx=10,anchor='w').pack()







def clicking_proceed_in_view_books_admin():
    global book_name_select_for_view_books_admin_var
    global main_list_regarding_book_and_author_info_for_view_books_admin
    global dict_of_view_books_admin

    try:
        book_name_select_for_view_books_admin=book_name_select_for_view_books_admin_var.get()
    except:
        book_name_select_for_view_books_admin='chumma'
    main_list_regarding_book_and_author_info_for_view_books_admin=[]
    if book_name_select_for_view_books_admin==0:
        messagebox.showerror('View books','please select a book to view')
    elif book_name_select_for_view_books_admin=='chumma' or book_name_select_for_view_books_admin_var=='chumma':
        messagebox.showinfo('oops','there are no books to view right now')
        librarymanag_from_view_books_admin()
    else:
        main_list_regarding_book_and_author_info_for_view_books_admin=dict_of_view_books_admin[book_name_select_for_view_books_admin][0:3]   #just so that the 4th column is taken
        book_view_books_admin_tkinter_page_book_details()



def creating_dict_table_for_view_books_admin():
    global count_of_view_books_admin
    global list_of_view_books_admin 
    global dict_of_view_books_admin

    list_of_view_books_admin=[]
    dict_of_view_books_admin={}

    query1="select book_id,bookname,bookauthor from bookdata;"
    cursor_mysql.execute(query1)
    output=cursor_mysql.fetchall()

    if output==[]:
        list_of_view_books_admin=[]
        dict_of_view_books_admin={}
        count_of_view_books_admin=0
    else:
        for i in range(len(output)):
            dict_of_view_books_admin[i+1]=[output[i][0],output[i][1],output[i][2]]
            list_of_view_books_admin.append([output[i][0],output[i][1],output[i][2],(i+1)])
            count_of_view_books_admin=len(list_of_view_books_admin)



def obtaining_book_info_for_view_books_admin(list_to_regard):
    global main_book_id_for_showing_in_book_view_admin
    global main_bookname_for_showing_in_book_view_admin
    global main_bookauthor_for_showing_in_book_view_admin
    global main_number_of_pages_for_showing_in_book_view_admin
    global main_book_cover_for_showing_in_book_view_admin
    global main_bookinfo_for_showing_in_book_view_admin
    global main_author_info_for_showing_in_book_view_admin
    global main_username_who_issued_the_book_view_admin
    global main_issue_date_when_book_was_issued_view_admin
    global main_return_date_when_book_will_be_returned_view_admin

    query_for_book_last_update='''select * from bookdata where book_id='{0}';'''
    cursor_mysql.execute(query_for_book_last_update.format(list_to_regard[0]))
    new_list6=cursor_mysql.fetchall()

    main_book_id_for_showing_in_book_view_admin=new_list6[0][0]
    main_bookname_for_showing_in_book_view_admin=new_list6[0][1]
    main_bookauthor_for_showing_in_book_view_admin=new_list6[0][2]
    main_number_of_pages_for_showing_in_book_view_admin=new_list6[0][3]
    main_book_cover_for_showing_in_book_view_admin=new_list6[0][6]
    main_bookinfo_for_showing_in_book_view_admin=new_list6[0][4]
    if new_list6[0][5]==None:
        main_author_info_for_showing_in_book_view_admin='No Information Available'
    else:
        main_author_info_for_showing_in_book_view_admin=new_list6[0][5]

    query121="select * from bookissue where book_id2='{0}';"
    cursor_mysql.execute(query121.format(main_book_id_for_showing_in_book_view_admin))
    output=cursor_mysql.fetchall()
    if output[0][1]==None:
        main_username_who_issued_the_book_view_admin='Not Issued'
        main_issue_date_when_book_was_issued_view_admin='-NA-'
        main_return_date_when_book_will_be_returned_view_admin='-NA-'
    else:
        main_username_who_issued_the_book_view_admin=output[0][1]
        main_issue_date_when_book_was_issued_view_admin_2=str(output[0][2])
        main_return_date_when_book_will_be_returned_view_admin_2=str(output[0][3])

        l1=main_issue_date_when_book_was_issued_view_admin_2.split('-')
        l2=main_return_date_when_book_will_be_returned_view_admin_2.split('-')

        main_issue_date_when_book_was_issued_view_admin=l1[2]+'-'+l1[1]+'-'+l1[0]
        main_return_date_when_book_will_be_returned_view_admin=l2[2]+'-'+l2[1]+'-'+l2[0]



def book_view_books_admin_tkinter_page_book_details():
    global main_list_regarding_book_and_author_info_for_view_books_admin
    global view_books_info_admin_page_root

    view_books_admin_page_root.destroy()

    view_books_info_admin_page_root=Tk()
    view_books_info_admin_page_root.title('View Books')
    view_books_info_admin_page_root.state("zoomed")

    view_books_info_admin_page_root.config(background = "black", pady=10)

    obtaining_book_info_for_view_books_admin(main_list_regarding_book_and_author_info_for_view_books_admin)

    Label(view_books_info_admin_page_root,text="Book Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=40)
    Label(view_books_info_admin_page_root,text="Issued By:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=40)
    Label(view_books_info_admin_page_root,text="Book Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=170)
    Label(view_books_info_admin_page_root,text="Book Author:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=170)
    Label(view_books_info_admin_page_root,text="Number Of Pages:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=270)
    Label(view_books_info_admin_page_root,text="Book Cover:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=270)
    Label(view_books_info_admin_page_root,text="Book Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=420)
    Label(view_books_info_admin_page_root,text="Author Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=420)
    Label(view_books_info_admin_page_root,text="Issue Date:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=750)
    Label(view_books_info_admin_page_root,text="Return Date:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=750)

    Label(view_books_info_admin_page_root,text=main_book_id_for_showing_in_book_view_admin,font=("verdana", 20),width=20,anchor='w').place(x=310,y=40)
    Label(view_books_info_admin_page_root,text=main_username_who_issued_the_book_view_admin,font=("verdana", 20),width=20,anchor='w').place(x=1245,y=40)
    Label(view_books_info_admin_page_root,text=main_bookname_for_showing_in_book_view_admin,font=("verdana", 20),width=30,anchor='w').place(x=350,y=170)
    Label(view_books_info_admin_page_root,text=main_bookauthor_for_showing_in_book_view_admin,font=("verdana", 20),width=30,anchor='w').place(x=1275,y=170)
    Label(view_books_info_admin_page_root,text=main_number_of_pages_for_showing_in_book_view_admin,font=("verdana", 20),width=20,anchor='w').place(x=460,y=270)
    Label(view_books_info_admin_page_root,text=main_book_cover_for_showing_in_book_view_admin,font=("verdana", 20),width=20,anchor='w').place(x=1245,y=270)
    Label(view_books_info_admin_page_root,text=main_issue_date_when_book_was_issued_view_admin,font=("verdana", 20),width=20,anchor='w').place(x=350,y=750)
    Label(view_books_info_admin_page_root,text=main_return_date_when_book_will_be_returned_view_admin,font=("verdana", 20),width=20,anchor='w').place(x=1270,y=750)

    first_scroll_for_view_books_admin=scrolledtext.ScrolledText(view_books_info_admin_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    second_scroll_for_view_books_admin=scrolledtext.ScrolledText(view_books_info_admin_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    first_scroll_for_view_books_admin.insert(END,main_bookinfo_for_showing_in_book_view_admin)
    second_scroll_for_view_books_admin.insert(END,main_author_info_for_showing_in_book_view_admin)
    first_scroll_for_view_books_admin.place(x=330,y=420)
    second_scroll_for_view_books_admin.place(x=1270,y=420)

    Button(view_books_info_admin_page_root,text='Go Back',font=('verdana',25),cursor='hand2',command=librarymang_home_page_admin_from_view_books_admin_tkinter_info_page).place(x=900,y=900)
    photo = PhotoImage(file = "e.png")
    view_books_info_admin_page_root.iconphoto(False, photo)






#****************************************************************************************************************************************************************************************

def students_info_admin_page():

    global students_info_admin_page_root
    global count_of_students_info_admin
    global list_of_students_info_admin
    global dict_of_students_info_admin
    global search_bar_students_info_for_admin_var

    librarymang_home_page_admin_root.destroy()

    students_info_admin_page_root=Tk()
    students_info_admin_page_root.title("View Students")
    students_info_admin_page_root.state("zoomed")
    students_info_admin_page_root.config(background = "black", pady=10)
    Label(students_info_admin_page_root, text="Student Info",width=100, font=("freestyle script", 70)).pack()
    search_bar_students_info_for_admin_var=StringVar()
    Entry(students_info_admin_page_root, font=('verdana',30),textvariable=search_bar_students_info_for_admin_var,width=50).place(x=250,y=200)
    Button(students_info_admin_page_root,text='Search',cursor='hand2',font=('verdana',30),bg='grey',command=searcher_bar_mid_fn_for_student_info_admin).place(x=1600,y=180)
    Button(students_info_admin_page_root,text='Go Back',cursor='hand2',font=('verdana',30),command=librarymanag_from_student_info_admin).place(x=1050,y=900)
    Button(students_info_admin_page_root,text='Student info',cursor='hand2',font=('verdana',30),command=clicking_proceed_in_student_info_admin).place(x=640,y=900)
    photo = PhotoImage(file = "e.png")
    students_info_admin_page_root.iconphoto(False, photo)
    

    creating_dict_table_for_student_info_admin()    # creating dictionary and list
    

    if count_of_students_info_admin==0:
        no_students_to_view_admin()
    elif count_of_students_info_admin<=4:
        no_scroll_for_students_info_admin()
    else:
        if_is_scroll_for_students_info_admin()



def student_view_books_admin_tkinter_page_student_details():
    global main_list_regarding_username_and_name_student_info_admin
    global students_info_admin_tk_page_root

    students_info_admin_page_root.destroy()

    students_info_admin_tk_page_root=Tk()
    students_info_admin_tk_page_root.title('View students')
    students_info_admin_tk_page_root.state("zoomed")

    students_info_admin_tk_page_root.config(background = "black", pady=10)

    obtaining_student_info_for_view_student_info_admin(main_list_regarding_username_and_name_student_info_admin)

    global main_username_for_student_info_page
    global main_emailid_for_student_info_page
    global main_phoneno_for_student_info_page
    global main_firstname_for_student_info_page
    global main_lastname_for_student_info_page
    global main_gender_for_student_info_page
    global main_country_for_student_info_page


    Label(students_info_admin_tk_page_root,text="Username:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=80)
    Label(students_info_admin_tk_page_root,text="Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=80)
    Label(students_info_admin_tk_page_root,text="Email-Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=210)
    Label(students_info_admin_tk_page_root,text="Gender:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=210)
    Label(students_info_admin_tk_page_root,text="Country:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=350)
    Label(students_info_admin_tk_page_root,text="Phone no:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=350)
    Label(students_info_admin_tk_page_root,text="Issued Books: ",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=490)

    Label(students_info_admin_tk_page_root,text=main_username_for_student_info_page,font=("verdana", 20),width=30,anchor='w').place(x=335,y=80)
    Label(students_info_admin_tk_page_root,text=main_firstname_for_student_info_page+main_lastname_for_student_info_page,font=("verdana", 20),width=30,anchor='w').place(x=1175,y=80)
    Label(students_info_admin_tk_page_root,text=main_emailid_for_student_info_page,font=("verdana", 20),width=30,anchor='w').place(x=325,y=210)
    Label(students_info_admin_tk_page_root,text=main_gender_for_student_info_page,font=("verdana", 20),width=30,anchor='w').place(x=1200,y=210)
    Label(students_info_admin_tk_page_root,text=main_country_for_student_info_page,font=("verdana", 20),width=30,anchor='w').place(x=300,y=350)
    Label(students_info_admin_tk_page_root,text=str(main_phoneno_for_student_info_page),font=("verdana", 20),width=30,anchor='w').place(x=1225,y=350)
    photo = PhotoImage(file = "e.png")
    students_info_admin_tk_page_root.iconphoto(False, photo)
    if main_issue3_for_student_info!=None:
        Issued_books_if_3()
    elif main_issue2_for_student_info!=None and main_issue3_for_student_info==None:
        Issued_books_if_2()
    elif main_issue1_for_student_info!=None and main_issue2_for_student_info==None and main_issue3_for_student_info==None:
        Issued_books_if_1()
    elif main_issue1_for_student_info==None and main_issue2_for_student_info==None and main_issue3_for_student_info==None:
        No_issued_books()

    Button(students_info_admin_tk_page_root,text='Go Back',font=('verdana',25),cursor='hand2',command=librarymanag_from_student_info_admin_tk).place(x=900,y=900)
def no_issued_books():
    Label(students_info_admin_tk_page_root,text='No Book Issued',font=("verdana", 20),width=30,anchor='w').place(x=380,y=490)

def Issued_books_if_3():
    global students_info_admin_tk_page_root

    innerframe9=LabelFrame(students_info_admin_tk_page_root,text='Issue1',bd=15,width=1000,font=('verdana',15))
    innerframe9.place(x=70,y=580)

    #Creating Main fram:
    main_frame9=Frame(innerframe9,width=1000,padx=15)
    main_frame9.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    issuedate1=str(main_issue_date1__for_student_info)
    li1=issuedate1.split('-')
    returndate1=str(main_return_date1__for_student_info)
    lr1=returndate1.split('-')
    Label(main_frame9,text="Book: "+main_bookname1_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Author: "+main_author1_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Issue Date: "+li1[2]+'-'+li1[1]+'-'+li1[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Return Date: "+lr1[2]+'-'+lr1[1]+'-'+lr1[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9).pack()
    if checking_if_due_date_is_past_for_student_info(returndate1):
        send_reminder_mail_student_info(main_frame9,main_bookname1_for_student_info,issuedate1,returndate1)
    else:
        empty_pack(main_frame9)


    innerframe10=LabelFrame(students_info_admin_tk_page_root,text='Issue2',bd=15,width=1000,font=('verdana',15))
    innerframe10.place(x=660,y=580)

    #Creating Main fram:
    main_frame10=Frame(innerframe10,width=20,padx=15)
    main_frame10.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y

    issuedate2=str(main_issue_date2__for_student_info)
    li2=issuedate2.split('-')
    returndate2=str(main_return_date2__for_student_info)
    lr2=returndate2.split('-')

    Label(main_frame10,text="Book: "+main_bookname2_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame10,text="Author: "+main_author2_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame10,text="Issue Date: "+li2[2]+'-'+li2[1]+'-'+li2[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame10,text="Return Date: "+lr2[2]+'-'+lr2[1]+'-'+lr2[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame10,).pack()
    if checking_if_due_date_is_past_for_student_info(returndate2):
        send_reminder_mail_student_info(main_frame10,main_bookname2_for_student_info,issuedate2,returndate2)
    else:
        empty_pack(main_frame10)


    innerframe11=LabelFrame(students_info_admin_tk_page_root,text='Issue3',bd=15,width=1000,font=('verdana',15))
    innerframe11.place(x=1260,y=580)

    #Creating Main fram:
    main_frame11=Frame(innerframe11,width=1000,padx=15)
    main_frame11.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y

    issuedate3=str(main_issue_date3__for_student_info)
    li3=issuedate3.split('-')
    returndate3=str(main_return_date3__for_student_info)
    lr3=returndate3.split('-')

    Label(main_frame11,text="Book: "+main_bookname3_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame11,text="Author: "+main_author3_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame11,text="Issue Date: "+li3[2]+'-'+li3[1]+'-'+li3[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame11,text="Return Date: "+lr3[2]+'-'+lr3[1]+'-'+lr3[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame11,).pack()
    if checking_if_due_date_is_past_for_student_info(returndate3):
        send_reminder_mail_student_info(main_frame11,main_bookname3_for_student_info,issuedate3,returndate3)
    else:
        empty_pack(main_frame11)


def Issued_books_if_2():
    global students_info_admin_tk_page_root

    innerframe9=LabelFrame(students_info_admin_tk_page_root,text='Issue1',bd=15,width=1000,font=('verdana',15))
    innerframe9.place(x=250,y=580)

    #Creating Main fram:
    main_frame9=Frame(innerframe9,width=1000,padx=15)
    main_frame9.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    issuedate1=str(main_issue_date1__for_student_info)
    li1=issuedate1.split('-')
    returndate1=str(main_return_date1__for_student_info)
    lr1=returndate1.split('-')
    Label(main_frame9,text="Book: "+main_bookname1_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Author: "+main_author1_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Issue Date: "+li1[2]+'-'+li1[1]+'-'+li1[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Return Date: "+lr1[2]+'-'+lr1[1]+'-'+lr1[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9).pack()
    if checking_if_due_date_is_past_for_student_info(returndate1):
        send_reminder_mail_student_info(main_frame9,main_bookname1_for_student_info,issuedate1,returndate1)
    else:
        empty_pack(main_frame9)

    innerframe10=LabelFrame(students_info_admin_tk_page_root,text='Issue2',bd=15,width=1000,font=('verdana',15))
    innerframe10.place(x=1100,y=580)

    #Creating Main fram:
    main_frame10=Frame(innerframe10,width=20,padx=15)
    main_frame10.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y

    issuedate2=str(main_issue_date2__for_student_info)
    li2=issuedate2.split('-')
    returndate2=str(main_return_date2__for_student_info)
    lr2=returndate2.split('-')

    Label(main_frame10,text="Book: "+main_bookname2_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame10,text="Author: "+main_author2_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame10,text="Issue Date: "+li2[2]+'-'+li2[1]+'-'+li2[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame10,text="Return Date: "+lr2[2]+'-'+lr2[1]+'-'+lr2[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame10,).pack()
    if checking_if_due_date_is_past_for_student_info(returndate2):
        send_reminder_mail_student_info(main_frame10,main_bookname2_for_student_info,issuedate2,returndate2)
    else:
        empty_pack(main_frame10)

def Issued_books_if_1():
    global students_info_admin_tk_page_root

    innerframe9=LabelFrame(students_info_admin_tk_page_root,text='Issue1',bd=15,width=1000,font=('verdana',15))
    innerframe9.place(x=680,y=580)

    #Creating Main fram:
    main_frame9=Frame(innerframe9,width=1000,padx=15)
    main_frame9.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    issuedate1=str(main_issue_date1__for_student_info)
    li1=issuedate1.split('-')
    returndate1=str(main_return_date1__for_student_info)
    lr1=returndate1.split('-')
    Label(main_frame9,text="Book: "+main_bookname1_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Author: "+main_author1_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Issue Date: "+li1[2]+'-'+li1[1]+'-'+li1[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Return Date: "+lr1[2]+'-'+lr1[1]+'-'+lr1[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9).pack()
    if checking_if_due_date_is_past_for_student_info(returndate1):
        send_reminder_mail_student_info(main_frame9,main_bookname1_for_student_info,issuedate1,returndate1)
    else:
        empty_pack(main_frame9)


def empty_pack(root):
    Label(root).pack()
    Label(root).pack()


def checking_if_due_date_is_past_for_student_info(retdate):
    list_of_day_month_year=retdate.split('-')
    year_of_return=int(list_of_day_month_year[0])
    month_of_return=int(list_of_day_month_year[1])
    day_of_return=int(list_of_day_month_year[2])
    bool_val_for_date=(datetime.now()>datetime(year_of_return,month_of_return,day_of_return))
    return bool_val_for_date

def send_reminder_mail_student_info(frame,book,idate,retdate):
    global i
    global r
    global b
    li=idate.split('-')
    i=li[2]+'-'+li[1]+'-'+li[0]
    lr=retdate.split('-')
    r=lr[2]+'-'+lr[1]+'-'+lr[0]
    b=book

    Button(frame,text='Send Reminder',font=('verdana',15),command=send_reminder_mail_for_student_info).pack()

def send_reminder_mail_for_student_info():
    email=os.environ.get('project_email')
    passkey=os.environ.get('project_email_password')
    msg_for_reminder=MIMEText('The Book - (  '+b+'  ) you issued on '+i+' was due on '+r+' .\nPlease do return the issued book at the earliest.')

    msg_for_reminder['Subject']='Friendly Reminder:'
    msg_for_reminder['From']=email
    msg_for_reminder['To']=main_emailid_for_student_info_page
    ref_111=1
    try:
        with smtplib.SMTP('smtp.gmail.com','587') as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(email,passkey)
            smtp.sendmail(email,main_emailid_for_student_info_page,msg_for_reminder.as_string())
        ref_111=1
    except Exception as e:
        newe=str(e)
        if newe=='[Errno 11001] getaddrinfo failed':
            messagebox.showinfo('no internet','Please connect to the internet')
        else:
            messagebox.showerror('error','invalid email id')
        ref_111=0

    if ref_111==1:
        messagebox.showinfo('reminder','reminder mail sent to '+main_username_for_student_info_page)
    else:
        pass

def obtaining_student_info_for_view_student_info_admin(list_to_regard):
    global main_username_for_student_info_page
    global main_emailid_for_student_info_page
    global main_phoneno_for_student_info_page
    global main_firstname_for_student_info_page
    global main_lastname_for_student_info_page
    global main_gender_for_student_info_page
    global main_country_for_student_info_page
    global main_issue1_for_student_info
    global main_issue2_for_student_info
    global main_issue3_for_student_info
    global main_bookname1_for_student_info
    global main_bookname2_for_student_info
    global main_bookname3_for_student_info
    global main_author1_for_student_info
    global main_author2_for_student_info
    global main_author3_for_student_info
    global main_issue_date1__for_student_info
    global main_issue_date2__for_student_info
    global main_issue_date3__for_student_info
    global main_return_date1__for_student_info    
    global main_return_date2__for_student_info
    global main_return_date3__for_student_info
    query_for_student_last_update="select username,emailid,phoneno,firstname,lastname,gender,country from logindata where username='{0}';"
    cursor_mysql.execute(query_for_student_last_update.format(list_to_regard[0]))
    new_list7=cursor_mysql.fetchall()

    main_username_for_student_info_page=new_list7[0][0]
    main_emailid_for_student_info_page=new_list7[0][1]
    main_phoneno_for_student_info_page=new_list7[0][2]
    main_firstname_for_student_info_page=new_list7[0][3]
    main_lastname_for_student_info_page=new_list7[0][4]
    main_gender_for_student_info_page=new_list7[0][5]
    main_country_for_student_info_page=new_list7[0][6]

    query1211="select * from loginissue where username='{0}';"
    cursor_mysql.execute(query1211.format(main_username_for_student_info_page))
    output=cursor_mysql.fetchall()
    main_issue1_for_student_info=output[0][1]
    main_issue2_for_student_info=output[0][2]
    main_issue3_for_student_info=output[0][3]

    if main_issue1_for_student_info==None:
        main_bookname1_for_student_info=None
        main_bookname2_for_student_info=None
        main_bookname3_for_student_info=None
        main_issue_date1__for_student_info=None
        main_issue_date2__for_student_info=None
        main_issue_date3__for_student_info=None
        main_return_date1__for_student_info=None
        main_return_date2__for_student_info=None
        main_return_date3__for_student_info=None
        main_author1_for_student_info=None
        main_author2_for_student_info=None
        main_author3_for_student_info=None
    
    elif main_issue3_for_student_info!=None:
        q11="select bookname,bookauthor from bookdata where book_id='{0}';"
        q12="select date_of_issue,date_of_return from bookissue where book_id2='{0}';"
        cursor_mysql.execute(q11.format(main_issue1_for_student_info))
        out11=cursor_mysql.fetchall()
        a=1
        cursor_mysql.execute(q12.format(main_issue1_for_student_info))
        out12=cursor_mysql.fetchall()
        main_bookname1_for_student_info=out11[0][0]
        main_author1_for_student_info=out11[0][1]
        main_issue_date1__for_student_info=out12[0][0]
        main_return_date1__for_student_info=out12[0][1]

        q21="select bookname,bookauthor from bookdata where book_id='{0}';"
        q22="select date_of_issue,date_of_return from bookissue where book_id2='{0}';"
        cursor_mysql.execute(q21.format(main_issue2_for_student_info))
        out21=cursor_mysql.fetchall()
        a=1
        cursor_mysql.execute(q22.format(main_issue2_for_student_info))
        out22=cursor_mysql.fetchall()
        main_bookname2_for_student_info=out21[0][0]
        main_author2_for_student_info=out21[0][1]
        main_issue_date2__for_student_info=out22[0][0]
        main_return_date2__for_student_info=out22[0][1]

        q31="select bookname,bookauthor from bookdata where book_id='{0}';"
        q32="select date_of_issue,date_of_return from bookissue where book_id2='{0}';"
        cursor_mysql.execute(q31.format(main_issue3_for_student_info))
        out31=cursor_mysql.fetchall()
        a=1
        cursor_mysql.execute(q32.format(main_issue3_for_student_info))
        out32=cursor_mysql.fetchall()
        main_bookname3_for_student_info=out31[0][0]
        main_author3_for_student_info=out31[0][1]
        main_issue_date3__for_student_info=out32[0][0]
        main_return_date3__for_student_info=out32[0][1]


    elif main_issue3_for_student_info==None and main_issue2_for_student_info!=None:
        q11="select bookname,bookauthor from bookdata where book_id='{0}';"
        q12="select date_of_issue,date_of_return from bookissue where book_id2='{0}';"
        cursor_mysql.execute(q11.format(main_issue1_for_student_info))
        out11=cursor_mysql.fetchall()
        a=1
        cursor_mysql.execute(q12.format(main_issue1_for_student_info))
        out12=cursor_mysql.fetchall()
        main_bookname1_for_student_info=out11[0][0]
        main_author1_for_student_info=out11[0][1]
        main_issue_date1__for_student_info=out12[0][0]
        main_return_date1__for_student_info=out12[0][1]

        q21="select bookname,bookauthor from bookdata where book_id='{0}';"
        q22="select date_of_issue,date_of_return from bookissue where book_id2='{0}';"
        cursor_mysql.execute(q21.format(main_issue2_for_student_info))
        out21=cursor_mysql.fetchall()
        a=1
        cursor_mysql.execute(q22.format(main_issue2_for_student_info))
        out22=cursor_mysql.fetchall()
        main_bookname2_for_student_info=out21[0][0]
        main_author2_for_student_info=out21[0][1]
        main_issue_date2__for_student_info=out22[0][0]
        main_return_date2__for_student_info=out22[0][1]

        main_bookname3_for_student_info=None
        main_author3_for_student_info=None
        main_issue_date3__for_student_info=None
        main_return_date3__for_student_info=None

    elif main_issue3_for_student_info==None and main_issue2_for_student_info==None and main_issue1_for_student_info!=None:
        q11="select bookname,bookauthor from bookdata where book_id='{0}';"
        q12="select date_of_issue,date_of_return from bookissue where book_id2='{0}';"
        cursor_mysql.execute(q11.format(main_issue1_for_student_info))
        out11=cursor_mysql.fetchall()
        a=1
        cursor_mysql.execute(q12.format(main_issue1_for_student_info))
        out12=cursor_mysql.fetchall()
        main_bookname1_for_student_info=out11[0][0]
        main_author1_for_student_info=out11[0][1]
        main_issue_date1__for_student_info=out12[0][0]
        main_return_date1__for_student_info=out12[0][1]

        main_bookname2_for_student_info=None
        main_author2_for_student_info=None
        main_issue_date2__for_student_info=None
        main_return_date2__for_student_info=None

        main_bookname3_for_student_info=None
        main_author3_for_student_info=None
        main_issue_date3__for_student_info=None
        main_return_date3__for_student_info=None


def clicking_proceed_in_student_info_admin():
    global user_name_select_for_view_students_admin_var
    global main_list_regarding_username_and_name_student_info_admin
    global dict_of_students_info_admin

    try:
        user_name_select_for_view_students_admin=user_name_select_for_view_students_admin_var.get()
    except:
        user_name_select_for_view_students_admin='chumma'
    main_list_regarding_username_and_name_student_info_admin=[]
    if user_name_select_for_view_students_admin==0:
        messagebox.showerror('View Students','Please Select a Student')
    elif user_name_select_for_view_students_admin=='chumma' or user_name_select_for_view_students_admin_var=='chumma':
        messagebox.showinfo('oops','there are no students to view right now')
        librarymanag_from_student_info_admin()
    else:
        main_list_regarding_username_and_name_student_info_admin=dict_of_students_info_admin[user_name_select_for_view_students_admin][0:2]   #just so that the 4th column is taken
        student_view_books_admin_tkinter_page_student_details()




def no_students_to_view_admin():
    global user_name_select_for_view_students_admin_var
    global user_name_select_for_view_students_admin
    book_name_select_for_view_students_admin=user_name_select_for_view_students_admin_var='chumma'
    Label(students_info_admin_page_root,text="There are no books available right now",font=("lucida handwriting", 30),bg='black',fg='white').place(x=500,y=500)


def if_is_scroll_for_students_info_admin():

    global students_info_admin_page_root
    global dict_of_students_info_admin
    innerframe8=LabelFrame(students_info_admin_page_root,text='Students',bd=15,width=1000,font=('verdana',15))
    innerframe8.place(x=350,y=300)

    #Creating Main fram:
    main_frame8=Frame(innerframe8,width=1000)
    main_frame8.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva8=Canvas(main_frame8,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva8.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll8=ttk.Scrollbar(main_frame8,orient=VERTICAL,command=canva8.yview) 
    scroll8.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva8.configure(yscrollcommand=scroll8.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva8.bind('<Configure>', lambda e: canva8.configure(scrollregion=canva8.bbox("all")))
    #Creating another frame inside canvas
    second_frame8=Frame(canva8,width=1000)
    #placing the second frame inside canva
    canva8.create_window((0,0),window=second_frame8,anchor='nw',)#nw means on the top right corner
    global user_name_select_for_view_students_admin_var
    user_name_select_for_view_students_admin_var=IntVar()
    for i in range(1,count_of_students_info_admin+1):
        if i%2==0:
            Radiobutton(second_frame8,text='Username: '+dict_of_students_info_admin[i][0]+'\nName: '+dict_of_students_info_admin[i][1],fg='black',font=("lucida handwriting", 25),indicator=0,variable=user_name_select_for_view_students_admin_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame8,text='Username: '+dict_of_students_info_admin[i][0]+'\nName: '+dict_of_students_info_admin[i][1],fg='black',font=("lucida handwriting", 25),indicator=0,variable=user_name_select_for_view_students_admin_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()







def no_scroll_for_students_info_admin():
    global students_info_admin_page_root
    global dict_of_students_info_admin
    global count_of_students_info_admin

    innerframe8=LabelFrame(students_info_admin_page_root,text='Students',bd=15,width=1000,font=('verdana',15))
    innerframe8.place(x=350,y=300)

    #Creating Main fram:
    main_frame8=Frame(innerframe8,width=1000)
    main_frame8.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    global user_name_select_for_view_students_admin_var
    user_name_select_for_view_students_admin_var=IntVar()
    for i in range(1,count_of_students_info_admin+1):
        if i%2==0:
            Radiobutton(main_frame8,text='Username: '+dict_of_students_info_admin[i][0]+'\nName: '+dict_of_students_info_admin[i][1],fg='black',font=("lucida handwriting", 25),indicator=0,variable=user_name_select_for_view_students_admin_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame8,text='Username: '+dict_of_students_info_admin[i][0]+'\nName: '+dict_of_students_info_admin[i][1],fg='black',font=("lucida handwriting", 25),indicator=0,variable=user_name_select_for_view_students_admin_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()




def creating_dict_table_for_student_info_admin():
    global count_of_students_info_admin
    global list_of_students_info_admin 
    global dict_of_students_info_admin

    list_of_students_info_admin=[]
    dict_of_students_info_admin={}
    query1="select username,firstname,lastname from logindata where accountype='Student';"
    cursor_mysql.execute(query1)
    output=cursor_mysql.fetchall()

    if output==[]:
        list_of_students_info_admin=[]
        dict_of_students_info_admin={}
        count_of_students_info_admin=0
    else:
        for i in range(len(output)):
            dict_of_students_info_admin[i+1]=[output[i][0],output[i][1]+' '+output[i][2]]
            list_of_students_info_admin.append([output[i][0],output[i][1]+' '+output[i][2],(i+1)])
            count_of_students_info_admin=len(list_of_students_info_admin)



def searcher_bar_mid_fn_for_student_info_admin():
    global search_bar_students_info_for_admin_var
    global search_bar_students_info_for_admin
    global dict_of_students_info_admin
    global count_of_students_info_admin
    search_bar_students_info_for_admin_2=search_bar_students_info_for_admin_var.get()
    search_bar_students_info_for_admin=search_bar_students_info_for_admin_2.lower()
    if count_of_students_info_admin==0:
        no_students_to_view_admin()
    elif count_of_students_info_admin<=4:
        no_scroll_for_students_info_admin_mid_fn()
    else:
        if_is_scroll_for_view_students_info_for_mid_fn()



def if_is_scroll_for_view_students_info_for_mid_fn():
    global count_of_students_info_admin
    global dict_of_students_info_admin
    global list_of_students_info_admin
    global search_bar_students_info_for_admin
    global variable_list_order_for_students_info_admin_2
    variable_list_order_for_students_info_admin_2=[]

    #search bar

    if search_bar_students_info_for_admin=='':
        searaching_and_reodering_radiobutton_of_students_info_admin_page_for_scroll(list_of_students_info_admin)
    else:
        pass
        for sample in list_of_students_info_admin:
            if (sample[0].lower()==search_bar_students_info_for_admin) and (sample[1].lower()==search_bar_students_info_for_admin) and ((sample[0].lower()).startswith(search_bar_students_info_for_admin)) and ((sample[1].lower()).startswith(search_bar_students_info_for_admin)) and ((sample[0].lower()).endswith(search_bar_students_info_for_admin)) and ((sample[1].lower()).endswith(search_bar_students_info_for_admin)) and (search_bar_students_info_for_admin in sample[0].lower()) and (search_bar_students_info_for_admin in sample[1].lower()):
                variable_list_order_for_students_info_admin_2.append(sample)
            else:
                continue
        for sample2 in list_of_students_info_admin:
            if (sample2 not in variable_list_order_for_students_info_admin_2) and (sample2[0].lower()==search_bar_students_info_for_admin):
                variable_list_order_for_students_info_admin_2.append(sample2)
            else:
                continue
        for sample3 in list_of_students_info_admin:
            if (sample3 not in variable_list_order_for_students_info_admin_2) and (sample3[1].lower()==search_bar_students_info_for_admin):
                variable_list_order_for_students_info_admin_2.append(sample3)
            else:
                continue
        for sample5 in list_of_students_info_admin:
            if (sample5 not in variable_list_order_for_students_info_admin_2) and ((sample5[0].lower()).startswith(search_bar_students_info_for_admin)):
                variable_list_order_for_students_info_admin_2.append(sample5)
            else:
                continue
        for sample6 in list_of_students_info_admin:
            if (sample6 not in variable_list_order_for_students_info_admin_2) and ((sample6[1].lower()).startswith(search_bar_students_info_for_admin)):
                variable_list_order_for_students_info_admin_2.append(sample6)
            else:
                continue
        for sample7 in list_of_students_info_admin:
            if (sample7 not in variable_list_order_for_students_info_admin_2) and ((sample7[0].lower()).endswith(search_bar_students_info_for_admin)):
                variable_list_order_for_students_info_admin_2.append(sample7)
            else:
                continue
        for sample8 in list_of_students_info_admin:
            if (sample8 not in variable_list_order_for_students_info_admin_2) and ((sample8[1].lower()).endswith(search_bar_students_info_for_admin)):
                variable_list_order_for_students_info_admin_2.append(sample8)
            else:
                continue
        for sample9 in list_of_students_info_admin:
            if (sample9 not in variable_list_order_for_students_info_admin_2) and (search_bar_students_info_for_admin in sample9[0].lower()):
                variable_list_order_for_students_info_admin_2.append(sample9)
            else:
                continue
        for sample10 in list_of_students_info_admin:
            if (sample10 not in variable_list_order_for_students_info_admin_2) and (search_bar_students_info_for_admin in sample10[1].lower()):
                variable_list_order_for_students_info_admin_2.append(sample10)
            else:
                continue
        for sample11 in list_of_students_info_admin:
            if sample11 not in variable_list_order_for_students_info_admin_2:
                variable_list_order_for_students_info_admin_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_students_info_admin_page_for_scroll(variable_list_order_for_students_info_admin_2)







def searaching_and_reodering_radiobutton_of_students_info_admin_page_for_scroll(list_ordered):
    global user_name_select_for_view_students_admin_var
    global count_of_students_info_admin
    global dict_of_students_info_admin
    global list_of_students_info_admin
    global search_bar_students_info_for_admin
    global variable_list_order_for_students_info_admin_2
    variable_list_order_for_students_info_admin_2=[]



    innerframe8=LabelFrame(students_info_admin_page_root,text='Students',bd=15,width=1000,font=('verdana',15))
    innerframe8.place(x=350,y=300)

    #Creating Main fram:
    main_frame8=Frame(innerframe8,width=1000)
    main_frame8.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva8=Canvas(main_frame8,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva8.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll8=ttk.Scrollbar(main_frame8,orient=VERTICAL,command=canva8.yview) 
    scroll8.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva8.configure(yscrollcommand=scroll8.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva8.bind('<Configure>', lambda e: canva8.configure(scrollregion=canva8.bbox("all")))
    #Creating another frame inside canvas
    second_frame8=Frame(canva8,width=1000)
    #placing the second frame inside canva
    canva8.create_window((0,0),window=second_frame8,anchor='nw',)#nw means on the top right corner


    user_name_select_for_view_students_admin_var=IntVar()

    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(second_frame8,text='Username: '+i[0]+'\nName: '+i[1],fg='black',font=("lucida handwriting", 25),indicator=0,variable=user_name_select_for_view_students_admin_var,value=i[2],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame8,text='Username: '+i[0]+'\nName: '+i[1],fg='black',font=("lucida handwriting", 25),indicator=0,variable=user_name_select_for_view_students_admin_var,value=i[2],width=50,bg='cyan',padx=10,anchor='w').pack()






def no_scroll_for_students_info_admin_mid_fn():
    global count_of_students_info_admin
    global dict_of_students_info_admin
    global list_of_students_info_admin
    global search_bar_students_info_for_admin
    global variable_list_order_for_students_info_admin_2
    variable_list_order_for_students_info_admin_2=[]



    #search Bar operation

    if search_bar_students_info_for_admin=='':
        searaching_and_reodering_radiobutton_of_students_info_admin_page_for_no_scroll(list_of_students_info_admin)
    else:
        pass
        for sample in list_of_students_info_admin:
            if (sample[0].lower()==search_bar_students_info_for_admin) and (sample[1].lower()==search_bar_students_info_for_admin) and ((sample[0].lower()).startswith(search_bar_students_info_for_admin)) and ((sample[1].lower()).startswith(search_bar_students_info_for_admin)) and ((sample[0].lower()).endswith(search_bar_students_info_for_admin)) and ((sample[1].lower()).endswith(search_bar_students_info_for_admin)) and (search_bar_students_info_for_admin in sample[0].lower()) and (search_bar_students_info_for_admin in sample[1].lower()):
                variable_list_order_for_students_info_admin_2.append(sample)
            else:
                continue
        for sample2 in list_of_students_info_admin:
            if (sample2 not in variable_list_order_for_students_info_admin_2) and (sample2[0].lower()==search_bar_students_info_for_admin):
                variable_list_order_for_students_info_admin_2.append(sample2)
            else:
                continue
        for sample3 in list_of_students_info_admin:
            if (sample3 not in variable_list_order_for_students_info_admin_2) and (sample3[1].lower()==search_bar_students_info_for_admin):
                variable_list_order_for_students_info_admin_2.append(sample3)
            else:
                continue
        for sample5 in list_of_students_info_admin:
            if (sample5 not in variable_list_order_for_students_info_admin_2) and ((sample5[0].lower()).startswith(search_bar_students_info_for_admin)):
                variable_list_order_for_students_info_admin_2.append(sample5)
            else:
                continue
        for sample6 in list_of_students_info_admin:
            if (sample6 not in variable_list_order_for_students_info_admin_2) and ((sample6[1].lower()).startswith(search_bar_students_info_for_admin)):
                variable_list_order_for_students_info_admin_2.append(sample6)
            else:
                continue
        for sample7 in list_of_students_info_admin:
            if (sample7 not in variable_list_order_for_students_info_admin_2) and ((sample7[0].lower()).endswith(search_bar_students_info_for_admin)):
                variable_list_order_for_students_info_admin_2.append(sample7)
            else:
                continue
        for sample8 in list_of_students_info_admin:
            if (sample8 not in variable_list_order_for_students_info_admin_2) and ((sample8[1].lower()).endswith(search_bar_students_info_for_admin)):
                variable_list_order_for_students_info_admin_2.append(sample8)
            else:
                continue
        for sample9 in list_of_students_info_admin:
            if (sample9 not in variable_list_order_for_students_info_admin_2) and (search_bar_students_info_for_admin in sample9[0].lower()):
                variable_list_order_for_students_info_admin_2.append(sample9)
            else:
                continue
        for sample10 in list_of_students_info_admin:
            if (sample10 not in variable_list_order_for_students_info_admin_2) and (search_bar_students_info_for_admin in sample10[1].lower()):
                variable_list_order_for_students_info_admin_2.append(sample10)
            else:
                continue
        for sample11 in list_of_students_info_admin:
            if sample11 not in variable_list_order_for_students_info_admin_2:
                variable_list_order_for_students_info_admin_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_students_info_admin_page_for_no_scroll(variable_list_order_for_students_info_admin_2)


def searaching_and_reodering_radiobutton_of_students_info_admin_page_for_no_scroll(list_ordered):
    global user_name_select_for_view_students_admin_var
    global count_of_students_info_admin
    global dict_of_students_info_admin
    global list_of_students_info_admin
    global search_bar_students_info_for_admin
    global variable_list_order_for_students_info_admin_2
    variable_list_order_for_students_info_admin_2=[]

    innerframe8=LabelFrame(students_info_admin_page_root,text='Students',bd=15,width=1000,font=('verdana',15))
    innerframe8.place(x=350,y=300)

    #Creating Main fram:
    main_frame8=Frame(innerframe8,width=1000)
    main_frame8.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    user_name_select_for_view_students_admin_var=IntVar()
    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(main_frame8,text='Username: '+i[0]+'\nName: '+i[1],fg='black',font=("lucida handwriting", 25),indicator=0,variable=user_name_select_for_view_students_admin_var,value=i[2],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame8,text='Username: '+i[0]+'\nName: '+i[1],fg='black',font=("lucida handwriting", 25),indicator=0,variable=user_name_select_for_view_students_admin_var,value=i[2],width=50,bg='cyan',padx=10,anchor='w').pack()


#*************************************************************************************************************************************************************************************

def librarymanag_from_student_info_admin_tk():
    global librarymang_home_page_admin_root
    students_info_admin_tk_page_root.destroy()

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)





def librarymanag_from_student_info_admin():
    global librarymang_home_page_admin_root
    students_info_admin_page_root.destroy()

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)




def librarymang_home_page_admin_from_view_books_admin_tkinter_info_page():
    global librarymang_home_page_admin_root
    view_books_info_admin_page_root.destroy()

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)

def librarymanag_from_view_books_admin():
    global librarymang_home_page_admin_root
    view_books_admin_page_root.destroy()

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)


def librarymanag_from_update_verification():
    global librarymang_home_page_admin_root
    book_update_verification_tkinter_page_root.destroy()

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)


def librarymanag_from_update_search_page():
    global librarymang_home_page_admin_root
    update_books_admin_page_root.destroy()

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)






def librarymang_home_page_admin():
    global librarymang_home_page_admin_root
    login_screen.destroy()

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)


def librarymang_home_page_admin_after_adding():
    
    add_books_admin_page_root.destroy()

    global librarymang_home_page_admin_root

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)



def librarymang_home_page_admin_from_deleting_confirmation_page():
    
    book_delete_verification_tkinter_page_root.destroy()

    global librarymang_home_page_admin_root

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)


def librarymang_home_page_admin_from_book_selecting_from_delete_page():
    
    delete_books_admin_page_root.destroy()

    global librarymang_home_page_admin_root

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)



def librarymang_home_page_admin_after_profile():
    
    profile_admin_root.destroy()

    global librarymang_home_page_admin_root

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)

def librarymang_home_page_admin_after_profile_updation():
    
    profile_admin_root_edit.destroy()

    global librarymang_home_page_admin_root

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)



#***************************************************************************************************************************************************************************************************



def profile_page_admin():
    global profile_admin_root
    librarymang_home_page_admin_root.destroy()
    profile_admin_root=Tk()
    profile_admin_root.title("Profile")
    profile_admin_root.state("zoomed")
    profile_admin_root.config(background = "black", pady=10)
    Label(profile_admin_root, text="Profile",width=100, font=("freestyle script", 70)).pack()
    Label(profile_admin_root,text="Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(profile_admin_root,text="Username:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(profile_admin_root,text="Email-Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=350)
    Label(profile_admin_root,text="Gender:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=350)
    Label(profile_admin_root,text="Country:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=600)
    Label(profile_admin_root,text="Account Type:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=600)



    Label(profile_admin_root,text=user_name,font=("verdana", 20),width=30,anchor='w').place(x=250,y=150)
    Label(profile_admin_root,text=user_username,font=("verdana", 20),width=20,anchor='w').place(x=1225,y=150)
    Label(profile_admin_root,text=user_email_id,font=("verdana", 20),width=30,anchor='w').place(x=310,y=350)
    Label(profile_admin_root,text=user_gender,font=("verdana", 20),width=20,anchor='w').place(x=1185,y=350)
    Label(profile_admin_root,text=user_country,font=("verdana", 20),width=20,anchor='w').place(x=300,y=600)
    Label(profile_admin_root,text=user_account,font=("verdana", 20),width=20,anchor='w').place(x=1300,y=600)

    Button(profile_admin_root,text='Edit',font=('verdana',25),cursor='hand2',bg='green',width=10,command=profile_page_admin_edit).place(x=850,y=800)
    Button(profile_admin_root,text='Go Back',font=('verdana',25),cursor='hand2',width=10,command=librarymang_home_page_admin_after_profile).place(x=500,y=800)
    Button(profile_admin_root,text='Log Out',font=('verdana',25),cursor='hand2',bg='red',width=10,command=log_out_from_profile_admin).place(x=1200,y=800)
    photo = PhotoImage(file = "e.png")
    profile_admin_root.iconphoto(False, photo)

def profile_page_admin_edit():
    global profile_admin_root_edit
    global edit_profile_first_name_var
    global edit_profile_last_name_var
    global edit_profile_username_var
    global edit_profile_gender_var
    global edit_profile_country_var
    global edit_profile_phone_no_var
    if user_phone_no==None:
        phoneno=''
    else:
        phoneno=str(user_phone_no)
    profile_admin_root.destroy()
    profile_admin_root_edit=Tk()
    profile_admin_root_edit.title("Login")
    profile_admin_root_edit.state("zoomed")
    profile_admin_root_edit.config(background = "black", pady=10)
    Label(profile_admin_root_edit, text="Profile",width=100, font=("freestyle script", 70)).pack()
    Label(profile_admin_root_edit,text="First Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(profile_admin_root_edit,text="Last Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(profile_admin_root_edit,text="Username:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=350)
    Label(profile_admin_root_edit,text="Email-Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=350)
    Label(profile_admin_root_edit,text="Gender:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=600)
    Label(profile_admin_root_edit,text="Country:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=600)
    Label(profile_admin_root_edit,text="Phone No:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=850)

    edit_profile_first_name_var=StringVar()
    edit_profile_last_name_var=StringVar()
    edit_profile_username_var=StringVar()
    edit_profile_gender_var=StringVar()
    edit_profile_country_var=StringVar()
    edit_profile_phone_no_var=StringVar()

    edit_profile_first_name_var.set(user_first_name)
    edit_profile_last_name_var.set(user_last_name)
    edit_profile_username_var.set(user_username)
    edit_profile_gender_var.set(user_gender)
    edit_profile_country_var.set(user_country)
    edit_profile_phone_no_var.set(phoneno)


    e1=Entry(profile_admin_root_edit,textvariable=edit_profile_first_name_var,font=("verdana", 20),width=30)
    e2=Entry(profile_admin_root_edit,textvariable=edit_profile_last_name_var,font=("verdana", 20),width=20)
    e3=Entry(profile_admin_root_edit,textvariable=edit_profile_username_var,font=("verdana", 20),width=20)
    e4=Label(profile_admin_root_edit,text=user_email_id,font=("verdana", 20),width=30,anchor='w')

    edit_profile_gender_list=[ 'male','female']
    edit_profile_gender_droplist=OptionMenu(profile_admin_root_edit, edit_profile_gender_var, *edit_profile_gender_list)
    edit_profile_gender_droplist.config(font=("verdana", 20),width=20)

    edit_profile_country_list=[ 'India' ,'US' , 'UK' ,'Australia' ,'Canada']
    edit_profile_country_droplist=OptionMenu(profile_admin_root_edit, edit_profile_country_var, *edit_profile_country_list)
    edit_profile_country_droplist.config(font=("verdana", 20),width=20)
    edit_profile_country_droplist.place(x=1250,y=250)

    e7=Entry(profile_admin_root_edit,textvariable=edit_profile_phone_no_var,font=("verdana", 20),width=20)

    e1.place(x=350,y=150)
    e2.place(x=1235,y=150)
    e3.place(x=350,y=350)
    e4.place(x=1245,y=350)
    edit_profile_gender_droplist.place(x=300,y=600)
    edit_profile_country_droplist.place(x=1200,y=600)
    e7.place(x=310,y=850)

    Button(profile_admin_root_edit,text='Edit',font=('verdana',25),cursor='hand2',bg='green',width=10,command=check_edit_profile_info_admin).place(x=1350,y=750)
    Button(profile_admin_root_edit,text='Go Back',font=('verdana',25),cursor='hand2',width=10,command=librarymang_home_page_admin_after_profile_updation).place(x=1350,y=900)
    photo = PhotoImage(file = "e.png")
    profile_admin_root_edit.iconphoto(False, photo)



def check_edit_profile_info_admin():
    edit_profile_first_name=edit_profile_first_name_var.get()
    edit_profile_last_name=edit_profile_last_name_var.get()
    edit_profile_username=edit_profile_username_var.get()
    edit_profile_gender=edit_profile_gender_var.get()
    edit_profile_country=edit_profile_country_var.get()
    edit_profile_phone_no=edit_profile_phone_no_var.get()
    ref_for_edit_verify=0
    query_edit_info="select username from logindata where emailid!='{0}';"      #We are creating 2 lists of already eisting username and emails from testlogin
    cursor_mysql.execute(query_edit_info.format(user_email_id))
    output1=cursor_mysql.fetchall()
    list_of_usernames=[]
    for username_tuple in output1:
        list_of_usernames.append(username_tuple[0])
    if ref_for_edit_verify==0:
        if edit_profile_username=='' and ref_for_edit_verify==0:
            messagebox.showerror('username error','please enter username')
            ref_for_edit_verify=2
        elif len(edit_profile_username)<6 and len(edit_profile_username)>=20 and ref_for_edit_verify==0:
            messagebox.showerror('username error','username must have atleast 6 char')
            ref_for_edit_verify=2
        elif edit_profile_username[0].isdigit() and ref_for_edit_verify==0:
            messagebox.showerror('username error','username cant start with numbers')
            ref_for_edit_verify=2
        elif edit_profile_username in list_of_usernames:   #checking for duplicates of username
            messagebox.showerror('username error','Username is taken')
            ref_for_edit_verify=2
        else:
            pass
    
    if ref_for_edit_verify==0:
        if edit_profile_phone_no=='':
            pass
        elif not edit_profile_phone_no.isdigit():
            messagebox.showerror('phone no','invaid phone no')
            ref_for_edit_verify=4
        elif len(str(edit_profile_phone_no))!=10:
            messagebox.showerror('phone no','invaid phone no')
            ref_for_edit_verify=4
        else:
            pass
    else:
        pass
    if len(edit_profile_first_name)==0 and ref_for_edit_verify==0:
        messagebox.showerror('error','please enter name')
        ref_for_edit_verify=5
    elif len(edit_profile_last_name)==0 and ref_for_edit_verify==0:
        messagebox.showerror('error','please enter last name')
        ref_for_edit_verify=5
    elif len(edit_profile_first_name)>20 and ref_for_edit_verify==0:
        messagebox.showerror('error','name should be less than 21 charcters')
        ref_for_edit_verify=5
    elif len(edit_profile_last_name)>20 and ref_for_edit_verify==0:
        messagebox.showerror('error','last name should be less than 21 charcters')
        ref_for_edit_verify=5
    else:
        pass

    if edit_profile_gender=='' and ref_for_edit_verify==0:
        messagebox.showerror('error','please enter your gender')
        ref_for_edit_verify=6
    elif edit_profile_gender not in ['male','female']:
        messagebox.showerror('error','please enter your gender')
        ref_for_edit_verify=6
    else:
        pass
    if ref_for_edit_verify==0 and edit_profile_country=='':
        messagebox.showerror('error','please enter country')
        ref_for_edit_verify=7
    elif ref_for_edit_verify==0 and (edit_profile_country not in [ 'India' ,'US' , 'UK' ,'Australia' ,'Canada']):
        messagebox.showerror('error','cant verify your country')
        ref_for_edit_verify=7
    else:
        pass


    if (('\'' in edit_profile_username) or ('\"' in edit_profile_username) or ('\'' in edit_profile_first_name) or ('\"' in edit_profile_first_name) or ('\'' in edit_profile_last_name) or ('\"' in edit_profile_last_name)) and  ref_for_edit_verify==0:
        messagebox.showinfo('error','Dnot use \' or \" in any field')
        ref_for_edit_verify=9
    if ref_for_edit_verify==0:
        updating_profile_admin(edit_profile_username,edit_profile_phone_no,edit_profile_first_name,edit_profile_last_name,edit_profile_gender,edit_profile_country)  # True and False returned is just for reference. In the main program define a global variable using 'global' and assign true and false to that. if the variable is true follow on with the sign up and then break out of while loop int new page but if false reload page using while loop.
    else:
        pass

def updating_profile_admin(username,phoneno,firstname,lastname,gender,country):
    global user_username
    global user_name
    global user_gender
    global user_phone_no
    global user_first_name
    global user_last_name
    global user_country 
    try:
        if phoneno=='':
            query1="update logindata set username='{0}',phoneno=Null,firstname='{1}',lastname='{2}',gender='{3}',country='{4}' where emailid='{5}';"
            query2="update loginissue set username='{0}' where username='{1}';"
            query3="update bookissue set username='{0}' where username='{1}';"
            cursor_mysql.execute(query1.format(username,firstname,lastname,gender,country,user_email_id))
            mycon.commit()
            a=2
            cursor_mysql.execute(query2.format(username,user_username))
            mycon.commit()
            a=3
            cursor_mysql.execute(query3.format(username,user_username))
            mycon.commit()
        else:
            query1="update logindata set username='{0}',phoneno='{1}',firstname='{2}',lastname='{3}',gender='{4}',country='{5}' where emailid='{6}';"
            query2="update loginissue set username='{0}' where username='{1}';"
            query3="update bookissue set username='{0}' where username='{1}';"
            cursor_mysql.execute(query1.format(username,phoneno,firstname,lastname,gender,country,user_email_id))
            mycon.commit()
            a=2
            cursor_mysql.execute(query2.format(username,user_username))
            mycon.commit()
            a=3
            cursor_mysql.execute(query3.format(username,user_username))
            mycon.commit()
        ref=1
    except:
        messagebox.showinfo('oops','something went wrong')
        ref=2
        librarymang_home_page_admin_after_profile_updation()
    if ref==1:
        messagebox.showinfo('success','Profile Updated')

        user_username=username
        user_name=firstname+' '+lastname
        user_gender=gender
        user_phone_no=phoneno
        user_first_name=firstname
        user_last_name=lastname
        user_country=country
        librarymang_home_page_admin_after_profile_updation()









def log_out_from_profile_admin():
    global user_email_id
    global user_name
    global user_username           
    global user_gender
    global user_phone_no
    global user_country
    global user_account
    user_email_id=''
    user_name=''
    user_username=''
    user_phone_no=None
    user_gender=''
    user_country=''
    user_account=''
    profile_admin_root.destroy()
    login_screen_from_student_profile()









#***********************************************************************************************************************************************************************************





def clear_frame(frame):
    frame.destroy()



def email_verification_send_mail(email_to_be_verified):
    global OTP_generated
    OTP_gen=random.randint(100000,999999)
    OTP_generated=str(OTP_gen)
    email=os.environ.get('project_email')
    passkey=os.environ.get('project_email_password')
    msg_OTP_verify=MIMEText(str(OTP_gen))

    msg_OTP_verify['Subject']='OTP'
    msg_OTP_verify['From']=email
    msg_OTP_verify['To']=email_to_be_verified

    with smtplib.SMTP('smtp.gmail.com','587') as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email,passkey)
        smtp.sendmail(email,email_to_be_verified,msg_OTP_verify.as_string())

def email_verification():
    OTP_GENERATED=OTP_GENerated.get()
    if OTP_GENERATED==OTP_generated:
        After_verify_new_password_page()
    else:
        messagebox.showerror('OTP','Incorrect OTP')


def sending_the_mailFn():
    try:
        global reg_email_id_verification_variable_73746
        email_verification_send_mail(reg_email_id_verification_variable_73746)
        forgot_password_page()
    except Exception as e:
        newe=str(e)
        if newe=='[Errno 11001] getaddrinfo failed':
            messagebox.showinfo('no internet','Please connect to the internet')
        else:
            messagebox.showerror('error','invalid email id')

def forgot_password_page():
    email_for_email_verification_root.destroy()
    global OTP_GENERATED
    global forgot_password_root
    global OTP_GENerated
    forgot_password_root=Tk()
    forgot_password_root.title('email verification')
    forgot_password_root.state("zoomed")
    forgot_password_root.config(bg='black',)
    OTP_GENerated=StringVar()
    Label(forgot_password_root, text="Email Verification",width=100, font=("freestyle script", 70)).pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root, text="Enter the 'One Time Password' sent to your registered emailid", fg='white',bg='black',font=('verdana',20)).pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    
    otp_gen=Entry(forgot_password_root, textvariable=OTP_GENerated, font=("verdana", 20),width=30)
    otp_gen.pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Button(forgot_password_root, text="Verify OTP", width=14, height=1, font=("Helvetica 10 underline",15),cursor='hand2', command=email_verification).pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Button(forgot_password_root, text="Cancel", width=14, height=1, font=("Helvetica 10 underline",15),cursor='hand2', command=login_screen_after_cancel_from_otp_verification_forget_password).pack()
    photo = PhotoImage(file = "e.png")
    forgot_password_root.iconphoto(False, photo)

def checking_whether_mail_in_database():
    global reg_email_id_verification_variable_73746
    global emailid_for_verification_12645
    reg_email_id_verification_variable_73746=emailid_for_verification_12645.get()
    query_for_email_verification='select emailid from logindata;'
    cursor_mysql.execute(query_for_email_verification)
    output_for_email_verification=cursor_mysql.fetchall()
    count_for_verify=0
    for email_for_verify in output_for_email_verification:
        if email_for_verify[0]==reg_email_id_verification_variable_73746:
            count_for_verify=1
            break
        else:
            continue
    if count_for_verify==1:
        sending_the_mailFn()
    else:
        messagebox.showerror('Email','Cant find registered email id')

def email_for_email_verification_page():
    global reg_email_id_verification_variable_73746
    global emailid_for_verification_12645
    global email_for_email_verification_root
    login_screen.destroy()
    email_for_email_verification_root=Tk()
    email_for_email_verification_root.title('Email Verification')
    email_for_email_verification_root.state('zoomed')
    email_for_email_verification_root.config(background = "black", pady=10)
    emailid_for_verification_12645=StringVar()
    Label(email_for_email_verification_root, text="Email Verification",width=100, font=("freestyle script", 70)).pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root, text="Enter your registered email-id:", fg='white',bg='black',font=('verdana',20)).pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    reg_emai_id_entry=Entry(email_for_email_verification_root, textvariable=emailid_for_verification_12645, font=("verdana", 20),width=30)
    reg_emai_id_entry.pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Button(email_for_email_verification_root, text="Verify Email", width=14, height=1, font=("Helvetica 10 underline",15),cursor='hand2', command=checking_whether_mail_in_database).pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Button(email_for_email_verification_root, text="Go Back", width=14, height=1, font=("Helvetica 10 underline",15),cursor='hand2', command=login_screen_after_cancel_from_emial_verification_forget_password).pack()
    photo = PhotoImage(file = "e.png")
    email_for_email_verification_root.iconphoto(False, photo)

def new_password_verification_through_python():
    global reg_email_id_verification_variable_73746
    global new_password_for_After_verify_new_password_page
    global confirm_password_for_After_verify_new_password_page
    ref_for_new_password_verification_through_python=0
    new_password_for_After_verify_new_password_page=new_password_for_After_verify_new_password_page_var.get()
    confirm_password_for_After_verify_new_password_page=confirm_password_for_After_verify_new_password_page_var.get()
    if len(new_password_for_After_verify_new_password_page)==0:
        messagebox.showerror('password error','please enter password')
        ref_for_new_password_verification_through_python=1
    elif len(confirm_password_for_After_verify_new_password_page)==0:
        messagebox.showerror('password error','please enter password')
        ref_for_new_password_verification_through_python=1
    elif new_password_for_After_verify_new_password_page!=confirm_password_for_After_verify_new_password_page:
        messagebox.showerror('password error','Password do not match')
        ref_for_new_password_verification_through_python=1
    elif len(new_password_for_After_verify_new_password_page)<8:
        messagebox.showerror('password error','password should be more than 8 characters')
        ref_for_new_password_verification_through_python=1
    elif len(new_password_for_After_verify_new_password_page)>35:
        messagebox.showerror('password error','password should be less than or equal to 35 characters')
        ref_for_new_password_verification_through_python=1
    elif True:
        upper=0
        lower=0
        special=0
        for element_pass_signup in new_password_for_After_verify_new_password_page:
            if element_pass_signup.isupper():
                upper+=1
            elif element_pass_signup.islower():
                lower+=1
            elif element_pass_signup in '!@#$%^&*+-_=~/':
                special+=1
            else:
                pass
        if (upper>0) and (lower>0) and (special>0):
            pass
        elif upper==0:
            messagebox.showerror('password error','password should have atleast 1 upper case character')
            ref_for_new_password_verification_through_python=1
        elif lower==0:
            messagebox.showerror('password error','password should have atleast 1 lower case character')
            ref_for_new_password_verification_through_python=1
        else:
            messagebox.showerror('password error',"password must have atleast 1 special character - '!@#$%^&*+-_=~/'")
            ref_for_new_password_verification_through_python=1

    if (('\'' in new_password_for_After_verify_new_password_page) or ('\"' in new_password_for_After_verify_new_password_page)) and ref_for_new_password_verification_through_python==0:
        messagebox.showinfo('error','There should be no \' or \" in any of the fields')
        ref_for_new_password_verification_through_python=2
    else:
        pass
    if ref_for_new_password_verification_through_python==0:
        query_for_new_password_verification_through_python="update logindata set password='{0}' where emailid='{1}';"
        cursor_mysql.execute(query_for_new_password_verification_through_python.format(new_password_for_After_verify_new_password_page,reg_email_id_verification_variable_73746))
        mycon.commit()
        messagebox.showinfo('password',"Password Succesfully Changed")
        login_screen_after_changing_password_forgot_password()
    else:
        pass


def After_verify_new_password_page():
    forgot_password_root.destroy()
    global After_verify_new_password_page_root
    global new_password_for_After_verify_new_password_page_var
    global confirm_password_for_After_verify_new_password_page_var
    After_verify_new_password_page_root=Tk()
    After_verify_new_password_page_root.title('hello')
    After_verify_new_password_page_root.state("zoomed")
    After_verify_new_password_page_root.config(background='black',pady=10)
    new_password_for_After_verify_new_password_page_var=StringVar()
    confirm_password_for_After_verify_new_password_page_var=StringVar()
    Label(After_verify_new_password_page_root, text="New Password",width=100, font=("freestyle script", 70)).pack()
    Label(After_verify_new_password_page_root,bg='black').pack()
    Label(After_verify_new_password_page_root,bg='black').pack()
    Label(After_verify_new_password_page_root,bg='black').pack()
    Label(After_verify_new_password_page_root,bg='black').pack()
    Label(After_verify_new_password_page_root,text='New password',font=('verdana',20),width=20,pady=5).place(x=450,y=300)
    Entry(After_verify_new_password_page_root,font=('verdana',25),textvariable=new_password_for_After_verify_new_password_page_var,show='*').place(x=950,y=300)
    Label(After_verify_new_password_page_root,text='Confirm Password',font=('verdana',20),width=20,pady=5).place(x=450,y=600)
    Entry(After_verify_new_password_page_root,font=('verdana',25),textvariable=confirm_password_for_After_verify_new_password_page_var,show='*').place(x=950,y=600)
    Button(After_verify_new_password_page_root,text='Submit',width=15,font=('verdana',15),cursor='hand2',command=new_password_verification_through_python).place(x=850,y=800)
    photo = PhotoImage(file = "e.png")
    After_verify_new_password_page_root.iconphoto(False, photo)


def login_success_and_creating_user_variables():
    global user_email_id
    global user_name
    global user_username 
    global user_gender
    global user_phone_no
    global user_country
    global user_account
    global user_first_name
    global user_last_name

    user_email_id=reg_email_id

    query='''select username,phoneno,firstname,lastname,gender,country,accountype from logindata where emailid="{0}";'''
    cursor_mysql.execute(query.format(user_email_id))
    output=cursor_mysql.fetchall()
    user_first_name=output[0][2]
    user_last_name=output[0][3]
    user_email_id=reg_email_id
    user_username=output[0][0]
    user_name=output[0][2]+' '+output[0][3]
    user_gender=output[0][4]
    user_country=output[0][5]
    user_account=output[0][6]
    if output[0][1]==None:
        user_phone_no=None
    else:
        user_phone_no=output[0][1]

    admin_or_student_page_chooser_fn()





def admin_or_student_page_chooser_fn():
    global user_account

    if user_account=='Student':
        librarymang_home_page_student()

    else:
        librarymang_home_page_admin()



def login_verification():
    global reg_email_id
    reg_email_id=reg_email_id_tk.get()
    reg_password=reg_password_tk.get()
    query_login="select emailid,password from logindata;"
    cursor_mysql.execute(query_login)
    out=cursor_mysql.fetchall()
    count=0
    for tup in out:
        if tup[0]==reg_email_id:   # note : count of each email id in a table is 1 because it is a primary key and google does not accept different email ids   so no needto check for duplicates.
            if tup[1]==reg_password:
                retvalue='success'
                bool_val=True
                break
                #break and go to next page

            else:
                retvalue='password incorrect'
                bool_val=False
                break
                #break and reload page by while loop in main program
        else:
            continue
    else:
        if count==0: #count=0 is a false condition because there is 3 cases i)emailfound,passkey correct then program brakes and goes to next page  ii)email found passcode incorrect terminates the loop (does not read the else of for-else) and refreshes page iii)email not found so count is 0 and unnaffected so it displays emailnot found and automatically comes out of the loop (using for-else) and when page is refreshed using while loop.
            retvalue='Registered email id not found'
            bool_val=False
    if reg_email_id=='':
        messagebox.showerror('email missing','please enter email id')
    elif reg_password=='':
        messagebox.showerror('password missing','please enter password')
    elif bool_val==True:
        login_success_and_creating_user_variables()
    else:
        if retvalue=='Registered email id not found':
            messagebox.showerror('email missing','Registered email id not found')
        else:
            messagebox.showerror('password','Password Incorrect')

def login_screen():
    clear_frame(main_page) # clears the mainpage
    global reg_email_id_tk
    global reg_password_tk
    global login_screen
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.state("zoomed")
    login_screen.config(background = "black", pady=10)
    reg_email_id_tk=StringVar()
    reg_password_tk=StringVar()
    Label(login_screen, text="Please enter login details:",width=50, font=("freestyle script", 100)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="Registered email-ID:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    emailid_login_entry = Entry(login_screen, textvariable=reg_email_id_tk,width=30,font=("verdana",15))
    emailid_login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="Password:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    password__login_entry = Entry(login_screen, textvariable=reg_password_tk, show= '*',width=30,font=("verdana",15))
    password__login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="Forgot password", width=14, height=1, font=("Helvetica 10 underline",15),bg='black',fg='white',bd=0,cursor='hand2',command=email_for_email_verification_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Button(login_screen, text='Create an Account',width=20,bg='black',fg='white',bd=0,cursor='hand2',font=('helvetica 8 underline' , 12),command=sign_up_from_login_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="submit", width=20,cursor='hand2', height=2,command=login_verification).pack()
    photo = PhotoImage(file = "e.png")
    login_screen.iconphoto(False, photo)


def login_screen_after_cancel_from_otp_verification_forget_password():
    forgot_password_root.destroy() # clears the mainpage
    global reg_email_id_tk
    global reg_password_tk
    global login_screen
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.state("zoomed")
    login_screen.config(background = "black", pady=10)
    reg_email_id_tk=StringVar()
    reg_password_tk=StringVar()
    Label(login_screen, text="Please enter login details:",width=50, font=("freestyle script", 100)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="Registered email-ID:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    emailid_login_entry = Entry(login_screen, textvariable=reg_email_id_tk,width=30,font=("verdana",15))
    emailid_login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="Password:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    password__login_entry = Entry(login_screen, textvariable=reg_password_tk, show= '*',width=30,font=("verdana",15))
    password__login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="Forgot password", width=14, height=1, font=("Helvetica 10 underline",15),bg='black',fg='white',bd=0,cursor='hand2',command=email_for_email_verification_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Button(login_screen, text='Create an Account',width=20,bg='black',fg='white',bd=0,cursor='hand2',font=('helvetica 8 underline' , 12),command=sign_up_from_login_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="submit", width=20,cursor='hand2', height=2,command=login_verification).pack()
    photo = PhotoImage(file = "e.png")
    login_screen.iconphoto(False, photo)




def login_screen_after_cancel_from_emial_verification_forget_password():
    email_for_email_verification_root.destroy() # clears the mainpage
    global reg_email_id_tk
    global reg_password_tk
    global login_screen
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.state("zoomed")
    login_screen.config(background = "black", pady=10)
    reg_email_id_tk=StringVar()
    reg_password_tk=StringVar()
    Label(login_screen, text="Please enter login details:",width=50, font=("freestyle script", 100)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="Registered email-ID:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    emailid_login_entry = Entry(login_screen, textvariable=reg_email_id_tk,width=30,font=("verdana",15))
    emailid_login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="Password:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    password__login_entry = Entry(login_screen, textvariable=reg_password_tk, show= '*',width=30,font=("verdana",15))
    password__login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="Forgot password", width=14, height=1, font=("Helvetica 10 underline",15),bg='black',fg='white',bd=0,cursor='hand2',command=email_for_email_verification_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Button(login_screen, text='Create an Account',width=20,bg='black',fg='white',bd=0,cursor='hand2',font=('helvetica 8 underline' , 12),command=sign_up_from_login_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="submit", width=20,cursor='hand2', height=2,command=login_verification).pack()
    photo = PhotoImage(file = "e.png")
    login_screen.iconphoto(False, photo)


def login_screen_from_student_profile():
    #lib.destroy() # clears the mainpage
    global reg_email_id_tk
    global reg_password_tk
    global login_screen
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.state("zoomed")
    login_screen.config(background = "black", pady=10)
    reg_email_id_tk=StringVar()
    reg_password_tk=StringVar()
    Label(login_screen, text="Please enter login details:",width=50, font=("freestyle script", 100)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="Registered email-ID:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    emailid_login_entry = Entry(login_screen, textvariable=reg_email_id_tk,width=30,font=("verdana",15))
    emailid_login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="Password:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    password__login_entry = Entry(login_screen, textvariable=reg_password_tk, show= '*',width=30,font=("verdana",15))
    password__login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="Forgot password", width=14, height=1, font=("Helvetica 10 underline",15),bg='black',fg='white',bd=0,cursor='hand2',command=email_for_email_verification_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Button(login_screen, text='Create an Account',width=20,bg='black',fg='white',bd=0,cursor='hand2',font=('helvetica 8 underline' , 12),command=sign_up_from_login_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="submit", width=20,cursor='hand2', height=2,command=login_verification).pack()
    photo = PhotoImage(file = "e.png")
    login_screen.iconphoto(False, photo)





def login_screen_after_changing_password_forgot_password():
    global After_verify_new_password_page_root
    global reg_email_id_tk
    global reg_password_tk
    global login_screen
    After_verify_new_password_page_root.destroy()
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.state("zoomed")
    login_screen.config(background = "black", pady=10)
    reg_email_id_tk=StringVar()
    reg_password_tk=StringVar()
    Label(login_screen, text="Please enter login details:",width=50, font=("freestyle script", 100)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="Registered email-ID:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    emailid_login_entry = Entry(login_screen, textvariable=reg_email_id_tk,width=30,font=("verdana",15))
    emailid_login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="Password:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    password__login_entry = Entry(login_screen, textvariable=reg_password_tk, show= '*',width=30,font=("verdana",15))
    password__login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="Forgot password", width=14, height=1, font=("Helvetica 10 underline",15),bg='black',fg='white',bd=0,cursor='hand2',command=email_for_email_verification_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Button(login_screen, text='Create an Account',width=20,bg='black',fg='white',bd=0,cursor='hand2',font=('helvetica 8 underline' , 12),command=sign_up_from_login_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="submit", width=20,cursor='hand2', height=2,command=login_verification).pack()
    photo = PhotoImage(file = "e.png")
    login_screen.iconphoto(False, photo)






def login_screen_after_sign_up():
    #clear_frame(main_page) # clears the mainpage
    after_root_sign_up.destroy()
    global reg_email_id_tk
    global reg_password_tk
    global login_screen
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.state("zoomed")
    login_screen.config(background = "black", pady=10)
    reg_email_id_tk=StringVar()
    reg_password_tk=StringVar()
    Label(login_screen, text="Please enter login details:",width=50, font=("freestyle script", 100)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="Registered email-ID:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    emailid_login_entry = Entry(login_screen, textvariable=reg_email_id_tk,width=30,font=("verdana",15))
    emailid_login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="Password:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    password__login_entry = Entry(login_screen, textvariable=reg_password_tk, show= '*',width=30,font=("verdana",15))
    password__login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="Forgot password", width=14, height=1, font=("Helvetica 10 underline",15),bg='black',fg='white',bd=0,cursor='hand2',command=email_for_email_verification_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Button(login_screen, text='Create an Account',width=20,bg='black',fg='white',bd=0,cursor='hand2',font=('helvetica 8 underline' , 12),command=sign_up_from_login_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="submit", width=20,cursor='hand2', height=2,command=login_verification).pack()
    photo = PhotoImage(file = "e.png")
    login_screen.iconphoto(False, photo)

def login_screen_from_sign_up():
    #clear_frame(main_page) # clears the mainpage
    sign_up_page_root.destroy()
    global reg_email_id_tk
    global reg_password_tk
    global login_screen
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.state("zoomed")
    login_screen.config(background = "black", pady=10)
    reg_email_id_tk=StringVar()
    reg_password_tk=StringVar()
    Label(login_screen, text="Please enter login details:",width=50, font=("freestyle script", 100)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="Registered email-ID:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    emailid_login_entry = Entry(login_screen, textvariable=reg_email_id_tk,width=30,font=("verdana",15))
    emailid_login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="Password:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    password__login_entry = Entry(login_screen, textvariable=reg_password_tk, show= '*',width=30,font=("verdana",15))
    password__login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="Forgot password", width=14, height=1, font=("Helvetica 10 underline",15),bg='black',fg='white',bd=0,cursor='hand2',command=email_for_email_verification_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Button(login_screen, text='Create an Account',width=20,bg='black',fg='white',bd=0,cursor='hand2',font=('helvetica 8 underline' , 12),command=sign_up_from_login_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="submit", width=20,cursor='hand2', height=2,command=login_verification).pack()
    photo = PhotoImage(file = "e.png")
    login_screen.iconphoto(False, photo)



def email_verification_send_mail_for_sign_up(email_to_be_verified):
    global OTP_generated_sign_up
    OTP_gen_sign_up=random.randint(100000,999999)
    OTP_generated_sign_up=str(OTP_gen_sign_up)
    email=os.environ.get('project_email')
    passkey=os.environ.get('project_email_password')
    msg_OTP_verify_for_signup=MIMEText(str(OTP_generated_sign_up))

    msg_OTP_verify_for_signup['Subject']='OTP'
    msg_OTP_verify_for_signup['From']=email
    msg_OTP_verify_for_signup['To']=email_to_be_verified

    with smtplib.SMTP('smtp.gmail.com','587') as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email,passkey)
        smtp.sendmail(email,email_to_be_verified,msg_OTP_verify_for_signup.as_string())
def After_verify_sign_up():
    global after_root_sign_up
    forgot_password_root_sign_up.destroy()
    after_root_sign_up=Tk()
    after_root_sign_up.title('hello')
    after_root_sign_up.state("zoomed")
    Label(after_root_sign_up, text="Register success",width=100, font=("freestyle script", 70)).pack()
    Label(after_root_sign_up).pack()
    Label(after_root_sign_up).pack()
    Label(after_root_sign_up).pack()
    Label(after_root_sign_up).pack()
    Label(after_root_sign_up).pack()
    Label(after_root_sign_up).pack()
    Label(after_root_sign_up).pack()
    Button(after_root_sign_up,text='Go to login Page',cursor='hand2',bg='black',font=('Comic Sans MS',20),fg='white',command=login_screen_after_sign_up).pack()
    photo = PhotoImage(file = "e.png")
    after_root_sign_up.iconphoto(False, photo)


def email_verification_sign_up():
    global first_name_sign_up
    global last_name_sign_up
    global username_sign_up
    global gender_sign_up
    global sign_up_country
    global email_id_sign_up
    global phone_no_sign_up
    global first_password_sign_up
    global confirm_password_sign_up
    global sign_up_account_type
    global real_account_type
    global real_gender
    OTP_GENERATED_sign_up=OTP_GENerated_sign_up.get()
    if OTP_GENERATED_sign_up==OTP_generated_sign_up:
        signup(email_id_sign_up,username_sign_up,first_password_sign_up,confirm_password_sign_up,first_name_sign_up,last_name_sign_up,real_gender,sign_up_country,real_account_type,phone_no_sign_up)
        After_verify_sign_up()
    else:
        messagebox.showerror('OTP','Incorrect OTP')

def midway_btw_forgot_password_page_for_sign_up_and_midfn():
    try:
        global email_id_sign_up
        email_verification_send_mail_for_sign_up(email_id_sign_up)
        forgot_password_page_for_sign_up()
    except Exception as e:
        newe=str(e)
        if newe=='[Errno 11001] getaddrinfo failed':
            messagebox.showinfo('no internet','Please connect to the internet')
        else:
            messagebox.showerror('error','invalid email id')


def forgot_password_page_for_sign_up():
    sign_up_page_root.destroy()
    global email_id_sign_up
    global OTP_GENERATED_sign_up
    global forgot_password_root_sign_up
    global OTP_GENerated_sign_up
    forgot_password_root_sign_up=Tk()
    forgot_password_root_sign_up.title('email verification')
    forgot_password_root_sign_up.state("zoomed")
    forgot_password_root_sign_up.config(bg='black',)
    OTP_GENerated_sign_up=StringVar()
    Label(forgot_password_root_sign_up, text="Email Verification",width=100, font=("freestyle script", 70)).pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up, text="Enter the 'One Time Password' sent to your registered emailid", fg='white',bg='black',font=('verdana',20)).pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    otp_gen=Entry(forgot_password_root_sign_up, textvariable=OTP_GENerated_sign_up, font=("verdana", 20),width=30)
    otp_gen.pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Button(forgot_password_root_sign_up, text="Verify OTP", width=14,cursor='hand2', height=1, font=("Helvetica 10 underline",15), command=email_verification_sign_up).pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Button(forgot_password_root_sign_up, text="Go Back", width=14,cursor='hand2', height=1, font=("Helvetica 10 underline",15), command=signup_page_from_email_verification_signup_fn).pack()
    photo = PhotoImage(file = "e.png")
    forgot_password_root_sign_up.iconphoto(False, photo)


def check_signup_info(reg_email_id_signup,username_signup,first_password_signup,confirm_password_signup,first_name_signup,last_name_signup,gender_sign_up,country_signup,account_type_signup,phone_signup_optional=0):
    
    query_signup_info="select username,emailid from logindata;"      #We are creating 2 lists of already eisting username and emails from logindata
    cursor_mysql.execute(query_signup_info)
    output1=cursor_mysql.fetchall()
    list_of_email_ids=[]
    list_of_usernames=[]
    for mail_username_tuple in output1:
        list_of_usernames.append(mail_username_tuple[0])
        list_of_email_ids.append(mail_username_tuple[1]) 
    ref_for_signup_verify=0   #ref is reference whether the sign up is true or false. In the end if ref is 0 then there is no problem with sign up. but if ref=1 there is a problem with email info. if ref is 2 at the end then there is a problem with username info. if ref=3 then problem with password info. if ref = 4 then problem with phone no.
    email_domain_list=reg_email_id_signup.split('@')  #for line 31
    if len(reg_email_id_signup)==0:
        ref_for_signup_verify=1
        messagebox.showerror('email missing','please enter email id')
    elif len(reg_email_id_signup)<6 and len(reg_email_id_signup)>=320:
        ref_for_signup_verify=1
        messagebox.showerror('email error','Invalid email id')#email length must be more than 6 char
    elif '@' not in reg_email_id_signup:   #email must have @
        messagebox.showerror('email error','Invalid email id')
        ref_for_signup_verify=1
    elif reg_email_id_signup.startswith('@'):     #cant start with @
        messagebox.showerror('email error','Invalid email id')
        ref_for_signup_verify_for_signup_verify=1
    elif not reg_email_id_signup.endswith('.com'):  # should end with .com
        messagebox.showerror('email error','Invalid email id')
        ref_for_signup_verify=1
    elif not reg_email_id_signup[0].isalnum():   #first char must be alphabet\numerical
        messagebox.showerror('email error','Invalid email id')
        ref_for_signup_verify=1
    elif reg_email_id_signup in list_of_email_ids:  # checking for duplicates of email
        messagebox.showinfo("email error", "Email already in use")
        ref_for_signup_verify=1
    elif True:
        alpha=0
        for z in range(len(email_domain_list)-1):    # after splitting the string into list the last element is the domain - gmail.com/outlook.com so dont consider that
            for email_element in email_domain_list[z]:
                if email_element.isalpha():    
                    alpha+=1
                else:
                    continue
        if alpha<1:
            messagebox.showerror('email error','Invalid email id')  #must have atleast 1 alphabet other than domain
            ref_for_signup_verify=1
        else:
            pass
    else:
        pass
    if ref_for_signup_verify==0:
        if username_signup=='' and ref_for_signup_verify==0:
            messagebox.showerror('username error','please enter username')
            ref_for_signup_verify=2
        elif len(username_signup)<6 or len(username_signup)>=20 and ref_for_signup_verify==0:
            messagebox.showerror('username error','username must be atleast 6 char and less than 21 charactes')
            ref_for_signup_verify=2
        elif username_signup[0].isdigit() and ref_for_signup_verify==0:
            messagebox.shoewrror('username error','username cant start with numbers')
            ref_for_signup_verify=2
        elif username_signup in list_of_usernames:   #checking for duplicates of username
            messagebox.showerror('username error','Username is taken')
            ref_for_signup_verify=2
        else:
            pass
    if ref_for_signup_verify==0:
        if len(first_password_signup)==0 and ref_for_signup_verify==0:
            messagebox.showerror('password error','please enter password')
            ref_for_signup_verify=3
        elif len(confirm_password_signup)==0 and ref_for_signup_verify==0:
            messagebox.showerror('password error','please enter password')
            ref_for_signup_verify=3
        elif first_password_signup!=confirm_password_signup and ref_for_signup_verify==0:
            messagebox.showerror('password error','Password do not match')
            ref_for_signup_verify=3
        elif len(first_password_signup)<8 and ref_for_signup_verify==0:
            messagebox.showerror('password error','password should be more than 8 characters')
            ref_for_signup_verify=3
        elif len(first_password_signup)>35 and ref_for_signup_verify==0:
            messagebox.showerror('password error','password should be less than or equal to 35 characters')
            ref_for_signup_verify=3
        elif ref_for_signup_verify==0:
            upper=0
            lower=0
            special=0
            for element_pass_signup in first_password_signup:
                if element_pass_signup.isupper():
                    upper+=1
                elif element_pass_signup.islower():
                    lower+=1
                elif element_pass_signup in '!@#$%^&*+-_=~/':
                    special+=1
                else:
                    pass
            if (upper>0) and (lower>0) and (special>0):
                pass
            elif upper==0:
                messagebox.showerror('password error','password should have atleast 1 upper case character')
                ref_for_signup_verify=3
            elif lower==0:
                messagebox.showerror('password error','password should have atleast 1 lower case character')
                ref_for_signup_verify=3
            else:
                messagebox.showerror('password error',"password must have atleast 1 special character - '!@#$%^&*+-_=~/'")
                ref_for_signup_verify=3
    if ref_for_signup_verify==0:
        if phone_signup_optional==0:
            pass
        elif not phone_signup_optional.isdigit():
            messagebox.showerror('phone no','invaid phone no')
            ref_for_signup_verify=4
        elif len(str(phone_signup_optional))!=10:
            messagebox.showerror('phone no','invaid phone no')
            ref_for_signup_verify=4
        else:
            pass
    else:
        pass
    if len(first_name_signup)==0 and ref_for_signup_verify==0:
        messagebox.showerror('error','please enter name')
        ref_for_signup_verify=5
    elif len(last_name_signup)==0 and ref_for_signup_verify==0:
        messagebox.showerror('error','please enter last name')
        ref_for_signup_verify=5
    elif len(first_name_signup)>20 and ref_for_signup_verify==0:
        messagebox.showerror('error','name should be less than 21 charcters')
        ref_for_signup_verify=5
    elif len(last_name_signup)>20 and ref_for_signup_verify==0:
        messagebox.showerror('error','last name should be less than 21 charcters')
        ref_for_signup_verify=5
    else:
        pass

    if gender_sign_up=='' and ref_for_signup_verify==0:
        messagebox.showerror('error','please enter your gender')
        ref_for_signup_verify=6
    else:
        pass
    if ref_for_signup_verify==0 and country_signup=='':
        messagebox.showerror('error','please enter country')
        ref_for_signup_verify=7
    elif ref_for_signup_verify==0 and (country_signup not in [ 'India' ,'US' , 'UK' ,'Australia' ,'Canada']):
        messagebox.showerror('error','cant verify your country')
        ref_for_signup_verify=7
    else:
        pass

    if ref_for_signup_verify==0 and account_type_signup=='':
        messagebox.showerror('error','please choose an account type')
        ref_for_signup_verify=8
    else: 
        pass

    if (('\'' in reg_email_id_signup) or ('\"' in reg_email_id_signup) or ('\'' in username_signup) or ('\"' in username_signup) or ('\'' in first_password_signup) or ('\"' in first_password_signup) or ('\'' in first_name_signup) or ('\"' in first_name_signup) or ('\'' in last_name_signup) or ('\"' in last_name_signup)) and  ref_for_signup_verify==0:
        messagebox.showinfo('error','Dnot use \' or \" in any field')
        ref_for_signup_verify=9
    if ref_for_signup_verify==0:
        midway_btw_forgot_password_page_for_sign_up_and_midfn()  # True and False returned is just for reference. In the main program define a global variable using 'global' and assign true and false to that. if the variable is true follow on with the sign up and then break out of while loop int new page but if false reload page using while loop.
    else:
        pass

def signup(reg_email_id_signup,username_signup,first_password_signup,confirm_password_signup,first_name_signup,last_name_signup,gender_sign_up,country_signup,account_type_signup,phone_signup_optional=0):
    global realphoneno
    global phone_no_sign_up
    
    
    if phone_signup_optional=='':

        #here email verification
        query_signup='''insert into logindata(username,emailid,password,firstname,lastname,gender,country,accountype) values("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}");'''
        cursor_mysql.execute(query_signup.format(username_signup,reg_email_id_signup,first_password_signup,first_name_signup,last_name_signup,gender_sign_up,country_signup,account_type_signup))
        mycon.commit()
        username=username_signup
        query_signup_2='''insert into loginissue(username) values("{0}");'''
        cursor_mysql.execute(query_signup_2.format(username))
        mycon.commit()
    else:
        #here email verification
        realphoneno=int(phone_signup_optional)
        query_signup='''insert into logindata(username,emailid,phoneno,password,firstname,lastname,gender,country,accountype) values("{0}","{1}",{2},"{3}","{4}","{5}","{6}","{7}","{8}");'''
        cursor_mysql.execute(query_signup.format(username_signup,reg_email_id_signup,realphoneno,first_password_signup,first_name_signup,last_name_signup,gender_sign_up,country_signup,account_type_signup,))
        mycon.commit()
        username=username_signup
        query_signup_2='''insert into loginissue(username) values("{0}");'''
        cursor_mysql.execute(query_signup_2.format(username))
        mycon.commit()

def midfn():
    global first_name_sign_up_var
    global last_name_sign_up_var
    global username_sign_up_var
    global gender_sign_up_var
    global sign_up_country_var
    global phone_no_sign_up_var
    global email_id_sign_up_var
    global first_password_sign_up_var
    global confirm_password_sign_up_var
    global sign_up_account_type_var
    
    global first_name_sign_up
    global last_name_sign_up
    global username_sign_up
    global gender_sign_up
    global sign_up_country
    global phone_no_sign_up
    global email_id_sign_up
    global first_password_sign_up
    global confirm_password_sign_up
    global sign_up_account_type
    global realphoneno
    global real_gender
    global real_account_type

    first_name_sign_up=first_name_sign_up_var.get()
    last_name_sign_up=last_name_sign_up_var.get()
    username_sign_up=username_sign_up_var.get()
    gender_sign_up=gender_sign_up_var.get()
    sign_up_country=sign_up_country_var.get()
    phone_no_sign_up=phone_no_sign_up_var.get()
    email_id_sign_up=email_id_sign_up_var.get()
    first_password_sign_up=first_password_sign_up_var.get()
    confirm_password_sign_up=confirm_password_sign_up_var.get()
    sign_up_account_type=sign_up_account_type_var.get()
    if gender_sign_up==1:
        real_gender='male'
    elif gender_sign_up==2:
        real_gender='female'
    else:
        real_gender=''
    if sign_up_account_type==1:
        real_account_type='Administrator'
    elif sign_up_account_type==2:
        real_account_type='Student'
    else:
        real_account_type=''
    if phone_no_sign_up=='':
        realphoneno=0
        check_signup_info(email_id_sign_up,username_sign_up,first_password_sign_up,confirm_password_sign_up,first_name_sign_up,last_name_sign_up,real_gender,sign_up_country,real_account_type)
    else:
        realphoneno=None
        check_signup_info(email_id_sign_up,username_sign_up,first_password_sign_up,confirm_password_sign_up,first_name_sign_up,last_name_sign_up,real_gender,sign_up_country,real_account_type,phone_no_sign_up)



def signup_page_fn():
    main_page.destroy()
    global first_name_sign_up_var
    global last_name_sign_up_var
    global username_sign_up_var
    global gender_sign_up_var
    global sign_up_country_var
    global phone_no_sign_up_var
    global email_id_sign_up_var
    global first_password_sign_up_var
    global confirm_password_sign_up_var
    global sign_up_account_type_var
    global sign_up_page_root

    sign_up_page_root = Tk()
    sign_up_page_root.state('zoomed')
    sign_up_page_root.title('Registration form')
    sign_up_page_root.config(background = "black", pady=10)

    first_name_sign_up_var=StringVar()
    last_name_sign_up_var=StringVar()
    username_sign_up_var=StringVar()
    phone_no_sign_up_var=StringVar()
    email_id_sign_up_var=StringVar()
    first_password_sign_up_var=StringVar()
    confirm_password_sign_up_var=StringVar()
    sign_up_account_type_var=IntVar()
    sign_up_country_var=StringVar()
    gender_sign_up_var=IntVar()


    sign_up_label_0 =Label(sign_up_page_root, text="Registeration Form",width=100, font=("freestyle script", 70)).pack()

    sign_up_label_1 =Label(sign_up_page_root,text="first name:", width=17,font=("lucida handwriting",13))
    sign_up_label_1.place(x=670,y=250)

    sign_up_entry_1=Entry(sign_up_page_root,textvariable=first_name_sign_up_var,font=('verdana',15))
    sign_up_entry_1.place(x=950,y=250)

    sign_up_label_3 =Label(sign_up_page_root,text="Last name", width=17,font=("lucida handwriting",13))
    sign_up_label_3.place(x=670,y=300)

    sign_up_entry_3=Entry(sign_up_page_root,textvariable=last_name_sign_up_var,font=('verdana',15))
    sign_up_entry_3.place(x=950,y=300)

    sign_up_label_11 =Label(sign_up_page_root,text="Username", width=17,font=("lucida handwriting",13))
    sign_up_label_11.place(x=670,y=350)

    sign_up_entry_11=Entry(sign_up_page_root,textvariable=username_sign_up_var,font=('verdana',15))
    sign_up_entry_11.place(x=950,y=350)

    sign_up_label_4 =Label(sign_up_page_root,text="Gender", width=17,font=("lucida handwriting",13))
    sign_up_label_4.place(x=670,y=400)

    Radiobutton(sign_up_page_root,text="Male",padx= 20, variable= gender_sign_up_var, value=1,font=('verdana',13)).place(x=950,y=400)
    Radiobutton(sign_up_page_root,text="Female",padx= 20, variable=gender_sign_up_var, value=2,font=('verdana',13)).place(x=1055,y=400)

    sign_up_label_5=Label(sign_up_page_root,text="Country",width=17,font=("lucida handwriting",13))
    sign_up_label_5.place(x=670,y=450)

    sign_up_list_of_country=[ 'India' ,'US' , 'UK' ,'Australia' ,'Canada']

    sign_up_droplist=OptionMenu(sign_up_page_root, sign_up_country_var, *sign_up_list_of_country)
    sign_up_droplist.config(width=20)
    sign_up_country_var.set('Select your Country')
    sign_up_droplist.place(x=950,y=450)

    sign_up_label_6=Label(sign_up_page_root,text="Phone no:(optional)",width=17,font=("lucida handwriting",13))
    sign_up_label_6.place(x=670,y=500)

    sign_up_entry_6=Entry(sign_up_page_root,textvariable=phone_no_sign_up_var,font=('verdana',15))
    sign_up_entry_6.place(x=950,y=500)

    sign_up_label_7=Label(sign_up_page_root,text="Email-ID:",width=17,font=("lucida handwriting",13))
    sign_up_label_7.place(x=670,y=550)

    sign_up_entry_7=Entry(sign_up_page_root,textvariable=email_id_sign_up_var,font=('verdana',15),width=30)
    sign_up_entry_7.place(x=950,y=550)

    sign_up_label_8=Label(sign_up_page_root,text="Password:",width=17,font=("lucida handwriting",13))
    sign_up_label_8.place(x=670,y=600)

    sign_up_entry_8=Entry(sign_up_page_root,textvariable=first_password_sign_up_var,font=('verdana',15),show='*')
    sign_up_entry_8.place(x=950,y=600)

    sign_up_label_9=Label(sign_up_page_root,text="Confirm password:",width=17,font=("lucida handwriting",13))
    sign_up_label_9.place(x=670,y=650)

    sign_up_entry_9=Entry(sign_up_page_root,textvariable=confirm_password_sign_up_var,font=('verdana',15),show='*')
    sign_up_entry_9.place(x=950,y=650)

    sign_up_label_10=Label(sign_up_page_root,text="Account type:",width=17,font=("lucida handwriting",13))
    sign_up_label_10.place(x=670,y=700)


    Radiobutton(sign_up_page_root,text="administrator",padx= 10,variable= sign_up_account_type_var, value=1,font=('verdana',14)).place(x=950,y=700)
    Radiobutton(sign_up_page_root,text="student",padx= 10, variable= sign_up_account_type_var, value=2,font=('verdana',14)).place(x=1125,y=700)

    Button(sign_up_page_root, text='Already have an account',width=20,cursor='hand2',bg='black',fg='white',bd=0,font=('helvetica 8 underline' , 12),command=login_screen_from_sign_up).place(x=820,y=800)
    Button(sign_up_page_root, text='Submit' , width=10,bg="white",cursor='hand2',fg='black',font=('Comic Sans MS',15),command=midfn).place(x=850 ,y=860)
    photo = PhotoImage(file = "e.png")
    sign_up_page_root.iconphoto(False, photo)



def signup_page_from_email_verification_signup_fn():
    forgot_password_root_sign_up.destroy()
    global first_name_sign_up_var
    global last_name_sign_up_var
    global username_sign_up_var
    global gender_sign_up_var
    global sign_up_country_var
    global phone_no_sign_up_var
    global email_id_sign_up_var
    global first_password_sign_up_var
    global confirm_password_sign_up_var
    global sign_up_account_type_var
    global sign_up_page_root

    sign_up_page_root = Tk()
    sign_up_page_root.state('zoomed')
    sign_up_page_root.title('Registration form')
    sign_up_page_root.config(background = "black", pady=10)

    first_name_sign_up_var=StringVar()
    last_name_sign_up_var=StringVar()
    username_sign_up_var=StringVar()
    phone_no_sign_up_var=StringVar()
    email_id_sign_up_var=StringVar()
    first_password_sign_up_var=StringVar()
    confirm_password_sign_up_var=StringVar()
    sign_up_account_type_var=IntVar()
    sign_up_country_var=StringVar()
    gender_sign_up_var=IntVar()


    sign_up_label_0 =Label(sign_up_page_root, text="Registeration Form",width=100, font=("freestyle script", 70)).pack()

    sign_up_label_1 =Label(sign_up_page_root,text="first name:", width=17,font=("lucida handwriting",13))
    sign_up_label_1.place(x=670,y=250)

    sign_up_entry_1=Entry(sign_up_page_root,textvariable=first_name_sign_up_var,font=('verdana',15))
    sign_up_entry_1.place(x=950,y=250)

    sign_up_label_3 =Label(sign_up_page_root,text="Last name", width=17,font=("lucida handwriting",13))
    sign_up_label_3.place(x=670,y=300)

    sign_up_entry_3=Entry(sign_up_page_root,textvariable=last_name_sign_up_var,font=('verdana',15))
    sign_up_entry_3.place(x=950,y=300)

    sign_up_label_11 =Label(sign_up_page_root,text="Username", width=17,font=("lucida handwriting",13))
    sign_up_label_11.place(x=670,y=350)

    sign_up_entry_11=Entry(sign_up_page_root,textvariable=username_sign_up_var,font=('verdana',15))
    sign_up_entry_11.place(x=950,y=350)

    sign_up_label_4 =Label(sign_up_page_root,text="Gender", width=17,font=("lucida handwriting",13))
    sign_up_label_4.place(x=670,y=400)

    Radiobutton(sign_up_page_root,text="Male",padx= 20, variable= gender_sign_up_var, value=1,font=('verdana',13)).place(x=950,y=400)
    Radiobutton(sign_up_page_root,text="Female",padx= 20, variable=gender_sign_up_var, value=2,font=('verdana',13)).place(x=1055,y=400)

    sign_up_label_5=Label(sign_up_page_root,text="Country",width=17,font=("lucida handwriting",13))
    sign_up_label_5.place(x=670,y=450)

    sign_up_list_of_country=[ 'India' ,'US' , 'UK' ,'Australia' ,'Canada']

    sign_up_droplist=OptionMenu(sign_up_page_root, sign_up_country_var, *sign_up_list_of_country)
    sign_up_droplist.config(width=20)
    sign_up_country_var.set('Select your Country')
    sign_up_droplist.place(x=950,y=450)

    sign_up_label_6=Label(sign_up_page_root,text="Phone no:(optional)",width=17,font=("lucida handwriting",13))
    sign_up_label_6.place(x=670,y=500)

    sign_up_entry_6=Entry(sign_up_page_root,textvariable=phone_no_sign_up_var,font=('verdana',15))
    sign_up_entry_6.place(x=950,y=500)

    sign_up_label_7=Label(sign_up_page_root,text="Email-ID:",width=17,font=("lucida handwriting",13))
    sign_up_label_7.place(x=670,y=550)

    sign_up_entry_7=Entry(sign_up_page_root,textvariable=email_id_sign_up_var,font=('verdana',15),width=30)
    sign_up_entry_7.place(x=950,y=550)

    sign_up_label_8=Label(sign_up_page_root,text="Password:",width=17,font=("lucida handwriting",13))
    sign_up_label_8.place(x=670,y=600)

    sign_up_entry_8=Entry(sign_up_page_root,textvariable=first_password_sign_up_var,font=('verdana',15),show='*')
    sign_up_entry_8.place(x=950,y=600)

    sign_up_label_9=Label(sign_up_page_root,text="Confirm password:",width=17,font=("lucida handwriting",13))
    sign_up_label_9.place(x=670,y=650)

    sign_up_entry_9=Entry(sign_up_page_root,textvariable=confirm_password_sign_up_var,font=('verdana',15),show='*')
    sign_up_entry_9.place(x=950,y=650)

    sign_up_label_10=Label(sign_up_page_root,text="Account type:",width=17,font=("lucida handwriting",13))
    sign_up_label_10.place(x=670,y=700)


    Radiobutton(sign_up_page_root,text="administrator",padx= 10,variable= sign_up_account_type_var, value=1,font=('verdana',14)).place(x=950,y=700)
    Radiobutton(sign_up_page_root,text="student",padx= 10, variable= sign_up_account_type_var, value=2,font=('verdana',14)).place(x=1125,y=700)

    Button(sign_up_page_root, text='Already have an account',width=20,cursor='hand2',bg='black',fg='white',bd=0,font=('helvetica 8 underline' , 12),command=login_screen_from_sign_up).place(x=820,y=800)
    Button(sign_up_page_root, text='Submit' , width=10,bg="white",cursor='hand2',fg='black',font=('Comic Sans MS',15),command=midfn).place(x=850 ,y=860)
    photo = PhotoImage(file = "e.png")
    sign_up_page_root.iconphoto(False, photo)




def sign_up_from_login_page():
    login_screen.destroy()
    global first_name_sign_up_var
    global last_name_sign_up_var
    global username_sign_up_var
    global gender_sign_up_var
    global sign_up_country_var
    global phone_no_sign_up_var
    global email_id_sign_up_var
    global first_password_sign_up_var
    global confirm_password_sign_up_var
    global sign_up_account_type_var
    global sign_up_page_root

    sign_up_page_root = Tk()
    sign_up_page_root.state('zoomed')
    sign_up_page_root.title('Registration form')
    sign_up_page_root.config(background = "black", pady=10)

    first_name_sign_up_var=StringVar()
    last_name_sign_up_var=StringVar()
    username_sign_up_var=StringVar()
    phone_no_sign_up_var=StringVar()
    email_id_sign_up_var=StringVar()
    first_password_sign_up_var=StringVar()
    confirm_password_sign_up_var=StringVar()
    sign_up_account_type_var=IntVar()
    sign_up_country_var=StringVar()
    gender_sign_up_var=IntVar()


    sign_up_label_0 =Label(sign_up_page_root, text="Registeration Form",width=100, font=("freestyle script", 70)).pack()

    sign_up_label_1 =Label(sign_up_page_root,text="first name:", width=17,font=("lucida handwriting",13))
    sign_up_label_1.place(x=670,y=250)

    sign_up_entry_1=Entry(sign_up_page_root,textvariable=first_name_sign_up_var,font=('verdana',15))
    sign_up_entry_1.place(x=950,y=250)

    sign_up_label_3 =Label(sign_up_page_root,text="Last name", width=17,font=("lucida handwriting",13))
    sign_up_label_3.place(x=670,y=300)

    sign_up_entry_3=Entry(sign_up_page_root,textvariable=last_name_sign_up_var,font=('verdana',15))
    sign_up_entry_3.place(x=950,y=300)

    sign_up_label_11 =Label(sign_up_page_root,text="Username", width=17,font=("lucida handwriting",13))
    sign_up_label_11.place(x=670,y=350)

    sign_up_entry_11=Entry(sign_up_page_root,textvariable=username_sign_up_var,font=('verdana',15))
    sign_up_entry_11.place(x=950,y=350)

    sign_up_label_4 =Label(sign_up_page_root,text="Gender", width=17,font=("lucida handwriting",13))
    sign_up_label_4.place(x=670,y=400)

    Radiobutton(sign_up_page_root,text="Male",padx= 20, variable= gender_sign_up_var, value=1,font=('verdana',13)).place(x=950,y=400)
    Radiobutton(sign_up_page_root,text="Female",padx= 20, variable=gender_sign_up_var, value=2,font=('verdana',13)).place(x=1055,y=400)

    sign_up_label_5=Label(sign_up_page_root,text="Country",width=17,font=("lucida handwriting",13))
    sign_up_label_5.place(x=670,y=450)

    sign_up_list_of_country=[ 'India' ,'US' , 'UK' ,'Australia' ,'Canada']

    sign_up_droplist=OptionMenu(sign_up_page_root, sign_up_country_var, *sign_up_list_of_country)
    sign_up_droplist.config(width=20)
    sign_up_country_var.set('Select your Country')
    sign_up_droplist.place(x=950,y=450)

    sign_up_label_6=Label(sign_up_page_root,text="Phone no:(optional)",width=17,font=("lucida handwriting",13))
    sign_up_label_6.place(x=670,y=500)

    sign_up_entry_6=Entry(sign_up_page_root,textvariable=phone_no_sign_up_var,font=('verdana',15))
    sign_up_entry_6.place(x=950,y=500)

    sign_up_label_7=Label(sign_up_page_root,text="Email-ID:",width=17,font=("lucida handwriting",13))
    sign_up_label_7.place(x=670,y=550)

    sign_up_entry_7=Entry(sign_up_page_root,textvariable=email_id_sign_up_var,font=('verdana',15),width=30)
    sign_up_entry_7.place(x=950,y=550)

    sign_up_label_8=Label(sign_up_page_root,text="Password:",width=17,font=("lucida handwriting",13))
    sign_up_label_8.place(x=670,y=600)

    sign_up_entry_8=Entry(sign_up_page_root,textvariable=first_password_sign_up_var,font=('verdana',15),show='*')
    sign_up_entry_8.place(x=950,y=600)

    sign_up_label_9=Label(sign_up_page_root,text="Confirm password:",width=17,font=("lucida handwriting",13))
    sign_up_label_9.place(x=670,y=650)

    sign_up_entry_9=Entry(sign_up_page_root,textvariable=confirm_password_sign_up_var,font=('verdana',15),show='*')
    sign_up_entry_9.place(x=950,y=650)

    sign_up_label_10=Label(sign_up_page_root,text="Account type:",width=17,font=("lucida handwriting",13))
    sign_up_label_10.place(x=670,y=700)


    Radiobutton(sign_up_page_root,text="administrator",padx= 10,variable= sign_up_account_type_var, value=1,font=('verdana',14)).place(x=950,y=700)
    Radiobutton(sign_up_page_root,text="student",padx= 10, variable= sign_up_account_type_var, value=2,font=('verdana',14)).place(x=1125,y=700)

    Button(sign_up_page_root, text='Already have an account',width=20,cursor='hand2',bg='black',fg='white',bd=0,font=('helvetica 8 underline' , 12),command=login_screen_from_sign_up).place(x=820,y=800)
    Button(sign_up_page_root, text='Submit' , width=10,bg="white",cursor='hand2',fg='black',font=('Comic Sans MS',15),command=midfn).place(x=850 ,y=860)
    photo = PhotoImage(file = "e.png")
    sign_up_page_root.iconphoto(False, photo)




#Function definitins******************************************************************************************

 #***********************************************************Main Page********************************************   



main_page=Tk()
main_page.title("Home")
main_page.state("zoomed")
main_page.config(background = "black", pady=10)
Label(main_page, text="Library Management",width=50, font=("freestyle script", 100)).pack()
Label(main_page, text="",bg = "black").pack()
button_login=Button(main_page, text="Login", width=10,height=4,cursor='hand2', font=("Helvetica 10 underline",50),bg='red',command=login_screen)
button_login.pack()
Label(main_page, text="",bg = "black").pack()
button_signup=Button(main_page, text="Sign-Up", width=10, height=4,cursor='hand2', font=("Helvetica 10 underline",50),bg='red',command=signup_page_fn)
button_signup.pack()
Label(main_page, text="",bg = "black").pack()
photo = PhotoImage(file = "e.png")
main_page.iconphoto(False, photo)
main_page.mainloop()

#***************************************************Main Page******************************************************
def librarymang_home_page_student():
    global librarymang_home_page_student_root
    login_screen.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)

def force_exit_from_borrow_due_to_more_than_3_issue_to_librarymang_home_page_student():
    global librarymang_home_page_student_root
    book_issue_verification_tkinter_page_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)


def librarymang_home_page_student_from_the_borrow_book_page():
    global librarymang_home_page_student_root
    borrow_books_student_page_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)


def librarymang_home_page_student_from_book_issue_verification_tkinter_page():
    global librarymang_home_page_student_root
    book_issue_verification_tkinter_page_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)

def librarymang_home_page_student_after_issue_of_book():
    global librarymang_home_page_student_root
    book_issue_verification_tkinter_page_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)



def librarymang_home_page_student_from_return_of_book():
    global librarymang_home_page_student_root
    return_books_student_page_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)



def librarymang_home_page_student_after_return_of_book():
    global librarymang_home_page_student_root
    book_return_verification_tkinter_page_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)


def librarymang_home_page_student_from_view_borrowed_of_book():
    global librarymang_home_page_student_root
    view_borrowed_books_page_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)



def librarymang_home_page_student_after_viewing_of_book():
    global librarymang_home_page_student_root
    book_view_verification_tkinter_page_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)

def librarymang_home_page_student_after_profile():
    global librarymang_home_page_student_root
    profile_student_root.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)


def librarymang_home_page_student_after_profile_edit():
    global librarymang_home_page_student_root
    profile_student_root_edit.destroy()
    librarymang_home_page_student_root=Tk()
    librarymang_home_page_student_root.title("Login")
    librarymang_home_page_student_root.state("zoomed")
    librarymang_home_page_student_root.config(background = "black", pady=10)
    Label(librarymang_home_page_student_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Label(librarymang_home_page_student_root, text="",bg = "black").pack()
    Button(librarymang_home_page_student_root, text="Borrow books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=borrow_books_student_page_fn).place(x=400,y=300)
    Button(librarymang_home_page_student_root, text="Return books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=return_books_student_page).place(x=1100,y=300)
    Button(librarymang_home_page_student_root, text="View Borrowed \nBooks", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_borrowed_books).place(x=400,y=650)
    Button(librarymang_home_page_student_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_student).place(x=1100,y=650)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_student_root.iconphoto(False, photo)



#*********************************************************************************************************************************************************************************





def profile_page_student():
    global profile_student_root
    librarymang_home_page_student_root.destroy()
    profile_student_root=Tk()
    profile_student_root.title('Profile')
    profile_student_root.state("zoomed")
    profile_student_root.config(background = "black", pady=10)
    Label(profile_student_root, text="Profile",width=100, font=("freestyle script", 70)).pack()
    Label(profile_student_root,text="Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(profile_student_root,text="Username:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(profile_student_root,text="Email-Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=350)
    Label(profile_student_root,text="Gender:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=350)
    Label(profile_student_root,text="Country:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=600)
    Label(profile_student_root,text="Account Type:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=600)



    Label(profile_student_root,text=user_name,font=("verdana", 20),width=30,anchor='w').place(x=250,y=150)
    Label(profile_student_root,text=user_username,font=("verdana", 20),width=20,anchor='w').place(x=1225,y=150)
    Label(profile_student_root,text=user_email_id,font=("verdana", 20),width=30,anchor='w').place(x=310,y=350)
    Label(profile_student_root,text=user_gender,font=("verdana", 20),width=20,anchor='w').place(x=1185,y=350)
    Label(profile_student_root,text=user_country,font=("verdana", 20),width=20,anchor='w').place(x=300,y=600)
    Label(profile_student_root,text=user_account,font=("verdana", 20),width=20,anchor='w').place(x=1300,y=600)

    Button(profile_student_root,text='Edit',font=('verdana',25),cursor='hand2',bg='green',width=10,command=profile_page_student_edit).place(x=850,y=800)
    Button(profile_student_root,text='Go Back',font=('verdana',25),cursor='hand2',width=10,command=librarymang_home_page_student_after_profile).place(x=500,y=800)
    Button(profile_student_root,text='Log Out',font=('verdana',25),cursor='hand2',bg='red',width=10,command=log_out_from_profile).place(x=1200,y=800)
    photo = PhotoImage(file = "e.png")
    profile_student_root.iconphoto(False, photo)

def profile_page_student_edit():
    global profile_student_root_edit
    global edit_profile_first_name_var
    global edit_profile_last_name_var
    global edit_profile_username_var
    global edit_profile_gender_var
    global edit_profile_country_var
    global edit_profile_phone_no_var
    if user_phone_no==None:
        phoneno=''
    else:
        phoneno=str(user_phone_no)
    profile_student_root.destroy()
    profile_student_root_edit=Tk()
    profile_student_root_edit.title("Edit")
    profile_student_root_edit.state("zoomed")
    profile_student_root_edit.config(background = "black", pady=10)
    Label(profile_student_root_edit, text="Profile",width=100, font=("freestyle script", 70)).pack()
    Label(profile_student_root_edit,text="First Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(profile_student_root_edit,text="Last Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(profile_student_root_edit,text="Username:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=350)
    Label(profile_student_root_edit,text="Email-Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=350)
    Label(profile_student_root_edit,text="Gender:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=600)
    Label(profile_student_root_edit,text="Country:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=600)
    Label(profile_student_root_edit,text="Phone No:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=850)

    edit_profile_first_name_var=StringVar()
    edit_profile_last_name_var=StringVar()
    edit_profile_username_var=StringVar()
    edit_profile_gender_var=StringVar()
    edit_profile_country_var=StringVar()
    edit_profile_phone_no_var=StringVar()

    edit_profile_first_name_var.set(user_first_name)
    edit_profile_last_name_var.set(user_last_name)
    edit_profile_username_var.set(user_username)
    edit_profile_gender_var.set(user_gender)
    edit_profile_country_var.set(user_country)
    edit_profile_phone_no_var.set(phoneno)


    e1=Entry(profile_student_root_edit,textvariable=edit_profile_first_name_var,font=("verdana", 20),width=30)
    e2=Entry(profile_student_root_edit,textvariable=edit_profile_last_name_var,font=("verdana", 20),width=20)
    e3=Entry(profile_student_root_edit,textvariable=edit_profile_username_var,font=("verdana", 20),width=20)
    e4=Label(profile_student_root_edit,text=user_email_id,font=("verdana", 20),width=30,anchor='w')

    edit_profile_gender_list=[ 'male','female']
    edit_profile_gender_droplist=OptionMenu(profile_student_root_edit, edit_profile_gender_var, *edit_profile_gender_list)
    edit_profile_gender_droplist.config(font=("verdana", 20),width=20)

    edit_profile_country_list=[ 'India' ,'US' , 'UK' ,'Australia' ,'Canada']
    edit_profile_country_droplist=OptionMenu(profile_student_root_edit, edit_profile_country_var, *edit_profile_country_list)
    edit_profile_country_droplist.config(font=("verdana", 20),width=20)
    edit_profile_country_droplist.place(x=1250,y=250)

    e7=Entry(profile_student_root_edit,textvariable=edit_profile_phone_no_var,font=("verdana", 20),width=20)

    e1.place(x=350,y=150)
    e2.place(x=1235,y=150)
    e3.place(x=350,y=350)
    e4.place(x=1245,y=350)
    edit_profile_gender_droplist.place(x=300,y=600)
    edit_profile_country_droplist.place(x=1200,y=600)
    e7.place(x=310,y=850)

    Button(profile_student_root_edit,text='Edit',font=('verdana',25),cursor='hand2',bg='green',width=10,command=check_edit_profile_info_student).place(x=1350,y=750)
    Button(profile_student_root_edit,text='Go Back',font=('verdana',25),cursor='hand2',width=10,command=librarymang_home_page_student_after_profile_edit).place(x=1350,y=900)
    photo = PhotoImage(file = "e.png")
    profile_student_root_edit.iconphoto(False, photo)


def check_edit_profile_info_student():
    edit_profile_first_name=edit_profile_first_name_var.get()
    edit_profile_last_name=edit_profile_last_name_var.get()
    edit_profile_username=edit_profile_username_var.get()
    edit_profile_gender=edit_profile_gender_var.get()
    edit_profile_country=edit_profile_country_var.get()
    edit_profile_phone_no=edit_profile_phone_no_var.get()
    ref_for_edit_verify=0
    query_edit_info="select username from logindata where emailid!='{0}';"      #We are creating 2 lists of already eisting username and emails from testlogin
    cursor_mysql.execute(query_edit_info.format(user_email_id))
    output1=cursor_mysql.fetchall()
    list_of_usernames=[]
    for username_tuple in output1:
        list_of_usernames.append(username_tuple[0])
  
    if edit_profile_username=='' and ref_for_edit_verify==0:
        messagebox.showerror('username error','please enter username')
        ref_for_edit_verify=2
    elif len(edit_profile_username)<6 and len(edit_profile_username)>=20 and ref_for_edit_verify==0:
        messagebox.showerror('username error','username must have atleast 6 char')
        ref_for_edit_verify=2
    elif edit_profile_username[0].isdigit() and ref_for_edit_verify==0:
        messagebox.showerror('username error','username cant start with numbers')
        ref_for_edit_verify=2
    elif edit_profile_username in list_of_usernames:   #checking for duplicates of username
        messagebox.showerror('username error','Username is taken')
        ref_for_edit_verify=2
    else:
        pass
    
    if ref_for_edit_verify==0:
        if edit_profile_phone_no=='':
            pass
        elif not edit_profile_phone_no.isdigit():
            messagebox.showerror('phone no','invaid phone no')
            ref_for_edit_verify=4
        elif len(str(edit_profile_phone_no))!=10:
            messagebox.showerror('phone no','invaid phone no')
            ref_for_edit_verify=4
        else:
            pass
    else:
        pass
    if len(edit_profile_first_name)==0 and ref_for_edit_verify==0:
        messagebox.showerror('error','please enter name')
        ref_for_edit_verify=5
    elif len(edit_profile_last_name)==0 and ref_for_edit_verify==0:
        messagebox.showerror('error','please enter last name')
        ref_for_edit_verify=5
    elif len(edit_profile_first_name)>20 and ref_for_edit_verify==0:
        messagebox.showerror('error','name should be less than 21 charcters')
        ref_for_edit_verify=5
    elif len(edit_profile_last_name)>20 and ref_for_edit_verify==0:
        messagebox.showerror('error','last name should be less than 21 charcters')
        ref_for_edit_verify=5
    else:
        pass

    if edit_profile_gender=='' and ref_for_edit_verify==0:
        messagebox.showerror('error','please enter your gender')
        ref_for_edit_verify=6
    elif edit_profile_gender not in ['male','female']:
        messagebox.showerror('error','please enter your gender')
        ref_for_edit_verify=6
    else:
        pass
    if ref_for_edit_verify==0 and edit_profile_country=='':
        messagebox.showerror('error','please enter country')
        ref_for_edit_verify=7
    elif ref_for_edit_verify==0 and (edit_profile_country not in [ 'India' ,'US' , 'UK' ,'Australia' ,'Canada']):
        messagebox.showerror('error','cant verify your country')
        ref_for_edit_verify=7
    else:
        pass


    if (('\'' in edit_profile_username) or ('\"' in edit_profile_username) or ('\'' in edit_profile_first_name) or ('\"' in edit_profile_first_name) or ('\'' in edit_profile_last_name) or ('\"' in edit_profile_last_name)) and  ref_for_edit_verify==0:
        messagebox.showinfo('error','Dnot use \' or \" in any field')
        ref_for_edit_verify=9
    if ref_for_edit_verify==0:
        updating_profile_student(edit_profile_username,edit_profile_phone_no,edit_profile_first_name,edit_profile_last_name,edit_profile_gender,edit_profile_country)  # True and False returned is just for reference. In the main program define a global variable using 'global' and assign true and false to that. if the variable is true follow on with the sign up and then break out of while loop int new page but if false reload page using while loop.
    else:
        pass

def updating_profile_student(username,phoneno,firstname,lastname,gender,country):
    global user_username
    global user_name
    global user_gender
    global user_phone_no
    global user_first_name
    global user_last_name
    global user_country
    try:
        if phoneno=='':
            query1="update logindata set username='{0}',phoneno=Null,firstname='{1}',lastname='{2}',gender='{3}',country='{4}' where emailid='{5}';"
            query2="update loginissue set username='{0}' where username='{1}';"
            query3="update bookissue set username='{0}' where username='{1}';"
            cursor_mysql.execute(query1.format(username,firstname,lastname,gender,country,user_email_id))
            mycon.commit()
            a=2
            cursor_mysql.execute(query2.format(username,user_username))
            mycon.commit()
            a=3
            cursor_mysql.execute(query3.format(username,user_username))
            mycon.commit()
        else:
            query1="update logindata set username='{0}',phoneno='{1}',firstname='{2}',lastname='{3}',gender='{4}',country='{5}' where emailid='{6}';"
            query2="update loginissue set username='{0}' where username='{1}';"
            query3="update bookissue set username='{0}' where username='{1}';"
            cursor_mysql.execute(query1.format(username,phoneno,firstname,lastname,gender,country,user_email_id))
            mycon.commit()
            a=2
            cursor_mysql.execute(query2.format(username,user_username))
            mycon.commit()
            a=3
            cursor_mysql.execute(query3.format(username,user_username))
            mycon.commit()
        ref=1
    except:
        messagebox.showinfo('oops','something went wrong')
        ref=2
        librarymang_home_page_student_after_profile_edit()
    if ref==1:
        messagebox.showinfo('success','Profile Updated')

        user_username=username
        user_name=firstname+' '+lastname
        user_gender=gender
        user_phone_no=phoneno
        user_first_name=firstname
        user_last_name=lastname
        user_country=country
        librarymang_home_page_student_after_profile_edit()









def log_out_from_profile():
    global user_email_id
    global user_name
    global user_username           
    global user_gender
    global user_phone_no
    global user_country
    global user_account
    user_email_id=''
    user_name=''
    user_username=''
    user_phone_no=None
    user_gender=''
    user_country=''
    user_account=''
    profile_student_root.destroy()
    login_screen_from_student_profile()











#************************************************************************************************************************************************************************************




def view_borrowed_books():
    global view_borrowed_books_page_root
    librarymang_home_page_student_root.destroy()
    view_borrowed_books_page_root=Tk()
    view_borrowed_books_page_root.title('View Borrowed Books')
    view_borrowed_books_page_root.config(bg='black',pady=10)
    view_borrowed_books_page_root.state('zoomed')
    Label(view_borrowed_books_page_root, text="View Borrowed book",width=100, font=("freestyle script", 70)).pack()
    count_of_borrowed_books_for_view()

    Button(view_borrowed_books_page_root,text='Go Back',font=('verdana',25),cursor='hand2',command=librarymang_home_page_student_from_view_borrowed_of_book).place(x=1070,y=800)
    Button(view_borrowed_books_page_root,text='Show Book Info',font=('verdana',25),cursor='hand2',command=clicking_proceed_in_view_fn,).place(x=700,y=800)
    photo = PhotoImage(file = "e.png")
    view_borrowed_books_page_root.iconphoto(False, photo)


def count_of_borrowed_books_for_view():
    global no_of_borrowed_books_for_view
    global list_of_books_for_view
    global dict_of_books_for_view
    dict_of_books_for_view={}
    list_of_books_for_view=[]
    query="select * from loginissue where username='{0}'"
    cursor_mysql.execute(query.format(user_username))
    output=cursor_mysql.fetchall()
    no_of_borrowed_books_for_view=0
    tup_of_borrowed_books_for_view=output[0]
    if tup_of_borrowed_books_for_view[1]==None:
        no_of_borrowed_books_for_view=0
    else:
        if tup_of_borrowed_books_for_view[2]==None:
            no_of_borrowed_books_for_view=1
        else:
            if tup_of_borrowed_books_for_view[3]==None:
                no_of_borrowed_books_for_view=2
            else:
                no_of_borrowed_books_for_view=3

    if no_of_borrowed_books_for_view==0:
        nothing_to_view_fn()
    elif no_of_borrowed_books_for_view==1:
        query1="select book_id2,date_of_issue,date_of_return from bookissue where username='{0}';"
        cursor_mysql.execute(query1.format(user_username))
        out1=cursor_mysql.fetchall()
        bookid=out1[0][0]
        query12="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query12.format(bookid))
        out12=cursor_mysql.fetchall()
        dict_of_books_for_view[1]=[bookid,out12[0][0],out12[0][1],str(out1[0][1]),str(out1[0][2])]
        list_of_books_for_view.append([bookid,out12[0][0],out12[0][1],str(out1[0][1]),str(out1[0][2]),1])
        one_book_to_view()
    elif no_of_borrowed_books_for_view==2:
        query2="select book_id2,date_of_issue,date_of_return from bookissue where username='{0}';"
        cursor_mysql.execute(query2.format(user_username))
        out2=cursor_mysql.fetchall()
        bookid21=out2[0][0]
        bookid22=out2[1][0]
        
        query21="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query21.format(bookid21))
        out22=cursor_mysql.fetchall()
        dict_of_books_for_view[1]=[bookid21,out22[0][0],out22[0][1],str(out2[0][1]),str(out2[0][2])]
        list_of_books_for_view.append([bookid21,out22[0][0],out22[0][1],str(out2[0][1]),str(out2[0][2]),1])
        
        query23="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query23.format(bookid22))
        out23=cursor_mysql.fetchall()
        dict_of_books_for_view[2]=[bookid22,out23[0][0],out23[0][1],str(out2[1][1]),str(out2[1][2])]
        list_of_books_for_view.append([bookid22,out23[0][0],out23[0][1],str(out2[1][1]),str(out2[1][2]),2])
        two_books_to_view()
    else:
        query3="select book_id2,date_of_issue,date_of_return from bookissue where username='{0}';"
        cursor_mysql.execute(query3.format(user_username))
        out3=cursor_mysql.fetchall()
        bookid31=out3[0][0]
        bookid32=out3[1][0]
        bookid33=out3[2][0]

        query31="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query31.format(bookid31))
        out32=cursor_mysql.fetchall()
        dict_of_books_for_view[1]=[bookid31,out32[0][0],out32[0][1],str(out3[0][1]),str(out3[0][2])]
        list_of_books_for_view.append([bookid31,out32[0][0],out32[0][1],str(out3[0][1]),str(out3[0][2]),1])

        query32="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query32.format(bookid32))
        out33=cursor_mysql.fetchall()
        dict_of_books_for_view[2]=[bookid32,out33[0][0],out33[0][1],str(out3[1][1]),str(out3[1][2])]
        list_of_books_for_view.append([bookid32,out33[0][0],out33[0][1],str(out3[1][1]),str(out3[1][2]),2])

        query33="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query33.format(bookid33))
        out34=cursor_mysql.fetchall()
        dict_of_books_for_view[3]=[bookid33,out34[0][0],out34[0][1],str(out3[2][1]),str(out3[2][2])]
        list_of_books_for_view.append([bookid33,out34[0][0],out34[0][1],str(out3[2][1]),str(out3[2][2]),3])
        three_books_to_view()

def obtaining_month_day_year_of_view(due_date):

    list_of_day_month_year=due_date.split('-')
    year_of_view=int(list_of_day_month_year[0])
    month_of_view=int(list_of_day_month_year[1])
    day_of_view=int(list_of_day_month_year[2])
    bool_val_for_date=(datetime.now()>datetime(year_of_view,month_of_view,day_of_view))
    return bool_val_for_date



def nothing_to_view_fn():
    global book_name_select_for_view
    global book_name_select_for_view_var
    book_name_select_for_view_var=book_name_select_for_view='chumma'
    Label(view_borrowed_books_page_root,text="You Have Not Borrowed Any Book",font=("lucida handwriting", 30),bg='black',fg='white').place(x=600,y=300)


def one_book_to_view():
    global book_name_select_for_view_var
    global main_frame6
    innerframe6=LabelFrame(view_borrowed_books_page_root,text='books',bd=15,width=1000)
    innerframe6.place(x=300,y=300)

    #Creating Main fram:
    main_frame6=Frame(innerframe6,width=1000)
    main_frame6.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_view_var=IntVar()
    if obtaining_month_day_year_of_view(dict_of_books_for_view[1][4]):
        radiobutton_color_if_due_date_is_past_view(list_of_books_for_view[0][5],list_of_books_for_view[0][1],list_of_books_for_view[0][2],list_of_books_for_view[0][4])
    else:
        radiobutton_color_if_due_date_is_only_coming_view(list_of_books_for_view[0][5],list_of_books_for_view[0][1],list_of_books_for_view[0][2],list_of_books_for_view[0][4])



def two_books_to_view():
    global book_name_select_for_view_var
    global main_frame6
    innerframe6=LabelFrame(view_borrowed_books_page_root,text='books',bd=15,width=1000)
    innerframe6.place(x=300,y=300)

    #Creating Main fram:
    main_frame6=Frame(innerframe6,width=1000)
    main_frame6.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_view_var=IntVar()
    if obtaining_month_day_year_of_view(dict_of_books_for_view[1][4]):
        radiobutton_color_if_due_date_is_past_view(list_of_books_for_view[0][5],list_of_books_for_view[0][1],list_of_books_for_view[0][2],list_of_books_for_view[0][4])
    else:
        radiobutton_color_if_due_date_is_only_coming_view(list_of_books_for_view[0][5],list_of_books_for_view[0][1],list_of_books_for_view[0][2],list_of_books_for_view[0][4])

    if obtaining_month_day_year_of_view(dict_of_books_for_view[2][4]):
        radiobutton_color_if_due_date_is_past_view(list_of_books_for_view[1][5],list_of_books_for_view[1][1],list_of_books_for_view[1][2],list_of_books_for_view[1][4])
    else:
        radiobutton_color_if_due_date_is_only_coming_view(list_of_books_for_view[1][5],list_of_books_for_view[1][1],list_of_books_for_view[1][2],list_of_books_for_view[1][4],)

def three_books_to_view():
    global book_name_select_for_view_var
    global main_frame6
    innerframe6=LabelFrame(view_borrowed_books_page_root,text='books',bd=15,width=1000)
    innerframe6.place(x=300,y=300)

    #Creating Main fram:
    main_frame6=Frame(innerframe6,width=1000)
    main_frame6.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_view_var=IntVar()
    if obtaining_month_day_year_of_view(dict_of_books_for_view[1][4]):
        radiobutton_color_if_due_date_is_past_view(list_of_books_for_view[0][5],list_of_books_for_view[0][1],list_of_books_for_view[0][2],list_of_books_for_view[0][4])
    else:
        radiobutton_color_if_due_date_is_only_coming_view(list_of_books_for_view[0][5],list_of_books_for_view[0][1],list_of_books_for_view[0][2],list_of_books_for_view[0][4])

    if obtaining_month_day_year_of_view(dict_of_books_for_view[2][4]):
        radiobutton_color_if_due_date_is_past_view(list_of_books_for_view[1][5],list_of_books_for_view[1][1],list_of_books_for_view[1][2],list_of_books_for_view[1][4])
    else:
        radiobutton_color_if_due_date_is_only_coming_view(list_of_books_for_view[1][5],list_of_books_for_view[1][1],list_of_books_for_view[1][2],list_of_books_for_view[1][4],)
    
    if obtaining_month_day_year_of_view(dict_of_books_for_view[3][4]):
        radiobutton_color_if_due_date_is_past_view(list_of_books_for_view[2][5],list_of_books_for_view[2][1],list_of_books_for_view[2][2],list_of_books_for_view[2][4])
    else:
        radiobutton_color_if_due_date_is_only_coming_view(list_of_books_for_view[2][5],list_of_books_for_view[2][1],list_of_books_for_view[2][2],list_of_books_for_view[2][4])
    
    

def radiobutton_color_if_due_date_is_only_coming_view(ival,bookname,bookauthor,duedate):
    global book_name_select_for_view_var
    Radiobutton(main_frame6,text=bookname+'        (   by  '+bookauthor+' )\n(   Due On '+duedate+'   )',font=("lucida handwriting", 30),indicator=0,variable=book_name_select_for_view_var,value=ival,width=50,bg='cyan',fg='black',padx=10,anchor='w').pack()
def radiobutton_color_if_due_date_is_past_view(ival,bookname,bookauthor,duedate):
    global book_name_select_for_view_var
    Radiobutton(main_frame6,text=bookname+'        (   by  '+bookauthor+' )\n(   Book Due    )',font=("lucida handwriting", 30),indicator=0,variable=book_name_select_for_view_var,value=ival,width=50,bg='red',fg='black',padx=10,anchor='w').pack()




def clicking_proceed_in_view_fn():
    global book_name_select_for_view_var
    global main_list_regarding_book_and_author_info_for_view
    global dict_of_books_for_view

    try:
        book_name_select_for_view=book_name_select_for_view_var.get()
    except:
        book_name_select_for_view='chumma'
    main_list_regarding_book_and_author_info_for_view=[]
    if book_name_select_for_view==0:
        messagebox.showerror('view book','please select a book')
        ref=1
    elif book_name_select_for_view=='chumma' or book_name_select_for_view_var=='chumma':
        messagebox.showinfo('oops','You have not borrwed any book')
        librarymang_home_page_student_from_view_borrowed_of_book()
        ref=1
    else:
        main_list_regarding_book_and_author_info_for_view=dict_of_books_for_view[book_name_select_for_view][0:5]   #just so that the 4th column is taken
        book_view_verification_tkinter_page()







def book_view_verification_tkinter_page():
    global main_list_regarding_book_and_author_info_for_view
    global book_view_verification_tkinter_page_root

    view_borrowed_books_page_root.destroy()

    book_view_verification_tkinter_page_root=Tk()
    book_view_verification_tkinter_page_root.title('View Books')
    book_view_verification_tkinter_page_root.state("zoomed")

    book_view_verification_tkinter_page_root.config(background = "black", pady=10)

    obtaining_book_info_for_view(main_list_regarding_book_and_author_info_for_view)

    Label(book_view_verification_tkinter_page_root,text="Book Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=700,y=20)
    Label(book_view_verification_tkinter_page_root,text="Book Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(book_view_verification_tkinter_page_root,text="Book Author:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(book_view_verification_tkinter_page_root,text="Number Of Pages:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=250)
    Label(book_view_verification_tkinter_page_root,text="Book Cover:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=250)
    Label(book_view_verification_tkinter_page_root,text="Book Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=400)
    Label(book_view_verification_tkinter_page_root,text="Author Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=400)
    Label(book_view_verification_tkinter_page_root,text="Issue Date:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=680)
    Label(book_view_verification_tkinter_page_root,text="Return Date:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=680)

    Label(book_view_verification_tkinter_page_root,text=main_book_id_for_showing_in_book_view,font=("verdana", 20),width=20,anchor='w').place(x=890,y=20)
    Label(book_view_verification_tkinter_page_root,text=main_bookname_for_showing_in_book_view,font=("verdana", 20),width=30,anchor='w').place(x=350,y=150)
    Label(book_view_verification_tkinter_page_root,text=main_bookauthor_for_showing_in_book_view,font=("verdana", 20),width=30,anchor='w').place(x=1275,y=150)
    Label(book_view_verification_tkinter_page_root,text=str(main_number_of_pages_for_showing_in_book_view),font=("verdana", 20),width=20,anchor='w').place(x=460,y=250)
    Label(book_view_verification_tkinter_page_root,text=main_book_cover_for_showing_in_book_view,font=("verdana", 20),width=20,anchor='w').place(x=1245,y=250)
    Label(book_view_verification_tkinter_page_root,text=main_issue_date_for_showing_in_book_view,font=("verdana", 20),width=20,anchor='w').place(x=340,y=680)
    Label(book_view_verification_tkinter_page_root,text=main_return_date_for_showing_in_book_view,font=("verdana", 20),width=20,anchor='w').place(x=1270,y=680)

    first_scroll_for_view=scrolledtext.ScrolledText(book_view_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    second_scroll_for_view=scrolledtext.ScrolledText(book_view_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    first_scroll_for_view.insert(END,main_bookinfo_for_showing_in_book_view)
    second_scroll_for_view.insert(END,main_author_info_for_showing_in_book_view)
    first_scroll_for_view.place(x=330,y=400)
    second_scroll_for_view.place(x=1270,y=400)

    Button(book_view_verification_tkinter_page_root,text='Go Back',font=('verdana',25),cursor='hand2',command=librarymang_home_page_student_after_viewing_of_book).place(x=800,y=800)
    photo = PhotoImage(file = "e.png")
    book_view_verification_tkinter_page_root.iconphoto(False, photo)
    


def obtaining_book_info_for_view(list_to_regard):
    global main_book_id_for_showing_in_book_view
    global main_bookname_for_showing_in_book_view
    global main_bookauthor_for_showing_in_book_view
    global main_bookinfo_for_showing_in_book_view
    global main_number_of_pages_for_showing_in_book_view
    global main_book_cover_for_showing_in_book_view
    global main_author_info_for_showing_in_book_view
    global main_issue_date_for_showing_in_book_view
    global main_return_date_for_showing_in_book_view

    query_for_book_last_view='''select * from bookdata where book_id='{0}';'''
    cursor_mysql.execute(query_for_book_last_view.format(list_to_regard[0]))
    new_list5=cursor_mysql.fetchall()


    main_book_id_for_showing_in_book_view=new_list5[0][0]
    main_bookname_for_showing_in_book_view=new_list5[0][1]
    main_bookauthor_for_showing_in_book_view=new_list5[0][2]
    main_number_of_pages_for_showing_in_book_view=new_list5[0][3]
    main_book_cover_for_showing_in_book_view=new_list5[0][6]
    main_bookinfo_for_showing_in_book_view=new_list5[0][4]
    if new_list5[0][5]==None:
        main_author_info_for_showing_in_book_view='No Information Available'
    else:
        main_author_info_for_showing_in_book_view=new_list5[0][5]

    query_for_books_view_2="select * from bookissue where book_id2='{0}';"
    cursor_mysql.execute(query_for_books_view_2.format(main_book_id_for_showing_in_book_view))
    newlist6=cursor_mysql.fetchall()
    list_local_issuedateview=(str(newlist6[0][2])).split('-')
    list_local_returndateview=(str(newlist6[0][3])).split('-')
    yearissueview=list_local_issuedateview[0]
    monthissueview=list_local_issuedateview[1]
    dayissueview=list_local_issuedateview[2]
    yearreturnview=list_local_returndateview[0]
    monthreturnview=list_local_returndateview[1]
    dayreturnview=list_local_returndateview[2]
    main_issue_date_for_showing_in_book_view=dayissueview+'-'+monthissueview+'-'+yearissueview
    main_return_date_for_showing_in_book_view=dayreturnview+'-'+monthreturnview+'-'+yearreturnview






#************************************************************************************************************************************************************************************


def return_books_student_page():
    global return_books_student_page_root
    librarymang_home_page_student_root.destroy()
    return_books_student_page_root=Tk()
    return_books_student_page_root.title('Return Books')
    return_books_student_page_root.config(bg='black',pady=10)
    return_books_student_page_root.state('zoomed')
    Label(return_books_student_page_root, text="Return book",width=100, font=("freestyle script", 70)).pack()
    count_of_borrowed_books()

    Button(return_books_student_page_root,text='Cancel',font=('verdana',25),cursor='hand2',command=librarymang_home_page_student_from_return_of_book).place(x=1000,y=800)
    Button(return_books_student_page_root,text='Proceed',font=('verdana',25),cursor='hand2',command=clicking_proceed_in_return_fn,).place(x=700,y=800)
    photo = PhotoImage(file = "e.png")
    return_books_student_page_root.iconphoto(False, photo)

def count_of_borrowed_books():
    global no_of_borrowed_books_for_return
    global list_of_books_for_return
    global dict_of_books_for_return
    dict_of_books_for_return={}
    list_of_books_for_return=[]
    query="select * from loginissue where username='{0}'"
    cursor_mysql.execute(query.format(user_username))
    output=cursor_mysql.fetchall()
    no_of_borrowed_books_for_return=0
    tup_of_borrowed_books_for_return=output[0]
    if tup_of_borrowed_books_for_return[1]==None:
        no_of_borrowed_books_for_return=0
    else:
        if tup_of_borrowed_books_for_return[2]==None:
            no_of_borrowed_books_for_return=1
        else:
            if tup_of_borrowed_books_for_return[3]==None:
                no_of_borrowed_books_for_return=2
            else:
                no_of_borrowed_books_for_return=3

    if no_of_borrowed_books_for_return==0:
        nothing_to_return_fn()
    elif no_of_borrowed_books_for_return==1:
        query1="select book_id2,date_of_issue,date_of_return from bookissue where username='{0}';"
        cursor_mysql.execute(query1.format(user_username))
        out1=cursor_mysql.fetchall()
        bookid=out1[0][0]
        query12="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query12.format(bookid))
        out12=cursor_mysql.fetchall()
        dict_of_books_for_return[1]=[bookid,out12[0][0],out12[0][1],str(out1[0][1]),str(out1[0][2])]
        list_of_books_for_return.append([bookid,out12[0][0],out12[0][1],str(out1[0][1]),str(out1[0][2]),1])
        one_book_to_return()
    elif no_of_borrowed_books_for_return==2:
        query2="select book_id2,date_of_issue,date_of_return from bookissue where username='{0}';"
        cursor_mysql.execute(query2.format(user_username))
        out2=cursor_mysql.fetchall()
        bookid21=out2[0][0]
        bookid22=out2[1][0]
        
        query21="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query21.format(bookid21))
        out22=cursor_mysql.fetchall()
        dict_of_books_for_return[1]=[bookid21,out22[0][0],out22[0][1],str(out2[0][1]),str(out2[0][2])]
        list_of_books_for_return.append([bookid21,out22[0][0],out22[0][1],str(out2[0][1]),str(out2[0][2]),1])
        
        query23="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query23.format(bookid22))
        out23=cursor_mysql.fetchall()
        dict_of_books_for_return[2]=[bookid22,out23[0][0],out23[0][1],str(out2[1][1]),str(out2[1][2])]
        list_of_books_for_return.append([bookid22,out23[0][0],out23[0][1],str(out2[1][1]),str(out2[1][2]),2])
        two_books_to_return()
    else:
        query3="select book_id2,date_of_issue,date_of_return from bookissue where username='{0}';"
        cursor_mysql.execute(query3.format(user_username))
        out3=cursor_mysql.fetchall()
        bookid31=out3[0][0]
        bookid32=out3[1][0]
        bookid33=out3[2][0]

        query31="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query31.format(bookid31))
        out32=cursor_mysql.fetchall()
        dict_of_books_for_return[1]=[bookid31,out32[0][0],out32[0][1],str(out3[0][1]),str(out3[0][2])]
        list_of_books_for_return.append([bookid31,out32[0][0],out32[0][1],str(out3[0][1]),str(out3[0][2]),1])

        query32="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query32.format(bookid32))
        out33=cursor_mysql.fetchall()
        dict_of_books_for_return[2]=[bookid32,out33[0][0],out33[0][1],str(out3[1][1]),str(out3[1][2])]
        list_of_books_for_return.append([bookid32,out33[0][0],out33[0][1],str(out3[1][1]),str(out3[1][2]),2])

        query33="select bookname,bookauthor from bookdata where book_id='{0}';"
        cursor_mysql.execute(query33.format(bookid33))
        out34=cursor_mysql.fetchall()
        dict_of_books_for_return[3]=[bookid33,out34[0][0],out34[0][1],str(out3[2][1]),str(out3[2][2])]
        list_of_books_for_return.append([bookid33,out34[0][0],out34[0][1],str(out3[2][1]),str(out3[2][2]),3])
        three_books_to_return()

def obtaining_month_day_year_of_return(due_date):

    list_of_day_month_year=due_date.split('-')
    year_of_return=int(list_of_day_month_year[0])
    month_of_return=int(list_of_day_month_year[1])
    day_of_return=int(list_of_day_month_year[2])
    bool_val_for_date=(datetime.now()>datetime(year_of_return,month_of_return,day_of_return))
    return bool_val_for_date

def nothing_to_return_fn():
    global book_name_select_for_return
    global book_name_select_for_return_var
    book_name_select_for_return_var=book_name_select_for_return='chumma'
    Label(return_books_student_page_root,text="No Books To Return",font=("lucida handwriting", 30),bg='black',fg='white').place(x=700,y=300)


def one_book_to_return():
    global book_name_select_for_return_var
    global main_frame5
    innerframe5=LabelFrame(return_books_student_page_root,text='books',bd=15,width=1000)
    innerframe5.place(x=300,y=300)

    #Creating Main fram:
    main_frame5=Frame(innerframe5,width=1000)
    main_frame5.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_return_var=IntVar()
    if obtaining_month_day_year_of_return(dict_of_books_for_return[1][4]):
        radiobutton_color_if_due_date_is_past(list_of_books_for_return[0][5],list_of_books_for_return[0][1],list_of_books_for_return[0][2],list_of_books_for_return[0][4])
    else:
        radiobutton_color_if_due_date_is_only_coming(list_of_books_for_return[0][5],list_of_books_for_return[0][1],list_of_books_for_return[0][2],list_of_books_for_return[0][4])



def two_books_to_return():
    global book_name_select_for_return_var
    global main_frame5
    innerframe5=LabelFrame(return_books_student_page_root,text='books',bd=15,width=1000)
    innerframe5.place(x=300,y=300)

    #Creating Main fram:
    main_frame5=Frame(innerframe5,width=1000)
    main_frame5.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_return_var=IntVar()
    if obtaining_month_day_year_of_return(dict_of_books_for_return[1][4]):
        radiobutton_color_if_due_date_is_past(list_of_books_for_return[0][5],list_of_books_for_return[0][1],list_of_books_for_return[0][2],list_of_books_for_return[0][4])
    else:
        radiobutton_color_if_due_date_is_only_coming(list_of_books_for_return[0][5],list_of_books_for_return[0][1],list_of_books_for_return[0][2],list_of_books_for_return[0][4])

    if obtaining_month_day_year_of_return(dict_of_books_for_return[2][4]):
        radiobutton_color_if_due_date_is_past(list_of_books_for_return[1][5],list_of_books_for_return[1][1],list_of_books_for_return[1][2],list_of_books_for_return[1][4])
    else:
        radiobutton_color_if_due_date_is_only_coming(list_of_books_for_return[1][5],list_of_books_for_return[1][1],list_of_books_for_return[1][2],list_of_books_for_return[1][4],)

def three_books_to_return():
    global book_name_select_for_return_var
    global main_frame5
    innerframe5=LabelFrame(return_books_student_page_root,text='books',bd=15,width=1000)
    innerframe5.place(x=300,y=300)

    #Creating Main fram:
    main_frame5=Frame(innerframe5,width=1000)
    main_frame5.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_return_var=IntVar()
    if obtaining_month_day_year_of_return(dict_of_books_for_return[1][4]):
        radiobutton_color_if_due_date_is_past(list_of_books_for_return[0][5],list_of_books_for_return[0][1],list_of_books_for_return[0][2],list_of_books_for_return[0][4])
    else:
        radiobutton_color_if_due_date_is_only_coming(list_of_books_for_return[0][5],list_of_books_for_return[0][1],list_of_books_for_return[0][2],list_of_books_for_return[0][4])

    if obtaining_month_day_year_of_return(dict_of_books_for_return[2][4]):
        radiobutton_color_if_due_date_is_past(list_of_books_for_return[1][5],list_of_books_for_return[1][1],list_of_books_for_return[1][2],list_of_books_for_return[1][4])
    else:
        radiobutton_color_if_due_date_is_only_coming(list_of_books_for_return[1][5],list_of_books_for_return[1][1],list_of_books_for_return[1][2],list_of_books_for_return[1][4],)
    
    if obtaining_month_day_year_of_return(dict_of_books_for_return[3][4]):
        radiobutton_color_if_due_date_is_past(list_of_books_for_return[2][5],list_of_books_for_return[2][1],list_of_books_for_return[2][2],list_of_books_for_return[2][4])
    else:
        radiobutton_color_if_due_date_is_only_coming(list_of_books_for_return[2][5],list_of_books_for_return[2][1],list_of_books_for_return[2][2],list_of_books_for_return[2][4])
    
    

def radiobutton_color_if_due_date_is_only_coming(ival,bookname,bookauthor,duedate):
    global book_name_select_for_return_var
    Radiobutton(main_frame5,text=bookname+'        (   by  '+bookauthor+' )\n(   Due On '+duedate+'   )',font=("lucida handwriting", 30),indicator=0,variable=book_name_select_for_return_var,value=ival,width=50,bg='cyan',fg='black',padx=10,anchor='w').pack()
def radiobutton_color_if_due_date_is_past(ival,bookname,bookauthor,duedate):
    global book_name_select_for_return_var
    Radiobutton(main_frame5,text=bookname+'        (   by  '+bookauthor+' )\n(   Book Due    )',font=("lucida handwriting", 30),indicator=0,variable=book_name_select_for_return_var,value=ival,width=50,bg='red',fg='black',padx=10,anchor='w').pack()


def clicking_proceed_in_return_fn():
    global book_name_select_for_return_var
    global main_list_regarding_book_and_author_info_for_return
    global dict_of_books_for_return

    try:
        book_name_select_for_return=book_name_select_for_return_var.get()
    except:
        book_name_select_for_return='chumma'
    main_list_regarding_book_and_author_info_for_return=[]
    if book_name_select_for_return==0:
        messagebox.showerror('return book','please select a book')
        ref=1
    elif book_name_select_for_return=='chumma' or book_name_select_for_return_var=='chumma':
        messagebox.showinfo('oops','You have not borrwed any book')
        librarymang_home_page_student_from_return_of_book()
        ref=1
    else:
        main_list_regarding_book_and_author_info_for_return=dict_of_books_for_return[book_name_select_for_return][0:5]   #just so that the 4th column is taken
        book_return_verification_tkinter_page()



def book_return_verification_tkinter_page():
    global main_list_regarding_book_and_author_info_for_return
    global book_return_verification_tkinter_page_root

    return_books_student_page_root.destroy()

    book_return_verification_tkinter_page_root=Tk()
    book_return_verification_tkinter_page_root.title('Return Books')
    book_return_verification_tkinter_page_root.state("zoomed")

    book_return_verification_tkinter_page_root.config(background = "black", pady=10)

    obtaining_book_info_for_return(main_list_regarding_book_and_author_info_for_return)

    Label(book_return_verification_tkinter_page_root,text="Book Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=700,y=20)
    Label(book_return_verification_tkinter_page_root,text="Book Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(book_return_verification_tkinter_page_root,text="Book Author:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(book_return_verification_tkinter_page_root,text="Number Of Pages:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=250)
    Label(book_return_verification_tkinter_page_root,text="Book Cover:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=250)
    Label(book_return_verification_tkinter_page_root,text="Book Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=400)
    Label(book_return_verification_tkinter_page_root,text="Author Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=400)
    Label(book_return_verification_tkinter_page_root,text="Issue Date:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=680)
    Label(book_return_verification_tkinter_page_root,text="Return Date:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=680)

    Label(book_return_verification_tkinter_page_root,text=main_book_id_for_showing_in_book_return,font=("verdana", 20),width=20,anchor='w').place(x=890,y=20)
    Label(book_return_verification_tkinter_page_root,text=main_bookname_for_showing_in_book_return,font=("verdana", 20),width=30,anchor='w').place(x=350,y=150)
    Label(book_return_verification_tkinter_page_root,text=main_bookauthor_for_showing_in_book_return,font=("verdana", 20),width=30,anchor='w').place(x=1275,y=150)
    Label(book_return_verification_tkinter_page_root,text=str(main_number_of_pages_for_showing_in_book_return),font=("verdana", 20),width=20,anchor='w').place(x=460,y=250)
    Label(book_return_verification_tkinter_page_root,text=main_book_cover_for_showing_in_book_return,font=("verdana", 20),width=20,anchor='w').place(x=1245,y=250)
    Label(book_return_verification_tkinter_page_root,text=main_issue_date_for_showing_in_book_return,font=("verdana", 20),width=20,anchor='w').place(x=340,y=680)
    Label(book_return_verification_tkinter_page_root,text=main_return_date_for_showing_in_book_return,font=("verdana", 20),width=20,anchor='w').place(x=1270,y=680)

    first_scroll_for_return=scrolledtext.ScrolledText(book_return_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    second_scroll_for_return=scrolledtext.ScrolledText(book_return_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    first_scroll_for_return.insert(END,main_bookinfo_for_showing_in_book_return)
    second_scroll_for_return.insert(END,main_author_info_for_showing_in_book_return)
    first_scroll_for_return.place(x=330,y=400)
    second_scroll_for_return.place(x=1270,y=400)

    Button(book_return_verification_tkinter_page_root,text='Cancel',font=('verdana',25),cursor='hand2',command=librarymang_home_page_student_after_return_of_book).place(x=1000,y=800)
    Button(book_return_verification_tkinter_page_root,text='Return Book',font=('verdana',25),cursor='hand2',bg='red',command=returning_book_fn).place(x=700,y=800)
    photo = PhotoImage(file = "e.png")
    book_return_verification_tkinter_page_root.iconphoto(False, photo)


def obtaining_book_info_for_return(list_to_regard):
    global main_book_id_for_showing_in_book_return
    global main_bookname_for_showing_in_book_return
    global main_bookauthor_for_showing_in_book_return
    global main_bookinfo_for_showing_in_book_return
    global main_number_of_pages_for_showing_in_book_return
    global main_book_cover_for_showing_in_book_return
    global main_author_info_for_showing_in_book_return
    global main_issue_date_for_showing_in_book_return
    global main_return_date_for_showing_in_book_return

    query_for_book_last_return='''select * from bookdata where book_id='{0}';'''
    cursor_mysql.execute(query_for_book_last_return.format(list_to_regard[0]))
    new_list3=cursor_mysql.fetchall()


    main_book_id_for_showing_in_book_return=new_list3[0][0]
    main_bookname_for_showing_in_book_return=new_list3[0][1]
    main_bookauthor_for_showing_in_book_return=new_list3[0][2]
    main_number_of_pages_for_showing_in_book_return=new_list3[0][3]
    main_book_cover_for_showing_in_book_return=new_list3[0][6]
    main_bookinfo_for_showing_in_book_return=new_list3[0][4]
    if new_list3[0][5]==None:
        main_author_info_for_showing_in_book_return='No Information Available'
    else:
        main_author_info_for_showing_in_book_return=new_list3[0][5]

    query_for_books_return_2="select * from bookissue where book_id2='{0}';"
    cursor_mysql.execute(query_for_books_return_2.format(main_book_id_for_showing_in_book_return))
    newlist4=cursor_mysql.fetchall()
    list_local_issuedate=(str(newlist4[0][2])).split('-')
    list_local_returndate=(str(newlist4[0][3])).split('-')
    yearissue=list_local_issuedate[0]
    monthissue=list_local_issuedate[1]
    dayissue=list_local_issuedate[2]
    yearreturn=list_local_returndate[0]
    monthreturn=list_local_returndate[1]
    dayreturn=list_local_returndate[2]
    main_issue_date_for_showing_in_book_return=dayissue+'-'+monthissue+'-'+yearissue
    main_return_date_for_showing_in_book_return=dayreturn+'-'+monthreturn+'-'+yearreturn


def returning_book_fn():
    query1="select * from bookissue where book_id2='{0}';"
    cursor_mysql.execute(query1.format(main_book_id_for_showing_in_book_return))
    out1=cursor_mysql.fetchall()
    bookid=main_book_id_for_showing_in_book_return
    query2="select * from loginissue where username='{0}';"
    cursor_mysql.execute(query2.format(user_username))
    out2=cursor_mysql.fetchall()
    user=out2[0][0]
    i1=out2[0][1]
    i2=out2[0][2]
    i3=out2[0][3]
    ref=0
    if (i1==bookid) and i2==None and i3==None:
        query="update loginissue set book_id1=Null where username='{0}';"
        query0="update bookissue set username=Null,date_of_issue=Null,date_of_return=Null where book_id2='{0}';"
        cursor_mysql.execute(query.format(user_username))
        mycon.commit()
        a=1
        cursor_mysql.execute(query0.format(main_book_id_for_showing_in_book_return))
        mycon.commit()
        ref=1

    elif (i1==bookid) and i3==None and i2!=None:
        query="update loginissue set book_id1='{0}',book_id2=Null where username='{1}';"
        query0="update bookissue set username=Null,date_of_issue=Null,date_of_return=Null where book_id2='{0}';"
        cursor_mysql.execute(query.format(i2,user_username))
        mycon.commit()
        a=1
        cursor_mysql.execute(query0.format(main_book_id_for_showing_in_book_return))
        mycon.commit()
        ref=1

    elif (i1==bookid) and i2!=None and i3!=None:
        query="update loginissue set book_id1='{0}',book_id2='{1}',book_id3=Null where username='{2}';"
        query0="update bookissue set username=Null,date_of_issue=Null,date_of_return=Null where book_id2='{0}';"
        cursor_mysql.execute(query.format(i2,i3,user_username))
        mycon.commit()
        a=1
        cursor_mysql.execute(query0.format(main_book_id_for_showing_in_book_return))
        mycon.commit()
        ref=1

    elif (i2==bookid) and i3==None and i1!=None:
        query="update loginissue set book_id2=Null where username='{0}';"
        query0="update bookissue set username=Null,date_of_issue=Null,date_of_return=Null where book_id2='{0}';"
        cursor_mysql.execute(query.format(user_username))
        mycon.commit()
        a=1
        cursor_mysql.execute(query0.format(main_book_id_for_showing_in_book_return))
        mycon.commit()
        ref=1
    elif (i2==bookid) and i3!=None and i1!=None:
        query="update loginissue set book_id2='{0}',book_id3=Null where username='{1}';"
        query0="update bookissue set username=Null,date_of_issue=Null,date_of_return=Null where book_id2='{0}';"
        cursor_mysql.execute(query.format(i3,user_username))
        mycon.commit()
        a=1
        cursor_mysql.execute(query0.format(main_book_id_for_showing_in_book_return))
        mycon.commit()
        ref=1
    elif (i3==bookid) and i1!=None and i2!=None:
        query="update loginissue set book_id3=Null where username='{0}';"
        query0="update bookissue set username=Null,date_of_issue=Null,date_of_return=Null where book_id2='{0}';"
        cursor_mysql.execute(query.format(user_username))
        mycon.commit()
        a=1
        cursor_mysql.execute(query0.format(main_book_id_for_showing_in_book_return))
        mycon.commit()
        ref=1

    if ref==1:
        messagebox.showinfo('success','You have returned The book : '+main_bookname_for_showing_in_book_return)
        librarymang_home_page_student_after_return_of_book()
    else:
        messagebox.showinfo('oops','Something Went Wrong')
        librarymang_home_page_student_after_return_of_book()


#***********************************************************************************************************************************************************************************

def searcher_bar_mid_fn():
    global search_bar_borrow_books_student_page_var
    global search_bar_borrow_books_student_page
    global dict_of_non_issued_books
    global count_of_books_for_non_issued
    search_bar_borrow_books_student_page_1=search_bar_borrow_books_student_page_var.get()
    search_bar_borrow_books_student_page=search_bar_borrow_books_student_page_1.lower()
    if count_of_books_for_non_issued==0:
        if_no_books_to_borrow()
    elif count_of_books_for_non_issued<=12:
        if_there_is_no_scroll_from_mifn()
    else:
        if_there_is_scroll_in_issue_from_mifn()


def if_there_is_scroll_in_issue_from_mifn():
    global count_of_books_for_non_issued
    global dict_of_non_issued_books
    global list_of_non_issued_books
    global search_bar_borrow_books_student_page
    global variable_list_order_2
    variable_list_order_2=[]

    #search bar

    if search_bar_borrow_books_student_page=='':
        searaching_and_reodering_radiobutton_of_issue_page_for_scroll(list_of_non_issued_books)
    else:
        pass
        for sample in list_of_non_issued_books:
            if (sample[0].lower()==search_bar_borrow_books_student_page) and (sample[1].lower()==search_bar_borrow_books_student_page) and (sample[2].lower()==search_bar_borrow_books_student_page) and ((sample[1].lower()).startswith(search_bar_borrow_books_student_page)) and ((sample[2].lower()).startswith(search_bar_borrow_books_student_page)) and ((sample[1].lower()).endswith(search_bar_borrow_books_student_page)) and ((sample[2].lower()).endswith(search_bar_borrow_books_student_page)) and (search_bar_borrow_books_student_page in sample[1].lower()) and (search_bar_borrow_books_student_page in sample[2].lower()):
                variable_list_order_2.append(sample)
            else:
                continue
        for sample2 in list_of_non_issued_books:
            if (sample2 not in variable_list_order_2) and (sample2[0].lower()==search_bar_borrow_books_student_page):
                variable_list_order_2.append(sample2)
            else:
                continue
        for sample3 in list_of_non_issued_books:
            if (sample3 not in variable_list_order_2) and (sample3[1].lower()==search_bar_borrow_books_student_page):
                variable_list_order_2.append(sample3)
            else:
                continue
        for sample4 in list_of_non_issued_books:
            if (sample4 not in variable_list_order_2) and (sample4[2].lower()==search_bar_borrow_books_student_page):
                variable_list_order_2.append(sample4)
            else:
                continue
        for sample5 in list_of_non_issued_books:
            if (sample5 not in variable_list_order_2) and ((sample5[1].lower()).startswith(search_bar_borrow_books_student_page)):
                variable_list_order_2.append(sample5)
            else:
                continue
        for sample6 in list_of_non_issued_books:
            if (sample6 not in variable_list_order_2) and ((sample6[2].lower()).startswith(search_bar_borrow_books_student_page)):
                variable_list_order_2.append(sample6)
            else:
                continue
        for sample7 in list_of_non_issued_books:
            if (sample7 not in variable_list_order_2) and ((sample7[1].lower()).endswith(search_bar_borrow_books_student_page)):
                variable_list_order_2.append(sample7)
            else:
                continue
        for sample8 in list_of_non_issued_books:
            if (sample8 not in variable_list_order_2) and ((sample8[2].lower()).endswith(search_bar_borrow_books_student_page)):
                variable_list_order_2.append(sample8)
            else:
                continue
        for sample9 in list_of_non_issued_books:
            if (sample9 not in variable_list_order_2) and (search_bar_borrow_books_student_page in sample9[1].lower()):
                variable_list_order_2.append(sample9)
            else:
                continue
        for sample10 in list_of_non_issued_books:
            if (sample10 not in variable_list_order_2) and (search_bar_borrow_books_student_page in sample10[2].lower()):
                variable_list_order_2.append(sample10)
            else:
                continue 
        for sample11 in list_of_non_issued_books:
            if sample11 not in variable_list_order_2:
                variable_list_order_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_issue_page_for_scroll(variable_list_order_2)



def searaching_and_reodering_radiobutton_of_issue_page_for_scroll(list_ordered):
    global book_name_select_for_issue_var
    global count_of_books_for_non_issued
    global dict_of_non_issued_books
    global list_of_non_issued_books
    global search_bar_borrow_books_student_page
    global variable_list_order_2

    innerframe=LabelFrame(borrow_books_student_page_root,text='books',bd=15,width=1000)
    innerframe.place(x=600,y=300)

    #Creating Main fram:
    main_frame=Frame(innerframe,width=1000)
    main_frame.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva=Canvas(main_frame,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll=ttk.Scrollbar(main_frame,orient=VERTICAL,command=canva.yview) 
    scroll.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva.configure(yscrollcommand=scroll.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva.bind('<Configure>', lambda e: canva.configure(scrollregion=canva.bbox("all")))
    #Creating another frame inside canvas
    second_frame=Frame(canva,width=1000)
    #placing the second frame inside canva
    canva.create_window((0,0),window=second_frame,anchor='nw',)#nw means on the top right corner


    book_name_select_for_issue_var=IntVar()

    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(second_frame,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_issue_var,value=i[3],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_issue_var,value=i[3],width=50,bg='cyan',padx=10,anchor='w').pack()




def if_there_is_no_scroll_from_mifn():
    global count_of_books_for_non_issued
    global dict_of_non_issued_books
    global list_of_non_issued_books
    global search_bar_borrow_books_student_page
    global variable_list_order
    global variable_list_order_2
    variable_list_order=[]
    variable_list_order_2=[]


    #search Bar operation

    if search_bar_borrow_books_student_page=='':
        searaching_and_reodering_radiobutton_of_issue_page_for_no_scroll(list_of_non_issued_books)
    else:        
        for sample in list_of_non_issued_books:
            if (sample[0].lower()==search_bar_borrow_books_student_page) and (sample[1].lower()==search_bar_borrow_books_student_page) and (sample[2].lower()==search_bar_borrow_books_student_page) and ((sample[1].lower()).startswith(search_bar_borrow_books_student_page)) and ((sample[2].lower()).startswith(search_bar_borrow_books_student_page)) and ((sample[1].lower()).endswith(search_bar_borrow_books_student_page)) and ((sample[2].lower()).endswith(search_bar_borrow_books_student_page)) and (search_bar_borrow_books_student_page in sample[1].lower()) and (search_bar_borrow_books_student_page in sample[2].lower()):
                variable_list_order_2.append(sample)
            else:
                continue
        for sample2 in list_of_non_issued_books:
            if (sample2 not in variable_list_order_2) and (sample2[0].lower()==search_bar_borrow_books_student_page):
                variable_list_order_2.append(sample2)
            else:
                continue
        for sample3 in list_of_non_issued_books:
            if (sample3 not in variable_list_order_2) and (sample3[1].lower()==search_bar_borrow_books_student_page):
                variable_list_order_2.append(sample3)
            else:
                continue
        for sample4 in list_of_non_issued_books:
            if (sample4 not in variable_list_order_2) and (sample4[2].lower()==search_bar_borrow_books_student_page):
                variable_list_order_2.append(sample4)
            else:
                continue
        for sample5 in list_of_non_issued_books:
            if (sample5 not in variable_list_order_2) and ((sample5[1].lower()).startswith(search_bar_borrow_books_student_page)):
                variable_list_order_2.append(sample5)
            else:
                continue
        for sample6 in list_of_non_issued_books:
            if (sample6 not in variable_list_order_2) and ((sample6[2].lower()).startswith(search_bar_borrow_books_student_page)):
                variable_list_order_2.append(sample6)
            else:
                continue
        for sample7 in list_of_non_issued_books:
            if (sample7 not in variable_list_order_2) and ((sample7[1].lower()).endswith(search_bar_borrow_books_student_page)):
                variable_list_order_2.append(sample7)
            else:
                continue
        for sample8 in list_of_non_issued_books:
            if (sample8 not in variable_list_order_2) and ((sample8[2].lower()).endswith(search_bar_borrow_books_student_page)):
                variable_list_order_2.append(sample8)
            else:
                continue
        for sample9 in list_of_non_issued_books:
            if (sample9 not in variable_list_order_2) and (search_bar_borrow_books_student_page in sample9[1].lower()):
                variable_list_order_2.append(sample9)
            else:
                continue
        for sample10 in list_of_non_issued_books:
            if (sample10 not in variable_list_order_2) and (search_bar_borrow_books_student_page in sample10[2].lower()):
                variable_list_order_2.append(sample10)
            else:
                continue
        for sample11 in list_of_non_issued_books:
            if sample11 not in variable_list_order_2:
                variable_list_order_2.append(sample11)
            else:
                pass
        searaching_and_reodering_radiobutton_of_issue_page_for_no_scroll(variable_list_order_2)




def searaching_and_reodering_radiobutton_of_issue_page_for_no_scroll(list_ordered):
    global book_name_select_for_issue_var
    global count_of_books_for_non_issued
    global dict_of_non_issued_books
    global list_of_non_issued_books
    global search_bar_borrow_books_student_page
    global variable_list_order
    variable_list_order=[]
    innerframe=LabelFrame(borrow_books_student_page_root,text='books',bd=15,width=1000)
    innerframe.place(x=600,y=300)

    #Creating Main fram:
    main_frame=Frame(innerframe,width=1000)
    main_frame.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_issue_var=IntVar()
    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(main_frame,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_issue_var,value=i[3],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_issue_var,value=i[3],width=50,bg='cyan',padx=10,anchor='w').pack()



def if_there_is_scroll_in_issue():
    global borrow_books_student_page_root
    global dict_of_non_issued_books
    innerframe=LabelFrame(borrow_books_student_page_root,text='books',bd=15,width=1000)
    innerframe.place(x=600,y=300)

    #Creating Main fram:
    main_frame=Frame(innerframe,width=1000)
    main_frame.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva=Canvas(main_frame,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll=ttk.Scrollbar(main_frame,orient=VERTICAL,command=canva.yview) 
    scroll.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva.configure(yscrollcommand=scroll.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva.bind('<Configure>', lambda e: canva.configure(scrollregion=canva.bbox("all")))
    #Creating another frame inside canvas
    second_frame=Frame(canva,width=1000)
    #placing the second frame inside canva
    canva.create_window((0,0),window=second_frame,anchor='nw',)#nw means on the top right corner
    global book_name_select_for_issue_var
    book_name_select_for_issue_var=IntVar()
    for i in range(1,count_of_books_for_non_issued+1):
        if i%2==0:
            Radiobutton(second_frame,text=dict_of_non_issued_books[i][1]+'        (   by  '+dict_of_non_issued_books[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_issue_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame,text=dict_of_non_issued_books[i][1]+'        (   by  '+dict_of_non_issued_books[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_issue_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()


def if_there_is_no_scroll():
    global dict_of_non_issued_books
    global count_of_books_for_non_issued

    innerframe=LabelFrame(borrow_books_student_page_root,text='books',bd=15,width=1000,)
    innerframe.place(x=600,y=300)

    #Creating Main fram:
    main_frame=Frame(innerframe,width=1000)
    main_frame.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    global book_name_select_for_issue_var
    book_name_select_for_issue_var=IntVar()
    for i in range(1,count_of_books_for_non_issued+1):
        if i%2==0:
            Radiobutton(main_frame,text=dict_of_non_issued_books[i][1]+'        (   by  '+dict_of_non_issued_books[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_issue_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame,text=dict_of_non_issued_books[i][1]+'        (   by  '+dict_of_non_issued_books[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_issue_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()

def if_no_books_to_borrow():
    global book_name_select_for_issue
    global book_name_select_for_issue_var
    book_name_select_for_issue_var=book_name_select_for_issue='chumma'
    Label(borrow_books_student_page_root,text="There are no books available right now",font=("lucida handwriting", 30),bg='black',fg='white').place(x=500,y=500)



def creating_dict_table_for_issue():

    global count_of_books_for_non_issued
    global dict_of_non_issued_books
    global list_of_non_issued_books
    list_of_non_issued_books=[]
    dict_of_non_issued_books={}

    query1="select book_id2 from bookissue;"
    cursor_mysql.execute(query1)
    out3_1=cursor_mysql.fetchall()
    query2="select book_id,bookname,bookauthor from bookdata;"
    cursor_mysql.execute(query2)
    out3_2=cursor_mysql.fetchall()
    if out3_1==[]:
        for tups3_1 in out3_2:
            list_of_non_issued_books.append([tups3_1[0],tups3_1[1],tups3_1[2]])
        count_of_books_for_non_issued=len(list_of_non_issued_books)
        if count_of_books_for_non_issued==0:
            dict_of_non_issued_books={}
            list_of_non_issued_books=[]
        else:
            for i in range(1,count_of_books_for_non_issued+1):
                dict_of_non_issued_books[i]=list_of_non_issued_books[i-1]
                list_of_non_issued_books[i-1].append(i)
    else:
        query="select book_id2,username from bookissue;"
        cursor_mysql.execute(query)
        out3=cursor_mysql.fetchall()
        query122="select book_id,bookname,bookauthor from bookdata;"
        cursor_mysql.execute(query122)
        out322=cursor_mysql.fetchall()
        dict1={}
        dict2={}
        for p in out322:
            dict1[p[0]]=[p[1],p[2]]
        for t in out3:
            dict2[t[0]]=[t[1],]
        for q in dict1:
            if dict2[q][0]==None:
                list_of_non_issued_books.append([q,dict1[q][0],dict1[q][1]])
            else:
                continue
        count_of_books_for_non_issued=len(list_of_non_issued_books)
        if count_of_books_for_non_issued==0:
            dict_of_non_issued_books={}
            list_of_non_issued_books=[]
        else:
            for i in range(1,count_of_books_for_non_issued+1):
                dict_of_non_issued_books[i]=list_of_non_issued_books[i-1]
                list_of_non_issued_books[i-1].append(i)



def clicking_proceed_in_borrow_fn():
    global book_name_select_for_issue_var
    global main_list_regarding_book_and_author_info
    global dict_of_non_issued_books

    try:
        book_name_select_for_issue=book_name_select_for_issue_var.get()
    except:
        book_name_select_for_issue='chumma'
    main_list_regarding_book_and_author_info=[]
    if book_name_select_for_issue==0:
        messagebox.showerror('issue book','please select a book to borrow')
    elif book_name_select_for_issue=='chumma' or book_name_select_for_issue_var=='chumma':
        messagebox.showinfo('oops','There are no books availiable right now')
        librarymang_home_page_student_from_the_borrow_book_page()
    else:
        main_list_regarding_book_and_author_info=dict_of_non_issued_books[book_name_select_for_issue][0:3]   #just so that the 4th column is taken
        book_issue_verification_tkinter_page()






def return_date_findding_fn(daystoadd):
    today_date=date.today()
    ret_date=today_date+timedelta(days=daystoadd)
    return str(ret_date)




def check_for_issue_period_and_mid_fn():
    global period_of_issue_var
    global period_of_issue_list
    global period_of_issue
    query="select * from loginissue;"
    cursor_mysql.execute(query)
    out=cursor_mysql.fetchall()
    for tups_dup in out:
        if tups_dup[0]==user_username:
            issue1=tups_dup[1]
            issue2=tups_dup[2]
            issue3=tups_dup[3]
        else:
            continue
    period_of_issue=period_of_issue_var.get()
    ref=0
    if issue3!=None:
        messagebox.showerror('issue books','You Have Already Issued 3 Books Please Return Them to Borrow More')
        ref=1
    elif period_of_issue not in period_of_issue_list:
        messagebox.showerror('issue books','please enter period of issue')
        ref=2
    else:
        if period_of_issue=='3 days':
            date_of_return=return_date_findding_fn(3)
        elif period_of_issue=='7 days':
            date_of_return=return_date_findding_fn(7)
        elif period_of_issue=='14 days':
            date_of_return=return_date_findding_fn(14)
        elif period_of_issue=='28 days':
            date_of_return=return_date_findding_fn(28)
        else:
            date_of_return=return_date_findding_fn(56)

    if ref==1:
        force_exit_from_borrow_due_to_more_than_3_issue_to_librarymang_home_page_student()
        
    elif ref==2:
        pass

    else:
        issuing_books_fn(issue1,issue2,issue3,date_of_return)
        messagebox.showinfo('success','Book has been Succesfully Issued')
        librarymang_home_page_student_after_issue_of_book()

def issuing_books_fn(i1,i2,i3,dateret):
    global user_username
    global main_book_id_for_showing_in_book_issue
    dateissue=str(date.today())
    datereturn=dateret
    bookId=main_book_id_for_showing_in_book_issue
    if i1==None:
        query1='''update bookissue set username="{0}",date_of_issue="{1}",date_of_return="{2}" where book_id2="{3}";'''
        cursor_mysql.execute(query1.format(user_username,dateissue,datereturn,bookId))
        mycon.commit()
        username=user_username
        query2='''update loginissue set book_id1="{0}" where username="{1}";'''
        cursor_mysql.execute(query2.format(bookId,username))
        mycon.commit()
    elif i2==None:
        query1='''update bookissue set username="{0}",date_of_issue="{1}",date_of_return="{2}" where book_id2="{3}";'''
        cursor_mysql.execute(query1.format(user_username,dateissue,datereturn,bookId))
        mycon.commit()
        username=user_username
        query2='''update loginissue set book_id2="{0}" where username="{1}";'''
        cursor_mysql.execute(query2.format(bookId,username))
        mycon.commit()
    elif i3==None:
        query1='''update bookissue set username="{0}",date_of_issue="{1}",date_of_return="{2}" where book_id2="{3}";'''
        cursor_mysql.execute(query1.format(user_username,dateissue,datereturn,bookId))
        mycon.commit()
        username=user_username
        query2='''update loginissue set book_id3="{0}" where username="{1}";'''
        cursor_mysql.execute(query2.format(bookId,username))
        mycon.commit()
    else:
        messagebox.showerror('issue books','You Have Already Issued 3 Books Please Return Them to Borrow More')
        force_exit_from_borrow_due_to_more_than_3_issue_to_librarymang_home_page_student()


def obtaining_book_info(list_to_regard):
    global main_book_id_for_showing_in_book_issue
    global main_bookname_for_showing_in_book_issue
    global main_bookauthor_for_showing_in_book_issue
    global main_number_of_pages_for_showing_in_book_issue
    global main_book_cover_for_showing_in_book_issue
    global main_bookinfo_for_showing_in_book_issue
    global main_author_info_for_showing_in_book_issue

    query_for_book_last_issue='''select * from bookdata where book_id='{0}';'''
    cursor_mysql.execute(query_for_book_last_issue.format(list_to_regard[0]))
    new_list=cursor_mysql.fetchall()

    main_book_id_for_showing_in_book_issue=new_list[0][0]
    main_bookname_for_showing_in_book_issue=new_list[0][1]
    main_bookauthor_for_showing_in_book_issue=new_list[0][2]
    main_number_of_pages_for_showing_in_book_issue=new_list[0][3]
    main_book_cover_for_showing_in_book_issue=new_list[0][6]
    main_bookinfo_for_showing_in_book_issue=new_list[0][4]
    if new_list[0][5]==None:
        main_author_info_for_showing_in_book_issue='No Information Available'
    else:
        main_author_info_for_showing_in_book_issue=new_list[0][5]






def book_issue_verification_tkinter_page():
    global main_list_regarding_book_and_author_info
    global book_issue_verification_tkinter_page_root
    global period_of_issue_list
    global period_of_issue_var

    borrow_books_student_page_root.destroy()

    book_issue_verification_tkinter_page_root=Tk()
    book_issue_verification_tkinter_page_root.title('Borrow Books')
    book_issue_verification_tkinter_page_root.state("zoomed")

    book_issue_verification_tkinter_page_root.config(background = "black", pady=10)

    obtaining_book_info(main_list_regarding_book_and_author_info)

    Label(book_issue_verification_tkinter_page_root,text="Book Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=700,y=20)
    Label(book_issue_verification_tkinter_page_root,text="Book Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(book_issue_verification_tkinter_page_root,text="Book Author:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(book_issue_verification_tkinter_page_root,text="Number Of Pages:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=250)
    Label(book_issue_verification_tkinter_page_root,text="Book Cover:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=250)
    Label(book_issue_verification_tkinter_page_root,text="Book Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=400)
    Label(book_issue_verification_tkinter_page_root,text="Author Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=400)

    Label(book_issue_verification_tkinter_page_root,text=main_book_id_for_showing_in_book_issue,font=("verdana", 20),width=20,anchor='w').place(x=890,y=20)
    Label(book_issue_verification_tkinter_page_root,text=main_bookname_for_showing_in_book_issue,font=("verdana", 20),width=30,anchor='w').place(x=350,y=150)
    Label(book_issue_verification_tkinter_page_root,text=main_bookauthor_for_showing_in_book_issue,font=("verdana", 20),width=30,anchor='w').place(x=1275,y=150)
    Label(book_issue_verification_tkinter_page_root,text=main_number_of_pages_for_showing_in_book_issue,font=("verdana", 20),width=20,anchor='w').place(x=460,y=250)
    Label(book_issue_verification_tkinter_page_root,text=main_book_cover_for_showing_in_book_issue,font=("verdana", 20),width=20,anchor='w').place(x=1245,y=250)

    first_scroll=scrolledtext.ScrolledText(book_issue_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    second_scroll=scrolledtext.ScrolledText(book_issue_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    first_scroll.insert(END,main_bookinfo_for_showing_in_book_issue)
    second_scroll.insert(END,main_author_info_for_showing_in_book_issue)
    first_scroll.place(x=330,y=400)
    second_scroll.place(x=1270,y=400)
    global period_of_issue_list
    period_of_issue_list=['3 days','7 days','14 days','28 days','56 days']
    period_of_issue_var=StringVar()
    droplist_for_period_issue=OptionMenu(book_issue_verification_tkinter_page_root, period_of_issue_var, *period_of_issue_list)
    droplist_for_period_issue.config(width=30,font=("verdana", 10))
    period_of_issue_var.set('Select Period Of Issue')
    droplist_for_period_issue.place(x=800,y=700)

    Button(book_issue_verification_tkinter_page_root,text='Cancel',font=('verdana',25),cursor='hand2',command=librarymang_home_page_student_from_book_issue_verification_tkinter_page).place(x=1000,y=800)
    Button(book_issue_verification_tkinter_page_root,text='Issue Book',font=('verdana',25),cursor='hand2',bg='blue',command=check_for_issue_period_and_mid_fn).place(x=700,y=800)
    photo = PhotoImage(file = "e.png")
    book_issue_verification_tkinter_page_root.iconphoto(False, photo)


def borrow_books_student_page_fn():
    librarymang_home_page_student_root.destroy()
    global borrow_books_student_page_root
    global search_bar_borrow_books_student_page_var
    global search_bar_borrow_books_student_page
    global dict_of_non_issued_books
    global count_of_books_for_non_issued
    global search_bar_borrow_books_student_page_var

    borrow_books_student_page_root=Tk()
    borrow_books_student_page_root.title('Borrow books')
    borrow_books_student_page_root.state('zoomed')

    search_bar_borrow_books_student_page_var=StringVar()

    borrow_books_student_page_root.config(background = "black", pady=10)
    Label(borrow_books_student_page_root, text="Select Books to borrow",width=100, font=("freestyle script", 70)).pack()
    try:
        Entry(borrow_books_student_page_root, font=('verdana',30),textvariable=search_bar_borrow_books_student_page_var,width=50).place(x=250,y=200)
    except:
        messagebox.showinfo('error',"Dont type \" or  in any of the fields")
    Button(borrow_books_student_page_root,text='Search',cursor='hand2',font=('verdana',30),bg='grey',command=searcher_bar_mid_fn).place(x=1600,y=180)
    Button(borrow_books_student_page_root,text='Go Back',cursor='hand2',font=('verdana',30),command=librarymang_home_page_student_from_the_borrow_book_page).place(x=1050,y=900)
    Button(borrow_books_student_page_root,text='Proceed',cursor='hand2',font=('verdana',30),command=clicking_proceed_in_borrow_fn).place(x=750,y=900)
    photo = PhotoImage(file = "e.png")
    borrow_books_student_page_root.iconphoto(False, photo)


    #checking for issued books

    creating_dict_table_for_issue()


    if count_of_books_for_non_issued==0:
        if_no_books_to_borrow()
    elif count_of_books_for_non_issued<=12:
        if_there_is_no_scroll()
    else:
        if_there_is_scroll_in_issue()






#***********************************************************************************************************************************************************************************









def verification_for_add_books():
    global book_info_add_books_admin_page_text_var
    global author_info_add_books_admin_page_text_var
    global book_name_for_add_books_admin_page_var
    global author_name_for_add_books_admin_page_var
    global number_of_pages_add_books_admin_page_var
    global book_cover_type_for_add_books_admin_page_var
    global add_books_admin_page_root

    global book_name_for_add_books_admin_page
    global author_name_for_add_books_admin_page
    global number_of_pages_add_books_admin_page
    global book_cover_type_for_add_books_admin_page
    global book_info_add_books_admin_page_text
    global author_info_add_books_admin_page_text
    global bookid_for_add_books_admin_page

    book_name_for_add_books_admin_page=book_name_for_add_books_admin_page_var.get()
    author_name_for_add_books_admin_page=author_name_for_add_books_admin_page_var.get()
    number_of_pages_add_books_admin_page=number_of_pages_add_books_admin_page_var.get()
    book_cover_type_for_add_books_admin_page=book_cover_type_for_add_books_admin_page_var.get()
    book_info_add_books_admin_page_text=book_info_add_books_admin_page_text_var.get(1.0,'end-1c')
    author_info_add_books_admin_page_text=author_info_add_books_admin_page_text_var.get(1.0,'end-1c')
    
    query_for_bookid_for_add_books_admin_page='select book_id from bookdata;'
    cursor_mysql.execute(query_for_bookid_for_add_books_admin_page)
    output_for_add_books_admin_page=cursor_mysql.fetchall()
    newl=[]
    for tups in output_for_add_books_admin_page:
        newl.append(tups[0])

    while True:
        alphabet_part_of_bookid_for_add_books_admin_page=''
        alphas='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(4):
            alphabet_part_of_bookid_for_add_books_admin_page+=alphas[(random.randint(0,51))]
        numberpart_part_of_bookid_for_add_books_admin_page=random.randint(10000000,99999999)
        bookid_for_add_books_admin_page=alphabet_part_of_bookid_for_add_books_admin_page+str(numberpart_part_of_bookid_for_add_books_admin_page)
        if bookid_for_add_books_admin_page in newl:
            continue
        else:
            break

    ref_for_add_books_admin_page=0
    if book_name_for_add_books_admin_page=='':
        messagebox.showerror('error','please enter book name')
        ref_for_add_books_admin_page=1
    elif len(book_name_for_add_books_admin_page)>50:
        messagebox.showerror('error','Book name should be less than 51 characters')
        ref_for_add_books_admin_page=1
    else:
        pass
    if ref_for_add_books_admin_page==0 and author_name_for_add_books_admin_page=='':
        messagebox.showerror('error','please enter Authors name')
        ref_for_add_books_admin_page=2
    elif ref_for_add_books_admin_page==0 and len(author_name_for_add_books_admin_page)>50:
        messagebox.showerror('error','Author name cannot be more than 51 characters')
        ref_for_add_books_admin_page=2
    else:
        pass
    if ref_for_add_books_admin_page==0 and number_of_pages_add_books_admin_page=='':
        messagebox.showerror('error','please enter the number of pages')
        ref_for_add_books_admin_page=3
    elif ref_for_add_books_admin_page==0 and (not number_of_pages_add_books_admin_page.isdigit()):
        messagebox.showerror('error','number of pages must only contain numbers')
        ref_for_add_books_admin_page=3
    else:
        pass
    if ref_for_add_books_admin_page==0 and book_cover_type_for_add_books_admin_page==0:
        messagebox.showerror('error','please enter the book cover type')
        ref_for_add_books_admin_page=4
    else:
        pass
    if ref_for_add_books_admin_page==0 and book_info_add_books_admin_page_text=='':
        messagebox.showerror('error','please enter the book description')
        ref_for_add_books_admin_page=5
    elif ref_for_add_books_admin_page==0 and len(book_info_add_books_admin_page_text)>6000:
        messagebox.showerror('error','book info must be less than 6001 characters')
        ref_for_add_books_admin_page=5
    else:
        pass
    if ref_for_add_books_admin_page==0 and len(author_info_add_books_admin_page_text)>6000:
        messagebox.showerror('error','author info must be less than 6001 characters')
        ref_for_add_books_admin_page=6
    else:
        pass
    if ref_for_add_books_admin_page==0 and (('\'' in book_name_for_add_books_admin_page) or ('\"' in book_name_for_add_books_admin_page) or ('\'' in author_name_for_add_books_admin_page) or ('\"' in author_name_for_add_books_admin_page) or ('\'' in book_info_add_books_admin_page_text) or ('\"' in book_info_add_books_admin_page_text) or ('\'' in author_info_add_books_admin_page_text) or ('\"' in author_info_add_books_admin_page_text)):
        messagebox.showinfo('error','Dnot use \' or \" in any field')
        ref_for_add_books_admin_page=7
    if ref_for_add_books_admin_page==0:
        mid_for_add_fns()
    else:
        pass

def add_books_fn(local_book_id,local_book_name,local_book_author,local_book_number_pages,local_bookinfo,local_book_cover,local_authorinfo=0):

    
    if local_authorinfo==0:
        query='''insert into bookdata(book_id,bookname,bookauthor,number_of_pages,bookinfo,bookcover) values("{0}","{1}","{2}",{3},"{4}","{5}");'''
        cursor_mysql.execute(query.format(local_book_id,local_book_name,local_book_author,local_book_number_pages,local_bookinfo,local_book_cover))
        mycon.commit()
        bookid=local_book_id
        query_2="insert into bookissue(book_id2) values('{0}');"
        cursor_mysql.execute(query_2.format(bookid))
        mycon.commit()
        aftereadding()

    
    else:
        query='''insert into bookdata(book_id,bookname,bookauthor,number_of_pages,bookinfo,authorinfo,bookcover) values("{0}","{1}","{2}",{3},"{4}","{5}","{6}");'''
        cursor_mysql.execute(query.format(local_book_id,local_book_name,local_book_author,local_book_number_pages,local_bookinfo,local_authorinfo,local_book_cover))
        mycon.commit()
        bookid=local_book_id
        query_2="insert into bookissue(book_id2) values('{0}');"
        cursor_mysql.execute(query_2.format(bookid))
        mycon.commit()
        aftereadding()

def aftereadding():
    messagebox.showinfo('success','Book successfully added')
    librarymang_home_page_admin_after_adding()



def mid_for_add_fns():
    global book_name_for_add_books_admin_page
    global author_name_for_add_books_admin_page
    global number_of_pages_add_books_admin_page
    global book_cover_type_for_add_books_admin_page
    global book_info_add_books_admin_page_text
    global author_info_add_books_admin_page_text
    global real_book_cover_type_for_add_books_admin_page
    global real_number_of_pages_add_books_admin_page
    global bookid_for_add_books_admin_page

    if book_cover_type_for_add_books_admin_page==1:
        real_book_cover_type_for_add_books_admin_page='paperback'
    else:
        real_book_cover_type_for_add_books_admin_page='hardcover'

    real_number_of_pages_add_books_admin_page=int(number_of_pages_add_books_admin_page)

    if author_info_add_books_admin_page_text=='':
        add_books_fn(bookid_for_add_books_admin_page,book_name_for_add_books_admin_page,author_name_for_add_books_admin_page,real_number_of_pages_add_books_admin_page,book_info_add_books_admin_page_text,real_book_cover_type_for_add_books_admin_page)
    else:
        add_books_fn(bookid_for_add_books_admin_page,book_name_for_add_books_admin_page,author_name_for_add_books_admin_page,real_number_of_pages_add_books_admin_page,book_info_add_books_admin_page_text,real_book_cover_type_for_add_books_admin_page,author_info_add_books_admin_page_text)





def add_books_admin_page():
    librarymang_home_page_admin_root.destroy()
    global book_info_add_books_admin_page_text_var
    global author_info_add_books_admin_page_text_var
    global book_name_for_add_books_admin_page_var
    global author_name_for_add_books_admin_page_var
    global number_of_pages_add_books_admin_page_var
    global book_cover_type_for_add_books_admin_page_var
    global add_books_admin_page_root

    add_books_admin_page_root=Tk()
    add_books_admin_page_root.title('Add Book')
    add_books_admin_page_root.state('zoomed')
    add_books_admin_page_root.config(bg='black',pady=10)


    Label(add_books_admin_page_root, text="Add Books",width=100, font=("freestyle script", 70)).pack()
    Label(add_books_admin_page_root,text='Book name : ',font=("lucida handwriting", 30),bg='black',fg='white').place(x=50,y=200)
    Label(add_books_admin_page_root,text='Book Author : ',font=("lucida handwriting", 30),bg='black',fg='white').place(x=50,y=350)
    Label(add_books_admin_page_root,text='Author info : ',font=("lucida handwriting", 30),bg='black',fg='white').place(x=900,y=550)
    Label(add_books_admin_page_root,text='*optional',font=("lucida handwriting", 12),bg='black',fg='red').place(x=900,y=600)
    Label(add_books_admin_page_root,text='Book info   :',font=("lucida handwriting", 30),bg='black',fg='white').place(x=900,y=200)
    Label(add_books_admin_page_root,text='Number of pages :',font=("lucida handwriting", 30),bg='black',fg='white').place(x=50,y=550)
    Label(add_books_admin_page_root,text='Book Cover : ',font=("lucida handwriting", 30),bg='black',fg='white').place(x=50,y=750)
    
    book_info_add_books_admin_page_text_var=scrolledtext.ScrolledText(add_books_admin_page_root,wrap=WORD,bg='white',width=30,height=7,font=('verdana',20))
    author_info_add_books_admin_page_text_var=scrolledtext.ScrolledText(add_books_admin_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))

    book_name_for_add_books_admin_page_var=StringVar()
    author_name_for_add_books_admin_page_var=StringVar()
    number_of_pages_add_books_admin_page_var=StringVar()
    book_cover_type_for_add_books_admin_page_var=StringVar()
    
    Entry(add_books_admin_page_root,font=('verdana',20),textvariable=book_name_for_add_books_admin_page_var).place(x=370,y=210)
    Entry(add_books_admin_page_root,font=('verdana',20),textvariable=author_name_for_add_books_admin_page_var).place(x=400,y=360)
    Entry(add_books_admin_page_root,font=('verdana',20),width=5,textvariable=number_of_pages_add_books_admin_page_var).place(x=485,y=560)
    book_info_add_books_admin_page_text_var.place(x=1230,y=200)
    author_info_add_books_admin_page_text_var.place(x=1230,y=550)

    book_cover_type_for_add_books_admin_page_var=IntVar()
    Radiobutton(add_books_admin_page_root,text="Paperback",padx= 10,variable= book_cover_type_for_add_books_admin_page_var, value=1,font=('verdana',17)).place(x=370,y=760)
    Radiobutton(add_books_admin_page_root,text="Hardcover",padx= 10, variable= book_cover_type_for_add_books_admin_page_var, value=2,font=('verdana',17)).place(x=530,y=760)

    Button(add_books_admin_page_root,text='Add Book',font=('verdana',25),command=verification_for_add_books,cursor='hand2').place(x=800,y=800)
    Button(add_books_admin_page_root,text='Go Back',font=('verdana',25),command=librarymang_home_page_admin_after_adding,cursor='hand2').place(x=810,y=900)
    photo = PhotoImage(file = "e.png")
    add_books_admin_page_root.iconphoto(False, photo)






#***********************************************************************************************************************************************************************************






def searcher_bar_mid_fn_for_delete():
    global search_bar_delete_books_student_page_var
    global search_bar_delete_books_student_page
    global dict_of_books_for_delete
    global count_of_books_for_delete
    search_bar_delete_books_student_page_2=search_bar_delete_books_student_page_var.get()
    search_bar_delete_books_student_page=search_bar_delete_books_student_page_2.lower()
    if count_of_books_for_delete==0:
        no_books_to_delete()
    elif count_of_books_for_delete<=12:
        no_scroll_for_delete_mid_fn()
    else:
        if_is_scroll_for_delete_for_mid_fn()





def if_is_scroll_for_delete_for_mid_fn():
    global count_of_books_for_delete
    global dict_of_books_for_delete
    global list_of_books_for_delete
    global search_bar_delete_books_student_page
    global variable_list_order_for_delete_2
    variable_list_order_for_delete_2=[]

    #search bar

    if search_bar_delete_books_student_page=='':
        searaching_and_reodering_radiobutton_of_delete_page_for_scroll(list_of_books_for_delete)
    else:
        pass
        for sample in list_of_books_for_delete:
            if (sample[0].lower()==search_bar_delete_books_student_page) and (sample[1].lower()==search_bar_delete_books_student_page) and (sample[2].lower()==search_bar_delete_books_student_page) and ((sample[1].lower()).startswith(search_bar_delete_books_student_page)) and ((sample[2].lower()).startswith(search_bar_delete_books_student_page)) and ((sample[1].lower()).endswith(search_bar_delete_books_student_page)) and ((sample[2].lower()).endswith(search_bar_delete_books_student_page)) and (search_bar_delete_books_student_page in sample[1].lower()) and (search_bar_delete_books_student_page in sample[2].lower()):
                variable_list_order_for_delete_2.append(sample)
            else:
                continue
        for sample2 in list_of_books_for_delete:
            if (sample2 not in variable_list_order_for_delete_2) and (sample2[0].lower()==search_bar_delete_books_student_page):
                variable_list_order_for_delete_2.append(sample2)
            else:
                continue
        for sample3 in list_of_books_for_delete:
            if (sample3 not in variable_list_order_for_delete_2) and (sample3[1].lower()==search_bar_delete_books_student_page):
                variable_list_order_for_delete_2.append(sample3)
            else:
                continue
        for sample4 in list_of_books_for_delete:
            if (sample4 not in variable_list_order_for_delete_2) and (sample4[2].lower()==search_bar_delete_books_student_page):
                variable_list_order_for_delete_2.append(sample4)
            else:
                continue
        for sample5 in list_of_books_for_delete:
            if (sample5 not in variable_list_order_for_delete_2) and ((sample5[1].lower()).startswith(search_bar_delete_books_student_page)):
                variable_list_order_for_delete_2.append(sample5)
            else:
                continue
        for sample6 in list_of_books_for_delete:
            if (sample6 not in variable_list_order_for_delete_2) and ((sample6[2].lower()).startswith(search_bar_delete_books_student_page)):
                variable_list_order_for_delete_2.append(sample6)
            else:
                continue
        for sample7 in list_of_books_for_delete:
            if (sample7 not in variable_list_order_for_delete_2) and ((sample7[1].lower()).endswith(search_bar_delete_books_student_page)):
                variable_list_order_for_delete_2.append(sample7)
            else:
                continue
        for sample8 in list_of_books_for_delete:
            if (sample8 not in variable_list_order_for_delete_2) and ((sample8[2].lower()).endswith(search_bar_delete_books_student_page)):
                variable_list_order_for_delete_2.append(sample8)
            else:
                continue
        for sample9 in list_of_books_for_delete:
            if (sample9 not in variable_list_order_for_delete_2) and (search_bar_delete_books_student_page in sample9[1].lower()):
                variable_list_order_for_delete_2.append(sample9)
            else:
                continue
        for sample10 in list_of_books_for_delete:
            if (sample10 not in variable_list_order_for_delete_2) and (search_bar_delete_books_student_page in sample10[2].lower()):
                variable_list_order_for_delete_2.append(sample10)
            else:
                continue
        for sample11 in list_of_books_for_delete:
            if sample11 not in variable_list_order_for_delete_2:
                variable_list_order_for_delete_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_delete_page_for_scroll(variable_list_order_for_delete_2)





def searaching_and_reodering_radiobutton_of_delete_page_for_scroll(list_ordered):
    global book_name_select_for_delete_var
    global count_of_books_for_delete
    global dict_of_books_for_delete
    global list_of_books_for_delete
    global search_bar_delete_books_student_page
    global variable_list_order_for_delete_2
    variable_list_order_for_delete_2=[]



    innerframe2=LabelFrame(delete_books_admin_page_root,text='books',bd=15,width=1000)
    innerframe2.place(x=600,y=300)

    #Creating Main fram:
    main_frame2=Frame(innerframe2,width=1000)
    main_frame2.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva2=Canvas(main_frame2,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva2.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll2=ttk.Scrollbar(main_frame2,orient=VERTICAL,command=canva2.yview) 
    scroll2.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva2.configure(yscrollcommand=scroll2.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva2.bind('<Configure>', lambda e: canva2.configure(scrollregion=canva2.bbox("all")))
    #Creating another frame inside canvas
    second_frame2=Frame(canva2,width=1000)
    #placing the second frame inside canva
    canva2.create_window((0,0),window=second_frame2,anchor='nw',)#nw means on the top right corner


    book_name_select_for_delete_var=IntVar()

    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(second_frame2,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_delete_var,value=i[3],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame2,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_delete_var,value=i[3],width=50,bg='cyan',padx=10,anchor='w').pack()














def no_scroll_for_delete_mid_fn():
    global count_of_books_for_delete
    global dict_of_books_for_delete
    global list_of_books_for_delete
    global search_bar_delete_books_student_page
    global variable_list_order_for_delete_2
    variable_list_order_for_delete_2=[]


    #search Bar operation

    if search_bar_delete_books_student_page=='':
        searaching_and_reodering_radiobutton_of_delete_page_for_no_scroll(list_of_books_for_delete)
    else:
        pass
        for sample in list_of_books_for_delete:
            if (sample[0].lower()==search_bar_delete_books_student_page) and (sample[1].lower()==search_bar_delete_books_student_page) and (sample[2].lower()==search_bar_delete_books_student_page) and ((sample[1].lower()).startswith(search_bar_delete_books_student_page)) and ((sample[2].lower()).startswith(search_bar_delete_books_student_page)) and ((sample[1].lower()).endswith(search_bar_delete_books_student_page)) and ((sample[2].lower()).endswith(search_bar_delete_books_student_page)) and (search_bar_delete_books_student_page in sample[1].lower()) and (search_bar_delete_books_student_page in sample[2].lower()):
                variable_list_order_for_delete_2.append(sample)
            else:
                continue
        for sample2 in list_of_books_for_delete:
            if (sample2 not in variable_list_order_for_delete_2) and (sample2[0].lower()==search_bar_delete_books_student_page):
                variable_list_order_for_delete_2.append(sample2)
            else:
                continue
        for sample3 in list_of_books_for_delete:
            if (sample3 not in variable_list_order_for_delete_2) and (sample3[1].lower()==search_bar_delete_books_student_page):
                variable_list_order_for_delete_2.append(sample3)
            else:
                continue
        for sample4 in list_of_books_for_delete:
            if (sample4 not in variable_list_order_for_delete_2) and (sample4[2].lower()==search_bar_delete_books_student_page):
                variable_list_order_for_delete_2.append(sample4)
            else:
                continue
        for sample5 in list_of_books_for_delete:
            if (sample5 not in variable_list_order_for_delete_2) and ((sample5[1].lower()).startswith(search_bar_delete_books_student_page)):
                variable_list_order_for_delete_2.append(sample5)
            else:
                continue
        for sample6 in list_of_books_for_delete:
            if (sample6 not in variable_list_order_for_delete_2) and ((sample6[2].lower()).startswith(search_bar_delete_books_student_page)):
                variable_list_order_for_delete_2.append(sample6)
            else:
                continue
        for sample7 in list_of_books_for_delete:
            if (sample7 not in variable_list_order_for_delete_2) and ((sample7[1].lower()).endswith(search_bar_delete_books_student_page)):
                variable_list_order_for_delete_2.append(sample7)
            else:
                continue
        for sample8 in list_of_books_for_delete:
            if (sample8 not in variable_list_order_for_delete_2) and ((sample8[2].lower()).endswith(search_bar_delete_books_student_page)):
                variable_list_order_for_delete_2.append(sample8)
            else:
                continue
        for sample9 in list_of_books_for_delete:
            if (sample9 not in variable_list_order_for_delete_2) and (search_bar_delete_books_student_page in sample9[1].lower()):
                variable_list_order_for_delete_2.append(sample9)
            else:
                continue
        for sample10 in list_of_books_for_delete:
            if (sample10 not in variable_list_order_for_delete_2) and (search_bar_delete_books_student_page in sample10[2].lower()):
                variable_list_order_for_delete_2.append(sample10)
            else:
                continue
        for sample11 in list_of_books_for_delete:
            if sample11 not in variable_list_order_for_delete_2:
                variable_list_order_for_delete_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_delete_page_for_no_scroll(variable_list_order_for_delete_2)


def searaching_and_reodering_radiobutton_of_delete_page_for_no_scroll(list_ordered):
    global book_name_select_for_delete_var
    global count_of_books_for_delete
    global dict_of_books_for_delete
    global list_of_books_for_delete
    global search_bar_delete_books_student_page
    global variable_list_order_for_delete_2
    variable_list_order_for_delete_2=[]
    innerframe2=LabelFrame(delete_books_admin_page_root,text='books',bd=15,width=1000)
    innerframe2.place(x=600,y=300)

    #Creating Main fram:
    main_frame2=Frame(innerframe2,width=1000)
    main_frame2.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_delete_var=IntVar()
    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(main_frame2,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_delete_var,value=i[3],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame2,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_delete_var,value=i[3],width=50,bg='cyan',padx=10,anchor='w').pack()








def if_is_scroll_for_delete_fn():

    global delete_books_admin_page_root
    global dict_of_books_for_delete
    innerframe2=LabelFrame(delete_books_admin_page_root,text='books',bd=15,width=1000)
    innerframe2.place(x=600,y=300)

    #Creating Main fram:
    main_frame2=Frame(innerframe2,width=1000)
    main_frame2.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva2=Canvas(main_frame2,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva2.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll2=ttk.Scrollbar(main_frame2,orient=VERTICAL,command=canva2.yview) 
    scroll2.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva2.configure(yscrollcommand=scroll2.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva2.bind('<Configure>', lambda e: canva2.configure(scrollregion=canva2.bbox("all")))
    #Creating another frame inside canvas
    second_frame2=Frame(canva2,width=1000)
    #placing the second frame inside canva
    canva2.create_window((0,0),window=second_frame2,anchor='nw',)#nw means on the top right corner
    global book_name_select_for_delete_var
    book_name_select_for_delete_var=IntVar()
    for i in range(1,count_of_books_for_delete+1):
        if i%2==0:
            Radiobutton(second_frame2,text=dict_of_books_for_delete[i][1]+'        (   by  '+dict_of_books_for_delete[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_delete_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame2,text=dict_of_books_for_delete[i][1]+'        (   by  '+dict_of_books_for_delete[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_delete_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()








def no_scroll_for_delete_fn():
    global dict_of_books_for_delete
    global count_of_books_for_delete

    innerframe2=LabelFrame(delete_books_admin_page_root,text='books',bd=15,width=1000,)
    innerframe2.place(x=600,y=300)

    #Creating Main fram:
    main_frame2=Frame(innerframe2,width=1000)
    main_frame2.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    global book_name_select_for_delete_var
    book_name_select_for_delete_var=IntVar()
    for i in range(1,count_of_books_for_delete+1):
        if i%2==0:
            Radiobutton(main_frame2,text=dict_of_books_for_delete[i][1]+'        (   by  '+dict_of_books_for_delete[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_delete_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame2,text=dict_of_books_for_delete[i][1]+'        (   by  '+dict_of_books_for_delete[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_delete_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()


def no_books_to_delete():
    global book_name_select_for_delete_var
    global book_name_select_for_delete_var

    book_name_select_for_delete=book_name_select_for_delete_var='chumma'
    Label(delete_books_admin_page_root,text="There are no books available right now",font=("lucida handwriting", 30),bg='black',fg='white').place(x=500,y=500)




def creating_dict_table_for_delete():
    global count_of_books_for_delete
    global list_of_books_for_delete  
    global dict_of_books_for_delete

    list_of_books_for_delete=[]
    dict_of_books_for_delete={}

    query1="select book_id,bookname,bookauthor from bookdata;"
    cursor_mysql.execute(query1)
    output=cursor_mysql.fetchall()

    if output==[]:
        list_of_books_for_delete=[]
        dict_of_books_for_delete={}
        count_of_books_for_delete=0
    else:
        for i in range(len(output)):
            dict_of_books_for_delete[i+1]=[output[i][0],output[i][1],output[i][2]]
            list_of_books_for_delete.append([output[i][0],output[i][1],output[i][2],(i+1)])
            count_of_books_for_delete=len(list_of_books_for_delete)



def clicking_proceed_in_delete_fn():
    global book_name_select_for_delete_var
    global main_list_regarding_book_and_author_info_for_delete
    global dict_of_books_for_delete

    try:
        book_name_select_for_delete=book_name_select_for_delete_var.get()
    except:
        book_name_select_for_delete='chumma'
    main_list_regarding_book_and_author_info_for_delete=[]
    if book_name_select_for_delete==0:
        messagebox.showerror('delete book','please select a book to delete')
    elif book_name_select_for_delete=='chumma' or book_name_select_for_delete_var=='chumma':
        messagebox.showinfo('oops','there are no books to delete right now')
        librarymang_home_page_admin_from_book_selecting_from_delete_page()
    else:
        main_list_regarding_book_and_author_info_for_delete=dict_of_books_for_delete[book_name_select_for_delete][0:3]   #just so that the 4th column is taken
        book_delete_verification_tkinter_page()






def checking_if_selected_book_is_issued_or_not_delete():
    global main_book_id_for_showing_in_book_delete
    
    query="select book_id2,username from bookissue where book_id2='{0}';"
    cursor_mysql.execute(query.format(main_book_id_for_showing_in_book_delete))
    out=cursor_mysql.fetchall()
    book_id_local=out[0][0]
    book_username_local=out[0][1]

    if book_username_local==None:
        delete_books_fn(main_book_id_for_showing_in_book_delete)
        messagebox.showinfo('success','Book has been successfully Deleted')
        librarymang_home_page_admin_from_deleting_confirmation_page()



    else:
        messagebox.showinfo('unsuccessful','Cannot Delete Books which have been issued')
        librarymang_home_page_admin_from_deleting_confirmation_page()




def delete_books_fn(book_to_delete):
    query1="delete from bookdata where book_id='{0}';"
    query2="delete from bookissue where book_id2='{0}';"
    cursor_mysql.execute(query1.format(book_to_delete))
    mycon.commit()
    bookidtodel=book_to_delete
    cursor_mysql.execute(query2.format(bookidtodel))
    mycon.commit()





def obtaining_book_info_for_delete(list_to_regard):
    global main_book_id_for_showing_in_book_delete
    global main_bookname_for_showing_in_book_delete
    global main_bookauthor_for_showing_in_book_delete
    global main_number_of_pages_for_showing_in_book_delete
    global main_book_cover_for_showing_in_book_delete
    global main_bookinfo_for_showing_in_book_delete
    global main_author_info_for_showing_in_book_delete

    query_for_book_last_delete='''select * from bookdata where book_id='{0}';'''
    cursor_mysql.execute(query_for_book_last_delete.format(list_to_regard[0]))
    new_list2=cursor_mysql.fetchall()

    main_book_id_for_showing_in_book_delete=new_list2[0][0]
    main_bookname_for_showing_in_book_delete=new_list2[0][1]
    main_bookauthor_for_showing_in_book_delete=new_list2[0][2]
    main_number_of_pages_for_showing_in_book_delete=new_list2[0][3]
    main_book_cover_for_showing_in_book_delete=new_list2[0][6]
    main_bookinfo_for_showing_in_book_delete=new_list2[0][4]
    if new_list2[0][5]==None:
        main_author_info_for_showing_in_book_delete='No Information Available'
    else:
        main_author_info_for_showing_in_book_delete=new_list2[0][5]















def book_delete_verification_tkinter_page():
    global main_list_regarding_book_and_author_info_for_delete
    global book_delete_verification_tkinter_page_root

    delete_books_admin_page_root.destroy()

    book_delete_verification_tkinter_page_root=Tk()
    book_delete_verification_tkinter_page_root.title('Delete Books')
    book_delete_verification_tkinter_page_root.state("zoomed")

    book_delete_verification_tkinter_page_root.config(background = "black", pady=10)

    obtaining_book_info_for_delete(main_list_regarding_book_and_author_info_for_delete)

    Label(book_delete_verification_tkinter_page_root,text="Book Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=700,y=20)
    Label(book_delete_verification_tkinter_page_root,text="Book Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(book_delete_verification_tkinter_page_root,text="Book Author:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(book_delete_verification_tkinter_page_root,text="Number Of Pages:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=250)
    Label(book_delete_verification_tkinter_page_root,text="Book Cover:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=250)
    Label(book_delete_verification_tkinter_page_root,text="Book Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=400)
    Label(book_delete_verification_tkinter_page_root,text="Author Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=400)

    Label(book_delete_verification_tkinter_page_root,text=main_book_id_for_showing_in_book_delete,font=("verdana", 20),width=20,anchor='w').place(x=890,y=20)
    Label(book_delete_verification_tkinter_page_root,text=main_bookname_for_showing_in_book_delete,font=("verdana", 20),width=30,anchor='w').place(x=350,y=150)
    Label(book_delete_verification_tkinter_page_root,text=main_bookauthor_for_showing_in_book_delete,font=("verdana", 20),width=30,anchor='w').place(x=1275,y=150)
    Label(book_delete_verification_tkinter_page_root,text=main_number_of_pages_for_showing_in_book_delete,font=("verdana", 20),width=20,anchor='w').place(x=460,y=250)
    Label(book_delete_verification_tkinter_page_root,text=main_book_cover_for_showing_in_book_delete,font=("verdana", 20),width=20,anchor='w').place(x=1245,y=250)

    first_scroll_for_delete=scrolledtext.ScrolledText(book_delete_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    second_scroll_for_delete=scrolledtext.ScrolledText(book_delete_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    first_scroll_for_delete.insert(END,main_bookinfo_for_showing_in_book_delete)
    second_scroll_for_delete.insert(END,main_author_info_for_showing_in_book_delete)
    first_scroll_for_delete.place(x=330,y=400)
    second_scroll_for_delete.place(x=1270,y=400)

    Button(book_delete_verification_tkinter_page_root,text='Cancel',font=('verdana',25),cursor='hand2',command=librarymang_home_page_admin_from_deleting_confirmation_page).place(x=1000,y=800)
    Button(book_delete_verification_tkinter_page_root,text='Delete Book',font=('verdana',25),cursor='hand2',bg='red',command=checking_if_selected_book_is_issued_or_not_delete).place(x=700,y=800)
    photo = PhotoImage(file = "e.png")
    book_delete_verification_tkinter_page_root.iconphoto(False, photo)





def delete_books_admin_page():

    global delete_books_admin_page_root
    global count_of_books_for_delete
    global list_of_books_for_delete
    global dict_of_books_for_delete
    global search_bar_delete_books_student_page_var

    librarymang_home_page_admin_root.destroy()

    delete_books_admin_page_root=Tk()
    delete_books_admin_page_root.title("Delete Books")
    delete_books_admin_page_root.state("zoomed")
    delete_books_admin_page_root.config(background = "black", pady=10)
    Label(delete_books_admin_page_root, text="Select Book to Delete",width=100, font=("freestyle script", 70)).pack()
    search_bar_delete_books_student_page_var=StringVar()
    Entry(delete_books_admin_page_root, font=('verdana',30),textvariable=search_bar_delete_books_student_page_var,width=50).place(x=250,y=200)
    Button(delete_books_admin_page_root,text='Search',cursor='hand2',font=('verdana',30),bg='grey',command=searcher_bar_mid_fn_for_delete).place(x=1600,y=180)
    Button(delete_books_admin_page_root,text='Go Back',cursor='hand2',font=('verdana',30),command=librarymang_home_page_admin_from_book_selecting_from_delete_page).place(x=1050,y=900)
    Button(delete_books_admin_page_root,text='Proceed',cursor='hand2',font=('verdana',30),command=clicking_proceed_in_delete_fn).place(x=750,y=900)
    photo = PhotoImage(file = "e.png")
    delete_books_admin_page_root.iconphoto(False, photo)
    

    creating_dict_table_for_delete()    # creating dictionary and list

    if count_of_books_for_delete==0:
        no_books_to_delete()
    elif count_of_books_for_delete<=12:
        no_scroll_for_delete_fn()
    else:
        if_is_scroll_for_delete_fn()




#***********************************************************************************************************************************************************************************



def searcher_bar_mid_fn_for_update():
    global search_bar_update_books_student_page_var
    global search_bar_update_books_student_page
    global dict_of_books_for_update
    global count_of_books_for_update
    search_bar_update_books_student_page_2=search_bar_update_books_student_page_var.get()
    search_bar_update_books_student_page=search_bar_update_books_student_page_2.lower()
    if count_of_books_for_update==0:
        no_books_to_update()
    elif count_of_books_for_update<=12:
        no_scroll_for_update_mid_fn()
    else:
        if_is_scroll_for_update_for_mid_fn()








def if_is_scroll_for_update_for_mid_fn():
    global count_of_books_for_update
    global dict_of_books_for_update
    global list_of_books_for_update
    global search_bar_update_books_student_page
    global variable_list_order_for_update_2
    variable_list_order_for_update_2=[]

    #search bar

    if search_bar_update_books_student_page=='':
        searaching_and_reodering_radiobutton_of_update_page_for_scroll(list_of_books_for_update)
    else:
        pass
        for sample in list_of_books_for_update:
            if (sample[0].lower()==search_bar_update_books_student_page) and (sample[1].lower()==search_bar_update_books_student_page) and (sample[2].lower()==search_bar_update_books_student_page) and ((sample[1].lower()).startswith(search_bar_update_books_student_page)) and ((sample[2].lower()).startswith(search_bar_update_books_student_page)) and ((sample[1].lower()).endswith(search_bar_update_books_student_page)) and ((sample[2].lower()).endswith(search_bar_update_books_student_page)) and (search_bar_update_books_student_page in sample[1].lower()) and (search_bar_update_books_student_page in sample[2].lower()):
                variable_list_order_for_update_2.append(sample)
            else:
                continue
        for sample2 in list_of_books_for_update:
            if (sample2 not in variable_list_order_for_update_2) and (sample2[0].lower()==search_bar_update_books_student_page):
                variable_list_order_for_update_2.append(sample2)
            else:
                continue
        for sample3 in list_of_books_for_update:
            if (sample3 not in variable_list_order_for_update_2) and (sample3[1].lower()==search_bar_update_books_student_page):
                variable_list_order_for_update_2.append(sample3)
            else:
                continue
        for sample4 in list_of_books_for_update:
            if (sample4 not in variable_list_order_for_update_2) and (sample4[2].lower()==search_bar_update_books_student_page):
                variable_list_order_for_update_2.append(sample4)
            else:
                continue
        for sample5 in list_of_books_for_update:
            if (sample5 not in variable_list_order_for_update_2) and ((sample5[1].lower()).startswith(search_bar_update_books_student_page)):
                variable_list_order_for_update_2.append(sample5)
            else:
                continue
        for sample6 in list_of_books_for_update:
            if (sample6 not in variable_list_order_for_update_2) and ((sample6[2].lower()).startswith(search_bar_update_books_student_page)):
                variable_list_order_for_update_2.append(sample6)
            else:
                continue
        for sample7 in list_of_books_for_update:
            if (sample7 not in variable_list_order_for_update_2) and ((sample7[1].lower()).endswith(search_bar_update_books_student_page)):
                variable_list_order_for_update_2.append(sample7)
            else:
                continue
        for sample8 in list_of_books_for_update:
            if (sample8 not in variable_list_order_for_update_2) and ((sample8[2].lower()).endswith(search_bar_update_books_student_page)):
                variable_list_order_for_update_2.append(sample8)
            else:
                continue
        for sample9 in list_of_books_for_update:
            if (sample9 not in variable_list_order_for_update_2) and (search_bar_update_books_student_page in sample9[1].lower()):
                variable_list_order_for_update_2.append(sample9)
            else:
                continue
        for sample10 in list_of_books_for_update:
            if (sample10 not in variable_list_order_for_update_2) and (search_bar_update_books_student_page in sample10[2].lower()):
                variable_list_order_for_update_2.append(sample10)
            else:
                continue
        for sample11 in list_of_books_for_update:
            if sample11 not in variable_list_order_for_update_2:
                variable_list_order_for_update_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_update_page_for_scroll(variable_list_order_for_update_2)







def searaching_and_reodering_radiobutton_of_update_page_for_scroll(list_ordered):
    global book_name_select_for_update_var
    global count_of_books_for_update
    global dict_of_books_for_update
    global list_of_books_for_update
    global search_bar_update_books_student_page
    global variable_list_order_for_update_2
    variable_list_order_for_update_2=[]



    innerframe3=LabelFrame(update_books_admin_page_root,text='books',bd=15,width=1000)
    innerframe3.place(x=600,y=300)

    #Creating Main fram:
    main_frame3=Frame(innerframe3,width=1000)
    main_frame3.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva3=Canvas(main_frame3,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva3.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll3=ttk.Scrollbar(main_frame3,orient=VERTICAL,command=canva3.yview) 
    scroll3.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva3.configure(yscrollcommand=scroll3.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva3.bind('<Configure>', lambda e: canva3.configure(scrollregion=canva3.bbox("all")))
    #Creating another frame inside canvas
    second_frame3=Frame(canva3,width=1000)
    #placing the second frame inside canva
    canva3.create_window((0,0),window=second_frame3,anchor='nw',)#nw means on the top right corner


    book_name_select_for_update_var=IntVar()

    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(second_frame3,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_update_var,value=i[3],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame3,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_update_var,value=i[3],width=50,bg='cyan',padx=10,anchor='w').pack()






def no_scroll_for_update_mid_fn():
    global count_of_books_for_update
    global dict_of_books_for_update
    global list_of_books_for_update
    global search_bar_update_books_student_page
    global variable_list_order_for_update_2
    variable_list_order_for_update_2=[]


    #search Bar operation

    if search_bar_update_books_student_page=='':
        searaching_and_reodering_radiobutton_of_update_page_for_no_scroll(list_of_books_for_update)
    else:
        pass
        for sample in list_of_books_for_update:
            if (sample[0].lower()==search_bar_update_books_student_page) and (sample[1].lower()==search_bar_update_books_student_page) and (sample[2].lower()==search_bar_update_books_student_page) and ((sample[1].lower()).startswith(search_bar_update_books_student_page)) and ((sample[2].lower()).startswith(search_bar_update_books_student_page)) and ((sample[1].lower()).endswith(search_bar_update_books_student_page)) and ((sample[2].lower()).endswith(search_bar_update_books_student_page)) and (search_bar_update_books_student_page in sample[1].lower()) and (search_bar_update_books_student_page in sample[2].lower()):
                variable_list_order_for_update_2.append(sample)
            else:
                continue
        for sample2 in list_of_books_for_update:
            if (sample2 not in variable_list_order_for_update_2) and (sample2[0].lower()==search_bar_update_books_student_page):
                variable_list_order_for_update_2.append(sample2)
            else:
                continue
        for sample3 in list_of_books_for_update:
            if (sample3 not in variable_list_order_for_update_2) and (sample3[1].lower()==search_bar_update_books_student_page):
                variable_list_order_for_update_2.append(sample3)
            else:
                continue
        for sample4 in list_of_books_for_update:
            if (sample4 not in variable_list_order_for_update_2) and (sample4[2].lower()==search_bar_update_books_student_page):
                variable_list_order_for_update_2.append(sample4)
            else:
                continue
        for sample5 in list_of_books_for_update:
            if (sample5 not in variable_list_order_for_update_2) and ((sample5[1].lower()).startswith(search_bar_update_books_student_page)):
                variable_list_order_for_update_2.append(sample5)
            else:
                continue
        for sample6 in list_of_books_for_update:
            if (sample6 not in variable_list_order_for_update_2) and ((sample6[2].lower()).startswith(search_bar_update_books_student_page)):
                variable_list_order_for_update_2.append(sample6)
            else:
                continue
        for sample7 in list_of_books_for_update:
            if (sample7 not in variable_list_order_for_update_2) and ((sample7[1].lower()).endswith(search_bar_update_books_student_page)):
                variable_list_order_for_update_2.append(sample7)
            else:
                continue
        for sample8 in list_of_books_for_update:
            if (sample8 not in variable_list_order_for_update_2) and ((sample8[2].lower()).endswith(search_bar_update_books_student_page)):
                variable_list_order_for_update_2.append(sample8)
            else:
                continue
        for sample9 in list_of_books_for_update:
            if (sample9 not in variable_list_order_for_update_2) and (search_bar_update_books_student_page in sample9[1].lower()):
                variable_list_order_for_update_2.append(sample9)
            else:
                continue
        for sample10 in list_of_books_for_update:
            if (sample10 not in variable_list_order_for_update_2) and (search_bar_update_books_student_page in sample10[2].lower()):
                variable_list_order_for_update_2.append(sample10)
            else:
                continue
        for sample11 in list_of_books_for_update:
            if sample11 not in variable_list_order_for_update_2:
                variable_list_order_for_update_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_update_page_for_no_scroll(variable_list_order_for_update_2)


def searaching_and_reodering_radiobutton_of_update_page_for_no_scroll(list_ordered):
    global book_name_select_for_update_var
    global count_of_books_for_update
    global dict_of_books_for_update
    global list_of_books_for_update
    global search_bar_update_books_student_page
    global variable_list_order_for_update_2
    variable_list_order_for_update_2=[]
    innerframe3=LabelFrame(update_books_admin_page_root,text='books',bd=15,width=1000)
    innerframe3.place(x=600,y=300)

    #Creating Main fram:
    main_frame3=Frame(innerframe3,width=1000)
    main_frame3.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_update_var=IntVar()
    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(main_frame3,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_update_var,value=i[3],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame3,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_update_var,value=i[3],width=50,bg='cyan',padx=10,anchor='w').pack()








def if_is_scroll_for_update_fn():

    global update_books_admin_page_root
    global dict_of_books_for_update
    innerframe3=LabelFrame(update_books_admin_page_root,text='books',bd=15,width=1000)
    innerframe3.place(x=600,y=300)

    #Creating Main fram:
    main_frame3=Frame(innerframe3,width=1000)
    main_frame3.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva3=Canvas(main_frame3,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva3.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll3=ttk.Scrollbar(main_frame3,orient=VERTICAL,command=canva3.yview) 
    scroll3.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva3.configure(yscrollcommand=scroll3.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva3.bind('<Configure>', lambda e: canva3.configure(scrollregion=canva3.bbox("all")))
    #Creating another frame inside canvas
    second_frame3=Frame(canva3,width=1000)
    #placing the second frame inside canva
    canva3.create_window((0,0),window=second_frame3,anchor='nw',)#nw means on the top right corner
    global book_name_select_for_update_var
    book_name_select_for_update_var=IntVar()
    for i in range(1,count_of_books_for_update+1):
        if i%2==0:
            Radiobutton(second_frame3,text=dict_of_books_for_update[i][1]+'        (   by  '+dict_of_books_for_update[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_update_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame3,text=dict_of_books_for_update[i][1]+'        (   by  '+dict_of_books_for_update[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_update_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()









def no_scroll_for_update_fn():
    global dict_of_books_for_update
    global count_of_books_for_update

    innerframe3=LabelFrame(update_books_admin_page_root,text='books',bd=15,width=1000,)
    innerframe3.place(x=600,y=300)

    #Creating Main fram:
    main_frame3=Frame(innerframe3,width=1000)
    main_frame3.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    global book_name_select_for_update_var
    book_name_select_for_update_var=IntVar()
    for i in range(1,count_of_books_for_update+1):
        if i%2==0:
            Radiobutton(main_frame3,text=dict_of_books_for_update[i][1]+'        (   by  '+dict_of_books_for_update[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_update_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame3,text=dict_of_books_for_update[i][1]+'        (   by  '+dict_of_books_for_update[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_update_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()





def no_books_to_update():
    global book_name_select_for_update_var
    global book_name_select_for_update
    book_name_select_for_update=book_name_select_for_update_var='chumma'
    Label(update_books_admin_page_root,text="There are no books available right now",font=("lucida handwriting", 30),bg='black',fg='white').place(x=500,y=500)






def creating_dict_table_for_update():
    global count_of_books_for_update
    global list_of_books_for_update 
    global dict_of_books_for_update

    list_of_books_for_update=[]
    dict_of_books_for_update={}

    query1="select book_id,bookname,bookauthor from bookdata;"
    cursor_mysql.execute(query1)
    output=cursor_mysql.fetchall()

    if output==[]:
        list_of_books_for_update=[]
        dict_of_books_for_update={}
        count_of_books_for_update=0
    else:
        for i in range(len(output)):
            dict_of_books_for_update[i+1]=[output[i][0],output[i][1],output[i][2]]
            list_of_books_for_update.append([output[i][0],output[i][1],output[i][2],(i+1)])
            count_of_books_for_update=len(list_of_books_for_update)





def clicking_proceed_in_update_fn():
    global book_name_select_for_update_var
    global main_list_regarding_book_and_author_info_for_update
    global dict_of_books_for_update

    try:
        book_name_select_for_update=book_name_select_for_update_var.get()
    except:
        book_name_select_for_update='chumma'
    main_list_regarding_book_and_author_info_for_update=[]
    if book_name_select_for_update==0:
        messagebox.showerror('update book','please select a book to update')
    elif book_name_select_for_update=='chumma' or book_name_select_for_update_var=='chumma':
        messagebox.showinfo('oops','there are no books to update right now')
        librarymanag_from_update_search_page()
    else:
        main_list_regarding_book_and_author_info_for_update=dict_of_books_for_update[book_name_select_for_update][0:3]   #just so that the 4th column is taken
        book_update_verification_tkinter_page()






def obtaining_book_info_for_update(list_to_regard):
    global main_book_id_for_showing_in_book_update
    global main_bookname_for_showing_in_book_update
    global main_bookauthor_for_showing_in_book_update
    global main_number_of_pages_for_showing_in_book_update
    global main_book_cover_for_showing_in_book_update
    global main_bookinfo_for_showing_in_book_update
    global main_author_info_for_showing_in_book_update

    query_for_book_last_update='''select * from bookdata where book_id='{0}';'''
    cursor_mysql.execute(query_for_book_last_update.format(list_to_regard[0]))
    new_list3=cursor_mysql.fetchall()

    main_book_id_for_showing_in_book_update=new_list3[0][0]
    main_bookname_for_showing_in_book_update=new_list3[0][1]
    main_bookauthor_for_showing_in_book_update=new_list3[0][2]
    main_number_of_pages_for_showing_in_book_update=new_list3[0][3]
    main_book_cover_for_showing_in_book_update=new_list3[0][6]
    main_bookinfo_for_showing_in_book_update=new_list3[0][4]
    if new_list3[0][5]==None:
        main_author_info_for_showing_in_book_update=''
    else:
        main_author_info_for_showing_in_book_update=new_list3[0][5]






def mid_for_update_fns():
    global main_book_id_for_showing_in_book_update
    global bookname_for_verification_update
    global bookauthor_for_verification_update
    global number_of_pages_for_verification_update
    global book_cover_for_verification_update
    global book_info_for_verification_update
    global authorinfo_for_verification_update
    global real_no_of_pages_for_update

    real_no_of_pages_for_update=int(number_of_pages_for_verification_update)

    
    query="select book_id2,username from bookissue where book_id2='{0}';"
    cursor_mysql.execute(query.format(main_book_id_for_showing_in_book_update))
    out=cursor_mysql.fetchall()
    book_id_local=out[0][0]
    book_username_local=out[0][1]

    if book_username_local==None:

        updating_data_fn()
        messagebox.showinfo('hooray','updation successful')
        librarymanag_from_update_verification()


    else:
        messagebox.showinfo('unsuccessful','Cannot Update Books which have been issued')
        librarymanag_from_update_verification()

def updating_data_fn():
    global main_book_id_for_showing_in_book_update
    global bookname_for_verification_update
    global bookauthor_for_verification_update
    global book_cover_for_verification_update
    global book_info_for_verification_update
    global authorinfo_for_verification_update
    global real_no_of_pages_for_update


    if authorinfo_for_verification_update=='':
        query_of_updation="update bookdata set bookname='{0}',bookauthor='{1}',number_of_pages={2},bookinfo='{3}',authorinfo=Null,bookcover='{4}' where book_id='{5}';"
        cursor_mysql.execute(query_of_updation.format(bookname_for_verification_update,bookauthor_for_verification_update,real_no_of_pages_for_update,book_info_for_verification_update,book_cover_for_verification_update,main_book_id_for_showing_in_book_update))
        mycon.commit()
    else:
        query_of_updation="update bookdata set bookname='{0}',bookauthor='{1}',number_of_pages={2},bookinfo='{3}',authorinfo='{4}',bookcover='{5}' where book_id='{6}';"
        cursor_mysql.execute(query_of_updation.format(bookname_for_verification_update,bookauthor_for_verification_update,real_no_of_pages_for_update,book_info_for_verification_update,authorinfo_for_verification_update,book_cover_for_verification_update,main_book_id_for_showing_in_book_update))
        mycon.commit()





def checking_updation_data():
    global main_list_regarding_book_and_author_info_for_update
    global book_update_verification_tkinter_page_root

    global bookname_for_verification_update_var
    global bookauthor_for_verification_update_var
    global number_of_pages_for_verification_update_var
    global book_cover_for_verification_update_var
    global book_info_for_verification_update_var
    global authorinfo_for_verification_update_var

    global main_book_id_for_showing_in_book_update
    global bookname_for_verification_update
    global bookauthor_for_verification_update
    global number_of_pages_for_verification_update
    global book_cover_for_verification_update
    global book_info_for_verification_update
    global authorinfo_for_verification_update

    bookname_for_verification_update=bookname_for_verification_update_var.get()
    bookauthor_for_verification_update=bookauthor_for_verification_update_var.get()
    number_of_pages_for_verification_update=number_of_pages_for_verification_update_var.get()
    book_cover_for_verification_update=book_cover_for_verification_update_var.get()
    book_info_for_verification_update=book_info_for_verification_update_var.get(1.0,'end-1c')
    authorinfo_for_verification_update=authorinfo_for_verification_update_var.get(1.0,'end-1c')


    ref_for_update_books_admin_page=0
    if bookname_for_verification_update=='':
        messagebox.showerror('error','please enter book name')
        ref_for_update_books_admin_page=1
    elif len(bookname_for_verification_update)>50:
        messagebox.showerror('error','Book name should be less than 51 characters')
        ref_for_update_books_admin_page=1
    else:
        pass
    if ref_for_update_books_admin_page==0 and bookauthor_for_verification_update=='':
        messagebox.showerror('error','please enter Authors name')
        ref_for_update_books_admin_page=2
    elif ref_for_update_books_admin_page==0 and len(bookauthor_for_verification_update)>50:
        messagebox.showerror('error','Author name cannot be more than 51 characters')
        ref_for_update_books_admin_page=2
    else:
        pass
    if ref_for_update_books_admin_page==0 and number_of_pages_for_verification_update=='':
        messagebox.showerror('error','please enter the number of pages')
        ref_for_update_books_admin_page=3
    elif ref_for_update_books_admin_page==0 and (not number_of_pages_for_verification_update.isdigit()):
        messagebox.showerror('error','number of pages must only contain numbers')
        ref_for_update_books_admin_page=3
    else:
        pass
    if ref_for_update_books_admin_page==0 and (book_cover_for_verification_update not in book_cover_for_verification_update_list):
        messagebox.showerror('error','please enter the book cover type')
        ref_for_update_books_admin_page=4
    else:
        pass
    if ref_for_update_books_admin_page==0 and book_info_for_verification_update=='':
        messagebox.showerror('error','please enter the book description')
        ref_for_update_books_admin_page=5
    elif ref_for_update_books_admin_page==0 and len(book_info_for_verification_update)>6000:
        messagebox.showerror('error','book info must be less than 6001 characters')
        ref_for_update_books_admin_page=5
    else:
        pass
    if ref_for_update_books_admin_page==0 and len(authorinfo_for_verification_update)>6000:
        messagebox.showerror('error','author info must be less than 6001 characters')
        ref_for_update_books_admin_page=6
    else:
        pass
    if ref_for_update_books_admin_page==0 and (('\"' in bookname_for_verification_update) or ('\"' in bookauthor_for_verification_update) or ('\"' in book_info_for_verification_update) or ('\"' in authorinfo_for_verification_update) or ('\'' in bookname_for_verification_update) or ('\'' in bookauthor_for_verification_update) or ('\'' in book_info_for_verification_update) or ('\'' in authorinfo_for_verification_update)):
        messagebox.showinfo('error','Dnot use \' or \" in any field')
        ref_for_update_books_admin_page=7
    if ref_for_update_books_admin_page==0:
        mid_for_update_fns()
    else:
        pass




def book_update_verification_tkinter_page():
    global main_list_regarding_book_and_author_info_for_update
    global book_update_verification_tkinter_page_root

    global main_book_id_for_showing_in_book_update
    global bookname_for_verification_update_var
    global bookauthor_for_verification_update_var
    global number_of_pages_for_verification_update_var
    global book_cover_for_verification_update_var
    global book_info_for_verification_update_var
    global authorinfo_for_verification_update_var
    global book_cover_for_verification_update_list

    update_books_admin_page_root.destroy()

    book_update_verification_tkinter_page_root=Tk()
    book_update_verification_tkinter_page_root.title('Delete Books')
    book_update_verification_tkinter_page_root.state("zoomed")

    book_update_verification_tkinter_page_root.config(background = "black", pady=10)

    obtaining_book_info_for_update(main_list_regarding_book_and_author_info_for_update)

    Label(book_update_verification_tkinter_page_root,text="Book Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=700,y=20)
    Label(book_update_verification_tkinter_page_root,text="Book Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(book_update_verification_tkinter_page_root,text="Book Author:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(book_update_verification_tkinter_page_root,text="Number Of Pages:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=250)
    Label(book_update_verification_tkinter_page_root,text="Book Cover:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=250)
    Label(book_update_verification_tkinter_page_root,text="Book Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=400)
    Label(book_update_verification_tkinter_page_root,text="Author Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=400)

    bookname_for_verification_update_var=StringVar()
    bookauthor_for_verification_update_var=StringVar()
    number_of_pages_for_verification_update_var=StringVar()
    book_cover_for_verification_update_var=StringVar()

    bookname_for_verification_update_var.set(main_bookname_for_showing_in_book_update)
    bookauthor_for_verification_update_var.set(main_bookauthor_for_showing_in_book_update)
    number_of_pages_for_verification_update_var.set(main_number_of_pages_for_showing_in_book_update)
    book_cover_for_verification_update_var.set(main_book_cover_for_showing_in_book_update)

    label_for_book_id=Label(book_update_verification_tkinter_page_root,text=main_book_id_for_showing_in_book_update,font=("verdana", 20),width=20)
    entry_for_bookname=Entry(book_update_verification_tkinter_page_root,textvariable=bookname_for_verification_update_var,font=("verdana", 20),width=30)
    entry_for_bookauthor=Entry(book_update_verification_tkinter_page_root,textvariable=bookauthor_for_verification_update_var,font=("verdana", 20),width=30)
    entry_for_number_of_pages=Entry(book_update_verification_tkinter_page_root,textvariable=number_of_pages_for_verification_update_var,font=("verdana", 20),width=20,)


    book_cover_for_verification_update_list=[ 'paperback','hardcover']
    book_cover_for_verification_update_droplist=OptionMenu(book_update_verification_tkinter_page_root, book_cover_for_verification_update_var, *book_cover_for_verification_update_list)
    book_cover_for_verification_update_droplist.config(font=("verdana", 20),width=20)
    book_cover_for_verification_update_droplist.place(x=1250,y=250)

    book_info_for_verification_update_var=scrolledtext.ScrolledText(book_update_verification_tkinter_page_root,wrap=WORD,bg='white',width=30,height=7,font=('verdana',20))
    authorinfo_for_verification_update_var=scrolledtext.ScrolledText(book_update_verification_tkinter_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))

    book_info_for_verification_update_var.insert(END,main_bookinfo_for_showing_in_book_update)
    authorinfo_for_verification_update_var.insert(END,main_author_info_for_showing_in_book_update)
    
    label_for_book_id.place(x=890,y=20)
    entry_for_bookname.place(x=350,y=150)
    entry_for_bookauthor.place(x=1275,y=150)
    entry_for_number_of_pages.place(x=460,y=250)
    book_info_for_verification_update_var.place(x=330,y=400)
    authorinfo_for_verification_update_var.place(x=1270,y=400)

    Button(book_update_verification_tkinter_page_root,text='Cancel',font=('verdana',25),cursor='hand2',command=librarymanag_from_update_verification).place(x=1000,y=800)
    Button(book_update_verification_tkinter_page_root,text='Update Book',font=('verdana',25),cursor='hand2',bg='green',command=checking_updation_data).place(x=700,y=800)
    photo = PhotoImage(file = "e.png")
    book_update_verification_tkinter_page_root.iconphoto(False, photo)





def update_books_admin_page():

    global update_books_admin_page_root
    global count_of_books_for_update
    global list_of_books_for_update
    global dict_of_books_for_update
    global search_bar_update_books_student_page_var

    librarymang_home_page_admin_root.destroy()

    update_books_admin_page_root=Tk()
    update_books_admin_page_root.title("Update Books")
    update_books_admin_page_root.state("zoomed")
    update_books_admin_page_root.config(background = "black", pady=10)
    Label(update_books_admin_page_root, text="Select Book to Update",width=100, font=("freestyle script", 70)).pack()
    search_bar_update_books_student_page_var=StringVar()
    Entry(update_books_admin_page_root, font=('verdana',30),textvariable=search_bar_update_books_student_page_var,width=50).place(x=250,y=200)
    Button(update_books_admin_page_root,text='Search',cursor='hand2',font=('verdana',30),bg='grey',command=searcher_bar_mid_fn_for_update).place(x=1600,y=180)
    Button(update_books_admin_page_root,text='Go Back',cursor='hand2',font=('verdana',30),command=librarymanag_from_update_search_page).place(x=1050,y=900)
    Button(update_books_admin_page_root,text='Proceed',cursor='hand2',font=('verdana',30),command=clicking_proceed_in_update_fn).place(x=750,y=900)
    photo = PhotoImage(file = "e.png")
    update_books_admin_page_root.iconphoto(False, photo)
    

    creating_dict_table_for_update()    # creating dictionary and list

    if count_of_books_for_update==0:
        no_books_to_update()
    elif count_of_books_for_update<=12:
        no_scroll_for_update_fn()
    else:
        if_is_scroll_for_update_fn()




#***********************************************************************************************************************************************************************************
def view_books_admin_page():

    global view_books_admin_page_root
    global count_of_view_books_admin
    global list_of_view_books_admin
    global dict_of_view_books_admin
    global search_bar_view_books_for_admin_var

    librarymang_home_page_admin_root.destroy()

    view_books_admin_page_root=Tk()
    view_books_admin_page_root.title("View Books")
    view_books_admin_page_root.state("zoomed")
    view_books_admin_page_root.config(background = "black", pady=10)
    Label(view_books_admin_page_root, text="Select Book to View",width=100, font=("freestyle script", 70)).pack()
    search_bar_view_books_for_admin_var=StringVar()
    Entry(view_books_admin_page_root, font=('verdana',30),textvariable=search_bar_view_books_for_admin_var,width=50).place(x=250,y=200)
    Button(view_books_admin_page_root,text='Search',cursor='hand2',font=('verdana',30),bg='grey',command=searcher_bar_mid_fn_for_view_books_admin).place(x=1600,y=180)
    Button(view_books_admin_page_root,text='Go Back',cursor='hand2',font=('verdana',30),command=librarymanag_from_view_books_admin).place(x=1050,y=900)
    Button(view_books_admin_page_root,text='Book info',cursor='hand2',font=('verdana',30),command=clicking_proceed_in_view_books_admin).place(x=700,y=900)
    photo = PhotoImage(file = "e.png")
    view_books_admin_page_root.iconphoto(False, photo)
    

    creating_dict_table_for_view_books_admin()    # creating dictionary and list

    if count_of_view_books_admin==0:
        no_books_to_view_admin()
    elif count_of_view_books_admin<=12:
        no_scroll_for_view_books_admin()
    else:
        if_is_scroll_for_view_books_admin()



def no_books_to_view_admin():
    global book_name_select_for_view_books_admin_var
    global book_name_select_for_view_books_admin
    book_name_select_for_view_books_admin=book_name_select_for_view_books_admin_var='chumma'
    Label(view_books_admin_page_root,text="There are no books available right now",font=("lucida handwriting", 30),bg='black',fg='white').place(x=500,y=500)


def if_is_scroll_for_view_books_admin():

    global view_books_admin_page_root
    global dict_of_view_books_admin
    innerframe7=LabelFrame(view_books_admin_page_root,text='books',bd=15,width=1000)
    innerframe7.place(x=600,y=300)

    #Creating Main fram:
    main_frame7=Frame(innerframe7,width=1000)
    main_frame7.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva7=Canvas(main_frame7,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva7.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll7=ttk.Scrollbar(main_frame7,orient=VERTICAL,command=canva7.yview) 
    scroll7.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva7.configure(yscrollcommand=scroll7.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva7.bind('<Configure>', lambda e: canva7.configure(scrollregion=canva7.bbox("all")))
    #Creating another frame inside canvas
    second_frame7=Frame(canva7,width=1000)
    #placing the second frame inside canva
    canva7.create_window((0,0),window=second_frame7,anchor='nw',)#nw means on the top right corner
    global book_name_select_for_view_books_admin_var
    book_name_select_for_view_books_admin_var=IntVar()
    for i in range(1,count_of_view_books_admin+1):
        if i%2==0:
            Radiobutton(second_frame7,text=dict_of_view_books_admin[i][1]+'        (   by  '+dict_of_view_books_admin[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_view_books_admin_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame7,text=dict_of_view_books_admin[i][1]+'        (   by  '+dict_of_view_books_admin[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_view_books_admin_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()







def no_scroll_for_view_books_admin():
    global dict_of_view_books_admin
    global count_of_view_books_admin

    innerframe7=LabelFrame(view_books_admin_page_root,text='books',bd=15,width=1000,)
    innerframe7.place(x=600,y=300)

    #Creating Main fram:
    main_frame7=Frame(innerframe7,width=1000)
    main_frame7.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    global book_name_select_for_view_books_admin_var
    book_name_select_for_view_books_admin_var=IntVar()
    for i in range(1,count_of_view_books_admin+1):
        if i%2==0:
            Radiobutton(main_frame7,text=dict_of_view_books_admin[i][1]+'        (   by  '+dict_of_view_books_admin[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_view_books_admin_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame7,text=dict_of_view_books_admin[i][1]+'        (   by  '+dict_of_view_books_admin[i][2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_view_books_admin_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()



def searcher_bar_mid_fn_for_view_books_admin():
    global search_bar_view_books_for_admin_var
    global search_bar_view_books_for_admin
    global dict_of_view_books_admin
    global count_of_view_books_admin
    search_bar_view_books_for_admin_2=search_bar_view_books_for_admin_var.get()
    search_bar_view_books_for_admin=search_bar_view_books_for_admin_2.lower()
    if count_of_view_books_admin==0:
        no_books_to_view_admin()
    elif count_of_view_books_admin<=12:
        no_scroll_for_view_books_admin_mid_fn()
    else:
        if_is_scroll_for_view_books_admin_for_mid_fn()



def if_is_scroll_for_view_books_admin_for_mid_fn():
    global count_of_view_books_admin
    global dict_of_view_books_admin
    global list_of_view_books_admin
    global search_bar_view_books_for_admin
    global variable_list_order_for_view_books_admin_2
    variable_list_order_for_view_books_admin_2=[]

    #search bar

    if search_bar_view_books_for_admin=='':
        searaching_and_reodering_radiobutton_of_view_books_admin_page_for_scroll(list_of_view_books_admin)
    else:
        pass
        for sample in list_of_view_books_admin:
            if (sample[0].lower()==search_bar_view_books_for_admin) and (sample[1].lower()==search_bar_view_books_for_admin) and (sample[2].lower()==search_bar_view_books_for_admin) and ((sample[1].lower()).startswith(search_bar_view_books_for_admin)) and ((sample[2].lower()).startswith(search_bar_view_books_for_admin)) and ((sample[1].lower()).endswith(search_bar_view_books_for_admin)) and ((sample[2].lower()).endswith(search_bar_view_books_for_admin)) and (search_bar_view_books_for_admin in sample[1].lower()) and (search_bar_view_books_for_admin in sample[2].lower()):
                variable_list_order_for_view_books_admin_2.append(sample)
            else:
                continue
        for sample2 in list_of_view_books_admin:
            if (sample2 not in variable_list_order_for_view_books_admin_2) and (sample2[0].lower()==search_bar_view_books_for_admin):
                variable_list_order_for_view_books_admin_2.append(sample2)
            else:
                continue
        for sample3 in list_of_view_books_admin:
            if (sample3 not in variable_list_order_for_view_books_admin_2) and (sample3[1].lower()==search_bar_view_books_for_admin):
                variable_list_order_for_view_books_admin_2.append(sample3)
            else:
                continue
        for sample4 in list_of_view_books_admin:
            if (sample4 not in variable_list_order_for_view_books_admin_2) and (sample4[2].lower()==search_bar_view_books_for_admin):
                variable_list_order_for_view_books_admin_2.append(sample4)
            else:
                continue
        for sample5 in list_of_view_books_admin:
            if (sample5 not in variable_list_order_for_view_books_admin_2) and ((sample5[1].lower()).startswith(search_bar_view_books_for_admin)):
                variable_list_order_for_view_books_admin_2.append(sample5)
            else:
                continue
        for sample6 in list_of_view_books_admin:
            if (sample6 not in variable_list_order_for_view_books_admin_2) and ((sample6[2].lower()).startswith(search_bar_view_books_for_admin)):
                variable_list_order_for_view_books_admin_2.append(sample6)
            else:
                continue
        for sample7 in list_of_view_books_admin:
            if (sample7 not in variable_list_order_for_view_books_admin_2) and ((sample7[1].lower()).endswith(search_bar_view_books_for_admin)):
                variable_list_order_for_view_books_admin_2.append(sample7)
            else:
                continue
        for sample8 in list_of_view_books_admin:
            if (sample8 not in variable_list_order_for_view_books_admin_2) and ((sample8[2].lower()).endswith(search_bar_view_books_for_admin)):
                variable_list_order_for_view_books_admin_2.append(sample8)
            else:
                continue
        for sample9 in list_of_view_books_admin:
            if (sample9 not in variable_list_order_for_view_books_admin_2) and (search_bar_view_books_for_admin in sample9[1].lower()):
                variable_list_order_for_view_books_admin_2.append(sample9)
            else:
                continue
        for sample10 in list_of_view_books_admin:
            if (sample10 not in variable_list_order_for_view_books_admin_2) and (search_bar_view_books_for_admin in sample10[2].lower()):
                variable_list_order_for_view_books_admin_2.append(sample10)
            else:
                continue
        for sample11 in list_of_view_books_admin:
            if sample11 not in variable_list_order_for_view_books_admin_2:
                variable_list_order_for_view_books_admin_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_view_books_admin_page_for_scroll(variable_list_order_for_view_books_admin_2)







def searaching_and_reodering_radiobutton_of_view_books_admin_page_for_scroll(list_ordered):
    global book_name_select_for_view_books_admin_var
    global count_of_view_books_admin
    global dict_of_view_books_admin
    global list_of_view_books_admin
    global search_bar_view_books_for_admin
    global variable_list_order_for_view_books_admin_2
    variable_list_order_for_view_books_admin_2=[]



    innerframe7=LabelFrame(view_books_admin_page_root,text='books',bd=15,width=1000)
    innerframe7.place(x=600,y=300)

    #Creating Main fram:
    main_frame7=Frame(innerframe7,width=1000)
    main_frame7.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva7=Canvas(main_frame7,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva7.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll7=ttk.Scrollbar(main_frame7,orient=VERTICAL,command=canva7.yview) 
    scroll7.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva7.configure(yscrollcommand=scroll7.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva7.bind('<Configure>', lambda e: canva7.configure(scrollregion=canva7.bbox("all")))
    #Creating another frame inside canvas
    second_frame7=Frame(canva7,width=1000)
    #placing the second frame inside canva
    canva7.create_window((0,0),window=second_frame7,anchor='nw',)#nw means on the top right corner


    book_name_select_for_view_books_admin_var=IntVar()

    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(second_frame7,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_view_books_admin_var,value=i[3],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame7,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_view_books_admin_var,value=i[3],width=50,bg='cyan',padx=10,anchor='w').pack()






def no_scroll_for_view_books_admin_mid_fn():
    global count_of_view_books_admin
    global dict_of_view_books_admin
    global list_of_view_books_admin
    global search_bar_view_books_for_admin
    global variable_list_order_for_view_books_admin_2
    variable_list_order_for_view_books_admin_2=[]



    #search Bar operation

    if search_bar_view_books_for_admin=='':
        searaching_and_reodering_radiobutton_of_view_books_admin_page_for_no_scroll(list_of_view_books_admin)
    else:
        pass
        for sample in list_of_view_books_admin:
            if (sample[0].lower()==search_bar_view_books_for_admin) and (sample[1].lower()==search_bar_view_books_for_admin) and (sample[2].lower()==search_bar_view_books_for_admin) and ((sample[1].lower()).startswith(search_bar_view_books_for_admin)) and ((sample[2].lower()).startswith(search_bar_view_books_for_admin)) and ((sample[1].lower()).endswith(search_bar_view_books_for_admin)) and ((sample[2].lower()).endswith(search_bar_view_books_for_admin)) and (search_bar_view_books_for_admin in sample[1].lower()) and (search_bar_view_books_for_admin in sample[2].lower()):
                variable_list_order_for_view_books_admin_2.append(sample)
            else:
                continue
        for sample2 in list_of_view_books_admin:
            if (sample2 not in variable_list_order_for_view_books_admin_2) and (sample2[0].lower()==search_bar_view_books_for_admin):
                variable_list_order_for_view_books_admin_2.append(sample2)
            else:
                continue
        for sample3 in list_of_view_books_admin:
            if (sample3 not in variable_list_order_for_view_books_admin_2) and (sample3[1].lower()==search_bar_view_books_for_admin):
                variable_list_order_for_view_books_admin_2.append(sample3)
            else:
                continue
        for sample4 in list_of_view_books_admin:
            if (sample4 not in variable_list_order_for_view_books_admin_2) and (sample4[2].lower()==search_bar_view_books_for_admin):
                variable_list_order_for_view_books_admin_2.append(sample4)
            else:
                continue
        for sample5 in list_of_view_books_admin:
            if (sample5 not in variable_list_order_for_view_books_admin_2) and ((sample5[1].lower()).startswith(search_bar_view_books_for_admin)):
                variable_list_order_for_view_books_admin_2.append(sample5)
            else:
                continue
        for sample6 in list_of_view_books_admin:
            if (sample6 not in variable_list_order_for_view_books_admin_2) and ((sample6[2].lower()).startswith(search_bar_view_books_for_admin)):
                variable_list_order_for_view_books_admin_2.append(sample6)
            else:
                continue
        for sample7 in list_of_view_books_admin:
            if (sample7 not in variable_list_order_for_view_books_admin_2) and ((sample7[1].lower()).endswith(search_bar_view_books_for_admin)):
                variable_list_order_for_view_books_admin_2.append(sample7)
            else:
                continue
        for sample8 in list_of_view_books_admin:
            if (sample8 not in variable_list_order_for_view_books_admin_2) and ((sample8[2].lower()).endswith(search_bar_view_books_for_admin)):
                variable_list_order_for_view_books_admin_2.append(sample8)
            else:
                continue
        for sample9 in list_of_view_books_admin:
            if (sample9 not in variable_list_order_for_view_books_admin_2) and (search_bar_view_books_for_admin in sample9[1].lower()):
                variable_list_order_for_view_books_admin_2.append(sample9)
            else:
                continue
        for sample10 in list_of_view_books_admin:
            if (sample10 not in variable_list_order_for_view_books_admin_2) and (search_bar_view_books_for_admin in sample10[2].lower()):
                variable_list_order_for_view_books_admin_2.append(sample10)
            else:
                continue
        for sample11 in list_of_view_books_admin:
            if sample11 not in variable_list_order_for_view_books_admin_2:
                variable_list_order_for_view_books_admin_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_view_books_admin_page_for_no_scroll(variable_list_order_for_view_books_admin_2)


def searaching_and_reodering_radiobutton_of_view_books_admin_page_for_no_scroll(list_ordered):
    global book_name_select_for_view_books_admin_var
    global count_of_view_books_admin
    global dict_of_view_books_admin
    global list_of_view_books_admin
    global search_bar_view_books_for_admin
    global variable_list_order_for_view_books_admin_2
    variable_list_order_for_view_books_admin_2=[]

    innerframe7=LabelFrame(view_books_admin_page_root,text='books',bd=15,width=1000,)
    innerframe7.place(x=600,y=300)

    #Creating Main fram:
    main_frame7=Frame(innerframe7,width=1000)
    main_frame7.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    book_name_select_for_view_books_admin_var=IntVar()
    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(main_frame7,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_view_books_admin_var,value=i[3],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame7,text=i[1]+'        (   by  '+i[2]+' )',fg='black',font=("lucida handwriting", 15),indicator=0,variable=book_name_select_for_view_books_admin_var,value=i[3],width=50,bg='cyan',padx=10,anchor='w').pack()







def clicking_proceed_in_view_books_admin():
    global book_name_select_for_view_books_admin_var
    global main_list_regarding_book_and_author_info_for_view_books_admin
    global dict_of_view_books_admin

    try:
        book_name_select_for_view_books_admin=book_name_select_for_view_books_admin_var.get()
    except:
        book_name_select_for_view_books_admin='chumma'
    main_list_regarding_book_and_author_info_for_view_books_admin=[]
    if book_name_select_for_view_books_admin==0:
        messagebox.showerror('View books','please select a book to view')
    elif book_name_select_for_view_books_admin=='chumma' or book_name_select_for_view_books_admin_var=='chumma':
        messagebox.showinfo('oops','there are no books to view right now')
        librarymanag_from_view_books_admin()
    else:
        main_list_regarding_book_and_author_info_for_view_books_admin=dict_of_view_books_admin[book_name_select_for_view_books_admin][0:3]   #just so that the 4th column is taken
        book_view_books_admin_tkinter_page_book_details()



def creating_dict_table_for_view_books_admin():
    global count_of_view_books_admin
    global list_of_view_books_admin 
    global dict_of_view_books_admin

    list_of_view_books_admin=[]
    dict_of_view_books_admin={}

    query1="select book_id,bookname,bookauthor from bookdata;"
    cursor_mysql.execute(query1)
    output=cursor_mysql.fetchall()

    if output==[]:
        list_of_view_books_admin=[]
        dict_of_view_books_admin={}
        count_of_view_books_admin=0
    else:
        for i in range(len(output)):
            dict_of_view_books_admin[i+1]=[output[i][0],output[i][1],output[i][2]]
            list_of_view_books_admin.append([output[i][0],output[i][1],output[i][2],(i+1)])
            count_of_view_books_admin=len(list_of_view_books_admin)



def obtaining_book_info_for_view_books_admin(list_to_regard):
    global main_book_id_for_showing_in_book_view_admin
    global main_bookname_for_showing_in_book_view_admin
    global main_bookauthor_for_showing_in_book_view_admin
    global main_number_of_pages_for_showing_in_book_view_admin
    global main_book_cover_for_showing_in_book_view_admin
    global main_bookinfo_for_showing_in_book_view_admin
    global main_author_info_for_showing_in_book_view_admin
    global main_username_who_issued_the_book_view_admin
    global main_issue_date_when_book_was_issued_view_admin
    global main_return_date_when_book_will_be_returned_view_admin

    query_for_book_last_update='''select * from bookdata where book_id='{0}';'''
    cursor_mysql.execute(query_for_book_last_update.format(list_to_regard[0]))
    new_list6=cursor_mysql.fetchall()

    main_book_id_for_showing_in_book_view_admin=new_list6[0][0]
    main_bookname_for_showing_in_book_view_admin=new_list6[0][1]
    main_bookauthor_for_showing_in_book_view_admin=new_list6[0][2]
    main_number_of_pages_for_showing_in_book_view_admin=new_list6[0][3]
    main_book_cover_for_showing_in_book_view_admin=new_list6[0][6]
    main_bookinfo_for_showing_in_book_view_admin=new_list6[0][4]
    if new_list6[0][5]==None:
        main_author_info_for_showing_in_book_view_admin='No Information Available'
    else:
        main_author_info_for_showing_in_book_view_admin=new_list6[0][5]

    query121="select * from bookissue where book_id2='{0}';"
    cursor_mysql.execute(query121.format(main_book_id_for_showing_in_book_view_admin))
    output=cursor_mysql.fetchall()
    if output[0][1]==None:
        main_username_who_issued_the_book_view_admin='Not Issued'
        main_issue_date_when_book_was_issued_view_admin='-NA-'
        main_return_date_when_book_will_be_returned_view_admin='-NA-'
    else:
        main_username_who_issued_the_book_view_admin=output[0][1]
        main_issue_date_when_book_was_issued_view_admin_2=str(output[0][2])
        main_return_date_when_book_will_be_returned_view_admin_2=str(output[0][3])

        l1=main_issue_date_when_book_was_issued_view_admin_2.split('-')
        l2=main_return_date_when_book_will_be_returned_view_admin_2.split('-')

        main_issue_date_when_book_was_issued_view_admin=l1[2]+'-'+l1[1]+'-'+l1[0]
        main_return_date_when_book_will_be_returned_view_admin=l2[2]+'-'+l2[1]+'-'+l2[0]



def book_view_books_admin_tkinter_page_book_details():
    global main_list_regarding_book_and_author_info_for_view_books_admin
    global view_books_info_admin_page_root

    view_books_admin_page_root.destroy()

    view_books_info_admin_page_root=Tk()
    view_books_info_admin_page_root.title('View Books')
    view_books_info_admin_page_root.state("zoomed")

    view_books_info_admin_page_root.config(background = "black", pady=10)

    obtaining_book_info_for_view_books_admin(main_list_regarding_book_and_author_info_for_view_books_admin)

    Label(view_books_info_admin_page_root,text="Book Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=40)
    Label(view_books_info_admin_page_root,text="Issued By:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=40)
    Label(view_books_info_admin_page_root,text="Book Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=170)
    Label(view_books_info_admin_page_root,text="Book Author:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=170)
    Label(view_books_info_admin_page_root,text="Number Of Pages:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=270)
    Label(view_books_info_admin_page_root,text="Book Cover:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=270)
    Label(view_books_info_admin_page_root,text="Book Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=420)
    Label(view_books_info_admin_page_root,text="Author Info:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=420)
    Label(view_books_info_admin_page_root,text="Issue Date:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=750)
    Label(view_books_info_admin_page_root,text="Return Date:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=750)

    Label(view_books_info_admin_page_root,text=main_book_id_for_showing_in_book_view_admin,font=("verdana", 20),width=20,anchor='w').place(x=310,y=40)
    Label(view_books_info_admin_page_root,text=main_username_who_issued_the_book_view_admin,font=("verdana", 20),width=20,anchor='w').place(x=1245,y=40)
    Label(view_books_info_admin_page_root,text=main_bookname_for_showing_in_book_view_admin,font=("verdana", 20),width=30,anchor='w').place(x=350,y=170)
    Label(view_books_info_admin_page_root,text=main_bookauthor_for_showing_in_book_view_admin,font=("verdana", 20),width=30,anchor='w').place(x=1275,y=170)
    Label(view_books_info_admin_page_root,text=main_number_of_pages_for_showing_in_book_view_admin,font=("verdana", 20),width=20,anchor='w').place(x=460,y=270)
    Label(view_books_info_admin_page_root,text=main_book_cover_for_showing_in_book_view_admin,font=("verdana", 20),width=20,anchor='w').place(x=1245,y=270)
    Label(view_books_info_admin_page_root,text=main_issue_date_when_book_was_issued_view_admin,font=("verdana", 20),width=20,anchor='w').place(x=350,y=750)
    Label(view_books_info_admin_page_root,text=main_return_date_when_book_will_be_returned_view_admin,font=("verdana", 20),width=20,anchor='w').place(x=1270,y=750)

    first_scroll_for_view_books_admin=scrolledtext.ScrolledText(view_books_info_admin_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    second_scroll_for_view_books_admin=scrolledtext.ScrolledText(view_books_info_admin_page_root,bg='white',wrap=WORD,width=30,height=7,font=('verdana',20))
    first_scroll_for_view_books_admin.insert(END,main_bookinfo_for_showing_in_book_view_admin)
    second_scroll_for_view_books_admin.insert(END,main_author_info_for_showing_in_book_view_admin)
    first_scroll_for_view_books_admin.place(x=330,y=420)
    second_scroll_for_view_books_admin.place(x=1270,y=420)

    Button(view_books_info_admin_page_root,text='Go Back',font=('verdana',25),cursor='hand2',command=librarymang_home_page_admin_from_view_books_admin_tkinter_info_page).place(x=900,y=900)
    photo = PhotoImage(file = "e.png")
    view_books_info_admin_page_root.iconphoto(False, photo)






#****************************************************************************************************************************************************************************************

def students_info_admin_page():

    global students_info_admin_page_root
    global count_of_students_info_admin
    global list_of_students_info_admin
    global dict_of_students_info_admin
    global search_bar_students_info_for_admin_var

    librarymang_home_page_admin_root.destroy()

    students_info_admin_page_root=Tk()
    students_info_admin_page_root.title("View Students")
    students_info_admin_page_root.state("zoomed")
    students_info_admin_page_root.config(background = "black", pady=10)
    Label(students_info_admin_page_root, text="Student Info",width=100, font=("freestyle script", 70)).pack()
    search_bar_students_info_for_admin_var=StringVar()
    Entry(students_info_admin_page_root, font=('verdana',30),textvariable=search_bar_students_info_for_admin_var,width=50).place(x=250,y=200)
    Button(students_info_admin_page_root,text='Search',cursor='hand2',font=('verdana',30),bg='grey',command=searcher_bar_mid_fn_for_student_info_admin).place(x=1600,y=180)
    Button(students_info_admin_page_root,text='Go Back',cursor='hand2',font=('verdana',30),command=librarymanag_from_student_info_admin).place(x=1050,y=900)
    Button(students_info_admin_page_root,text='Student info',cursor='hand2',font=('verdana',30),command=clicking_proceed_in_student_info_admin).place(x=640,y=900)
    photo = PhotoImage(file = "e.png")
    students_info_admin_page_root.iconphoto(False, photo)
    

    creating_dict_table_for_student_info_admin()    # creating dictionary and list

    if count_of_students_info_admin==0:
        no_students_to_view_admin()
    elif count_of_students_info_admin<=4:
        no_scroll_for_students_info_admin()
    else:
        if_is_scroll_for_students_info_admin()



def student_view_books_admin_tkinter_page_student_details():
    global main_list_regarding_username_and_name_student_info_admin
    global students_info_admin_tk_page_root

    students_info_admin_page_root.destroy()

    students_info_admin_tk_page_root=Tk()
    students_info_admin_tk_page_root.title('View students')
    students_info_admin_tk_page_root.state("zoomed")

    students_info_admin_tk_page_root.config(background = "black", pady=10)

    obtaining_student_info_for_view_student_info_admin(main_list_regarding_username_and_name_student_info_admin)

    global main_username_for_student_info_page
    global main_emailid_for_student_info_page
    global main_phoneno_for_student_info_page
    global main_firstname_for_student_info_page
    global main_lastname_for_student_info_page
    global main_gender_for_student_info_page
    global main_country_for_student_info_page


    Label(students_info_admin_tk_page_root,text="Username:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=80)
    Label(students_info_admin_tk_page_root,text="Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=80)
    Label(students_info_admin_tk_page_root,text="Email-Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=210)
    Label(students_info_admin_tk_page_root,text="Gender:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=210)
    Label(students_info_admin_tk_page_root,text="Country:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=350)
    Label(students_info_admin_tk_page_root,text="Phone no:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=350)
    Label(students_info_admin_tk_page_root,text="Issued Books: ",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=490)

    Label(students_info_admin_tk_page_root,text=main_username_for_student_info_page,font=("verdana", 20),width=30,anchor='w').place(x=335,y=80)
    Label(students_info_admin_tk_page_root,text=main_firstname_for_student_info_page+main_lastname_for_student_info_page,font=("verdana", 20),width=30,anchor='w').place(x=1175,y=80)
    Label(students_info_admin_tk_page_root,text=main_emailid_for_student_info_page,font=("verdana", 20),width=30,anchor='w').place(x=325,y=210)
    Label(students_info_admin_tk_page_root,text=main_gender_for_student_info_page,font=("verdana", 20),width=30,anchor='w').place(x=1200,y=210)
    Label(students_info_admin_tk_page_root,text=main_country_for_student_info_page,font=("verdana", 20),width=30,anchor='w').place(x=300,y=350)
    Label(students_info_admin_tk_page_root,text=str(main_phoneno_for_student_info_page),font=("verdana", 20),width=30,anchor='w').place(x=1225,y=350)
    photo = PhotoImage(file = "e.png")
    students_info_admin_tk_page_root.iconphoto(False, photo)
    if main_issue3_for_student_info!=None:
        Issued_books_if_3()
    elif main_issue2_for_student_info!=None and main_issue3_for_student_info==None:
        Issued_books_if_2()
    elif main_issue1_for_student_info!=None and main_issue2_for_student_info==None and main_issue3_for_student_info==None:
        Issued_books_if_1()
    elif main_issue1_for_student_info==None and main_issue2_for_student_info==None and main_issue3_for_student_info==None:
        No_issued_books()

    Button(students_info_admin_tk_page_root,text='Go Back',font=('verdana',25),cursor='hand2',command=librarymanag_from_student_info_admin_tk).place(x=900,y=900)
def No_issued_books():
    Label(students_info_admin_tk_page_root,text='No Books Issued',font=("verdana", 20),width=30,anchor='w').place(x=380,y=490)

def Issued_books_if_3():
    global students_info_admin_tk_page_root

    innerframe9=LabelFrame(students_info_admin_tk_page_root,text='Issue1',bd=15,width=1000,font=('verdana',15))
    innerframe9.place(x=70,y=580)

    #Creating Main fram:
    main_frame9=Frame(innerframe9,width=1000,padx=15)
    main_frame9.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    issuedate1=str(main_issue_date1__for_student_info)
    li1=issuedate1.split('-')
    returndate1=str(main_return_date1__for_student_info)
    lr1=returndate1.split('-')
    Label(main_frame9,text="Book: "+main_bookname1_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Author: "+main_author1_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Issue Date: "+li1[2]+'-'+li1[1]+'-'+li1[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Return Date: "+lr1[2]+'-'+lr1[1]+'-'+lr1[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9).pack()
    if checking_if_due_date_is_past_for_student_info(returndate1):
        send_reminder_mail_student_info(main_frame9,main_bookname1_for_student_info,issuedate1,returndate1)
    else:
        empty_pack(main_frame9)


    innerframe10=LabelFrame(students_info_admin_tk_page_root,text='Issue2',bd=15,width=1000,font=('verdana',15))
    innerframe10.place(x=660,y=580)

    #Creating Main fram:
    main_frame10=Frame(innerframe10,width=20,padx=15)
    main_frame10.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y

    issuedate2=str(main_issue_date2__for_student_info)
    li2=issuedate2.split('-')
    returndate2=str(main_return_date2__for_student_info)
    lr2=returndate2.split('-')

    Label(main_frame10,text="Book: "+main_bookname2_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame10,text="Author: "+main_author2_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame10,text="Issue Date: "+li2[2]+'-'+li2[1]+'-'+li2[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame10,text="Return Date: "+lr2[2]+'-'+lr2[1]+'-'+lr2[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame10,).pack()
    if checking_if_due_date_is_past_for_student_info(returndate2):
        send_reminder_mail_student_info(main_frame10,main_bookname2_for_student_info,issuedate2,returndate2)
    else:
        empty_pack(main_frame10)


    innerframe11=LabelFrame(students_info_admin_tk_page_root,text='Issue3',bd=15,width=1000,font=('verdana',15))
    innerframe11.place(x=1260,y=580)

    #Creating Main fram:
    main_frame11=Frame(innerframe11,width=1000,padx=15)
    main_frame11.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y

    issuedate3=str(main_issue_date3__for_student_info)
    li3=issuedate3.split('-')
    returndate3=str(main_return_date3__for_student_info)
    lr3=returndate3.split('-')

    Label(main_frame11,text="Book: "+main_bookname3_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame11,text="Author: "+main_author3_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame11,text="Issue Date: "+li3[2]+'-'+li3[1]+'-'+li3[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame11,text="Return Date: "+lr3[2]+'-'+lr3[1]+'-'+lr3[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame11,).pack()
    if checking_if_due_date_is_past_for_student_info(returndate3):
        send_reminder_mail_student_info(main_frame11,main_bookname3_for_student_info,issuedate3,returndate3)
    else:
        empty_pack(main_frame11)


def Issued_books_if_2():
    global students_info_admin_tk_page_root

    innerframe9=LabelFrame(students_info_admin_tk_page_root,text='Issue1',bd=15,width=1000,font=('verdana',15))
    innerframe9.place(x=250,y=580)

    #Creating Main fram:
    main_frame9=Frame(innerframe9,width=1000,padx=15)
    main_frame9.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    issuedate1=str(main_issue_date1__for_student_info)
    li1=issuedate1.split('-')
    returndate1=str(main_return_date1__for_student_info)
    lr1=returndate1.split('-')
    Label(main_frame9,text="Book: "+main_bookname1_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Author: "+main_author1_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Issue Date: "+li1[2]+'-'+li1[1]+'-'+li1[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Return Date: "+lr1[2]+'-'+lr1[1]+'-'+lr1[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9).pack()
    if checking_if_due_date_is_past_for_student_info(returndate1):
        send_reminder_mail_student_info(main_frame9,main_bookname1_for_student_info,issuedate1,returndate1)
    else:
        empty_pack(main_frame9)

    innerframe10=LabelFrame(students_info_admin_tk_page_root,text='Issue2',bd=15,width=1000,font=('verdana',15))
    innerframe10.place(x=1100,y=580)

    #Creating Main fram:
    main_frame10=Frame(innerframe10,width=20,padx=15)
    main_frame10.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y

    issuedate2=str(main_issue_date2__for_student_info)
    li2=issuedate2.split('-')
    returndate2=str(main_return_date2__for_student_info)
    lr2=returndate2.split('-')

    Label(main_frame10,text="Book: "+main_bookname2_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame10,text="Author: "+main_author2_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame10,text="Issue Date: "+li2[2]+'-'+li2[1]+'-'+li2[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame10,text="Return Date: "+lr2[2]+'-'+lr2[1]+'-'+lr2[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame10,).pack()
    if checking_if_due_date_is_past_for_student_info(returndate2):
        send_reminder_mail_student_info(main_frame10,main_bookname2_for_student_info,issuedate2,returndate2)
    else:
        empty_pack(main_frame10)

def Issued_books_if_1():
    global students_info_admin_tk_page_root

    innerframe9=LabelFrame(students_info_admin_tk_page_root,text='Issue1',bd=15,width=1000,font=('verdana',15))
    innerframe9.place(x=680,y=580)

    #Creating Main fram:
    main_frame9=Frame(innerframe9,width=1000,padx=15)
    main_frame9.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    issuedate1=str(main_issue_date1__for_student_info)
    li1=issuedate1.split('-')
    returndate1=str(main_return_date1__for_student_info)
    lr1=returndate1.split('-')
    Label(main_frame9,text="Book: "+main_bookname1_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Author: "+main_author1_for_student_info,font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Issue Date: "+li1[2]+'-'+li1[1]+'-'+li1[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9,text="Return Date: "+lr1[2]+'-'+lr1[1]+'-'+lr1[0],font=('Verdana',20),width=30,anchor='w').pack()
    Label(main_frame9).pack()
    if checking_if_due_date_is_past_for_student_info(returndate1):
        send_reminder_mail_student_info(main_frame9,main_bookname1_for_student_info,issuedate1,returndate1)
    else:
        empty_pack(main_frame9)


def empty_pack(root):
    Label(root).pack()
    Label(root).pack()


def checking_if_due_date_is_past_for_student_info(retdate):
    list_of_day_month_year=retdate.split('-')
    year_of_return=int(list_of_day_month_year[0])
    month_of_return=int(list_of_day_month_year[1])
    day_of_return=int(list_of_day_month_year[2])
    bool_val_for_date=(datetime.now()>datetime(year_of_return,month_of_return,day_of_return))
    return bool_val_for_date

def send_reminder_mail_student_info(frame,book,idate,retdate):
    global i
    global r
    global b
    li=idate.split('-')
    i=li[2]+'-'+li[1]+'-'+li[0]
    lr=retdate.split('-')
    r=lr[2]+'-'+lr[1]+'-'+lr[0]
    b=book

    Button(frame,text='Send Reminder',font=('verdana',15),command=send_reminder_mail_for_student_info).pack()

def send_reminder_mail_for_student_info():
    email=os.environ.get('project_email')
    passkey=os.environ.get('project_email_password')
    msg_for_reminder=MIMEText('The Book - (  '+b+'  ) you issued on '+i+' was due on '+r+' .\nPlease do return the issued book at the earliest.')

    msg_for_reminder['Subject']='Friendly Reminder:'
    msg_for_reminder['From']=email
    msg_for_reminder['To']=main_emailid_for_student_info_page
    ref_111=0
    try:
        with smtplib.SMTP('smtp.gmail.com','587') as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(email,passkey)
            smtp.sendmail(email,main_emailid_for_student_info_page,msg_for_reminder.as_string())
        ref_111=0
    except:
        ref_111=1

    if ref_111==1:
        messagebox.showinfo('oops','something went wrong')
    else:
        messagebox.showinfo('reminder','reminder mail sent to '+main_username_for_student_info_page)

def obtaining_student_info_for_view_student_info_admin(list_to_regard):
    global main_username_for_student_info_page
    global main_emailid_for_student_info_page
    global main_phoneno_for_student_info_page
    global main_firstname_for_student_info_page
    global main_lastname_for_student_info_page
    global main_gender_for_student_info_page
    global main_country_for_student_info_page
    global main_issue1_for_student_info
    global main_issue2_for_student_info
    global main_issue3_for_student_info
    global main_bookname1_for_student_info
    global main_bookname2_for_student_info
    global main_bookname3_for_student_info
    global main_author1_for_student_info
    global main_author2_for_student_info
    global main_author3_for_student_info
    global main_issue_date1__for_student_info
    global main_issue_date2__for_student_info
    global main_issue_date3__for_student_info
    global main_return_date1__for_student_info    
    global main_return_date2__for_student_info
    global main_return_date3__for_student_info
    query_for_student_last_update="select username,emailid,phoneno,firstname,lastname,gender,country from logindata where username='{0}';"
    cursor_mysql.execute(query_for_student_last_update.format(list_to_regard[0]))
    new_list7=cursor_mysql.fetchall()

    main_username_for_student_info_page=new_list7[0][0]
    main_emailid_for_student_info_page=new_list7[0][1]
    main_phoneno_for_student_info_page=new_list7[0][2]
    main_firstname_for_student_info_page=new_list7[0][3]
    main_lastname_for_student_info_page=new_list7[0][4]
    main_gender_for_student_info_page=new_list7[0][5]
    main_country_for_student_info_page=new_list7[0][6]

    query1211="select * from loginissue where username='{0}';"
    cursor_mysql.execute(query1211.format(main_username_for_student_info_page))
    output=cursor_mysql.fetchall()
    main_issue1_for_student_info=output[0][1]
    main_issue2_for_student_info=output[0][2]
    main_issue3_for_student_info=output[0][3]

    if main_issue1_for_student_info==None:
        main_bookname1_for_student_info=None
        main_bookname2_for_student_info=None
        main_bookname3_for_student_info=None
        main_issue_date1__for_student_info=None
        main_issue_date2__for_student_info=None
        main_issue_date3__for_student_info=None
        main_return_date1__for_student_info=None
        main_return_date2__for_student_info=None
        main_return_date3__for_student_info=None
        main_author1_for_student_info=None
        main_author2_for_student_info=None
        main_author3_for_student_info=None
    
    elif main_issue3_for_student_info!=None:
        q11="select bookname,bookauthor from bookdata where book_id='{0}';"
        q12="select date_of_issue,date_of_return from bookissue where book_id2='{0}';"
        cursor_mysql.execute(q11.format(main_issue1_for_student_info))
        out11=cursor_mysql.fetchall()
        a=1
        cursor_mysql.execute(q12.format(main_issue1_for_student_info))
        out12=cursor_mysql.fetchall()
        main_bookname1_for_student_info=out11[0][0]
        main_author1_for_student_info=out11[0][1]
        main_issue_date1__for_student_info=out12[0][0]
        main_return_date1__for_student_info=out12[0][1]

        q21="select bookname,bookauthor from bookdata where book_id='{0}';"
        q22="select date_of_issue,date_of_return from bookissue where book_id2='{0}';"
        cursor_mysql.execute(q21.format(main_issue2_for_student_info))
        out21=cursor_mysql.fetchall()
        a=1
        cursor_mysql.execute(q22.format(main_issue2_for_student_info))
        out22=cursor_mysql.fetchall()
        main_bookname2_for_student_info=out21[0][0]
        main_author2_for_student_info=out21[0][1]
        main_issue_date2__for_student_info=out22[0][0]
        main_return_date2__for_student_info=out22[0][1]

        q31="select bookname,bookauthor from bookdata where book_id='{0}';"
        q32="select date_of_issue,date_of_return from bookissue where book_id2='{0}';"
        cursor_mysql.execute(q31.format(main_issue3_for_student_info))
        out31=cursor_mysql.fetchall()
        a=1
        cursor_mysql.execute(q32.format(main_issue3_for_student_info))
        out32=cursor_mysql.fetchall()
        main_bookname3_for_student_info=out31[0][0]
        main_author3_for_student_info=out31[0][1]
        main_issue_date3__for_student_info=out32[0][0]
        main_return_date3__for_student_info=out32[0][1]


    elif main_issue3_for_student_info==None and main_issue2_for_student_info!=None:
        q11="select bookname,bookauthor from bookdata where book_id='{0}';"
        q12="select date_of_issue,date_of_return from bookissue where book_id2='{0}';"
        cursor_mysql.execute(q11.format(main_issue1_for_student_info))
        out11=cursor_mysql.fetchall()
        a=1
        cursor_mysql.execute(q12.format(main_issue1_for_student_info))
        out12=cursor_mysql.fetchall()
        main_bookname1_for_student_info=out11[0][0]
        main_author1_for_student_info=out11[0][1]
        main_issue_date1__for_student_info=out12[0][0]
        main_return_date1__for_student_info=out12[0][1]

        q21="select bookname,bookauthor from bookdata where book_id='{0}';"
        q22="select date_of_issue,date_of_return from bookissue where book_id2='{0}';"
        cursor_mysql.execute(q21.format(main_issue2_for_student_info))
        out21=cursor_mysql.fetchall()
        a=1
        cursor_mysql.execute(q22.format(main_issue2_for_student_info))
        out22=cursor_mysql.fetchall()
        main_bookname2_for_student_info=out21[0][0]
        main_author2_for_student_info=out21[0][1]
        main_issue_date2__for_student_info=out22[0][0]
        main_return_date2__for_student_info=out22[0][1]

        main_bookname3_for_student_info=None
        main_author3_for_student_info=None
        main_issue_date3__for_student_info=None
        main_return_date3__for_student_info=None

    elif main_issue3_for_student_info==None and main_issue2_for_student_info==None and main_issue1_for_student_info!=None:
        q11="select bookname,bookauthor from bookdata where book_id='{0}';"
        q12="select date_of_issue,date_of_return from bookissue where book_id2='{0}';"
        cursor_mysql.execute(q11.format(main_issue1_for_student_info))
        out11=cursor_mysql.fetchall()
        a=1
        cursor_mysql.execute(q12.format(main_issue1_for_student_info))
        out12=cursor_mysql.fetchall()
        main_bookname1_for_student_info=out11[0][0]
        main_author1_for_student_info=out11[0][1]
        main_issue_date1__for_student_info=out12[0][0]
        main_return_date1__for_student_info=out12[0][1]

        main_bookname2_for_student_info=None
        main_author2_for_student_info=None
        main_issue_date2__for_student_info=None
        main_return_date2__for_student_info=None

        main_bookname3_for_student_info=None
        main_author3_for_student_info=None
        main_issue_date3__for_student_info=None
        main_return_date3__for_student_info=None


def clicking_proceed_in_student_info_admin():
    global user_name_select_for_view_students_admin_var
    global main_list_regarding_username_and_name_student_info_admin
    global dict_of_students_info_admin

    try:
        user_name_select_for_view_students_admin=user_name_select_for_view_students_admin_var.get()
    except:
        user_name_select_for_view_students_admin='chumma'
    main_list_regarding_username_and_name_student_info_admin=[]
    if user_name_select_for_view_students_admin==0:
        messagebox.showerror('View Students','Please Select a Student')
    elif user_name_select_for_view_students_admin=='chumma' or user_name_select_for_view_students_admin_var=='chumma':
        messagebox.showinfo('oops','there are no students to view right now')
        librarymanag_from_student_info_admin()
    else:
        main_list_regarding_username_and_name_student_info_admin=dict_of_students_info_admin[user_name_select_for_view_students_admin][0:2]   #just so that the 4th column is taken
        student_view_books_admin_tkinter_page_student_details()




def no_students_to_view_admin():
    global user_name_select_for_view_students_admin_var
    global user_name_select_for_view_students_admin
    book_name_select_for_view_students_admin=user_name_select_for_view_students_admin_var='chumma'
    Label(students_info_admin_page_root,text="There are no books available right now",font=("lucida handwriting", 30),bg='black',fg='white').place(x=500,y=500)


def if_is_scroll_for_students_info_admin():

    global students_info_admin_page_root
    global dict_of_students_info_admin
    innerframe8=LabelFrame(students_info_admin_page_root,text='Students',bd=15,width=1000,font=('verdana',15))
    innerframe8.place(x=350,y=300)

    #Creating Main fram:
    main_frame8=Frame(innerframe8,width=1000)
    main_frame8.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva8=Canvas(main_frame8,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva8.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll8=ttk.Scrollbar(main_frame8,orient=VERTICAL,command=canva8.yview) 
    scroll8.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva8.configure(yscrollcommand=scroll8.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva8.bind('<Configure>', lambda e: canva8.configure(scrollregion=canva8.bbox("all")))
    #Creating another frame inside canvas
    second_frame8=Frame(canva8,width=1000)
    #placing the second frame inside canva
    canva8.create_window((0,0),window=second_frame8,anchor='nw',)#nw means on the top right corner
    global user_name_select_for_view_students_admin_var
    user_name_select_for_view_students_admin_var=IntVar()
    for i in range(1,count_of_students_info_admin+1):
        if i%2==0:
            Radiobutton(second_frame8,text='Username: '+dict_of_students_info_admin[i][0]+'\nName: '+dict_of_students_info_admin[i][1],fg='black',font=("lucida handwriting", 25),indicator=0,variable=user_name_select_for_view_students_admin_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame8,text='Username: '+dict_of_students_info_admin[i][0]+'\nName: '+dict_of_students_info_admin[i][1],fg='black',font=("lucida handwriting", 25),indicator=0,variable=user_name_select_for_view_students_admin_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()







def no_scroll_for_students_info_admin():
    global students_info_admin_page_root
    global dict_of_students_info_admin
    global count_of_students_info_admin

    innerframe8=LabelFrame(students_info_admin_page_root,text='Students',bd=15,width=1000,font=('verdana',15))
    innerframe8.place(x=350,y=300)

    #Creating Main fram:
    main_frame8=Frame(innerframe8,width=1000)
    main_frame8.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    global user_name_select_for_view_students_admin_var
    user_name_select_for_view_students_admin_var=IntVar()
    for i in range(1,count_of_students_info_admin+1):
        if i%2==0:
            Radiobutton(main_frame8,text='Username: '+dict_of_students_info_admin[i][0]+'\nName: '+dict_of_students_info_admin[i][1],fg='black',font=("lucida handwriting", 25),indicator=0,variable=user_name_select_for_view_students_admin_var,value=i,width=50,bg='cyan',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame8,text='Username: '+dict_of_students_info_admin[i][0]+'\nName: '+dict_of_students_info_admin[i][1],fg='black',font=("lucida handwriting", 25),indicator=0,variable=user_name_select_for_view_students_admin_var,value=i,width=50,bg='blue',padx=10,anchor='w').pack()




def creating_dict_table_for_student_info_admin():
    global count_of_students_info_admin
    global list_of_students_info_admin 
    global dict_of_students_info_admin

    list_of_students_info_admin=[]
    dict_of_students_info_admin={}
    query1="select username,firstname,lastname from logindata where accountype='Student';"
    cursor_mysql.execute(query1)
    output=cursor_mysql.fetchall()

    if output==[]:
        list_of_students_info_admin=[]
        dict_of_students_info_admin={}
        count_of_students_info_admin=0
    else:
        for i in range(len(output)):
            dict_of_students_info_admin[i+1]=[output[i][0],output[i][1]+' '+output[i][2]]
            list_of_students_info_admin.append([output[i][0],output[i][1]+' '+output[i][2],(i+1)])
            count_of_students_info_admin=len(list_of_students_info_admin)



def searcher_bar_mid_fn_for_student_info_admin():
    global search_bar_students_info_for_admin_var
    global search_bar_students_info_for_admin
    global dict_of_students_info_admin
    global count_of_students_info_admin
    search_bar_students_info_for_admin_2=search_bar_students_info_for_admin_var.get()
    search_bar_students_info_for_admin=search_bar_students_info_for_admin_2.lower()
    if count_of_students_info_admin==0:
        no_students_to_view_admin()
    elif count_of_students_info_admin<=4:
        no_scroll_for_students_info_admin_mid_fn()
    else:
        if_is_scroll_for_view_students_info_for_mid_fn()



def if_is_scroll_for_view_students_info_for_mid_fn():
    global count_of_students_info_admin
    global dict_of_students_info_admin
    global list_of_students_info_admin
    global search_bar_students_info_for_admin
    global variable_list_order_for_students_info_admin_2
    variable_list_order_for_students_info_admin_2=[]

    #search bar

    if search_bar_students_info_for_admin=='':
        searaching_and_reodering_radiobutton_of_students_info_admin_page_for_scroll(list_of_students_info_admin)
    else:
        pass
        for sample in list_of_students_info_admin:
            if (sample[0].lower()==search_bar_students_info_for_admin) and (sample[1].lower()==search_bar_students_info_for_admin) and ((sample[0].lower()).startswith(search_bar_students_info_for_admin)) and ((sample[1].lower()).startswith(search_bar_students_info_for_admin)) and ((sample[0].lower()).endswith(search_bar_students_info_for_admin)) and ((sample[1].lower()).endswith(search_bar_students_info_for_admin)) and (search_bar_students_info_for_admin in sample[0].lower()) and (search_bar_students_info_for_admin in sample[1].lower()):
                variable_list_order_for_students_info_admin_2.append(sample)
            else:
                continue
        for sample2 in list_of_students_info_admin:
            if (sample2 not in variable_list_order_for_students_info_admin_2) and (sample2[0].lower()==search_bar_students_info_for_admin):
                variable_list_order_for_students_info_admin_2.append(sample2)
            else:
                continue
        for sample3 in list_of_students_info_admin:
            if (sample3 not in variable_list_order_for_students_info_admin_2) and (sample3[1].lower()==search_bar_students_info_for_admin):
                variable_list_order_for_students_info_admin_2.append(sample3)
            else:
                continue
        for sample5 in list_of_students_info_admin:
            if (sample5 not in variable_list_order_for_students_info_admin_2) and ((sample5[0].lower()).startswith(search_bar_students_info_for_admin)):
                variable_list_order_for_students_info_admin_2.append(sample5)
            else:
                continue
        for sample6 in list_of_students_info_admin:
            if (sample6 not in variable_list_order_for_students_info_admin_2) and ((sample6[1].lower()).startswith(search_bar_students_info_for_admin)):
                variable_list_order_for_students_info_admin_2.append(sample6)
            else:
                continue
        for sample7 in list_of_students_info_admin:
            if (sample7 not in variable_list_order_for_students_info_admin_2) and ((sample7[0].lower()).endswith(search_bar_students_info_for_admin)):
                variable_list_order_for_students_info_admin_2.append(sample7)
            else:
                continue
        for sample8 in list_of_students_info_admin:
            if (sample8 not in variable_list_order_for_students_info_admin_2) and ((sample8[1].lower()).endswith(search_bar_students_info_for_admin)):
                variable_list_order_for_students_info_admin_2.append(sample8)
            else:
                continue
        for sample9 in list_of_students_info_admin:
            if (sample9 not in variable_list_order_for_students_info_admin_2) and (search_bar_students_info_for_admin in sample9[0].lower()):
                variable_list_order_for_students_info_admin_2.append(sample9)
            else:
                continue
        for sample10 in list_of_students_info_admin:
            if (sample10 not in variable_list_order_for_students_info_admin_2) and (search_bar_students_info_for_admin in sample10[1].lower()):
                variable_list_order_for_students_info_admin_2.append(sample10)
            else:
                continue
        for sample11 in list_of_students_info_admin:
            if sample11 not in variable_list_order_for_students_info_admin_2:
                variable_list_order_for_students_info_admin_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_students_info_admin_page_for_scroll(variable_list_order_for_students_info_admin_2)







def searaching_and_reodering_radiobutton_of_students_info_admin_page_for_scroll(list_ordered):
    global user_name_select_for_view_students_admin_var
    global count_of_students_info_admin
    global dict_of_students_info_admin
    global list_of_students_info_admin
    global search_bar_students_info_for_admin
    global variable_list_order_for_students_info_admin_2
    variable_list_order_for_students_info_admin_2=[]



    innerframe8=LabelFrame(students_info_admin_page_root,text='Students',bd=15,width=1000,font=('verdana',15))
    innerframe8.place(x=350,y=300)

    #Creating Main fram:
    main_frame8=Frame(innerframe8,width=1000)
    main_frame8.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and y
    #Creating Canvas
    canva8=Canvas(main_frame8,bd=20)  #Canvas is where we can draw but used for scrollin . This canvas is where the scrollbar will be placed
    canva8.pack(side=LEFT,fill=BOTH,expand=1)# same as main frame
    #Creating scroll bar
    scroll8=ttk.Scrollbar(main_frame8,orient=VERTICAL,command=canva8.yview) 
    scroll8.pack(side=RIGHT,fill=Y)  # Because Scroll bar is towards the right of the frame and fill it down
    #Configure the canvas
    canva8.configure(yscrollcommand=scroll8.set,width=710,height=500) #Canvas is enabling the yscroll command to Scroll and then we have to bind it
    canva8.bind('<Configure>', lambda e: canva8.configure(scrollregion=canva8.bbox("all")))
    #Creating another frame inside canvas
    second_frame8=Frame(canva8,width=1000)
    #placing the second frame inside canva
    canva8.create_window((0,0),window=second_frame8,anchor='nw',)#nw means on the top right corner


    user_name_select_for_view_students_admin_var=IntVar()

    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(second_frame8,text='Username: '+i[0]+'\nName: '+i[1],fg='black',font=("lucida handwriting", 25),indicator=0,variable=user_name_select_for_view_students_admin_var,value=i[2],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(second_frame8,text='Username: '+i[0]+'\nName: '+i[1],fg='black',font=("lucida handwriting", 25),indicator=0,variable=user_name_select_for_view_students_admin_var,value=i[2],width=50,bg='cyan',padx=10,anchor='w').pack()






def no_scroll_for_students_info_admin_mid_fn():
    global count_of_students_info_admin
    global dict_of_students_info_admin
    global list_of_students_info_admin
    global search_bar_students_info_for_admin
    global variable_list_order_for_students_info_admin_2
    variable_list_order_for_students_info_admin_2=[]



    #search Bar operation

    if search_bar_students_info_for_admin=='':
        searaching_and_reodering_radiobutton_of_students_info_admin_page_for_no_scroll(list_of_students_info_admin)
    else:
        pass
        for sample in list_of_students_info_admin:
            if (sample[0].lower()==search_bar_students_info_for_admin) and (sample[1].lower()==search_bar_students_info_for_admin) and ((sample[0].lower()).startswith(search_bar_students_info_for_admin)) and ((sample[1].lower()).startswith(search_bar_students_info_for_admin)) and ((sample[0].lower()).endswith(search_bar_students_info_for_admin)) and ((sample[1].lower()).endswith(search_bar_students_info_for_admin)) and (search_bar_students_info_for_admin in sample[0].lower()) and (search_bar_students_info_for_admin in sample[1].lower()):
                variable_list_order_for_students_info_admin_2.append(sample)
            else:
                continue
        for sample2 in list_of_students_info_admin:
            if (sample2 not in variable_list_order_for_students_info_admin_2) and (sample2[0].lower()==search_bar_students_info_for_admin):
                variable_list_order_for_students_info_admin_2.append(sample2)
            else:
                continue
        for sample3 in list_of_students_info_admin:
            if (sample3 not in variable_list_order_for_students_info_admin_2) and (sample3[1].lower()==search_bar_students_info_for_admin):
                variable_list_order_for_students_info_admin_2.append(sample3)
            else:
                continue
        for sample5 in list_of_students_info_admin:
            if (sample5 not in variable_list_order_for_students_info_admin_2) and ((sample5[0].lower()).startswith(search_bar_students_info_for_admin)):
                variable_list_order_for_students_info_admin_2.append(sample5)
            else:
                continue
        for sample6 in list_of_students_info_admin:
            if (sample6 not in variable_list_order_for_students_info_admin_2) and ((sample6[1].lower()).startswith(search_bar_students_info_for_admin)):
                variable_list_order_for_students_info_admin_2.append(sample6)
            else:
                continue
        for sample7 in list_of_students_info_admin:
            if (sample7 not in variable_list_order_for_students_info_admin_2) and ((sample7[0].lower()).endswith(search_bar_students_info_for_admin)):
                variable_list_order_for_students_info_admin_2.append(sample7)
            else:
                continue
        for sample8 in list_of_students_info_admin:
            if (sample8 not in variable_list_order_for_students_info_admin_2) and ((sample8[1].lower()).endswith(search_bar_students_info_for_admin)):
                variable_list_order_for_students_info_admin_2.append(sample8)
            else:
                continue
        for sample9 in list_of_students_info_admin:
            if (sample9 not in variable_list_order_for_students_info_admin_2) and (search_bar_students_info_for_admin in sample9[0].lower()):
                variable_list_order_for_students_info_admin_2.append(sample9)
            else:
                continue
        for sample10 in list_of_students_info_admin:
            if (sample10 not in variable_list_order_for_students_info_admin_2) and (search_bar_students_info_for_admin in sample10[1].lower()):
                variable_list_order_for_students_info_admin_2.append(sample10)
            else:
                continue
        for sample11 in list_of_students_info_admin:
            if sample11 not in variable_list_order_for_students_info_admin_2:
                variable_list_order_for_students_info_admin_2.append(sample11)
            else:
                continue
        searaching_and_reodering_radiobutton_of_students_info_admin_page_for_no_scroll(variable_list_order_for_students_info_admin_2)


def searaching_and_reodering_radiobutton_of_students_info_admin_page_for_no_scroll(list_ordered):
    global user_name_select_for_view_students_admin_var
    global count_of_students_info_admin
    global dict_of_students_info_admin
    global list_of_students_info_admin
    global search_bar_students_info_for_admin
    global variable_list_order_for_students_info_admin_2
    variable_list_order_for_students_info_admin_2=[]

    innerframe8=LabelFrame(students_info_admin_page_root,text='Students',bd=15,width=1000,font=('verdana',15))
    innerframe8.place(x=350,y=300)

    #Creating Main fram:
    main_frame8=Frame(innerframe8,width=1000)
    main_frame8.pack(fill=BOTH,expand=1) #This expands the fram to its limit . the both refer expanding both X and 
    user_name_select_for_view_students_admin_var=IntVar()
    for i in list_ordered:
        if list_ordered.index(i)%2==0:
            Radiobutton(main_frame8,text='Username: '+i[0]+'\nName: '+i[1],fg='black',font=("lucida handwriting", 25),indicator=0,variable=user_name_select_for_view_students_admin_var,value=i[2],width=50,bg='blue',padx=10,anchor='w').pack()
        else:
            Radiobutton(main_frame8,text='Username: '+i[0]+'\nName: '+i[1],fg='black',font=("lucida handwriting", 25),indicator=0,variable=user_name_select_for_view_students_admin_var,value=i[2],width=50,bg='cyan',padx=10,anchor='w').pack()


#*************************************************************************************************************************************************************************************

def librarymanag_from_student_info_admin_tk():
    global librarymang_home_page_admin_root
    students_info_admin_tk_page_root.destroy()

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)





def librarymanag_from_student_info_admin():
    global librarymang_home_page_admin_root
    students_info_admin_page_root.destroy()

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)




def librarymang_home_page_admin_from_view_books_admin_tkinter_info_page():
    global librarymang_home_page_admin_root
    view_books_info_admin_page_root.destroy()

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)

def librarymanag_from_view_books_admin():
    global librarymang_home_page_admin_root
    view_books_admin_page_root.destroy()

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)


def librarymanag_from_update_verification():
    global librarymang_home_page_admin_root
    book_update_verification_tkinter_page_root.destroy()

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)


def librarymanag_from_update_search_page():
    global librarymang_home_page_admin_root
    update_books_admin_page_root.destroy()

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)






def librarymang_home_page_admin():
    global librarymang_home_page_admin_root
    login_screen.destroy()

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)


def librarymang_home_page_admin_after_adding():
    
    add_books_admin_page_root.destroy()

    global librarymang_home_page_admin_root

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)



def librarymang_home_page_admin_from_deleting_confirmation_page():
    
    book_delete_verification_tkinter_page_root.destroy()

    global librarymang_home_page_admin_root

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)


def librarymang_home_page_admin_from_book_selecting_from_delete_page():
    
    delete_books_admin_page_root.destroy()

    global librarymang_home_page_admin_root

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)



def librarymang_home_page_admin_after_profile():
    
    profile_admin_root.destroy()

    global librarymang_home_page_admin_root

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)

def librarymang_home_page_admin_after_profile_updation():
    
    profile_admin_root_edit.destroy()

    global librarymang_home_page_admin_root

    librarymang_home_page_admin_root=Tk()
    librarymang_home_page_admin_root.title("Home")
    librarymang_home_page_admin_root.state("zoomed")
    librarymang_home_page_admin_root.config(background = "black", pady=10)
    Label(librarymang_home_page_admin_root, text="Library Management",width=100, font=("freestyle script", 70)).pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Label(librarymang_home_page_admin_root, text="",bg = "black").pack()
    Button(librarymang_home_page_admin_root, text="Add books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=add_books_admin_page).place(x=400,y=300)
    Button(librarymang_home_page_admin_root, text="Delete books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=delete_books_admin_page).place(x=1100,y=300)
    Button(librarymang_home_page_admin_root, text="Update books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=update_books_admin_page).place(x=400,y=500)
    Button(librarymang_home_page_admin_root, text="View books", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=view_books_admin_page).place(x=1100,y=500)
    Button(librarymang_home_page_admin_root, text="Student Info", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=students_info_admin_page).place(x=400,y=700)
    Button(librarymang_home_page_admin_root, text="Profile", width=15, height=2, font=("lucida handwriting",30),cursor='hand2',command=profile_page_admin).place(x=1100,y=700)
    photo = PhotoImage(file = "e.png")
    librarymang_home_page_admin_root.iconphoto(False, photo)



#***************************************************************************************************************************************************************************************************



def profile_page_admin():
    global profile_admin_root
    librarymang_home_page_admin_root.destroy()
    profile_admin_root=Tk()
    profile_admin_root.title("Profile")
    profile_admin_root.state("zoomed")
    profile_admin_root.config(background = "black", pady=10)
    Label(profile_admin_root, text="Profile",width=100, font=("freestyle script", 70)).pack()
    Label(profile_admin_root,text="Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(profile_admin_root,text="Username:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(profile_admin_root,text="Email-Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=350)
    Label(profile_admin_root,text="Gender:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=350)
    Label(profile_admin_root,text="Country:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=600)
    Label(profile_admin_root,text="Account Type:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=600)



    Label(profile_admin_root,text=user_name,font=("verdana", 20),width=30,anchor='w').place(x=250,y=150)
    Label(profile_admin_root,text=user_username,font=("verdana", 20),width=20,anchor='w').place(x=1225,y=150)
    Label(profile_admin_root,text=user_email_id,font=("verdana", 20),width=30,anchor='w').place(x=310,y=350)
    Label(profile_admin_root,text=user_gender,font=("verdana", 20),width=20,anchor='w').place(x=1185,y=350)
    Label(profile_admin_root,text=user_country,font=("verdana", 20),width=20,anchor='w').place(x=300,y=600)
    Label(profile_admin_root,text=user_account,font=("verdana", 20),width=20,anchor='w').place(x=1300,y=600)

    Button(profile_admin_root,text='Edit',font=('verdana',25),cursor='hand2',bg='green',width=10,command=profile_page_admin_edit).place(x=850,y=800)
    Button(profile_admin_root,text='Go Back',font=('verdana',25),cursor='hand2',width=10,command=librarymang_home_page_admin_after_profile).place(x=500,y=800)
    Button(profile_admin_root,text='Log Out',font=('verdana',25),cursor='hand2',bg='red',width=10,command=log_out_from_profile_admin).place(x=1200,y=800)
    photo = PhotoImage(file = "e.png")
    profile_admin_root.iconphoto(False, photo)

def profile_page_admin_edit():
    global profile_admin_root_edit
    global edit_profile_first_name_var
    global edit_profile_last_name_var
    global edit_profile_username_var
    global edit_profile_gender_var
    global edit_profile_country_var
    global edit_profile_phone_no_var
    if user_phone_no==None:
        phoneno=''
    else:
        phoneno=str(user_phone_no)
    profile_admin_root.destroy()
    profile_admin_root_edit=Tk()
    profile_admin_root_edit.title("Login")
    profile_admin_root_edit.state("zoomed")
    profile_admin_root_edit.config(background = "black", pady=10)
    Label(profile_admin_root_edit, text="Profile",width=100, font=("freestyle script", 70)).pack()
    Label(profile_admin_root_edit,text="First Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=150)
    Label(profile_admin_root_edit,text="Last Name:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=150)
    Label(profile_admin_root_edit,text="Username:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=350)
    Label(profile_admin_root_edit,text="Email-Id:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=350)
    Label(profile_admin_root_edit,text="Gender:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=600)
    Label(profile_admin_root_edit,text="Country:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=1000,y=600)
    Label(profile_admin_root_edit,text="Phone No:",bg='black',fg='white',font=("lucida handwriting", 25)).place(x=100,y=850)

    edit_profile_first_name_var=StringVar()
    edit_profile_last_name_var=StringVar()
    edit_profile_username_var=StringVar()
    edit_profile_gender_var=StringVar()
    edit_profile_country_var=StringVar()
    edit_profile_phone_no_var=StringVar()

    edit_profile_first_name_var.set(user_first_name)
    edit_profile_last_name_var.set(user_last_name)
    edit_profile_username_var.set(user_username)
    edit_profile_gender_var.set(user_gender)
    edit_profile_country_var.set(user_country)
    edit_profile_phone_no_var.set(phoneno)


    e1=Entry(profile_admin_root_edit,textvariable=edit_profile_first_name_var,font=("verdana", 20),width=30)
    e2=Entry(profile_admin_root_edit,textvariable=edit_profile_last_name_var,font=("verdana", 20),width=20)
    e3=Entry(profile_admin_root_edit,textvariable=edit_profile_username_var,font=("verdana", 20),width=20)
    e4=Label(profile_admin_root_edit,text=user_email_id,font=("verdana", 20),width=30,anchor='w')

    edit_profile_gender_list=[ 'male','female']
    edit_profile_gender_droplist=OptionMenu(profile_admin_root_edit, edit_profile_gender_var, *edit_profile_gender_list)
    edit_profile_gender_droplist.config(font=("verdana", 20),width=20)

    edit_profile_country_list=[ 'India' ,'US' , 'UK' ,'Australia' ,'Canada']
    edit_profile_country_droplist=OptionMenu(profile_admin_root_edit, edit_profile_country_var, *edit_profile_country_list)
    edit_profile_country_droplist.config(font=("verdana", 20),width=20)
    edit_profile_country_droplist.place(x=1250,y=250)

    e7=Entry(profile_admin_root_edit,textvariable=edit_profile_phone_no_var,font=("verdana", 20),width=20)

    e1.place(x=350,y=150)
    e2.place(x=1235,y=150)
    e3.place(x=350,y=350)
    e4.place(x=1245,y=350)
    edit_profile_gender_droplist.place(x=300,y=600)
    edit_profile_country_droplist.place(x=1200,y=600)
    e7.place(x=310,y=850)

    Button(profile_admin_root_edit,text='Edit',font=('verdana',25),cursor='hand2',bg='green',width=10,command=check_edit_profile_info_admin).place(x=1350,y=750)
    Button(profile_admin_root_edit,text='Go Back',font=('verdana',25),cursor='hand2',width=10,command=librarymang_home_page_admin_after_profile_updation).place(x=1350,y=900)
    photo = PhotoImage(file = "e.png")
    profile_admin_root_edit.iconphoto(False, photo)



def check_edit_profile_info_admin():
    edit_profile_first_name=edit_profile_first_name_var.get()
    edit_profile_last_name=edit_profile_last_name_var.get()
    edit_profile_username=edit_profile_username_var.get()
    edit_profile_gender=edit_profile_gender_var.get()
    edit_profile_country=edit_profile_country_var.get()
    edit_profile_phone_no=edit_profile_phone_no_var.get()
    ref_for_edit_verify=0
    query_edit_info="select username from logindata where emailid!='{0}';"      #We are creating 2 lists of already eisting username and emails from testlogin
    cursor_mysql.execute(query_edit_info.format(user_email_id))
    output1=cursor_mysql.fetchall()
    list_of_usernames=[]
    for username_tuple in output1:
        list_of_usernames.append(username_tuple[0])
    if ref_for_edit_verify==0:
        if edit_profile_username=='' and ref_for_edit_verify==0:
            messagebox.showerror('username error','please enter username')
            ref_for_edit_verify=2
        elif len(edit_profile_username)<6 and len(edit_profile_username)>=20 and ref_for_edit_verify==0:
            messagebox.showerror('username error','username must have atleast 6 char')
            ref_for_edit_verify=2
        elif edit_profile_username[0].isdigit() and ref_for_edit_verify==0:
            messagebox.showerror('username error','username cant start with numbers')
            ref_for_edit_verify=2
        elif edit_profile_username in list_of_usernames:   #checking for duplicates of username
            messagebox.showerror('username error','Username is taken')
            ref_for_edit_verify=2
        else:
            pass
    
    if ref_for_edit_verify==0:
        if edit_profile_phone_no=='':
            pass
        elif not edit_profile_phone_no.isdigit():
            messagebox.showerror('phone no','invaid phone no')
            ref_for_edit_verify=4
        elif len(str(edit_profile_phone_no))!=10:
            messagebox.showerror('phone no','invaid phone no')
            ref_for_edit_verify=4
        else:
            pass
    else:
        pass
    if len(edit_profile_first_name)==0 and ref_for_edit_verify==0:
        messagebox.showerror('error','please enter name')
        ref_for_edit_verify=5
    elif len(edit_profile_last_name)==0 and ref_for_edit_verify==0:
        messagebox.showerror('error','please enter last name')
        ref_for_edit_verify=5
    elif len(edit_profile_first_name)>20 and ref_for_edit_verify==0:
        messagebox.showerror('error','name should be less than 21 charcters')
        ref_for_edit_verify=5
    elif len(edit_profile_last_name)>20 and ref_for_edit_verify==0:
        messagebox.showerror('error','last name should be less than 21 charcters')
        ref_for_edit_verify=5
    else:
        pass

    if edit_profile_gender=='' and ref_for_edit_verify==0:
        messagebox.showerror('error','please enter your gender')
        ref_for_edit_verify=6
    elif edit_profile_gender not in ['male','female']:
        messagebox.showerror('error','please enter your gender')
        ref_for_edit_verify=6
    else:
        pass
    if ref_for_edit_verify==0 and edit_profile_country=='':
        messagebox.showerror('error','please enter country')
        ref_for_edit_verify=7
    elif ref_for_edit_verify==0 and (edit_profile_country not in [ 'India' ,'US' , 'UK' ,'Australia' ,'Canada']):
        messagebox.showerror('error','cant verify your country')
        ref_for_edit_verify=7
    else:
        pass


    if (('\'' in edit_profile_username) or ('\"' in edit_profile_username) or ('\'' in edit_profile_first_name) or ('\"' in edit_profile_first_name) or ('\'' in edit_profile_last_name) or ('\"' in edit_profile_last_name)) and  ref_for_edit_verify==0:
        messagebox.showinfo('error','Dnot use \' or \" in any field')
        ref_for_edit_verify=9
    if ref_for_edit_verify==0:
        updating_profile_admin(edit_profile_username,edit_profile_phone_no,edit_profile_first_name,edit_profile_last_name,edit_profile_gender,edit_profile_country)  # True and False returned is just for reference. In the main program define a global variable using 'global' and assign true and false to that. if the variable is true follow on with the sign up and then break out of while loop int new page but if false reload page using while loop.
    else:
        pass

def updating_profile_admin(username,phoneno,firstname,lastname,gender,country):
    global user_username
    global user_name
    global user_gender
    global user_phone_no
    global user_first_name
    global user_last_name
    global user_country 
    try:
        if phoneno=='':
            query1="update logindata set username='{0}',phoneno=Null,firstname='{1}',lastname='{2}',gender='{3}',country='{4}' where emailid='{5}';"
            query2="update loginissue set username='{0}' where username='{1}';"
            query3="update bookissue set username='{0}' where username='{1}';"
            cursor_mysql.execute(query1.format(username,firstname,lastname,gender,country,user_email_id))
            mycon.commit()
            a=2
            cursor_mysql.execute(query2.format(username,user_username))
            mycon.commit()
            a=3
            cursor_mysql.execute(query3.format(username,user_username))
            mycon.commit()
        else:
            query1="update logindata set username='{0}',phoneno='{1}',firstname='{2}',lastname='{3}',gender='{4}',country='{5}' where emailid='{6}';"
            query2="update loginissue set username='{0}' where username='{1}';"
            query3="update bookissue set username='{0}' where username='{1}';"
            cursor_mysql.execute(query1.format(username,phoneno,firstname,lastname,gender,country,user_email_id))
            mycon.commit()
            a=2
            cursor_mysql.execute(query2.format(username,user_username))
            mycon.commit()
            a=3
            cursor_mysql.execute(query3.format(username,user_username))
            mycon.commit()
        ref=1
    except:
        messagebox.showinfo('oops','something went wrong')
        ref=2
        librarymang_home_page_admin_after_profile_updation()
    if ref==1:
        messagebox.showinfo('success','Profile Updated')

        user_username=username
        user_name=firstname+' '+lastname
        user_gender=gender
        user_phone_no=phoneno
        user_first_name=firstname
        user_last_name=lastname
        user_country=country
        librarymang_home_page_admin_after_profile_updation()









def log_out_from_profile_admin():
    global user_email_id
    global user_name
    global user_username           
    global user_gender
    global user_phone_no
    global user_country
    global user_account
    user_email_id=''
    user_name=''
    user_username=''
    user_phone_no=None
    user_gender=''
    user_country=''
    user_account=''
    profile_admin_root.destroy()
    login_screen_from_student_profile()









#***********************************************************************************************************************************************************************************





def clear_frame(frame):
    frame.destroy()



def email_verification_send_mail(email_to_be_verified):
    global OTP_generated
    OTP_gen=random.randint(100000,999999)
    OTP_generated=str(OTP_gen)
    email=os.environ.get('project_email')
    passkey=os.environ.get('project_email_password')
    msg_OTP_verify=MIMEText(str(OTP_gen))

    msg_OTP_verify['Subject']='OTP'
    msg_OTP_verify['From']=email
    msg_OTP_verify['To']=email_to_be_verified

    with smtplib.SMTP('smtp.gmail.com','587') as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email,passkey)
        smtp.sendmail(email,email_to_be_verified,msg_OTP_verify.as_string())

def email_verification():
    OTP_GENERATED=OTP_GENerated.get()
    if OTP_GENERATED==OTP_generated:
        After_verify_new_password_page()
    else:
        messagebox.showerror('OTP','Incorrect OTP')


def sending_the_mailFn():
    try:
        global reg_email_id_verification_variable_73746
        email_verification_send_mail(reg_email_id_verification_variable_73746)
        forgot_password_page()
    except:
        messagebox.showerror('error','invalid email id')

def forgot_password_page():
    email_for_email_verification_root.destroy()
    global OTP_GENERATED
    global forgot_password_root
    global OTP_GENerated
    forgot_password_root=Tk()
    forgot_password_root.title('email verification')
    forgot_password_root.state("zoomed")
    forgot_password_root.config(bg='black',)
    OTP_GENerated=StringVar()
    Label(forgot_password_root, text="Email Verification",width=100, font=("freestyle script", 70)).pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root, text="Enter the 'One Time Password' sent to your registered emailid", fg='white',bg='black',font=('verdana',20)).pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    
    otp_gen=Entry(forgot_password_root, textvariable=OTP_GENerated, font=("verdana", 20),width=30)
    otp_gen.pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Button(forgot_password_root, text="Verify OTP", width=14, height=1, font=("Helvetica 10 underline",15),cursor='hand2', command=email_verification).pack()
    Label(forgot_password_root,bg='black').pack()
    Label(forgot_password_root,bg='black').pack()
    Button(forgot_password_root, text="Cancel", width=14, height=1, font=("Helvetica 10 underline",15),cursor='hand2', command=login_screen_after_cancel_from_otp_verification_forget_password).pack()
    photo = PhotoImage(file = "e.png")
    forgot_password_root.iconphoto(False, photo)

def checking_whether_mail_in_database():
    global reg_email_id_verification_variable_73746
    global emailid_for_verification_12645
    reg_email_id_verification_variable_73746=emailid_for_verification_12645.get()
    query_for_email_verification='select emailid from logindata;'
    cursor_mysql.execute(query_for_email_verification)
    output_for_email_verification=cursor_mysql.fetchall()
    count_for_verify=0
    for email_for_verify in output_for_email_verification:
        if email_for_verify[0]==reg_email_id_verification_variable_73746:
            count_for_verify=1
            break
        else:
            continue
    if count_for_verify==1:
        sending_the_mailFn()
    else:
        messagebox.showerror('Email','Cant find registered email id')

def email_for_email_verification_page():
    global reg_email_id_verification_variable_73746
    global emailid_for_verification_12645
    global email_for_email_verification_root
    login_screen.destroy()
    email_for_email_verification_root=Tk()
    email_for_email_verification_root.title('Email Verification')
    email_for_email_verification_root.state('zoomed')
    email_for_email_verification_root.config(background = "black", pady=10)
    emailid_for_verification_12645=StringVar()
    Label(email_for_email_verification_root, text="Email Verification",width=100, font=("freestyle script", 70)).pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root, text="Enter your registered email-id:", fg='white',bg='black',font=('verdana',20)).pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    reg_emai_id_entry=Entry(email_for_email_verification_root, textvariable=emailid_for_verification_12645, font=("verdana", 20),width=30)
    reg_emai_id_entry.pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Button(email_for_email_verification_root, text="Verify Email", width=14, height=1, font=("Helvetica 10 underline",15),cursor='hand2', command=checking_whether_mail_in_database).pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Label(email_for_email_verification_root,bg='black').pack()
    Button(email_for_email_verification_root, text="Go Back", width=14, height=1, font=("Helvetica 10 underline",15),cursor='hand2', command=login_screen_after_cancel_from_emial_verification_forget_password).pack()
    photo = PhotoImage(file = "e.png")
    email_for_email_verification_root.iconphoto(False, photo)

def new_password_verification_through_python():
    global reg_email_id_verification_variable_73746
    global new_password_for_After_verify_new_password_page
    global confirm_password_for_After_verify_new_password_page
    ref_for_new_password_verification_through_python=0
    new_password_for_After_verify_new_password_page=new_password_for_After_verify_new_password_page_var.get()
    confirm_password_for_After_verify_new_password_page=confirm_password_for_After_verify_new_password_page_var.get()
    if len(new_password_for_After_verify_new_password_page)==0:
        messagebox.showerror('password error','please enter password')
        ref_for_new_password_verification_through_python=1
    elif len(confirm_password_for_After_verify_new_password_page)==0:
        messagebox.showerror('password error','please enter password')
        ref_for_new_password_verification_through_python=1
    elif new_password_for_After_verify_new_password_page!=confirm_password_for_After_verify_new_password_page:
        messagebox.showerror('password error','Password do not match')
        ref_for_new_password_verification_through_python=1
    elif len(new_password_for_After_verify_new_password_page)<8:
        messagebox.showerror('password error','password should be more than 8 characters')
        ref_for_new_password_verification_through_python=1
    elif len(new_password_for_After_verify_new_password_page)>35:
        messagebox.showerror('password error','password should be less than or equal to 35 characters')
        ref_for_new_password_verification_through_python=1
    elif True:
        upper=0
        lower=0
        special=0
        for element_pass_signup in new_password_for_After_verify_new_password_page:
            if element_pass_signup.isupper():
                upper+=1
            elif element_pass_signup.islower():
                lower+=1
            elif element_pass_signup in '!@#$%^&*+-_=~/':
                special+=1
            else:
                pass
        if (upper>0) and (lower>0) and (special>0):
            pass
        elif upper==0:
            messagebox.showerror('password error','password should have atleast 1 upper case character')
            ref_for_new_password_verification_through_python=1
        elif lower==0:
            messagebox.showerror('password error','password should have atleast 1 lower case character')
            ref_for_new_password_verification_through_python=1
        else:
            messagebox.showerror('password error',"password must have atleast 1 special character - '!@#$%^&*+-_=~/'")
            ref_for_new_password_verification_through_python=1

    if (('\'' in new_password_for_After_verify_new_password_page) or ('\"' in new_password_for_After_verify_new_password_page)) and ref_for_new_password_verification_through_python==0:
        messagebox.showinfo('error','There should be no \' or \" in any of the fields')
        ref_for_new_password_verification_through_python=2
    else:
        pass
    if ref_for_new_password_verification_through_python==0:
        query_for_new_password_verification_through_python="update logindata set password='{0}' where emailid='{1}';"
        cursor_mysql.execute(query_for_new_password_verification_through_python.format(new_password_for_After_verify_new_password_page,reg_email_id_verification_variable_73746))
        mycon.commit()
        messagebox.showinfo('password',"Password Succesfully Changed")
        login_screen_after_changing_password_forgot_password()
    else:
        pass


def After_verify_new_password_page():
    forgot_password_root.destroy()
    global After_verify_new_password_page_root
    global new_password_for_After_verify_new_password_page_var
    global confirm_password_for_After_verify_new_password_page_var
    After_verify_new_password_page_root=Tk()
    After_verify_new_password_page_root.title('hello')
    After_verify_new_password_page_root.state("zoomed")
    After_verify_new_password_page_root.config(background='black',pady=10)
    new_password_for_After_verify_new_password_page_var=StringVar()
    confirm_password_for_After_verify_new_password_page_var=StringVar()
    Label(After_verify_new_password_page_root, text="New Password",width=100, font=("freestyle script", 70)).pack()
    Label(After_verify_new_password_page_root,bg='black').pack()
    Label(After_verify_new_password_page_root,bg='black').pack()
    Label(After_verify_new_password_page_root,bg='black').pack()
    Label(After_verify_new_password_page_root,bg='black').pack()
    Label(After_verify_new_password_page_root,text='New password',font=('verdana',20),width=20,pady=5).place(x=450,y=300)
    Entry(After_verify_new_password_page_root,font=('verdana',25),textvariable=new_password_for_After_verify_new_password_page_var,show='*').place(x=950,y=300)
    Label(After_verify_new_password_page_root,text='Confirm Password',font=('verdana',20),width=20,pady=5).place(x=450,y=600)
    Entry(After_verify_new_password_page_root,font=('verdana',25),textvariable=confirm_password_for_After_verify_new_password_page_var,show='*').place(x=950,y=600)
    Button(After_verify_new_password_page_root,text='Submit',width=15,font=('verdana',15),cursor='hand2',command=new_password_verification_through_python).place(x=850,y=800)
    photo = PhotoImage(file = "e.png")
    After_verify_new_password_page_root.iconphoto(False, photo)


def login_success_and_creating_user_variables():
    global user_email_id
    global user_name
    global user_username 
    global user_gender
    global user_phone_no
    global user_country
    global user_account
    global user_first_name
    global user_last_name

    user_email_id=reg_email_id

    query='''select username,phoneno,firstname,lastname,gender,country,accountype from logindata where emailid="{0}";'''
    cursor_mysql.execute(query.format(user_email_id))
    output=cursor_mysql.fetchall()
    user_first_name=output[0][2]
    user_last_name=output[0][3]
    user_email_id=reg_email_id
    user_username=output[0][0]
    user_name=output[0][2]+' '+output[0][3]
    user_gender=output[0][4]
    user_country=output[0][5]
    user_account=output[0][6]
    if output[0][1]==None:
        user_phone_no=None
    else:
        user_phone_no=output[0][1]

    admin_or_student_page_chooser_fn()





def admin_or_student_page_chooser_fn():
    global user_account

    if user_account=='Student':
        librarymang_home_page_student()

    else:
        librarymang_home_page_admin()



def login_verification():
    global reg_email_id
    reg_email_id=reg_email_id_tk.get()
    reg_password=reg_password_tk.get()
    query_login="select emailid,password from logindata;"
    cursor_mysql.execute(query_login)
    out=cursor_mysql.fetchall()
    count=0
    for tup in out:
        if tup[0]==reg_email_id:   # note : count of each email id in a table is 1 because it is a primary key and google does not accept different email ids   so no needto check for duplicates.
            if tup[1]==reg_password:
                retvalue='success'
                bool_val=True
                break
                #break and go to next page

            else:
                retvalue='password incorrect'
                bool_val=False
                break
                #break and reload page by while loop in main program
        else:
            continue
    else:
        if count==0: #count=0 is a false condition because there is 3 cases i)emailfound,passkey correct then program brakes and goes to next page  ii)email found passcode incorrect terminates the loop (does not read the else of for-else) and refreshes page iii)email not found so count is 0 and unnaffected so it displays emailnot found and automatically comes out of the loop (using for-else) and when page is refreshed using while loop.
            retvalue='Registered email id not found'
            bool_val=False
    if reg_email_id=='':
        messagebox.showerror('email missing','please enter email id')
    elif reg_password=='':
        messagebox.showerror('password missing','please enter password')
    elif bool_val==True:
        login_success_and_creating_user_variables()
    else:
        if retvalue=='Registered email id not found':
            messagebox.showerror('email missing','Registered email id not found')
        else:
            messagebox.showerror('password','Password Incorrect')

def login_screen():
    clear_frame(main_page) # clears the mainpage
    global reg_email_id_tk
    global reg_password_tk
    global login_screen
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.state("zoomed")
    login_screen.config(background = "black", pady=10)
    reg_email_id_tk=StringVar()
    reg_password_tk=StringVar()
    Label(login_screen, text="Please enter login details:",width=50, font=("freestyle script", 100)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="Registered email-ID:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    emailid_login_entry = Entry(login_screen, textvariable=reg_email_id_tk,width=30,font=("verdana",15))
    emailid_login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="Password:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    password__login_entry = Entry(login_screen, textvariable=reg_password_tk, show= '*',width=30,font=("verdana",15))
    password__login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="Forgot password", width=14, height=1, font=("Helvetica 10 underline",15),bg='black',fg='white',bd=0,cursor='hand2',command=email_for_email_verification_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Button(login_screen, text='Create an Account',width=20,bg='black',fg='white',bd=0,cursor='hand2',font=('helvetica 8 underline' , 12),command=sign_up_from_login_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="submit", width=20,cursor='hand2', height=2,command=login_verification).pack()
    photo = PhotoImage(file = "e.png")
    login_screen.iconphoto(False, photo)


def login_screen_after_cancel_from_otp_verification_forget_password():
    forgot_password_root.destroy() # clears the mainpage
    global reg_email_id_tk
    global reg_password_tk
    global login_screen
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.state("zoomed")
    login_screen.config(background = "black", pady=10)
    reg_email_id_tk=StringVar()
    reg_password_tk=StringVar()
    Label(login_screen, text="Please enter login details:",width=50, font=("freestyle script", 100)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="Registered email-ID:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    emailid_login_entry = Entry(login_screen, textvariable=reg_email_id_tk,width=30,font=("verdana",15))
    emailid_login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="Password:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    password__login_entry = Entry(login_screen, textvariable=reg_password_tk, show= '*',width=30,font=("verdana",15))
    password__login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="Forgot password", width=14, height=1, font=("Helvetica 10 underline",15),bg='black',fg='white',bd=0,cursor='hand2',command=email_for_email_verification_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Button(login_screen, text='Create an Account',width=20,bg='black',fg='white',bd=0,cursor='hand2',font=('helvetica 8 underline' , 12),command=sign_up_from_login_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="submit", width=20,cursor='hand2', height=2,command=login_verification).pack()
    photo = PhotoImage(file = "e.png")
    login_screen.iconphoto(False, photo)




def login_screen_after_cancel_from_emial_verification_forget_password():
    email_for_email_verification_root.destroy() # clears the mainpage
    global reg_email_id_tk
    global reg_password_tk
    global login_screen
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.state("zoomed")
    login_screen.config(background = "black", pady=10)
    reg_email_id_tk=StringVar()
    reg_password_tk=StringVar()
    Label(login_screen, text="Please enter login details:",width=50, font=("freestyle script", 100)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="Registered email-ID:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    emailid_login_entry = Entry(login_screen, textvariable=reg_email_id_tk,width=30,font=("verdana",15))
    emailid_login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="Password:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    password__login_entry = Entry(login_screen, textvariable=reg_password_tk, show= '*',width=30,font=("verdana",15))
    password__login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="Forgot password", width=14, height=1, font=("Helvetica 10 underline",15),bg='black',fg='white',bd=0,cursor='hand2',command=email_for_email_verification_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Button(login_screen, text='Create an Account',width=20,bg='black',fg='white',bd=0,cursor='hand2',font=('helvetica 8 underline' , 12),command=sign_up_from_login_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="submit", width=20,cursor='hand2', height=2,command=login_verification).pack()
    photo = PhotoImage(file = "e.png")
    login_screen.iconphoto(False, photo)


def login_screen_from_student_profile():
    #lib.destroy() # clears the mainpage
    global reg_email_id_tk
    global reg_password_tk
    global login_screen
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.state("zoomed")
    login_screen.config(background = "black", pady=10)
    reg_email_id_tk=StringVar()
    reg_password_tk=StringVar()
    Label(login_screen, text="Please enter login details:",width=50, font=("freestyle script", 100)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="Registered email-ID:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    emailid_login_entry = Entry(login_screen, textvariable=reg_email_id_tk,width=30,font=("verdana",15))
    emailid_login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="Password:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    password__login_entry = Entry(login_screen, textvariable=reg_password_tk, show= '*',width=30,font=("verdana",15))
    password__login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="Forgot password", width=14, height=1, font=("Helvetica 10 underline",15),bg='black',fg='white',bd=0,cursor='hand2',command=email_for_email_verification_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Button(login_screen, text='Create an Account',width=20,bg='black',fg='white',bd=0,cursor='hand2',font=('helvetica 8 underline' , 12),command=sign_up_from_login_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="submit", width=20,cursor='hand2', height=2,command=login_verification).pack()
    photo = PhotoImage(file = "e.png")
    login_screen.iconphoto(False, photo)





def login_screen_after_changing_password_forgot_password():
    global After_verify_new_password_page_root
    global reg_email_id_tk
    global reg_password_tk
    global login_screen
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.state("zoomed")
    login_screen.config(background = "black", pady=10)
    reg_email_id_tk=StringVar()
    reg_password_tk=StringVar()
    Label(login_screen, text="Please enter login details:",width=50, font=("freestyle script", 100)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="Registered email-ID:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    emailid_login_entry = Entry(login_screen, textvariable=reg_email_id_tk,width=30,font=("verdana",15))
    emailid_login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="Password:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    password__login_entry = Entry(login_screen, textvariable=reg_password_tk, show= '*',width=30,font=("verdana",15))
    password__login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="Forgot password", width=14, height=1, font=("Helvetica 10 underline",15),bg='black',fg='white',bd=0,cursor='hand2',command=email_for_email_verification_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Button(login_screen, text='Create an Account',width=20,bg='black',fg='white',bd=0,cursor='hand2',font=('helvetica 8 underline' , 12),command=sign_up_from_login_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="submit", width=20,cursor='hand2', height=2,command=login_verification).pack()
    photo = PhotoImage(file = "e.png")
    login_screen.iconphoto(False, photo)






def login_screen_after_sign_up():
    #clear_frame(main_page) # clears the mainpage
    after_root_sign_up.destroy()
    global reg_email_id_tk
    global reg_password_tk
    global login_screen
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.state("zoomed")
    login_screen.config(background = "black", pady=10)
    reg_email_id_tk=StringVar()
    reg_password_tk=StringVar()
    Label(login_screen, text="Please enter login details:",width=50, font=("freestyle script", 100)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="Registered email-ID:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    emailid_login_entry = Entry(login_screen, textvariable=reg_email_id_tk,width=30,font=("verdana",15))
    emailid_login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="Password:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    password__login_entry = Entry(login_screen, textvariable=reg_password_tk, show= '*',width=30,font=("verdana",15))
    password__login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="Forgot password", width=14, height=1, font=("Helvetica 10 underline",15),bg='black',fg='white',bd=0,cursor='hand2',command=email_for_email_verification_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Button(login_screen, text='Create an Account',width=20,bg='black',fg='white',bd=0,cursor='hand2',font=('helvetica 8 underline' , 12),command=sign_up_from_login_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="submit", width=20,cursor='hand2', height=2,command=login_verification).pack()
    photo = PhotoImage(file = "e.png")
    login_screen.iconphoto(False, photo)

def login_screen_from_sign_up():
    #clear_frame(main_page) # clears the mainpage
    sign_up_page_root.destroy()
    global reg_email_id_tk
    global reg_password_tk
    global login_screen
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.state("zoomed")
    login_screen.config(background = "black", pady=10)
    reg_email_id_tk=StringVar()
    reg_password_tk=StringVar()
    Label(login_screen, text="Please enter login details:",width=50, font=("freestyle script", 100)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="Registered email-ID:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    emailid_login_entry = Entry(login_screen, textvariable=reg_email_id_tk,width=30,font=("verdana",15))
    emailid_login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="Password:",width=25, font=("lucida handwriting", 30)).pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    password__login_entry = Entry(login_screen, textvariable=reg_password_tk, show= '*',width=30,font=("verdana",15))
    password__login_entry.pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="Forgot password", width=14, height=1, font=("Helvetica 10 underline",15),bg='black',fg='white',bd=0,cursor='hand2',command=email_for_email_verification_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Label(login_screen, text="",bg = "black").pack()
    Button(login_screen, text='Create an Account',width=20,bg='black',fg='white',bd=0,cursor='hand2',font=('helvetica 8 underline' , 12),command=sign_up_from_login_page).pack()
    Label(login_screen, text="", bg = "black").pack()
    Label(login_screen, text="", bg = "black").pack()
    Button(login_screen, text="submit", width=20,cursor='hand2', height=2,command=login_verification).pack()
    photo = PhotoImage(file = "e.png")
    login_screen.iconphoto(False, photo)



def email_verification_send_mail_for_sign_up(email_to_be_verified):
    global OTP_generated_sign_up
    OTP_gen_sign_up=random.randint(100000,999999)
    OTP_generated_sign_up=str(OTP_gen_sign_up)
    email=os.environ.get('project_email')
    passkey=os.environ.get('project_email_password')
    msg_OTP_verify_for_signup=MIMEText(str(OTP_generated_sign_up))

    msg_OTP_verify_for_signup['Subject']='OTP'
    msg_OTP_verify_for_signup['From']=email
    msg_OTP_verify_for_signup['To']=email_to_be_verified

    with smtplib.SMTP('smtp.gmail.com','587') as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email,passkey)
        smtp.sendmail(email,email_to_be_verified,msg_OTP_verify_for_signup.as_string())
def After_verify_sign_up():
    global after_root_sign_up
    forgot_password_root_sign_up.destroy()
    after_root_sign_up=Tk()
    after_root_sign_up.title('hello')
    after_root_sign_up.state("zoomed")
    Label(after_root_sign_up, text="Register success",width=100, font=("freestyle script", 70)).pack()
    Label(after_root_sign_up).pack()
    Label(after_root_sign_up).pack()
    Label(after_root_sign_up).pack()
    Label(after_root_sign_up).pack()
    Label(after_root_sign_up).pack()
    Label(after_root_sign_up).pack()
    Label(after_root_sign_up).pack()
    Button(after_root_sign_up,text='Go to login Page',cursor='hand2',bg='black',font=('Comic Sans MS',20),fg='white',command=login_screen_after_sign_up).pack()
    photo = PhotoImage(file = "e.png")
    after_root_sign_up.iconphoto(False, photo)


def email_verification_sign_up():
    global first_name_sign_up
    global last_name_sign_up
    global username_sign_up
    global gender_sign_up
    global sign_up_country
    global email_id_sign_up
    global phone_no_sign_up
    global first_password_sign_up
    global confirm_password_sign_up
    global sign_up_account_type
    global real_account_type
    global real_gender
    OTP_GENERATED_sign_up=OTP_GENerated_sign_up.get()
    if OTP_GENERATED_sign_up==OTP_generated_sign_up:
        signup(email_id_sign_up,username_sign_up,first_password_sign_up,confirm_password_sign_up,first_name_sign_up,last_name_sign_up,real_gender,sign_up_country,real_account_type,phone_no_sign_up)
        After_verify_sign_up()
    else:
        messagebox.showerror('OTP','Incorrect OTP')

def midway_btw_forgot_password_page_for_sign_up_and_midfn():
    try:
        global email_id_sign_up
        email_verification_send_mail_for_sign_up(email_id_sign_up)
        forgot_password_page_for_sign_up()
    except:
        messagebox.showerror('email','invalid email id')


def forgot_password_page_for_sign_up():
    sign_up_page_root.destroy()
    global email_id_sign_up
    global OTP_GENERATED_sign_up
    global forgot_password_root_sign_up
    global OTP_GENerated_sign_up
    forgot_password_root_sign_up=Tk()
    forgot_password_root_sign_up.title('email verification')
    forgot_password_root_sign_up.state("zoomed")
    forgot_password_root_sign_up.config(bg='black',)
    OTP_GENerated_sign_up=StringVar()
    Label(forgot_password_root_sign_up, text="Email Verification",width=100, font=("freestyle script", 70)).pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up, text="Enter the 'One Time Password' sent to your registered emailid", fg='white',bg='black',font=('verdana',20)).pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    otp_gen=Entry(forgot_password_root_sign_up, textvariable=OTP_GENerated_sign_up, font=("verdana", 20),width=30)
    otp_gen.pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Button(forgot_password_root_sign_up, text="Verify OTP", width=14,cursor='hand2', height=1, font=("Helvetica 10 underline",15), command=email_verification_sign_up).pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Label(forgot_password_root_sign_up,bg='black').pack()
    Button(forgot_password_root_sign_up, text="Go Back", width=14,cursor='hand2', height=1, font=("Helvetica 10 underline",15), command=signup_page_from_email_verification_signup_fn).pack()
    photo = PhotoImage(file = "e.png")
    forgot_password_root_sign_up.iconphoto(False, photo)


def check_signup_info(reg_email_id_signup,username_signup,first_password_signup,confirm_password_signup,first_name_signup,last_name_signup,gender_sign_up,country_signup,account_type_signup,phone_signup_optional=0):
    
    query_signup_info="select username,emailid from logindata;"      #We are creating 2 lists of already eisting username and emails from logindata
    cursor_mysql.execute(query_signup_info)
    output1=cursor_mysql.fetchall()
    list_of_email_ids=[]
    list_of_usernames=[]
    for mail_username_tuple in output1:
        list_of_usernames.append(mail_username_tuple[0])
        list_of_email_ids.append(mail_username_tuple[1]) 
    ref_for_signup_verify=0   #ref is reference whether the sign up is true or false. In the end if ref is 0 then there is no problem with sign up. but if ref=1 there is a problem with email info. if ref is 2 at the end then there is a problem with username info. if ref=3 then problem with password info. if ref = 4 then problem with phone no.
    email_domain_list=reg_email_id_signup.split('@')  #for line 31
    if len(reg_email_id_signup)==0:
        ref_for_signup_verify=1
        messagebox.showerror('email missing','please enter email id')
    elif len(reg_email_id_signup)<6 and len(reg_email_id_signup)>=320:
        ref_for_signup_verify=1
        messagebox.showerror('email error','Invalid email id')#email length must be more than 6 char
    elif '@' not in reg_email_id_signup:   #email must have @
        messagebox.showerror('email error','Invalid email id')
        ref_for_signup_verify=1
    elif reg_email_id_signup.startswith('@'):     #cant start with @
        messagebox.showerror('email error','Invalid email id')
        ref_for_signup_verify_for_signup_verify=1
    elif not reg_email_id_signup.endswith('.com'):  # should end with .com
        messagebox.showerror('email error','Invalid email id')
        ref_for_signup_verify=1
    elif not reg_email_id_signup[0].isalnum():   #first char must be alphabet\numerical
        messagebox.showerror('email error','Invalid email id')
        ref_for_signup_verify=1
    elif reg_email_id_signup in list_of_email_ids:  # checking for duplicates of email
        messagebox.showinfo("email error", "Email already in use")
        ref_for_signup_verify=1
    elif True:
        alpha=0
        for z in range(len(email_domain_list)-1):    # after splitting the string into list the last element is the domain - gmail.com/outlook.com so dont consider that
            for email_element in email_domain_list[z]:
                if email_element.isalpha():    
                    alpha+=1
                else:
                    continue
        if alpha<1:
            messagebox.showerror('email error','Invalid email id')  #must have atleast 1 alphabet other than domain
            ref_for_signup_verify=1
        else:
            pass
    else:
        pass
    if ref_for_signup_verify==0:
        if username_signup=='' and ref_for_signup_verify==0:
            messagebox.showerror('username error','please enter username')
            ref_for_signup_verify=2
        elif len(username_signup)<6 and len(username_signup)>=20 and ref_for_signup_verify==0:
            messagebox.showerror('username error','username must be atleast 6 char and less than 21 charactes')
            ref_for_signup_verify=2
        elif username_signup[0].isdigit() and ref_for_signup_verify==0:
            messagebox.shoewrror('username error','username cant start with numbers')
            ref_for_signup_verify=2
        elif username_signup in list_of_usernames:   #checking for duplicates of username
            messagebox.showerror('username error','Username is taken')
            ref_for_signup_verify=2
        else:
            pass
    if ref_for_signup_verify==0:
        if len(first_password_signup)==0 and ref_for_signup_verify==0:
            messagebox.showerror('password error','please enter password')
            ref_for_signup_verify=3
        elif len(confirm_password_signup)==0 and ref_for_signup_verify==0:
            messagebox.showerror('password error','please enter password')
            ref_for_signup_verify=3
        elif first_password_signup!=confirm_password_signup and ref_for_signup_verify==0:
            messagebox.showerror('password error','Password do not match')
            ref_for_signup_verify=3
        elif len(first_password_signup)<8 and ref_for_signup_verify==0:
            messagebox.showerror('password error','password should be more than 8 characters')
            ref_for_signup_verify=3
        elif len(first_password_signup)>35 and ref_for_signup_verify==0:
            messagebox.showerror('password error','password should be less than or equal to 35 characters')
            ref_for_signup_verify=3
        elif ref_for_signup_verify==0:
            upper=0
            lower=0
            special=0
            for element_pass_signup in first_password_signup:
                if element_pass_signup.isupper():
                    upper+=1
                elif element_pass_signup.islower():
                    lower+=1
                elif element_pass_signup in '!@#$%^&*+-_=~/':
                    special+=1
                else:
                    pass
            if (upper>0) and (lower>0) and (special>0):
                pass
            elif upper==0:
                messagebox.showerror('password error','password should have atleast 1 upper case character')
                ref_for_signup_verify=3
            elif lower==0:
                messagebox.showerror('password error','password should have atleast 1 lower case character')
                ref_for_signup_verify=3
            else:
                messagebox.showerror('password error',"password must have atleast 1 special character - '!@#$%^&*+-_=~/'")
                ref_for_signup_verify=3
    if ref_for_signup_verify==0:
        if phone_signup_optional==0:
            pass
        elif not phone_signup_optional.isdigit():
            messagebox.showerror('phone no','invaid phone no')
            ref_for_signup_verify=4
        elif len(str(phone_signup_optional))!=10:
            messagebox.showerror('phone no','invaid phone no')
            ref_for_signup_verify=4
        else:
            pass
    else:
        pass
    if len(first_name_signup)==0 and ref_for_signup_verify==0:
        messagebox.showerror('error','please enter name')
        ref_for_signup_verify=5
    elif len(last_name_signup)==0 and ref_for_signup_verify==0:
        messagebox.showerror('error','please enter last name')
        ref_for_signup_verify=5
    elif len(first_name_signup)>20 and ref_for_signup_verify==0:
        messagebox.showerror('error','name should be less than 21 charcters')
        ref_for_signup_verify=5
    elif len(last_name_signup)>20 and ref_for_signup_verify==0:
        messagebox.showerror('error','last name should be less than 21 charcters')
        ref_for_signup_verify=5
    else:
        pass

    if gender_sign_up=='' and ref_for_signup_verify==0:
        messagebox.showerror('error','please enter your gender')
        ref_for_signup_verify=6
    else:
        pass
    if ref_for_signup_verify==0 and country_signup=='':
        messagebox.showerror('error','please enter country')
        ref_for_signup_verify=7
    elif ref_for_signup_verify==0 and (country_signup not in [ 'India' ,'US' , 'UK' ,'Australia' ,'Canada']):
        messagebox.showerror('error','cant verify your country')
        ref_for_signup_verify=7
    else:
        pass

    if ref_for_signup_verify==0 and account_type_signup=='':
        messagebox.showerror('error','please choose an account type')
        ref_for_signup_verify=8
    else: 
        pass

    if (('\'' in reg_email_id_signup) or ('\"' in reg_email_id_signup) or ('\'' in username_signup) or ('\"' in username_signup) or ('\'' in first_password_signup) or ('\"' in first_password_signup) or ('\'' in first_name_signup) or ('\"' in first_name_signup) or ('\'' in last_name_signup) or ('\"' in last_name_signup)) and  ref_for_signup_verify==0:
        messagebox.showinfo('error','Dnot use \' or \" in any field')
        ref_for_signup_verify=9
    if ref_for_signup_verify==0:
        midway_btw_forgot_password_page_for_sign_up_and_midfn()  # True and False returned is just for reference. In the main program define a global variable using 'global' and assign true and false to that. if the variable is true follow on with the sign up and then break out of while loop int new page but if false reload page using while loop.
    else:
        pass

def signup(reg_email_id_signup,username_signup,first_password_signup,confirm_password_signup,first_name_signup,last_name_signup,gender_sign_up,country_signup,account_type_signup,phone_signup_optional=0):
    global realphoneno
    global phone_no_sign_up
    
    
    if phone_signup_optional=='':

        #here email verification
        query_signup='''insert into logindata(username,emailid,password,firstname,lastname,gender,country,accountype) values("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}");'''
        cursor_mysql.execute(query_signup.format(username_signup,reg_email_id_signup,first_password_signup,first_name_signup,last_name_signup,gender_sign_up,country_signup,account_type_signup))
        mycon.commit()
        username=username_signup
        query_signup_2='''insert into loginissue(username) values("{0}");'''
        cursor_mysql.execute(query_signup_2.format(username))
        mycon.commit()
    else:
        #here email verification
        realphoneno=int(phone_signup_optional)
        query_signup='''insert into logindata(username,emailid,phoneno,password,firstname,lastname,gender,country,accountype) values("{0}","{1}",{2},"{3}","{4}","{5}","{6}","{7}","{8}");'''
        cursor_mysql.execute(query_signup.format(username_signup,reg_email_id_signup,realphoneno,first_password_signup,first_name_signup,last_name_signup,gender_sign_up,country_signup,account_type_signup,))
        mycon.commit()
        username=username_signup
        query_signup_2='''insert into loginissue(username) values("{0}");'''
        cursor_mysql.execute(query_signup_2.format(username))
        mycon.commit()

def midfn():
    global first_name_sign_up_var
    global last_name_sign_up_var
    global username_sign_up_var
    global gender_sign_up_var
    global sign_up_country_var
    global phone_no_sign_up_var
    global email_id_sign_up_var
    global first_password_sign_up_var
    global confirm_password_sign_up_var
    global sign_up_account_type_var
    
    global first_name_sign_up
    global last_name_sign_up
    global username_sign_up
    global gender_sign_up
    global sign_up_country
    global phone_no_sign_up
    global email_id_sign_up
    global first_password_sign_up
    global confirm_password_sign_up
    global sign_up_account_type
    global realphoneno
    global real_gender
    global real_account_type

    first_name_sign_up=first_name_sign_up_var.get()
    last_name_sign_up=last_name_sign_up_var.get()
    username_sign_up=username_sign_up_var.get()
    gender_sign_up=gender_sign_up_var.get()
    sign_up_country=sign_up_country_var.get()
    phone_no_sign_up=phone_no_sign_up_var.get()
    email_id_sign_up=email_id_sign_up_var.get()
    first_password_sign_up=first_password_sign_up_var.get()
    confirm_password_sign_up=confirm_password_sign_up_var.get()
    sign_up_account_type=sign_up_account_type_var.get()
    if gender_sign_up==1:
        real_gender='male'
    elif gender_sign_up==2:
        real_gender='female'
    else:
        real_gender=''
    if sign_up_account_type==1:
        real_account_type='Administrator'
    elif sign_up_account_type==2:
        real_account_type='Student'
    else:
        real_account_type=''
    if phone_no_sign_up=='':
        realphoneno=0
        check_signup_info(email_id_sign_up,username_sign_up,first_password_sign_up,confirm_password_sign_up,first_name_sign_up,last_name_sign_up,real_gender,sign_up_country,real_account_type)
    else:
        realphoneno=None
        check_signup_info(email_id_sign_up,username_sign_up,first_password_sign_up,confirm_password_sign_up,first_name_sign_up,last_name_sign_up,real_gender,sign_up_country,real_account_type,phone_no_sign_up)



def signup_page_fn():
    main_page.destroy()
    global first_name_sign_up_var
    global last_name_sign_up_var
    global username_sign_up_var
    global gender_sign_up_var
    global sign_up_country_var
    global phone_no_sign_up_var
    global email_id_sign_up_var
    global first_password_sign_up_var
    global confirm_password_sign_up_var
    global sign_up_account_type_var
    global sign_up_page_root

    sign_up_page_root = Tk()
    sign_up_page_root.state('zoomed')
    sign_up_page_root.title('Registration form')
    sign_up_page_root.config(background = "black", pady=10)

    first_name_sign_up_var=StringVar()
    last_name_sign_up_var=StringVar()
    username_sign_up_var=StringVar()
    phone_no_sign_up_var=StringVar()
    email_id_sign_up_var=StringVar()
    first_password_sign_up_var=StringVar()
    confirm_password_sign_up_var=StringVar()
    sign_up_account_type_var=IntVar()
    sign_up_country_var=StringVar()
    gender_sign_up_var=IntVar()


    sign_up_label_0 =Label(sign_up_page_root, text="Registeration Form",width=100, font=("freestyle script", 70)).pack()

    sign_up_label_1 =Label(sign_up_page_root,text="first name:", width=17,font=("lucida handwriting",13))
    sign_up_label_1.place(x=670,y=250)

    sign_up_entry_1=Entry(sign_up_page_root,textvariable=first_name_sign_up_var,font=('verdana',15))
    sign_up_entry_1.place(x=950,y=250)

    sign_up_label_3 =Label(sign_up_page_root,text="Last name", width=17,font=("lucida handwriting",13))
    sign_up_label_3.place(x=670,y=300)

    sign_up_entry_3=Entry(sign_up_page_root,textvariable=last_name_sign_up_var,font=('verdana',15))
    sign_up_entry_3.place(x=950,y=300)

    sign_up_label_11 =Label(sign_up_page_root,text="Username", width=17,font=("lucida handwriting",13))
    sign_up_label_11.place(x=670,y=350)

    sign_up_entry_11=Entry(sign_up_page_root,textvariable=username_sign_up_var,font=('verdana',15))
    sign_up_entry_11.place(x=950,y=350)

    sign_up_label_4 =Label(sign_up_page_root,text="Gender", width=17,font=("lucida handwriting",13))
    sign_up_label_4.place(x=670,y=400)

    Radiobutton(sign_up_page_root,text="Male",padx= 20, variable= gender_sign_up_var, value=1,font=('verdana',13)).place(x=950,y=400)
    Radiobutton(sign_up_page_root,text="Female",padx= 20, variable=gender_sign_up_var, value=2,font=('verdana',13)).place(x=1055,y=400)

    sign_up_label_5=Label(sign_up_page_root,text="Country",width=17,font=("lucida handwriting",13))
    sign_up_label_5.place(x=670,y=450)

    sign_up_list_of_country=[ 'India' ,'US' , 'UK' ,'Australia' ,'Canada']

    sign_up_droplist=OptionMenu(sign_up_page_root, sign_up_country_var, *sign_up_list_of_country)
    sign_up_droplist.config(width=20)
    sign_up_country_var.set('Select your Country')
    sign_up_droplist.place(x=950,y=450)

    sign_up_label_6=Label(sign_up_page_root,text="Phone no:(optional)",width=17,font=("lucida handwriting",13))
    sign_up_label_6.place(x=670,y=500)

    sign_up_entry_6=Entry(sign_up_page_root,textvariable=phone_no_sign_up_var,font=('verdana',15))
    sign_up_entry_6.place(x=950,y=500)

    sign_up_label_7=Label(sign_up_page_root,text="Email-ID:",width=17,font=("lucida handwriting",13))
    sign_up_label_7.place(x=670,y=550)

    sign_up_entry_7=Entry(sign_up_page_root,textvariable=email_id_sign_up_var,font=('verdana',15),width=30)
    sign_up_entry_7.place(x=950,y=550)

    sign_up_label_8=Label(sign_up_page_root,text="Password:",width=17,font=("lucida handwriting",13))
    sign_up_label_8.place(x=670,y=600)

    sign_up_entry_8=Entry(sign_up_page_root,textvariable=first_password_sign_up_var,font=('verdana',15),show='*')
    sign_up_entry_8.place(x=950,y=600)

    sign_up_label_9=Label(sign_up_page_root,text="Confirm password:",width=17,font=("lucida handwriting",13))
    sign_up_label_9.place(x=670,y=650)

    sign_up_entry_9=Entry(sign_up_page_root,textvariable=confirm_password_sign_up_var,font=('verdana',15),show='*')
    sign_up_entry_9.place(x=950,y=650)

    sign_up_label_10=Label(sign_up_page_root,text="Account type:",width=17,font=("lucida handwriting",13))
    sign_up_label_10.place(x=670,y=700)


    Radiobutton(sign_up_page_root,text="administrator",padx= 10,variable= sign_up_account_type_var, value=1,font=('verdana',14)).place(x=950,y=700)
    Radiobutton(sign_up_page_root,text="student",padx= 10, variable= sign_up_account_type_var, value=2,font=('verdana',14)).place(x=1125,y=700)

    Button(sign_up_page_root, text='Already have an account',width=20,cursor='hand2',bg='black',fg='white',bd=0,font=('helvetica 8 underline' , 12),command=login_screen_from_sign_up).place(x=820,y=800)
    Button(sign_up_page_root, text='Submit' , width=10,bg="white",cursor='hand2',fg='black',font=('Comic Sans MS',15),command=midfn).place(x=850 ,y=860)
    photo = PhotoImage(file = "e.png")
    sign_up_page_root.iconphoto(False, photo)



def signup_page_from_email_verification_signup_fn():
    forgot_password_root_sign_up.destroy()
    global first_name_sign_up_var
    global last_name_sign_up_var
    global username_sign_up_var
    global gender_sign_up_var
    global sign_up_country_var
    global phone_no_sign_up_var
    global email_id_sign_up_var
    global first_password_sign_up_var
    global confirm_password_sign_up_var
    global sign_up_account_type_var
    global sign_up_page_root

    sign_up_page_root = Tk()
    sign_up_page_root.state('zoomed')
    sign_up_page_root.title('Registration form')
    sign_up_page_root.config(background = "black", pady=10)

    first_name_sign_up_var=StringVar()
    last_name_sign_up_var=StringVar()
    username_sign_up_var=StringVar()
    phone_no_sign_up_var=StringVar()
    email_id_sign_up_var=StringVar()
    first_password_sign_up_var=StringVar()
    confirm_password_sign_up_var=StringVar()
    sign_up_account_type_var=IntVar()
    sign_up_country_var=StringVar()
    gender_sign_up_var=IntVar()


    sign_up_label_0 =Label(sign_up_page_root, text="Registeration Form",width=100, font=("freestyle script", 70)).pack()

    sign_up_label_1 =Label(sign_up_page_root,text="first name:", width=17,font=("lucida handwriting",13))
    sign_up_label_1.place(x=670,y=250)

    sign_up_entry_1=Entry(sign_up_page_root,textvariable=first_name_sign_up_var,font=('verdana',15))
    sign_up_entry_1.place(x=950,y=250)

    sign_up_label_3 =Label(sign_up_page_root,text="Last name", width=17,font=("lucida handwriting",13))
    sign_up_label_3.place(x=670,y=300)

    sign_up_entry_3=Entry(sign_up_page_root,textvariable=last_name_sign_up_var,font=('verdana',15))
    sign_up_entry_3.place(x=950,y=300)

    sign_up_label_11 =Label(sign_up_page_root,text="Username", width=17,font=("lucida handwriting",13))
    sign_up_label_11.place(x=670,y=350)

    sign_up_entry_11=Entry(sign_up_page_root,textvariable=username_sign_up_var,font=('verdana',15))
    sign_up_entry_11.place(x=950,y=350)

    sign_up_label_4 =Label(sign_up_page_root,text="Gender", width=17,font=("lucida handwriting",13))
    sign_up_label_4.place(x=670,y=400)

    Radiobutton(sign_up_page_root,text="Male",padx= 20, variable= gender_sign_up_var, value=1,font=('verdana',13)).place(x=950,y=400)
    Radiobutton(sign_up_page_root,text="Female",padx= 20, variable=gender_sign_up_var, value=2,font=('verdana',13)).place(x=1055,y=400)

    sign_up_label_5=Label(sign_up_page_root,text="Country",width=17,font=("lucida handwriting",13))
    sign_up_label_5.place(x=670,y=450)

    sign_up_list_of_country=[ 'India' ,'US' , 'UK' ,'Australia' ,'Canada']

    sign_up_droplist=OptionMenu(sign_up_page_root, sign_up_country_var, *sign_up_list_of_country)
    sign_up_droplist.config(width=20)
    sign_up_country_var.set('Select your Country')
    sign_up_droplist.place(x=950,y=450)

    sign_up_label_6=Label(sign_up_page_root,text="Phone no:(optional)",width=17,font=("lucida handwriting",13))
    sign_up_label_6.place(x=670,y=500)

    sign_up_entry_6=Entry(sign_up_page_root,textvariable=phone_no_sign_up_var,font=('verdana',15))
    sign_up_entry_6.place(x=950,y=500)

    sign_up_label_7=Label(sign_up_page_root,text="Email-ID:",width=17,font=("lucida handwriting",13))
    sign_up_label_7.place(x=670,y=550)

    sign_up_entry_7=Entry(sign_up_page_root,textvariable=email_id_sign_up_var,font=('verdana',15),width=30)
    sign_up_entry_7.place(x=950,y=550)

    sign_up_label_8=Label(sign_up_page_root,text="Password:",width=17,font=("lucida handwriting",13))
    sign_up_label_8.place(x=670,y=600)

    sign_up_entry_8=Entry(sign_up_page_root,textvariable=first_password_sign_up_var,font=('verdana',15),show='*')
    sign_up_entry_8.place(x=950,y=600)

    sign_up_label_9=Label(sign_up_page_root,text="Confirm password:",width=17,font=("lucida handwriting",13))
    sign_up_label_9.place(x=670,y=650)

    sign_up_entry_9=Entry(sign_up_page_root,textvariable=confirm_password_sign_up_var,font=('verdana',15),show='*')
    sign_up_entry_9.place(x=950,y=650)

    sign_up_label_10=Label(sign_up_page_root,text="Account type:",width=17,font=("lucida handwriting",13))
    sign_up_label_10.place(x=670,y=700)


    Radiobutton(sign_up_page_root,text="administrator",padx= 10,variable= sign_up_account_type_var, value=1,font=('verdana',14)).place(x=950,y=700)
    Radiobutton(sign_up_page_root,text="student",padx= 10, variable= sign_up_account_type_var, value=2,font=('verdana',14)).place(x=1125,y=700)

    Button(sign_up_page_root, text='Already have an account',width=20,cursor='hand2',bg='black',fg='white',bd=0,font=('helvetica 8 underline' , 12),command=login_screen_from_sign_up).place(x=820,y=800)
    Button(sign_up_page_root, text='Submit' , width=10,bg="white",cursor='hand2',fg='black',font=('Comic Sans MS',15),command=midfn).place(x=850 ,y=860)
    photo = PhotoImage(file = "e.png")
    sign_up_page_root.iconphoto(False, photo)




def sign_up_from_login_page():
    login_screen.destroy()
    global first_name_sign_up_var
    global last_name_sign_up_var
    global username_sign_up_var
    global gender_sign_up_var
    global sign_up_country_var
    global phone_no_sign_up_var
    global email_id_sign_up_var
    global first_password_sign_up_var
    global confirm_password_sign_up_var
    global sign_up_account_type_var
    global sign_up_page_root

    sign_up_page_root = Tk()
    sign_up_page_root.state('zoomed')
    sign_up_page_root.title('Registration form')
    sign_up_page_root.config(background = "black", pady=10)

    first_name_sign_up_var=StringVar()
    last_name_sign_up_var=StringVar()
    username_sign_up_var=StringVar()
    phone_no_sign_up_var=StringVar()
    email_id_sign_up_var=StringVar()
    first_password_sign_up_var=StringVar()
    confirm_password_sign_up_var=StringVar()
    sign_up_account_type_var=IntVar()
    sign_up_country_var=StringVar()
    gender_sign_up_var=IntVar()


    sign_up_label_0 =Label(sign_up_page_root, text="Registeration Form",width=100, font=("freestyle script", 70)).pack()

    sign_up_label_1 =Label(sign_up_page_root,text="first name:", width=17,font=("lucida handwriting",13))
    sign_up_label_1.place(x=670,y=250)

    sign_up_entry_1=Entry(sign_up_page_root,textvariable=first_name_sign_up_var,font=('verdana',15))
    sign_up_entry_1.place(x=950,y=250)

    sign_up_label_3 =Label(sign_up_page_root,text="Last name", width=17,font=("lucida handwriting",13))
    sign_up_label_3.place(x=670,y=300)

    sign_up_entry_3=Entry(sign_up_page_root,textvariable=last_name_sign_up_var,font=('verdana',15))
    sign_up_entry_3.place(x=950,y=300)

    sign_up_label_11 =Label(sign_up_page_root,text="Username", width=17,font=("lucida handwriting",13))
    sign_up_label_11.place(x=670,y=350)

    sign_up_entry_11=Entry(sign_up_page_root,textvariable=username_sign_up_var,font=('verdana',15))
    sign_up_entry_11.place(x=950,y=350)

    sign_up_label_4 =Label(sign_up_page_root,text="Gender", width=17,font=("lucida handwriting",13))
    sign_up_label_4.place(x=670,y=400)

    Radiobutton(sign_up_page_root,text="Male",padx= 20, variable= gender_sign_up_var, value=1,font=('verdana',13)).place(x=950,y=400)
    Radiobutton(sign_up_page_root,text="Female",padx= 20, variable=gender_sign_up_var, value=2,font=('verdana',13)).place(x=1055,y=400)

    sign_up_label_5=Label(sign_up_page_root,text="Country",width=17,font=("lucida handwriting",13))
    sign_up_label_5.place(x=670,y=450)

    sign_up_list_of_country=[ 'India' ,'US' , 'UK' ,'Australia' ,'Canada']

    sign_up_droplist=OptionMenu(sign_up_page_root, sign_up_country_var, *sign_up_list_of_country)
    sign_up_droplist.config(width=20)
    sign_up_country_var.set('Select your Country')
    sign_up_droplist.place(x=950,y=450)

    sign_up_label_6=Label(sign_up_page_root,text="Phone no:(optional)",width=17,font=("lucida handwriting",13))
    sign_up_label_6.place(x=670,y=500)

    sign_up_entry_6=Entry(sign_up_page_root,textvariable=phone_no_sign_up_var,font=('verdana',15))
    sign_up_entry_6.place(x=950,y=500)

    sign_up_label_7=Label(sign_up_page_root,text="Email-ID:",width=17,font=("lucida handwriting",13))
    sign_up_label_7.place(x=670,y=550)

    sign_up_entry_7=Entry(sign_up_page_root,textvariable=email_id_sign_up_var,font=('verdana',15),width=30)
    sign_up_entry_7.place(x=950,y=550)

    sign_up_label_8=Label(sign_up_page_root,text="Password:",width=17,font=("lucida handwriting",13))
    sign_up_label_8.place(x=670,y=600)

    sign_up_entry_8=Entry(sign_up_page_root,textvariable=first_password_sign_up_var,font=('verdana',15),show='*')
    sign_up_entry_8.place(x=950,y=600)

    sign_up_label_9=Label(sign_up_page_root,text="Confirm password:",width=17,font=("lucida handwriting",13))
    sign_up_label_9.place(x=670,y=650)

    sign_up_entry_9=Entry(sign_up_page_root,textvariable=confirm_password_sign_up_var,font=('verdana',15),show='*')
    sign_up_entry_9.place(x=950,y=650)

    sign_up_label_10=Label(sign_up_page_root,text="Account type:",width=17,font=("lucida handwriting",13))
    sign_up_label_10.place(x=670,y=700)


    Radiobutton(sign_up_page_root,text="administrator",padx= 10,variable= sign_up_account_type_var, value=1,font=('verdana',14)).place(x=950,y=700)
    Radiobutton(sign_up_page_root,text="student",padx= 10, variable= sign_up_account_type_var, value=2,font=('verdana',14)).place(x=1125,y=700)

    Button(sign_up_page_root, text='Already have an account',width=20,cursor='hand2',bg='black',fg='white',bd=0,font=('helvetica 8 underline' , 12),command=login_screen_from_sign_up).place(x=820,y=800)
    Button(sign_up_page_root, text='Submit' , width=10,bg="white",cursor='hand2',fg='black',font=('Comic Sans MS',15),command=midfn).place(x=850 ,y=860)
    photo = PhotoImage(file = "e.png")
    sign_up_page_root.iconphoto(False, photo)




#Function definitins******************************************************************************************

 #***********************************************************Main Page********************************************   



main_page=Tk()
main_page.title("Home")
main_page.state("zoomed")
main_page.config(background = "black", pady=10)
Label(main_page, text="Library Management",width=50, font=("freestyle script", 100)).pack()
Label(main_page, text="",bg = "black").pack()
button_login=Button(main_page, text="Login", width=10,height=4,cursor='hand2', font=("Helvetica 10 underline",50),bg='red',command=login_screen)
button_login.pack()
Label(main_page, text="",bg = "black").pack()
button_signup=Button(main_page, text="Sign-Up", width=10, height=4,cursor='hand2', font=("Helvetica 10 underline",50),bg='red',command=signup_page_fn)
button_signup.pack()
Label(main_page, text="",bg = "black").pack()
photo = PhotoImage(file = "e.png")
main_page.iconphoto(False, photo)
main_page.mainloop()

#***************************************************Main Page******************************************************
