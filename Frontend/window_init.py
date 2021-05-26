# ======= Init for create windows ======= #
class Window:
    def __init__(self, root, title, h=0, w=0):
        """
        :param title:
            window title bar
        :param h:
            window height
        :param w:
            window width
        """

        self.root = root
        self.root.title(title)
        self.ws = root.winfo_screenwidth()
        self.hs = root.winfo_screenheight()
        self.x = (self.ws / 2) - (w / 2)
        self.y = (self.hs / 2) - (h / 2)
        root.geometry('%dx%d+%d+%d' % (w, h, self.x, self.y))

    @staticmethod
    def ClearFrame(frame):
        for widget in frame.winfo_children():
            widget.destroy()


    def combine_funcs(*funcs, **kwargs):
        """
        :combine_funcs - Combine functions for command button
        """
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)

        return combined_func

