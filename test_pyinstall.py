# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 09:55:22 2020

@author: David
"""

from tkinter.filedialog import askopenfilenames, askdirectory
from tkinter import Tk

root = Tk()
root.lift()
root.attributes("-topmost",True)
root.withdraw()
root.title("The Title Of the Box")

files = askopenfilenames(parent=root,
                         initialdir = "../Py_Input/")
root.destroy()