import loginMenu
from mainMenu import MainMenu
from dbConnect import DatabaseConnector
from tkinter import messagebox
from person import Person
from logPassGenerator import LogPassGenerator
from emailSender import Sender

class Login:

    def logIn(l, p):
        login = l.get()
        password = p.get()
        select = DatabaseConnector.select_user(DatabaseConnector, Person, Person.UserLogin==login, Person.UserPassword==password)
        for x in select:
            if x.UserLogin == login and  x.UserPassword == password:
                del loginMenu.LoginMenu
                MainMenu()
            else:
                messagebox.showerror('Nieudana próba logowania', 'Nieprawidłowy login lub hasło!')

    def send_reset_pass(self, address_entry):
        address = address_entry.get()
        result = DatabaseConnector.select(DatabaseConnector, Person, Person.Email==address).one()
        if result:
            new_pass = LogPassGenerator.GeneratePassword(LogPassGenerator)
            Sender(address, "Reset hasła", "Nowe hasło to: " + new_pass)
            result.UserPassword
            DatabaseConnector.update_password(Person, )
        else:
            messagebox.showerror('Błąd', "Podany adres e-mail nie istnieje w bazie.")