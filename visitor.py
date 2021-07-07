from tkinter import *
from tkinter import messagebox

visitor_login = Tk()
visitor_login.title("Life Choices Online")
visitor_login.geometry("500x500")
visitor_login.config(bg="skyblue")

def login():
    if user_input.get() == '' or passw_input.get() == '':
        messagebox.showerror("Invalid Entry", "Please fill in required fields")

def new():
    visitor_login.destroy()
    import register

def clear():
    user_input.delete(0, END)
    passw_input.delete(0, END)

def exit():
    visitor_login.destroy()
    import main

# Creating Labels
head1 = Label(visitor_login, text="Login", font="Arial 25 italic", bg="skyblue")
user = Label(visitor_login, text="Enter Username: ", font="Arial 15 bold", bg="skyblue")
passw = Label(visitor_login, text="Enter Password: ", font="Arial 15 bold", bg="skyblue")

# Creating Entries
user_input = Entry(visitor_login)
passw_input = Entry(visitor_login, show="*")

# Creating Buttons
login = Button(visitor_login, text="Login", width=10, borderwidth=10, command=login)
register = Button(visitor_login, text="Register as a new user", command=new)
clear = Button(visitor_login, text="Clear", command=clear)
back = Button(visitor_login, text="Return to main page", command=exit)

# Placing Buttons
login.place(x=190, y=300)
register.place(x=30, y=400)
clear.place(x=340, y=250)
back.place(x=320, y=400)

# Placing Entries
user_input.place(x=280, y=130)
passw_input.place(x=280, y=180)

# Placing Labels
head1.place(x=200, y=50)
user.place(x=60, y=130)
passw.place(x=60, y=180)

visitor_login.mainloop()
