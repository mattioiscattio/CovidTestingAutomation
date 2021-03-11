"""FizzBuzz Interview Question
Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

If the number is a multiple of 3 the output should be "Fizz".
If the number given is a multiple of 5, the output should be "Buzz".
If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
The output should always be a string even if it is not a multiple of 3 or 5.
Examples
fizz_buzz(3) ➞ "Fizz"

fizz_buzz(5) ➞ "Buzz"

fizz_buzz(15) ➞ "FizzBuzz"

fizz_buzz(4) ➞ "4"
Notes
Try to be precise with how you spell things and where you put the capital letters.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab."""

length = int(input("enter the number you want the loop to increment too."))
fizz = int(input("enter the number that x needs to be a multiple of to print fizz"))
buzz = int(input("enter the number that x needs to be a multiple of to print buzz"))

for i in range(length):
    i += 1
    if i%fizz == 0 and i%buzz == 0:
        print("fizzbuzz")
    elif i%fizz ==0:
        print("fizz")
    elif i%buzz ==0:
        print("buzz")
    else:
        print(i)



















