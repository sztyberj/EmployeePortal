import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from window_init import *
from tkcalendar import *
from abc import ABC, abstractmethod
import time


class MainMenu:
    def __init__(self):
        root = tk.Tk()
        windowinit = Window(root, 'Portal Pracownika', 700, 1200)
        root.resizable(True, True)
        root.minsize(900, 480)
        root.configure(background="#2A2828")

        title_frame = Frame(root, background='orange', height=50)
        title_frame.pack(side=TOP, fill='both', pady=0)
        main_title = Label(title_frame, text='Portal Pracownika', foreground='red')
        main_title.pack(side= LEFT, anchor=N)

        img = Image.open(r"/home/jakub/Desktop/Employee Portal (JIPP sem. 4 Project)/icon.png")
        img = img.resize((32, 32), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(img)

        img1 = Image.open(r"/home/jakub/Desktop/Employee Portal (JIPP sem. 4 Project)/user.png")
        img1 = img1.resize((32, 32), Image.ANTIALIAS)
        user_icon = ImageTk.PhotoImage(img1)

        content_frame = Frame(root, width=700, height=450, bg="white")
        content_frame.pack(side=RIGHT, fill="both", expand=True, padx=20, pady=20)
        left_frame = Frame(root, width=400, height=600, bg='white')
        left_frame.pack(side=LEFT, pady=20, anchor=NW)

        MainMenu.create_left_frame_buttons(self, root, content_frame, left_frame, title_frame, icon, user_icon)
        #MainMenu.show_contacts(self, content_frame)



        root.mainloop()

    # ========= Create left frame buttons  ========= #

    def create_left_frame_buttons(self, root, content_frame, left_frame, title_frame, icon, user_icon):
        Window.ClearFrame(title_frame)
        iconButton = Button(title_frame, width=30, highlightthickness=0, borderwidth=0, height=30,  image=icon,
                            command=lambda: MainMenu.hide_bar(self, left_frame, content_frame, root, title_frame, icon, user_icon))
        iconButton.place(rely=0, relx=0)

        userButton = Button(title_frame, width=30, highlightthickness=0, borderwidth=0, height=28,  image=user_icon)
        userButton.place(rely=0, relx=0.97)
        # ========= Work time button  ========= #
        work_time = Button(left_frame, width=30, height=3, bg='white', highlightthickness=0,
                           activebackground='#FFC71E', command= lambda : MainMenu.show_work_time(self, content_frame),
                           text='Czas pracy')
        work_time.pack()

        # ========= Contacts button  ========= #
        contacts = Button(left_frame, width=30, height=3, bg='white', highlightthickness=0,
                          activebackground='#FFC71E',
                          text='Kontakty', command=lambda: MainMenu.show_contacts(self, content_frame))
        contacts.pack()

        # ========= Applications button  ========= #
        applications = Button(left_frame, width=30, height=3, bg='white', highlightthickness=0,
                              activebackground='#FFC71E',
                              text='Wnioski', command=lambda: MainMenu.show_applications(self, content_frame))
        applications.pack()

        # ========= Settings button  ========= #
        adminPanel = Button(left_frame, width=30, height=3, bg='white', highlightthickness=0,
                          activebackground='#FF6666',
                          text='Panel Administratora', command=lambda: MainMenu.show_adminPanel(self, content_frame))
        adminPanel.pack()

    # ========= Active frame settings  ========= #

    def hide_bar(self, left_frame, content_frame, root, title_frame, icon, user_icon):
        left_frame.destroy()
        Window.ClearFrame(title_frame)
        left_frame = Frame(root, width=5, height=25, bg="#2A2828")
        left_frame.pack(pady=20, anchor=NW)
        iconButton = Button(title_frame, highlightthickness=0, borderwidth=0, bd=0, width=30, height=30, image=icon,
                            command=lambda: MainMenu.create_left_frame_buttons(self, root, content_frame, left_frame, title_frame, icon, user_icon))
        iconButton.place(rely=0, relx=0)

        userButton = Button(title_frame, width=30, highlightthickness=0, borderwidth=0, bd=0, height=30, image=user_icon)
        userButton.place(rely=0, relx=0.97)

    # ========= Left frame buttons functions  ========= #

    def show_applications(self, content_frame):
        Window.ClearFrame(content_frame)
        add_app = Button(content_frame, bg='red', text='Dodaj wniosek')
        add_app.pack()

        delete_app = Button(content_frame, bg='red', text='Usuń wniosek')
        delete_app.pack(side=LEFT)

    def show_vacations(self, content_frame):
        Window.ClearFrame(content_frame)
        add_app = Button(content_frame, bg='red', text='Dodaj urlop')
        add_app.place(relx=0.5, rely=0.1)
        cal = Calendar(content_frame, selectmode="day")
        cal.pack(anchor=NE, padx=20, pady=20)

    def show_work_time(self, content_frame):
        Window.ClearFrame(content_frame)
        add_work_time = Button(content_frame, bg='red', text='Dodaj czas pracy')
        add_work_time.place(relx=0.5, rely=0.1)

    def show_adminPanel(self, content_frame):
        Window.ClearFrame(content_frame)
        add_work_time = Button(content_frame, bg='red', text='Ustawienia')
        add_work_time.place(relx=0.5, rely=0.1)


    def show_contacts(self, content_frame):
        Window.ClearFrame(content_frame)
        """
        def ShowContact():
            SelectSQL('[SalesLT].[Customer]')
            for j in range(len(contact)):
                e = tk.Entry(content_frame, width=150, fg='blue')
                e.pack(anchor=NW)
                e.insert(END, contact[j])
                e.config(state='disabled')
        """
        add_work_time = Button(content_frame, bg='red', text='Kontakty')
        add_work_time.place(relx=0.5, rely=0.1)


run = MainMenu()




