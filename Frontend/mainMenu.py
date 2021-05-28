from window_init import Window
from tkinter import *
from tkinter import Image, ttk
from dbConnect import DatabaseConnector
from logPassGenerator import LogPassGenerator
from emailSender import Sender
from person import Person
import PIL.ImageTk
import tkcalendar
import fileSystem



#DO ZROBIENIA JUTRO! WIDOK USERA, WYSTARCZY ZMIANA HASŁA.
#SELECTY DO KONTAKTÓW I PANELU ADMINA


class MainMenu:
    def __init__(self):
        self.root = Toplevel()
        new = Window(self.root, 'Portal Pracownika', 700, 1200)
        self.root.resizable(True, True)
        self.root.minsize(1100, 520)
        self.root.configure(background="#2A2828")

        self.title_frame = Frame(self.root, background='orange', height=50)
        self.title_frame.pack(side=TOP, fill='both', pady=0)
        self.main_title = Label(self.title_frame, text='Portal Pracownika', foreground='red')
        self.main_title.pack(side= LEFT, anchor=N)

        self.content_frame = Frame(self.root, width=700, height=450, bg="white")
        self.content_frame.pack(side=RIGHT, fill="both", expand=True, padx=20, pady=20)
        self.left_frame = Frame(self.root, width=400, height=600, bg='white')
        self.left_frame.pack(side=LEFT, pady=20, anchor=NW)


        self.img = PIL.Image.open(r"/home/jakub/Desktop/Employee Portal (JIPP sem. 4 Project)/icon.png")
        self.img = self.img.resize((32, 32), PIL.Image.ANTIALIAS)
        self.icon = PIL.ImageTk.PhotoImage(self.img)

        self.delete = PIL.Image.open(r"/home/jakub/Desktop/Employee Portal (JIPP sem. 4 Project)/trash.png")
        self.delete = self.delete.resize((32, 32), PIL.Image.ANTIALIAS)
        self.delete_icon = PIL.ImageTk.PhotoImage(self.delete)

        self.img1 = PIL.Image.open(r"/home/jakub/Desktop/Employee Portal (JIPP sem. 4 Project)/user.png")
        self.img1 = self.img1.resize((32, 32), PIL.Image.ANTIALIAS)
        self.user_icon = PIL.ImageTk.PhotoImage(self.img1)

        MainMenu.create_left_frame_buttons(self)
        MainMenu.show_contacts(self)

        self.root.mainloop()


    # ========= Create left frame buttons  ========= #

    def create_left_frame_buttons(self):
        Window.ClearFrame(self.title_frame)
        iconButton = Button(self.title_frame, width=30, highlightthickness=0, borderwidth=0, height=30,  image=self.icon,
                            command=lambda: MainMenu.hide_bar(self))
        iconButton.place(rely=0, relx=0)


        userButton = Button(self.title_frame, width=30, highlightthickness=0, borderwidth=0, height=28,  image=self.user_icon, command=lambda: MainMenu.show_user_window(self))
        userButton.place(rely=0, relx=0.97)


        work_time = Button(self.left_frame, width=30, height=3, bg='white', highlightthickness=0,
                           activebackground='orange', command= lambda : MainMenu.show_work_time(self),
                           text='Czas pracy')
        work_time.pack()


        contacts = Button(self.left_frame, width=30, height=3, bg='white', highlightthickness=0,
                          activebackground='orange',
                          text='Kontakty', command=lambda: MainMenu.show_contacts(self))
        contacts.pack()


        applications = Button(self.left_frame, width=30, height=3, bg='white', highlightthickness=0,
                              activebackground='orange',
                              text='Wnioski', command=lambda: MainMenu.show_applications(self))
        applications.pack()


        adminPanel = Button(self.left_frame, width=30, height=3, bg='white', highlightthickness=0,
                          activebackground='#FF6666',
                          text='Panel Administratora', command=lambda: MainMenu.show_adminPanel(self))
        adminPanel.pack()

    # ========= Function for hiding bar  ========= #

    def hide_bar(self):
        self.left_frame.pack_forget()
        self.left_frame.config(width=5)
        Window.ClearFrame(self.title_frame)
        self.left_frame = Frame(self.root, width=5, height=25, bg="#2A2828")
        self.left_frame.pack(pady=20, anchor=NW)
        iconButton = Button(self.title_frame, highlightthickness=0, borderwidth=0, bd=0, width=30, height=30, image=self.icon,
                            command=lambda: MainMenu.create_left_frame_buttons(self))
        iconButton.place(rely=0, relx=0)

        userButton = Button(self.title_frame, width=30, highlightthickness=0, borderwidth=0, bd=0, height=30, image=self.user_icon,
                            command = lambda: MainMenu.show_user_window(self))
        userButton.place(rely=0, relx=0.97)

    # ========= Left frame buttons functions  ========= #

    def show_applications(self):
        Window.ClearFrame(self.content_frame)
        user_management = Button(self.content_frame, width=20, height=10, bg='orange', text='Dodaj wniosek',
                                 command=lambda: fileSystem.open_file())
        user_management.grid(row=0, column=0, padx=20, pady=10)



    def show_contacts(self):
        Window.ClearFrame(self.content_frame)

        contacts_tree = ttk.Treeview(self.content_frame, height=20)
        contacts_tree['columns'] = ("Imie", "Nazwisko", "Telefon", "Email")

        contacts_tree.column("#0", width=0)
        contacts_tree.column("Imie", anchor="center", width=50)
        contacts_tree.column("Nazwisko", anchor="center", width=50)
        contacts_tree.column("Email", anchor="center", width=50)
        contacts_tree.column("Telefon", anchor="center", width=50)


        contacts_tree.heading("#0", text='')
        contacts_tree.heading("Imie", text="Imie", anchor="center")
        contacts_tree.heading("Nazwisko", text="Nazwisko", anchor="center")
        contacts_tree.heading("Email", text="Telefon", anchor="center")
        contacts_tree.heading("Telefon", text="Email", anchor="center")


        contacts_tree['show'] = 'headings'

        contacts_tree.pack(pady=20, padx=20, fill="both", expand=True)

        cont = DatabaseConnector.select_contacts(DatabaseConnector, Person)

        for x in cont:
            contacts_tree.insert(parent='', index='end', iid=x[0],
                                 values=(x[1], x[2], x[3], x[4]))



    def show_work_time(self):
        i = 0
        Window.ClearFrame(self.content_frame)
        # ========= Calendar components ========= #

        add_work_time = Button(self.content_frame, text='Dodaj czas pracy', activebackground='orange', width=11, height=1, command=lambda: add_time(0))
        calendar = tkcalendar.Calendar(self.content_frame).place(relx=0.1, rely=0.1)
        hours = Scale(self.content_frame, from_=0, to=14, orient=HORIZONTAL, bg='white', activebackground='orange', border=0)
        hours.place(relx=0.1, rely=0.5)
        add_work_time.place(relx=0.1, rely=0.7)
        date_label = Label(self.content_frame, text="Format YYYY-MM-DD", bg='white')
        date_label.place(relx=0.25, rely=0.47)
        date_entry = Entry(self.content_frame)
        date_entry.place(relx=0.25, rely=0.52)

        def add_time(i):
            date =  date_entry.get()
            h = hours.get()
            work_tree.insert(parent='', index='end', iid=i+1,
                                 values=(str(date), str(h)))



        # ========= Work table  ========= #

        work_tree = ttk.Treeview(self.content_frame, height=20)
        work_tree['columns'] = ("Data", "Czas")

        work_tree.column("#0", width=0)
        work_tree.column("Data", anchor="center", width=100)
        work_tree.column("Czas", anchor="center", width=100)

        work_tree.heading("#0", text='')
        work_tree.heading("Data", text="Data", anchor="center")
        work_tree.heading("Czas", text="Czas", anchor="center")

        work_tree['show'] = 'headings'
        work_tree.place(relx=0.6, rely=0.1)



    def show_user_management(self):
        Window.ClearFrame(self.content_frame)

        user_m_Frame = Frame(self.content_frame, width=250, height=300, bg='white')
        user_m_Frame.pack(fill=Y, side = RIGHT, pady=40, padx=20)

        contacts_tree = ttk.Treeview(self.content_frame, height=20)
        contacts_tree['columns'] = ("Imie", "Nazwisko", "Telefon", "Email")



        contacts_tree.column("#0", width=0)
        contacts_tree.column("Imie", anchor="center", width=50)
        contacts_tree.column("Nazwisko", anchor="center", width=50)
        contacts_tree.column("Email", anchor="center", width=70)
        contacts_tree.column("Telefon", anchor="center", width=50)


        contacts_tree.heading("#0", text='')
        contacts_tree.heading("Imie", text="Imie", anchor="center")
        contacts_tree.heading("Nazwisko", text="Nazwisko", anchor="center")
        contacts_tree.heading("Email", text="Telefon", anchor="center")
        contacts_tree.heading("Telefon", text="Email", anchor="center")



        contacts_tree['show'] = 'headings'

        cont = DatabaseConnector.select_contacts(DatabaseConnector, Person)

        for x in cont:
            contacts_tree.insert(parent='', index='end', iid=x[0],
                                 values=(x[1], x[2], x[3], x[4]))



        contacts_tree.pack(pady=20, padx=20, fill="both", expand=True)

        add_button = Button(user_m_Frame, width=6, height=2, bg='green', text="Zatwierdź")
        add_button.grid(row=6, column=0,pady=90, padx=10)

        clear_button = Button(user_m_Frame, width=6, height=2, bg='red', text = "Usuń")
        clear_button.grid(row=6, column=1, padx=10)

        delete_button = Button(user_m_Frame, width=70, height=40, image=self.delete_icon)
        delete_button.grid(row=6, column=2, padx=10)

        fname = Entry(user_m_Frame, bg='white', foreground='#2A2828')
        sname = Entry(user_m_Frame, bg='white', foreground='#2A2828')
        phone = Entry(user_m_Frame, bg='white', foreground='#2A2828')
        email = Entry(user_m_Frame, bg='white', foreground='#2A2828')


        fname.grid(row=1, column=2, pady=10, padx=10)
        sname.grid(row=2, column=2, pady=10, padx=10)
        phone.grid(row=3, column=2, pady=10, padx=10)
        email.grid(row=4, column=2, pady=10, padx=10)



        fname_l = Label(user_m_Frame, text='Imie: ', bg='white', foreground='#2A2828', width=15).grid(row=1, column=0, columnspan=2, pady=10)
        sname_l = Label(user_m_Frame, text='Nazwisko: ', bg='white', foreground='#2A2828', width=18).grid(row=2, column=0, columnspan=2, pady=10, padx=10)
        phone_l = Label(user_m_Frame, text='Telefon: ', bg='white', foreground='#2A2828', width=20).grid(row=3, column=0, columnspan=2, pady=10, padx=10)
        email_l = Label(user_m_Frame, text='Email: ', bg='white', foreground='#2A2828', width=22).grid(row=4, column=0, columnspan=2, pady=10, padx=10)


        def selectItem(a):
            lst = []
            curItem = contacts_tree.focus()
            lst = contacts_tree.item(curItem, option = 'values')
            fname.delete(0, 'end')
            sname.delete(0, 'end')
            phone.delete(0, 'end')
            email.delete(0, 'end')


            fname.insert(0, lst[0])
            sname.insert(1, lst[1])
            phone.insert(2, lst[2])
            email.insert(3, lst[3])

        def clear(b):
            fname.delete(0, 'end')
            sname.delete(0, 'end')
            phone.delete(0, 'end')
            email.delete(0, 'end')

        def insert(c):
            firstname = fname.get()
            sndname = sname.get()
            phone_number = phone.get()
            email_get = email.get()
            password = LogPassGenerator.GeneratePassword(LogPassGenerator)
            login = LogPassGenerator.GenerateLogin(LogPassGenerator, firstname, sndname)

            person = Person(login, password, firstname, sndname, phone_number, email_get, 1)
            DatabaseConnector.insert_data(DatabaseConnector, person)

            Sender(email_get, 'Nowe konto', 'Witamy wśród użytkowników Potalu Pracownika. Oto twoje dane do logowania. Login: '+login+' Hasło: '+password)


        contacts_tree.bind('<ButtonRelease-1>', selectItem)
        clear_button.bind('<ButtonRelease-1>', clear)
        add_button.bind('<ButtonRelease-1>', insert)

    def show_adminPanel(self):
        Window.ClearFrame(self.content_frame)
        user_management = Button(self.content_frame, width=20, height=10, bg='#C51D1D', activebackground='white', text='Zarządzanie pracownikami', command=lambda: MainMenu.show_user_management(self))
        user_management.grid(row=0, column=0, padx=20, pady=10)

        deparment_management = Button(self.content_frame, width=20, height=10, bg='#1F3E84', activebackground='white', text='Zarządzanie działami')
        deparment_management.grid(row=0, column=1)

    def show_user_window(self):
        Window.ClearFrame(self.content_frame)

        password_label = Label(self.content_frame, text='Nowe hasło: ', background='white')
        password_label.pack(padx=20, pady=20)

        password_entry = Entry(self.content_frame)
        password_entry.pack(padx=20, pady=20)

        send_button = Button(self.content_frame, text="Zresetuj", bg='orange')
        send_button.pack(padx=20, pady=20)


if __name__ == '__main__':
    run = MainMenu()




