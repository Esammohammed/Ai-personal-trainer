
import os
import tkinter
from tkinter import filedialog
root = tkinter.Tk()
root.withdraw()
file = filedialog.askopenfile(mode='r', filetypes=[("All files", "*")])
if file:
    filepath = os.path.abspath(file.name)
    print (filepath)

