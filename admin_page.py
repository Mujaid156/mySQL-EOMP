from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

control = tk.Tk()
control.title("Admin Page")
control.geometry("1200x500")

connect = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='lifechoices', auth_plugin='mysql_native_password')
cursors = connect.cursor()
cursors.execute("SELECT * FROM Students")
tree = ttk.Treeview(control)
tree['show'] = 'headings'

tree["columns"] = ("Name", "Surname", "ID_number", "Cellnumber", "Kin_name", "Kin_number", "sign_date", "sign_time", "Password")
tree.column("Name", width=100, minwidth=100, anchor=tk.CENTER)
tree.column("Surname", width=100, minwidth=100, anchor=tk.CENTER)
tree.column("ID_number", width=150, minwidth=150, anchor=tk.CENTER)
tree.column("Cellnumber", width=150, minwidth=150, anchor=tk.CENTER)
tree.column("Kin_name", width=100, minwidth=100, anchor=tk.CENTER)
tree.column("Kin_number", width=150, minwidth=150, anchor=tk.CENTER)
tree.column("sign_date", width=100, minwidth=100, anchor=tk.CENTER)
tree.column("sign_time", width=100, minwidth=100, anchor=tk.CENTER)
tree.column("Password", width=150, minwidth=150, anchor=tk.CENTER)

tree.heading("Name", text="Name", anchor=tk.CENTER)
tree.heading("Surname", text="Surname", anchor=tk.CENTER)
tree.heading("ID_number", text="ID_number", anchor=tk.CENTER)
tree.heading("Cellnumber", text="Cellnumber", anchor=tk.CENTER)
tree.heading("Kin_name", text="Kin Name", anchor=tk.CENTER)
tree.heading("Kin_number", text="Kin Number", anchor=tk.CENTER)
tree.heading("sign_date", text="Sign in date", anchor=tk.CENTER)
tree.heading("sign_time", text="Sign in time", anchor=tk.CENTER)
tree.heading("Password", text="Password", anchor=tk.CENTER)

i = 0
for ro in cursors:
    tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8]))
    i = i + 1

name = tk.StringVar()
sur = tk.StringVar()
id = tk.StringVar()
cell = tk.StringVar()
kin_n = tk.StringVar()
kin_cell = tk.StringVar()
word = tk.StringVar()


def add_data(tree):
    f = Frame(control, width=400, height=400, background="black")
    f.place(x=400, y=80)

    user = Label(f, text="Name", width=10)
    name_input = Entry(f, textvariable=name, width=25)
    user.place(x=50, y=30)
    name_input.place(x=170, y=30)

    sname = Label(f, text="Surname", width=10)
    sname_input = Entry(f, textvariable=sur, width=25)
    sname.place(x=50, y=70)
    sname_input.place(x=170, y=70)

    id_num = Label(f, text="ID number", width=10)
    id_num_input = Entry(f, textvariable=id, width=25)
    id_num.place(x=50, y=110)
    id_num_input.place(x=170, y=110)

    phone = Label(f, text="Cellnumber", width=10)
    cell_input = Entry(f, textvariable=cell, width=25)
    phone.place(x=50, y=150)
    cell_input.place(x=170, y=150)

    kin_name = Label(f, text="Kin_name", width=10)
    kin_name_input = Entry(f, textvariable=kin_n, width=25)
    kin_name.place(x=50, y=190)
    kin_name_input.place(x=170, y=190)

    kin_num = Label(f, text="Kin number", width=10)
    kin_num_input = Entry(f, textvariable=kin_cell, width=25)
    kin_num.place(x=50, y=230)
    kin_num_input.place(x=170, y=230)

    passw = Label(f, text="Password", width=10)
    passw_input = Entry(f, textvariable=word, width=25)
    passw.place(x=50, y=270)
    passw_input.place(x=170, y=270)

    def data():
        nonlocal name_input, sname_input, id_num_input, cell_input, kin_name_input, kin_num_input, passw_input
        n = name.get()
        s = sur.get()
        i = id.get()
        c = cell.get()
        k = kin_n.get()
        g = kin_cell.get()
        p = word.get()
        cursors.execute('INSERT INTO Students(Name, Surname, ID_number, Cellnumber, Kin_name, Kin_number, Password) VALUES(%s, %s, %s, %s, %s, %s, %s)',
                        (n, s, i, c, k, g, p))
        connect.commit()
        tree.insert('', 'end', text="", values=(n, s, i, c, k, g, p))
        messagebox.showinfo("Success", "Information registered")
        name_input.delete(0, END)
        sname_input.delete(0, END)
        id_num_input.delete(0, END)
        cell_input.delete(0, END)
        kin_name_input.delete(0, END)
        kin_num_input.delete(0, END)
        passw_input.delete(0, END)
        f.destroy()

    def close():
        f.destroy()

    submit = tk.Button(f, text="Submit", command=data)
    submit.place(x=100, y=320)
    cancel = tk.Button(f, text="Cancel", command=close)
    cancel.place(x=240, y=320)


def delete_data(tree):
    selected_items = tree.selection()[0]
    print(tree.item(selected_items)['values'])
    uid = tree.item(selected_items)['values'][0]
    del_querry = "DELETE FROM Students WHERE Name=%s"
    sel_data = (uid,)
    cursors.execute(del_querry, sel_data)
    connect.commit()
    tree.delete(selected_items)
    messagebox.showinfo("Success", "Data Deleted")


# Creating and Placing Labels
admin = Label(control, text="Administrator", font="arial 30 italic")
admin.place(x=500, y=20)

# Creating and Placing Buttons
sert = Button(control, text="INSERT", command=lambda: add_data(tree))
delete = Button(control, text="DELETE", command=lambda: delete_data(tree))

sert.place(x=100, y=350)
delete.place(x=200, y=350)

tree.place(x=50, y=100)

control.mainloop()
