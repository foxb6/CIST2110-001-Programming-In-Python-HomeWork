# HW2.py
# Author:


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:

age=input('Enter your age: ')

# If the age is less than 13, print "You are a child."
age=int(age)
if age > 20:
    print("You are an afult.")
elif age < 13:
    print("You are a child.")
else:
    print("You are a teenager.")

# If the age is between 13 and 19, print "You are a teenager."
# If the age is 20 or older, print "You are an adult."


# Question 2:
# Write some code to display the following pattern using a for or while loop:
# 1
# 12
# 123
# 1234
# 12345
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()



# Question 3:
# Write a Python program that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:

num1=float(input('Enter a number: '))
num2=float(input('Enter a number: '))
num3=float(input('Enter a number: '))
num4=float(input('Enter a number: '))
num5=float(input('Enter a number: '))
num6=float(input('Enter a number: '))
num7=float(input('Enter a number: '))
num8=float(input('Enter a number: '))
num9=float(input('Enter a number: '))
num10=float(input('Enter a number: '))




# The highest number.
# The lowest number.
# The average of all the numbers.

# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i, o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement

