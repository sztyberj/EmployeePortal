from window_init import Window
from tkinter import *
from tkinter import font
from login import Login


class LoginMenu:
    def __init__(self):
        self.root = Tk()
        Window(self.root, '', 400, 330)
        self.root.resizable(False, False)
        self.main_frame = Frame(self.root, width=330, height=400, bg="#2A2828").place(relx=0, rely=0)
        LoginMenu.CreateLoginMenu(self)
        self.root.mainloop()

    def CreateLoginMenu(self):

        self.root.title('Logowanie')

        label_login = Label(self.main_frame, text="Login: ", width=15, height=2, bg="#2A2828", fg='orange')
        entry_login = Entry(self.main_frame, width=20, borderwidth=0, highlightthickness=0, bg="orange")

        label_password = Label(self.main_frame, text="Hasło: ", width=15, height=2, bg="#2A2828", fg='orange')
        entry_password = Entry(self.main_frame, width=20, borderwidth=0, highlightthickness=0, bg="orange")
        entry_password.config(show="*")

        button_remember = Button(self.main_frame, text="Zapomniałem hasła!", width=15, height=1, highlightthickness=0, bg="#2A2828", fg='orange',
                                 borderwidth=0, activebackground="#2A2828", activeforeground='#840707',
                                 command=lambda: LoginMenu.RememberPassword(self))

        button_login = Button(self.main_frame, text="Zaloguj się", width=9, height=2, bg='orange', fg="#2A2828",
                              activebackground='#840707', highlightthickness=0, command=lambda: Login.logIn(entry_login, entry_password))

        label_login.place(relx=0.05, rely=0.28)
        entry_login.place(relx=0.35, rely=0.3)

        label_password.place(relx=0.05, rely=0.38)
        entry_password.place(relx=0.35, rely=0.4)

        button_remember.place(relx=0.35, rely=0.47)

        button_login.place(relx=0.4, rely=0.75)

        self.root.mainloop()


    def RememberPassword(self):
        Window.ClearFrame(self.root)
        self.root.configure(background="#2A2828")
        self.root.title('Zapomniałem hasła')
        infoFont = font.Font(size=8)
        emailFont = font.Font(size=9)
        label_info = Label(self.main_frame, text="Na podany adres e-mail zostanie wysłane nowe hasło.",
                            width=45, height=2, font=infoFont, bg="#2A2828", fg='orange').place(relx=0.015, rely=0.2)

        label_email = Label(self.main_frame, text="Adres e-mail: ", width=10, height=2, bg="#2A2828", font=emailFont, fg='orange').place(relx=0.09, rely=0.39)

        entry_email = Entry(self.main_frame, width=20, borderwidth=1, highlightthickness=0, bg="orange")
        entry_email.place(relx=0.35, rely=0.4)

        send_button = Button(self.main_frame, bg="orange", text='Wyślij', highlightthickness=0, width=9, height=2, fg='#2A2828',
                             activebackground='#840707', command = lambda: Login.send_reset_pass(self, entry_email))
        send_button.place(relx=0.4, rely=0.7)

        cancel_button = Button(self.main_frame, bg="orange", text='Anuluj', highlightthickness=0, width=6, height=1, fg= '#2A2828', activebackground='#840707',
                               command=lambda: Window.combine_funcs(Window.ClearFrame(self.root), LoginMenu.CreateLoginMenu(self)))
        cancel_button.place(relx=0.433, rely=0.85)



if __name__ == '__main__':
    new = LoginMenu()


