from DatabaseConnection.dbConnect import *
from main import *


def logIn(l, p):
    login = l.get()
    password = p.get()
    cursor.execute("SELECT UserLogin, UserPassword FROM [dbo].[AppUser] WHERE UserLogin ='"+ login +"' AND UserPassword ='" + password + "'")
    results = cursor.fetchall()
    if results:
        MainMenu()

    else:
        tkinter.messagebox.showerror('Błąd', "Niepoprawny login lub hasło")