import tkinter as tk
from tkinter import messagebox
window = tk.Tk()

def popUp():
    messagebox.showinfo("PUP Title Test", "PUP Contents Test")
    print("test")

Button = tk.Button(window, text = "ButtonText", command = popUp, fg="blue", bg="green")

Button.pack()
window.mainloop()
