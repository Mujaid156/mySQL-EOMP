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

def quit_program():
    return option.destroy()

# Creating Labels
life = Label(option, text="Life choices online", font="Arial 25 italic", bg="skyblue")

# Placing Labels
life.place(x=120, y=50)

# Creating Buttons
visit = Button(option, text="Register/Visitor", width=15, borderwidth=5, command=visit)
employee = Button(option, text="Employee", width=15, borderwidth=5, command=employ)
admin = Button(option, text="Administrator", width=15, borderwidth=5, command=admin)
quit = Button(option, text="Exit", width=10, command=quit_program)

# Placing Buttons
visit.place(x=180, y=150)
employee.place(x=180, y=210)
admin.place(x=180, y=270)
quit.place(x=200, y=350)

option.mainloop()
