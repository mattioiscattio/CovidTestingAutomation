import tkinter as tk


def entryInput(parameter):#the function requires a paramater to execute.
    try:
        print(float(entry1.get()))#if it can be a float, prints to terminal
    except ValueError:
        print("bad input")#otherwise prints bad input and waits for a good input.
        pass

window = tk.Tk()#defines window
label1 = tk.Label(window, text="enter int")#defines a label with text entry input
entry1 = tk.Entry(window)
entry1.bind("<Return>", entryInput)#when enter(return) is pressed the runs the entry input function.
label1.pack()
entry1.pack()
window.mainloop()
