from _tkinter import *
from tkinter.ttk import *
from tkinter.font import *
import tkinter as tk
import time
from window_init import *
from loginMenu import *


class LoadingWindow:
    def __init__(self):
        self.mainroot = tk.Tk()

        # True - hide main bar window
        self.mainroot.overrideredirect(1)

        OpenWindow = Window(self.mainroot, '', 250, 400)

        self.mainroot.resizable(False, False)
        self.mainroot.configure(background='#2A2828')

        canvas_width = 400
        canvas = Canvas(self.mainroot, width=canvas_width, height=30, background='#2A2828', bd=0, highlightthickness=0, relief='ridge')

        Tittle = 'Portal pracownika'
        TittleFont = Font(family="Helvetica", size=25, weight="bold")
        FootFont = Font(size=10)

        MainBar = Label(self.mainroot, width=16, background="#2A2828", text=Tittle, font=TittleFont, foreground='orange')
        FootBar = Label(self.mainroot, background="#2A2828", text="Created by Jakub Sztyber", foreground='white', font=FootFont)


        rectangle = canvas.create_rectangle(50, 50,  0, 0, outline='orange',fill='orange')


        canvas.place(relx=0, rely=0.6)
        MainBar.place(relx=0.15, rely=0.25)
        FootBar.place(relx=0.55, rely=0.85)

        LoadingWindow.LoadingAnimation(self, rectangle, canvas, self.mainroot)
        self.mainroot.mainloop()
        login_menu = LoginMenu()


    def LoadingAnimation(self, rectangle, canvas, mainroot):

        for x in range(70):
            xspeed = 5
            yspeed = 0
            canvas.move(rectangle, xspeed, yspeed)
            time.sleep(0.03)
            mainroot.update()
        for y in range(70):
            xspeed = -5
            yspeed = 0
            canvas.move(rectangle, xspeed, yspeed)
            time.sleep(0.03)
            mainroot.update()
        mainroot.destroy()


OpenWindow = LoadingWindow()

