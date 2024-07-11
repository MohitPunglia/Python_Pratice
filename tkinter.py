from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title('Login Form')

#root.iconbitmap('favicon.ico')

root.geometry('350x500')

root.configure(background='#CC7A68')

#img=ImageTK.PhotoImage(Image.open('android-chrome-512x512.png'))
img=ImageTk.PhotoImage(Image.open('python-gui-tkinter\android-chrome-512x512.png'))

img_label=Label(root,image=img)
img_label.pack()


root.mainloop()
