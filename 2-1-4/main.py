#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk
from tkinter import font
# main window
root = tk.Tk()
root.wm_geometry("500x200")

#create empty frame
frame_login = tk.Frame(root)
frame_auth = tk.Frame(root)

frame_login.grid(row="0", column="0", sticky = "news")
frame_auth.grid(row="0", column="0", sticky = "news")


def login():
    frame_auth.tkraise()




custom_font = font.Font(family="Times New Roman", size=20)

#Username Label
lbl_username = tk.Label(frame_login, text="Username", font=custom_font)
lbl_username.pack(padx=50)

#Text Box For Username
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack()

#Password Setup
lbl_password = tk.Label(frame_login, text="Password", font=custom_font)
lbl_password.pack(padx=50)

#Text Box For Password
ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack()

#login button
button_login = tk.Button(frame_login, text="Login", font=custom_font, command=login)
button_login.pack(padx=10)
#Auth Frame Label
lbl_authorized = tk.Label(frame_auth, text="Authentication Screen", font=custom_font)
lbl_authorized.pack(padx=50)

frame_login.tkraise()
root.mainloop()