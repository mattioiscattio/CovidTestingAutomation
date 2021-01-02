import tkinter as tk


def entryInput(entryNum):#the function requires a paramater to execute.
    try:
        print(float(entry1.get()))#if it can be a float, prints to terminal
        print(float(entry2.get()))
    except ValueError:
        print("bad input")#otherwise prints bad input and waits for a good input.
        pass

x = "entry1"
window = tk.Tk()#defines window
window.title("testing window")#gives the window a title
label1 = tk.Label(window, text="enter int")#defines a label with text entry input
label2 = tk.Label(window, text="enter second input")
entry1 = tk.Entry(window)#
entry2 = tk.Entry(window)
entry1.bind("<Return>", entryInput)#when enter(return) is pressed the runs the entry input function.
entry2.bind("<Return>", entryInput)
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
window.mainloop()
