from tkinter import *

option = Tk()
option.title("Life Choices Online")
option.geometry("500x500")
option.config(bg="skyblue")

def admin():
    option.destroy()
    import admin

def employ():
    option.destroy()
    import employ

def visit():
    option.destroy()
    import visitor

def register():
    option.destroy()
    import register

def quit_program():
    return option.destroy()

# Creating Labels
life = Label(option, text="Life choices online", font="Arial 25 italic", bg="skyblue")

# Placing Labels
life.place(x=120, y=50)

# Creating Buttons
register = Button(option, text="Register", width=15, borderwidth=5, command=register)
visit = Button(option, text="Visitor", width=15, borderwidth=5, command=visit)
employee = Button(option, text="Employee", width=15, borderwidth=5, command=employ)
admin = Button(option, text="Administrator", width=15, borderwidth=5, command=admin)
quit = Button(option, text="Exit", width=10, command=quit_program)

# Placing Buttons
register.place(x=180, y=140)
visit.place(x=180, y=200)
employee.place(x=180, y=260)
admin.place(x=180, y=320)
quit.place(x=200, y=400)

option.mainloop()
