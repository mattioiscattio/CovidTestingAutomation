import tkinter as tk
window = tk.Tk()#defines the window

listBox1 = tk.Listbox(window) 
listBox1.insert(1, "testData1")
listBox1.insert(2, "testData2")



listBox1.pack()
window.mainloop()




















