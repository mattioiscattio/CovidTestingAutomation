import tkinter as tk
equationCreator = [[]]
inputTemp = ""
global x
x=0

def equationCompiler(num, equationCreator):#adds values from button presses to the list equation creator.
    global x
    print(str(equationCreator[-1]), num)
    if [] in equationCreator:
        x = equationCreator.index([])
    if str(num).isnumeric() == True or str(num) == ".":
        equationCreator[x].append(num)
    elif str(num) == "=":
        equationCompactor(equationCreator)
    else:
        if equationCreator[-1] == []:
            equationCreator[x].append(num)
            x+=1
            equationCreator.append([])
        else:
            x+=1
            equationCreator.append([num])
            x+=1
            equationCreator.append([])
    inputDisplay.configure(text=equationCreator)
    print(equationCreator)
def equationCompactor(equationCreator):#turns list of indexes with one value per index into lists of numbers and operators.
    a=0
    tempEquation = ""
    for i in equationCreator:
        if len(i) > 1:
            for x in equationCreator[a]:
                tempEquation += str(x)
                equationCreator[a] = [tempEquation]
        a+=1
        tempEquation = ""
    resultGenerator(equationCreator, "/")
    resultGenerator(equationCreator, "*")
    resultGenerator(equationCreator, "+")
    resultGenerator(equationCreator, "-")

def resultGenerator(equationCreator, operator):#performs the actual maths in the form of bidmas on the equation created in equation compactor/compiler.
    a = 0
    for i in equationCreator:
        if i == [operator]:
            if operator == "/":
                equationCreator[a][0] = float(equationCreator[a-1][0]) / float(equationCreator[a+1][0])#fix for float/0
            elif operator == "*":
                equationCreator[a][0] = float(equationCreator[a-1][0]) * float(equationCreator[a+1][0])
            elif operator == "+":
                equationCreator[a][0] = float(equationCreator[a-1][0]) + float(equationCreator[a+1][0])
            elif operator == "-":
                equationCreator[a][0] = float(equationCreator[a-1][0]) - float(equationCreator[a+1][0])
            equationCreator.pop(a-1)
            equationCreator.pop(a)
            resultGenerator(equationCreator, operator)
        a+=1
    inputDisplay.configure(text=equationCreator)

def equationReset(equationCreator):#algorithm for CE input, empties equation creator.
    equationCreator.clear()#inbuilt function to clear lists which apparently exists i did not spen 3 hours trying to work around lambda being bad at all pain.
    equationCreator.append([])#resets equationCreator to initial state, regardless of list contents.
    x=0#ensures that sync of equationCompilation behaves correctly.
    inputDisplay.configure(text="...")#resets text until next input.

window = tk.Tk()#defines window, window size(geomety) and button information/position.
window.geometry("300x700")
window.title("Simple Calculator")
inputDisplay = tk.Label(window, text = "...", cursor = "dot", bg="blue", fg="white", font=("Courier", 15))
inputDisplay.place(height=100, width=300, x=0, y=600)#.place needs to be seperate to allow editing of text in label, using.place immediately assigns value of none to inputdisplay so text cannot be edited.
button1 = tk.Button(window, text = "1", command = lambda: equationCompiler(1, equationCreator), cursor = "dot", fg = "white", bg = "red", font = ("Courier", 50)).place(height = 100, width = 100, x = 0, y = 0)#lambda needed as it is annonymous function, stops running on startup. try to use class in this section to compact and disable double operator inputs.
button2 = tk.Button(window, text = "2", command = lambda: equationCompiler(2, equationCreator), cursor = "dot", fg = "white", bg = "red", font = ("Courier", 50)).place(height = 100, width = 100, x = 100, y = 0)
button3 = tk.Button(window, text = "3", command = lambda: equationCompiler(3, equationCreator), cursor = "dot", fg = "white", bg = "red", font = ("Courier", 50)).place(height = 100, width = 100, x = 200, y = 0)
button4 = tk.Button(window, text = "4", command = lambda: equationCompiler(4, equationCreator), cursor = "dot", fg = "white", bg = "red", font = ("Courier", 50)).place(height = 100, width = 100, x = 0, y = 100)
button5 = tk.Button(window, text = "5", command = lambda: equationCompiler(5, equationCreator), cursor = "dot", fg = "white", bg = "red", font = ("Courier", 50)).place(height = 100, width = 100, x = 100, y = 100)
button6 = tk.Button(window, text = "6", command = lambda: equationCompiler(6, equationCreator), cursor = "dot", fg = "white", bg = "red", font = ("Courier", 50)).place(height = 100, width = 100, x = 200, y = 100)
button7 = tk.Button(window, text = "7", command = lambda: equationCompiler(7, equationCreator), cursor = "dot", fg = "white", bg = "red", font = ("Courier", 50)).place(height = 100, width = 100, x = 0, y = 200)
button8 = tk.Button(window, text = "8", command = lambda: equationCompiler(8, equationCreator), cursor = "dot", fg = "white", bg = "red", font = ("Courier", 50)).place(height = 100, width = 100, x = 100, y = 200)
button9 = tk.Button(window, text = "9", command = lambda: equationCompiler(9, equationCreator), cursor = "dot", fg = "white", bg = "red", font = ("Courier", 50)).place(height = 100, width = 100, x = 200, y = 200)
button0 = tk.Button(window, text = "0", command = lambda: equationCompiler(0, equationCreator), cursor = "dot", fg = "white", bg = "red", font = ("Courier", 50)).place(height = 100, width = 100, x = 0, y = 300)
buttonDot = tk.Button(window, text = ".", command = lambda: equationCompiler(".", equationCreator), cursor = "dot", fg = "white", bg = "red", font = ("Courier", 50)).place(height=100, width=100, x=100, y = 300)
buttonCe = tk.Button(window, text = "CE", command = lambda: equationReset(equationCreator), cursor = "dot", fg = "white", bg = "red", font = ("Courier", 50)).place(height = 100, width = 100, x = 200, y = 300)
buttonDivide = tk.Button(window, text = "/", command = lambda: equationCompiler("/", equationCreator), cursor = "dot", fg = "white", bg = "green", font = ("Courier", 50)).place(height = 100, width = 100, x=0, y = 400)
buttonMultiply = tk.Button(window, text = "*", command = lambda: equationCompiler("*", equationCreator), cursor = "dot", fg = "white", bg = "green", font = ("Courier", 50)).place(height = 100, width = 100, x = 100, y = 400)
buttonPi = tk.Button(window, text = "π", command = lambda: equationCompiler("π", equationCreator), cursor = "dot", fg = "white", bg = "green", font = ("Courier", 50)).place(height = 100, width = 100, x = 200, y =400)#create external pi class that can give pi value.
buttonMinus = tk.Button(window, text = "-", command = lambda: equationCompiler("-", equationCreator), cursor = "dot", fg = "white", bg = "green", font = ("Courier", 50)).place(height = 100, width = 100, x = 0, y = 500)
buttonPlus = tk.Button(window, text = "+", command = lambda: equationCompiler("+", equationCreator), cursor = "dot", fg = "white", bg = "green", font = ("Courier", 50)).place(height = 100, width = 100, x = 100, y = 500)
buttonEquals = tk.Button(window, text = "=", command = lambda: equationCompiler("=", equationCreator), cursor ="dot", fg = "white", bg = "black", font = ("Courier", 50)).place(height = 100, width = 100, x = 200, y = 500)

window.mainloop()#starts the program
