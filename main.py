from tkinter import *

option = Tk()
option.title("Life Choices Online")
option.geometry("500x500")
option.config(bg="skyblue")


def switch(event):
    import admin_page


class main:
    def __init__(self, master):
        # Creating Labels
        self.life = Label(option, text="Life choices online", font="Arial 25 italic", bg="skyblue")

        # Placing Labels
        self.life.place(x=120, y=50)

        # Creating Buttons
        self.register = Button(option, text="Register", width=15, borderwidth=5, command=self.register)
        self.visit = Button(option, text="Visitor", width=15, borderwidth=5, command=self.visit)
        self.employee = Button(option, text="Employee", width=15, borderwidth=5, command=self.employ)
        self.admin = Button(option, text="Administrator", width=15, borderwidth=5, command=self.admin)
        self.quit = Button(option, text="Exit", width=10, command=self.quit_program)

        # Placing Buttons
        self.register.place(x=180, y=140)
        self.visit.place(x=180, y=200)
        self.employee.place(x=180, y=260)
        self.admin.place(x=180, y=320)
        self.quit.place(x=200, y=400)

    def admin(self):
        option.destroy()
        import admin

    def employ(self):
        option.destroy()
        import employ

    def visit(self):
        option.destroy()
        import visitor

    def register(self):
        option.destroy()
        import register

    def quit_program(self):
        return option.destroy()


option.bind("<Control-a>", switch)
main(option)
option.mainloop()
