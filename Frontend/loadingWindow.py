from tkinter import *
from tkinter import font
from window_init import Window
from loginMenu import LoginMenu
import time


class LoadingWindow:
    def __init__(self):
        self.root = Tk()

        # True - hide main bar window
        self.root.overrideredirect(1)

        Window(self.root, '', 250, 400)

        self.root.resizable(False, False)
        self.root.configure(background='#2A2828')

        self.canvas_width = 400
        self.canvas = Canvas(self.root, width=self.canvas_width, height=30, background='#2A2828', bd=0, highlightthickness=0, relief='ridge')

        self.Tittle = 'Portal pracownika'
        self.TittleFont = font.Font(family="Helvetica", size=25, weight="bold")
        self.FootFont = font.Font(size=10)

        self.MainBar = Label(self.root, width=16, background="#2A2828", text=self.Tittle, font=self.TittleFont, foreground='orange')
        self.FootBar = Label(self.root, background="#2A2828", text="Created by Jakub Sztyber", foreground='white', font=self.FootFont)


        self.rectangle = self.canvas.create_rectangle(50, 50,  0, 0, outline='orange',fill='orange')


        self.canvas.place(relx=0, rely=0.6)
        self.MainBar.place(relx=0.15, rely=0.25)
        self.FootBar.place(relx=0.55, rely=0.85)

        LoadingWindow.LoadingAnimation(self)
        self.root.mainloop()
        self.login_menu = LoginMenu()


    def LoadingAnimation(self):

        for x in range(70):
            xspeed = 5
            yspeed = 0
            self.canvas.move(self.rectangle, xspeed, yspeed)
            time.sleep(0.03)
            self.root.update()
        for y in range(70):
            xspeed = -5
            yspeed = 0
            self.canvas.move(self.rectangle, xspeed, yspeed)
            time.sleep(0.03)
            self.root.update()
        self.root.destroy()

if __name__ == '__main__':
    OpenWindow = LoadingWindow()

