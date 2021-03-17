import pprint
import re
user_list = {}
iteration_num = int(input("enter the number of users data that you want to enter into the system"))

def dictionary_creation():
    name = str(input("please enter your first name"))
    surname = str(input("pleaes enter your surname"))
    age = int(input("please enter your age"))
    password = input("enter a password, it must begin with z and contain no numbers")
    if password[0].upper() == "Z" and len(password) == 6 and bool(re.search(r'\d', password)) == False:
        user_list[name] = "surname is: " + surname , "age is: " + str(age) , "username is: " + surname[0:2] + name[-1] + str(age), "password is: " + password
for iteration_num in range(iteration_num):
    dictionary_creation()

pprint.pprint(user_list)