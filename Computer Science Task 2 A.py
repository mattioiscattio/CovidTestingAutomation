minutes_worked = int(input("enter the number of minutes that you have worked today"))
hours_worked = minutes_worked // 60
excess_minutes_worked = minutes_worked % 60
if excess_minutes_worked == 0:
    bonus = 50
else:
    bonus = 0
print(hours_worked)
print(excess_minutes_worked)
if hours_worked <= 8:
    pay = round((minutes_worked/60) * 10, 2) + bonus

else:
    hours_worked -= 8
    pay = (hours_worked * 12) + 80 + ((excess_minutes_worked/60)*12) + bonus


print("today you have earned £", pay)