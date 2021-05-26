from DatabaseConnection.dbConnect import *
from logPassGenerator import *
from emailSender import *
from Frontend.mainMenu import *
from main import *

class Login:

    def logIn(l, p):
        login = l.get()
        password = p.get()
        cursor.execute("SELECT UserLogin, UserPassword FROM [dbo].[AppUser] WHERE UserLogin ='"+ login +"' AND UserPassword ='" + password + "'")
        results = cursor.fetchall()
        if results:
            MainMenu()
        else:
            tkinter.messagebox.showerror('Błąd', "Niepoprawny login lub hasło")

    def send_reset_pass(self, address_entry):
        address = address_entry.get()
        result = SqlQuery.Select(self, "SELECT UserID, Email FROM Person WHERE Email = ", address)
        if result:
            new_pass = LogPassGenerator.GeneratePassword(self)
            Sender(address, "Reset hasła", "Nowe hasło to: " + new_pass)
            SqlQuery.Update(self, "UPDATE AppUser SET UserPassword = '"+new_pass+"' FROM  Person WHERE Person.Email = '"+address+"' AND Person.UserID = AppUser.ID")
        else:
            tkinter.messagebox.showerror('Błąd', "Podany adres e-mail nie istnieje w bazie.")