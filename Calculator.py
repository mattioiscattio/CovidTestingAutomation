import sys
class Calculator():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    def addition(self):
        print(self.var1 + self.var2)
    def subtraction(self):
        print(self.var1 - self.var2)
    def division(self):
        print(self.var1/self.var2)
    def multiplication(self):
        print(self.var1*self.var2)

def application():
    input1 = int(input("enter first input"))
    input2 = int(input("enter second input"))
    inputs = Calculator(input1, input2)

    selection = input("enter add/subtract/divide/multiply to choose operand")
    while selection.upper() != "ADD" and selection.upper() != "SUBTRACT" and selection.upper() != "DIVIDE" and selection.upper() != "MULTIPLY":
        print(selection.upper())
        selection = input("incorrect input, enter add/subtract/divide/multiply to choose operand")
    if selection.upper() == "ADD":
        inputs.addition()
    elif selection.upper() == "SUBTRACT":
        inputs.subtraction()
    elif selection.upper() == "DIVIDE":
        inputs.division()
    elif selection.upper() == "MULTIPLY":
        inputs.multiplication()

    replay = input("play again? yes or no")
    while replay.upper() != "YES" and replay.upper() != "NO":
        replay = input("incorrect input, play again? yes or no")
    if replay.upper() == "YES":
        application()
    else:
        print("closing application")
        sys.exit()

application()

































