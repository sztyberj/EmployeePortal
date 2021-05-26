import tkinter as tk
from tkinter import filedialog as fd

def open_file():
    file_path = fd.askopenfilename(initialdir="~/home/jakub", filetypes=[('Image Files', '*')])
    if file_path is not None:
        pass

