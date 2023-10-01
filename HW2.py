# HW2.py
# Author:


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:

age=input('Enter your age: ')

# If the age is less than 13, print "You are a child."
age=int(age)
if age > 20:
    print("You are an adult.")
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


sum_of_numbers = 0
min_number = None
max_number = None


for i in range(10):
    number = float(input("Enter a number: "))
    sum_of_numbers += number

    
    if min_number is None or number < min_number:
        min_number = number
    if max_number is None or number > max_number:
        max_number = number


average = sum_of_numbers / 10


print("Sum of the numbers:", sum_of_numbers)
print("Average of the numbers:", average)
print("Minimum number:", min_number)
print("Maximum number:", max_number)


# The highest number.
# The lowest number.
# The average of all the numbers.

# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i, o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement

vowel_count = 0
user_input = input("Enter a string: ")
user_input = user_input.lower()
for count in user_input:
    if count in "aeiou":
        vowel_count += 1
print("Number of vowels:", vowel_count)