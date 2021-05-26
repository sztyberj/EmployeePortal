from main import *
import time


class LoadingWindow:
    def __init__(self):
        root = tk.Tk()

        # True - hide main bar window
        root.overrideredirect(1)

        Window(root, '', 250, 400)

        root.resizable(False, False)
        root.configure(background='#2A2828')

        canvas_width = 400
        canvas = Canvas(root, width=canvas_width, height=30, background='#2A2828', bd=0, highlightthickness=0, relief='ridge')

        Tittle = 'Portal pracownika'
        TittleFont = Font(family="Helvetica", size=25, weight="bold")
        FootFont = Font(size=10)

        MainBar = Label(root, width=16, background="#2A2828", text=Tittle, font=TittleFont, foreground='orange')
        FootBar = Label(root, background="#2A2828", text="Created by Jakub Sztyber", foreground='white', font=FootFont)


        rectangle = canvas.create_rectangle(50, 50,  0, 0, outline='orange',fill='orange')


        canvas.place(relx=0, rely=0.6)
        MainBar.place(relx=0.15, rely=0.25)
        FootBar.place(relx=0.55, rely=0.85)

        LoadingWindow.LoadingAnimation(self, rectangle, canvas, root)
        root.mainloop()
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

if __name__ == '__main__':
    OpenWindow = LoadingWindow()

