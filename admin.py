from tkinter import *
from tkinter import messagebox

admin_login = Tk()
admin_login.title("Life Choices Online")
admin_login.geometry("500x500")
admin_login.config(bg="skyblue")

def login():
    if user_input.get() == '' or passw_input.get() == '':
        messagebox.showerror("Invalid Entry", "Please fill in required fields")

def new():
    admin_login.destroy()
    import visitor

def clear():
    user_input.delete(0, END)
    passw_input.delete(0, END)

def exit():
    admin_login.destroy()
    import main

# Creating Labels
head1 = Label(admin_login, text="Login", font="Arial 25 italic", bg="skyblue")
user = Label(admin_login, text="Enter Username: ", font="Arial 15 bold", bg="skyblue")
passw = Label(admin_login, text="Enter Password: ", font="Arial 15 bold", bg="skyblue")

# Creating Entries
user_input = Entry(admin_login)
passw_input = Entry(admin_login, show="*")

# Creating Buttons
login = Button(admin_login, text="Login", width=10, borderwidth=10, command=login)
register = Button(admin_login, text="Register as a new user", command=new)
clear = Button(admin_login, text="Clear", command=clear)
back = Button(admin_login, text="Return to main page", command=exit)

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

admin_login.mainloop()
