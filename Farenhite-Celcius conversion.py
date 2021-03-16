file = open("Daily_Temps.txt","w+")
loopNum = int(input("enter the number of days you want to input for"))
mode = str(input("enter C to input celcius or F to input farenhiet"))
def C_to_F(temp):
    return((temp*9/5) + 32)
def F_to_C(temp):
    return((temp - 32) * 5/9)
for day in range(loopNum):
    temp = int(input("enter the temperature on this day"))
    date = input("enter the date that correlates with that temperature in the format dd/mm/yyyy")
    if mode.upper() == "C":
        temp = C_to_F(temp)
    elif mode.upper() == "F":
        temp = F_to_C(temp)
    write = str(temp)+" : "+str(date) + "\n"
    file.write(write)
file.close()
#formula for conversion from F to C (32°F − 32) × 5/9 = 0°C
#formula for conversion from C to F (0°C × 9/5) + 32 = 32°F