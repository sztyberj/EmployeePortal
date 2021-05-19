import tkinter.messagebox
from DatabaseConnection.dbConnect import *
from Frontend.mainMenu import *
from Frontend.loginMenu import *
class Login:
    @staticmethod
    def logIn(l, p):
        login = l.get()
        password = p.get()
        cursor.execute("SELECT * FROM [dbo].[AppUser] WHERE UserLogin ='"+ login +"' AND UserPassword ='"+ password + "'")
        results = cursor.fetchall()
        if results:
            openMenu = MainMenu()

        else:
            tkinter.messagebox.showerror('Błąd', "Niepoprawny login lub hasło")