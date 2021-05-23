
from DatabaseConnection import *
from main import *
from window_init import *


class MainMenu:
    def __init__(self):
        root = tk.Tk()
        Window(root, 'Portal Pracownika', 700, 1200)
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

        userButton = Button(title_frame, width=30, highlightthickness=0, borderwidth=0, height=28,  image=user_icon, command=lambda: (print("CHUJOZA")))
        userButton.place(rely=0, relx=0.97)

        # ========= Work time button  ========= #
        work_time = Button(left_frame, width=30, height=3, bg='white', highlightthickness=0,
                           activebackground='orange', command= lambda : MainMenu.show_work_time(self, content_frame),
                           text='Czas pracy')
        work_time.pack()

        # ========= Contacts button  ========= #
        contacts = Button(left_frame, width=30, height=3, bg='white', highlightthickness=0,
                          activebackground='orange',
                          text='Kontakty', command=lambda: MainMenu.show_contacts(self, content_frame))
        contacts.pack()

        # ========= Applications button  ========= #
        applications = Button(left_frame, width=30, height=3, bg='white', highlightthickness=0,
                              activebackground='orange',
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

    def show_contacts(self, content_frame):
        Window.ClearFrame(content_frame)
        TableFrame = Frame(content_frame, width=500, height=300, bg="white")
        TableFrame.pack(fill="both", expand=True, padx=40, pady=40)
        e = Label(TableFrame, width=10, text='Imię', borderwidth=1, relief='ridge', anchor=N, bg='gray')
        e.grid(row=0, column=0)
        e = Label(TableFrame, width=20, text='Nazwisko', borderwidth=1, relief='ridge', anchor='w', bg='gray')
        e.grid(row=0, column=1)
        e = Label(TableFrame, width=20, text='Numer Telefonu', borderwidth=1, relief='ridge', anchor='w', bg='gray')
        e.grid(row=0, column=2)
        e = Label(TableFrame, width=20, text='E-mail', borderwidth=1, relief='ridge', anchor='w', bg='gray')
        e.grid(row=0, column=3)
        e = Label(TableFrame, width=25, text='Departament', borderwidth=1, relief='ridge', anchor='w', bg='gray')
        e.grid(row=0, column=4)


        MainMenu.print_data(DatabaseConnection.sqlQuery.SelectContacts(), content_frame)

    def show_work_time(self, content_frame):
        Window.ClearFrame(content_frame)
        # ========= Calendar components ========= #

        add_work_time = Button(content_frame, text='Dodaj czas pracy', activebackground='orange', width=11)
        Calendar(content_frame).place(relx=0.07, rely=0.1)
        hours = Scale(content_frame, from_=0, to=14, orient=HORIZONTAL, bg='white', activebackground='orange', border=0)
        hours.place(relx=0.07, rely=0.49)
        add_work_time.place(relx=0.2, rely=0.5)

        # ========= Work table  ========= #
        date = Label(content_frame, width=20, text='Data', borderwidth=1, relief='ridge', anchor=N, bg='gray')
        date.place(relx=0.6, rely=0.1)
        hours = Label(content_frame, width=20, text='Czas', borderwidth=1, relief='ridge', anchor='w', bg='gray')
        hours.place(relx=0.76, rely=0.1)


    def show_user_management(self, content_frame):
        Window.ClearFrame(content_frame)

        TableFrame = Frame(content_frame, width=250, height=300, bg="white")
        TableFrame.pack(fill="both", expand=True, padx=40, pady=40)
        e = Label(TableFrame, width=10, text='Imię', borderwidth=1, relief='ridge', anchor=N, bg='gray')
        e.grid(row=0, column=0)
        e = Label(TableFrame, width=10, text='Nazwisko', borderwidth=1, relief='ridge', anchor='w', bg='gray')
        e.grid(row=0, column=1)
        e = Label(TableFrame, width=10, text='Telefon', borderwidth=1, relief='ridge', anchor='w', bg='gray')
        e.grid(row=0, column=2)
        e = Label(TableFrame, width=10, text='E-mail', borderwidth=1, relief='ridge', anchor='w', bg='gray')
        e.grid(row=0, column=3)
        e = Label(TableFrame, width=15, text='Departament', borderwidth=1, relief='ridge', anchor='w', bg='gray')
        e.grid(row=0, column=4)

        add_button = Button(content_frame, width=3, height=2, bg='blue')
        add_button.pack()

        edit_button = Button(content_frame, width=3, height=2, bg='blue')
        edit_button.pack()


    def show_adminPanel(self, content_frame):
        Window.ClearFrame(content_frame)
        user_management = Button(content_frame, width=20, height=10, bg='red', text='Zarządzanie pracownikami', command=lambda: MainMenu.show_user_management(self, content_frame))
        user_management.grid(row=0, column=0, padx=20, pady=10)

        deparment_management = Button(content_frame, width=20, height=10, bg='blue', text='Zarządzanie działami')
        deparment_management.grid(row=0, column=1)




    def print_data(self, z, content_frame):
        print(z)


if __name__ == '__main__':
    run = MainMenu()




