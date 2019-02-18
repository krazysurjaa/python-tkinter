#this will allow you to use jpg,png image format

from tkinter import *        
from PIL import ImageTk, Image
app_root = Tk()
#Setting it up
img = ImageTk.PhotoImage(Image.open("logo-python.jpg"))
#Displaying it
imglabel = Label(app_root, image=img).grid(row=1, column=1)        
app_root.mainloop()


