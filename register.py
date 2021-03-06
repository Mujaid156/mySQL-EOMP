from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk

register = tk.Tk()
register.title("Life Choices Online")
register.geometry("800x600")
register.config(bg="skyblue")

name = StringVar()
sur = StringVar()
id = StringVar()
cell = StringVar()
kin_n = StringVar()
kin_cell = StringVar()
word = StringVar()

mydb = mysql.connector.connect(host="localhost",user="lifechoices",password="@Lifechoices1234", auth_plugin='mysql_native_password',database="lifechoices")
def into_database():
    x = name.get()
    y = sur.get()
    z = id.get()
    m = cell.get()
    c = kin_n.get()
    d = kin_cell.get()
    if x == '' or y == '' or z == '' or m == '' or c == '' or d == '':
        messagebox.showinfo("Invalid Entry", "Please fillin all required feilds")
    else:
        cursor = mydb.cursor()
        cursor.excute('INSERT INTO Students (Name, Surname, ID_number, Cellnumber, Kin_name, Kin_number) VALUES (%s, %s, %s, %s, %s, $s)',
                        (x, y, z, m, c, d))
        mydb.commit()
        cursor.insert('', 'end', text="", values=(x, y, z, m, c, d))
        messagebox.showinfo("Well done", "Success")


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
names = Label(register, text="Name", bg="skyblue")
surname = Label(register, text="Surname", bg="skyblue")
id_num = Label(register, text="ID Number", bg="skyblue")
phone = Label(register, text="Phone Number", bg="skyblue")
kin = Label(register, text="Emergency Contact", font="Arial 20 italic", bg="skyblue")
kin_name = Label(register, text="Name", bg="skyblue")
kin_phone = Label(register, text="Phone Number", bg="skyblue")
passw = Label(register, text="Password", bg="skyblue")

# Creating Entries
name_input = Entry(register, textvariable=name)
surname_input = Entry(register, textvariable=sur)
id_input = Entry(register, textvariable=id)
phone_input = Entry(register, textvariable=cell)
kin_name_input = Entry(register, textvariable=kin_n)
kin_phone_input = Entry(register, textvariable=kin_cell)
passw_input = Entry(register, textvariable=word, show="*")

# Creating Buttons
clear = Button(register, text="Clear", command=clear)
exit = Button(register, text="Return to main page", command=exit_program)
login = Button(register, text="Create User", command=into_database)

# Placing Buttons
clear.place(x=200, y=500)
exit.place(x=450, y=500)
login.place(x=300, y=500)

# Placing Entries
name_input.place(x=200, y=200)
surname_input.place(x=200, y=250)
id_input.place(x=200, y=300)
phone_input.place(x=200, y=350)
kin_name_input.place(x=550, y=200)
kin_phone_input.place(x=550, y=250)
passw_input.place(x=200, y=400)

# Placing Labels
visit.place(x=340, y=30)
user.place(x=150, y=130)
names.place(x=50, y=200)
surname.place(x=50, y=250)
id_num.place(x=50, y=300)
phone.place(x=50, y=350)
passw.place(x=50, y=400)
kin.place(x=470, y=130)
kin_name.place(x=420, y=200)
kin_phone.place(x=420, y=250)

register.mainloop()
