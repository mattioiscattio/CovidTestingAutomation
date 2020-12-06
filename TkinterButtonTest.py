import tkinter as tk
from tkinter import messagebox
window = tk.Tk()

def popUp():
    messagebox.showinfo("PUP Title Test", "PUP Contents Test")

Button = tk.Button(window, text = "ButtonText", command = popUp)

Button.pack()
window.mainloop()
