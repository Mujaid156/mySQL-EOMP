from tkinter import *

register = Tk()
register.title("Life Choices Online")
register.geometry("800x500")
register.config(bg="skyblue")

def clear():
    name_input.delete(0, END)
    surname_input.delete(0, END)
    id_input.delete(0, END)
    phone_input.delete(0, END)
    kin_name_input.delete(0, END)
    kin_phone_input.delete(0, END)

def exit_program():
    register.destroy()
    import main

# Creating Labels
visit = Label(register, text="Register", font="Arial 30 italic", bg="skyblue")
user = Label(register, text="User Details", font="Arial 20 italic", bg="skyblue")
name = Label(register, text="Name", bg="skyblue")
surname = Label(register, text="Surname", bg="skyblue")
id = Label(register, text="ID Number", bg="skyblue")
phone = Label(register, text="Phone Number", bg="skyblue")
kin = Label(register, text="Emergency Contact", font="Arial 20 italic", bg="skyblue")
kin_name = Label(register, text="Name", bg="skyblue")
kin_phone = Label(register, text="Phone Number", bg="skyblue")

# Creating Entries
name_input = Entry(register)
surname_input = Entry(register)
id_input = Entry(register)
phone_input = Entry(register)
kin_name_input = Entry(register)
kin_phone_input = Entry(register)

# Creating Buttons
clear = Button(register, text="Clear", command=clear)
exit = Button(register, text="Return to main page", command=exit_program)
login = Button(register, text="Create User")

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
kin_name.place(x=420, y=200)
kin_phone.place(x=420, y=250)

register.mainloop()
