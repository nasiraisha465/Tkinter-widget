from tkinter import *
from tkinter import messagebox
root = Tk()
root.geomrtry("200x200")
#function for displaying warning message
#this will be called once the button is clicked
#messagebox,showwarning("window Name", "Text to be displayed")
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")