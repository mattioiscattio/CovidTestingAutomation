import tkinter as tk
class Calculator():
    def num1():
        print("test")

window = tk.Tk()
button1 = tk.Button(window, text="1", command = Calculator.num1())
button1.pack()
window.mainloop()
