import tkinter as tk
window = tk.Tk()#defines the window

listBox1 = tk.Listbox(window)#options for listboxes go in this area, after window, not in the below lines.
listBox1.insert(1, "testData1")
listBox1.insert(2, "testData2")
print(listBox1.size())#prints the number of items in the listbox
listBox1.pack()
window.mainloop()
print(listBox1.curselection())




















