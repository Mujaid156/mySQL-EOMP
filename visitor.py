from tkinter import *

visitor_login = Tk()
visitor_login.title("Life Choices Online")
visitor_login.geometry("800x500")
visitor_login.config(bg="skyblue")

def clear():
    name_input.delete(0, END)
    surname_input.delete(0, END)
    id_input.delete(0, END)
    phone_input.delete(0, END)
    kin_name_input.delete(0, END)
    kin_phone_input.delete(0, END)

def exit_program():
    visitor_login.destroy()
    import main

# Creating Labels
visit = Label(visitor_login, text="Register", font="Arial 30 italic", bg="skyblue")
user = Label(visitor_login, text="User Details", font="Arial 20 italic", bg="skyblue")
name = Label(visitor_login, text="Enter Name", bg="skyblue")
surname = Label(visitor_login, text="Enter Surname", bg="skyblue")
id = Label(visitor_login, text="Enter ID Number", bg="skyblue")
phone = Label(visitor_login, text="Enter Phone Number", bg="skyblue")
kin = Label(visitor_login, text="Emergency Contact", font="Arial 20 italic", bg="skyblue")
kin_name = Label(visitor_login, text="Enter Name", bg="skyblue")
kin_phone = Label(visitor_login, text="Enter Phone Number", bg="skyblue")

# Creating Entries
name_input = Entry(visitor_login)
surname_input = Entry(visitor_login)
id_input = Entry(visitor_login)
phone_input = Entry(visitor_login)
kin_name_input = Entry(visitor_login)
kin_phone_input = Entry(visitor_login)

# Creating Buttons
clear = Button(visitor_login, text="Clear", command=clear)
exit = Button(visitor_login, text="Return to main page", command=exit_program)
login = Button(visitor_login, text="Create User")

# Placing Buttons
clear.place(x=200, y=400)
exit.place(x=450, y=400)

# Placing Entries
name_input.place(x=200, y=200)
surname_input.place(x=200, y=250)
id_input.place(x=200, y=300)
phone_input.place(x=200, y=350)
kin_name_input.place(x=550, y=200)
kin_phone_input.place(x=550, y=250)

# Placing Labels
visit.place(x=340, y=30)
user.place(x=150, y=130)
name.place(x=50, y=200)
surname.place(x=50, y=250)
id.place(x=50, y=300)
phone.place(x=50, y=350)
kin.place(x=470, y=130)
kin_name.place(x=400, y=200)
kin_phone.place(x=400, y=250)

visitor_login.mainloop()
