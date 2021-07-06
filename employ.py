from tkinter import *

employee_login = Tk()
employee_login.title("Life Choices Online")
employee_login.geometry("500x500")
employee_login.config(bg="skyblue")

def clear():
    user_input.delete(0, END)
    passw_input.delete(0, END)

def exit():
    employee_login.destroy()
    import main

# Creating Labels
head1 = Label(employee_login, text="Login", font="Arial 25 italic")
user = Label(employee_login, text="Enter Username: ", font="Arial 15 bold")
passw = Label(employee_login, text="Enter Password: ", font="Arial 15 bold")

# Creating Entries
user_input = Entry(employee_login)
passw_input = Entry(employee_login, show="*")

# Creating Buttons
login = Button(employee_login, text="Login", width=10, borderwidth=10)
register = Button(employee_login, text="Register as a new user")
clear = Button(employee_login, text="Clear", command=clear)
back = Button(employee_login, text="Return to main page", command=exit)

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

employee_login.mainloop()
