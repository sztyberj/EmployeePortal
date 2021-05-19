from window_init import *
import tkinter as tk
from tkinter import *
from mainMenu import *
from Backend.login import *


class LoginMenu:
    def __init__(self):
        root = tk.Tk()
        LoginWindow = Window(root, '', 400, 330)
        root.resizable(False, False)
        main_frame = Frame(root, width=330, height=400, bg="#2A2828").place(relx=0, rely=0)
        LoginMenu.CreateLoginMenu(self, root, main_frame)
        root.mainloop()


    def CreateLoginMenu(self, root, main_frame):

        root.title('Logowanie')

        label_login = Label(main_frame, text="Login: ", width=15, height=2, bg="#2A2828", fg='orange')
        entry_login = Entry(main_frame, width=20, borderwidth=0, highlightthickness=0, bg="orange")

        label_password = Label(main_frame, text="Hasło: ", width=15, height=2, bg="#2A2828", fg='orange')
        entry_password = Entry(main_frame, width=20, borderwidth=0, highlightthickness=0, bg="orange")

        button_remember = Button(main_frame, text="Zapomniałem hasła!", width=15, height=1, highlightthickness=0, bg="#2A2828", fg='orange',
                                 borderwidth=0, activebackground="#2A2828", activeforeground='#840707',
                                 command=lambda: LoginMenu.RememberPassword(self, root, main_frame))

        button_login = Button(main_frame, text="Zaloguj się", width=9, height=2, bg='orange', fg="#2A2828",
                              activebackground='#840707', command=lambda: Login.logIn(entry_login, entry_password))

        label_login.place(relx=0.05, rely=0.28)
        entry_login.place(relx=0.35, rely=0.3)

        label_password.place(relx=0.05, rely=0.38)
        entry_password.place(relx=0.35, rely=0.4)

        button_remember.place(relx=0.35, rely=0.47)

        button_login.place(relx=0.4, rely=0.75)

        root.mainloop()



    def RememberPassword(self, root, main_frame):
        Window.ClearFrame(root)
        root.configure(background="#2A2828")
        root.title('Zapomniałem hasła')

        label_info = Label(main_frame, text="Na podany adres e-mail zostanie wysłane nowe hasło.",
                            width=40, height=2, bg="#2A2828", fg='orange').place(relx=0.1, rely=0.2)

        label_email = Label(main_frame, text="Adres e-mail: ", width=10, height=2, bg="#2A2828", fg='orange').place(relx=0.12, rely=0.38)

        entry_email = Entry(main_frame, width=20, borderwidth=1, highlightthickness=0, bg="orange").place(relx=0.35, rely=0.4)

        send_button = Button(main_frame, bg="orange", text='Wyślij', highlightthickness=0, width=9, height=2, fg='#2A2828',
                             activebackground='#840707').place(relx=0.4, rely=0.7)

        cancel_button = Button(main_frame, bg="orange", text='Anuluj', highlightthickness=0, width=6, height=1, fg= '#2A2828', activebackground='#840707',
                               command=lambda: Window.combine_funcs(Window.ClearFrame(root), LoginMenu.CreateLoginMenu(self, root, main_frame))).place(relx=0.433, rely=0.85)







