# HW1.py
# Author:

# Question 1:
# Print Hello World like we did in class

print('Hello World')

# Question 2:
# Print the following:
# Your name

print('Bodhi Fox')

# Your age

print('22')

# Your favorite color

print('Azure')

# Your favorite animal

print('Orca')

# Question 3:
# Create a variable called "myName" and set it equal to your name

myName='Bodhi Fox'

# Create a variable called "myAge" and set it equal to your age

myAge='22'

# Create a variable called "myColor" and set it equal to your favorite color

myColor='Azure'

# Create a variable called "myAnimal" and set it equal to your favorite animal

myAnimal='Orca'

# Print the following:
# Hello, my name is <myName>
# I am <myAge> years old
# My favorite color is <myColor>
# My favorite animal is <myAnimal>

print("Hello, my name is " + myName + ". I am " + myAge + " years old. My favorite color is " + myColor + " and my favorite animal is " + myAnimal + ".")


# Question 4:
# Calculate the following and print the result:
# 2 + 2

print((2+2))

# 3 * 4
print((3*4))


# 5 - 6

print((5-6))

# 8 / 2

print((8/2))

# Question 5:
# Create a variable called "num1" and set it equal to 2

num1=2

# Create a variable called "num2" and set it equal to 3

num2=3

# Create a variable called "num3" and set it equal to 4

num3=4

# Create a variable called "num4" and set it equal to 5

num4=5

# Calculate the following and print the result:
# num1 + num2

print((num1+num2))

# num3 * num4

print((num3*num4))

# num4 - num1

print((num4-num1))

# num2 / num1

print((num2/num1))

# Question 6: Write a program that asks the user for their name and then prints the following:

# Hello, <name>. Please enter three numbers.

name = input("Enter your name: ")
print("Hello, "+ name+". Please enter three numbers.")

# The program should then ask the user for three numbers (floats) and print the following:

num2_1 = float(input("Enter the first number: "))
num2_2 = float(input("Enter the second number: "))
num2_3 = float(input("Enter the third number: "))

# 1. The sum of the three numbers is <sum>

print("The sum of the three numbers is", ((num2_1+num2_2+num2_3)))

# 2. The product of the three numbers is <product>

print("The product of the three numbers is", ((num2_1*num2_2*num2_3)))

## 3. round the three numbers to the nearest integer and print the sum of the three rounded numbers divided by 3 

num2_1_rnd=round(num2_1,3)
num2_2_rnd=round(num2_2,3)
num2_3_rnd=round(num2_3,3)

print(((num2_1_rnd+num2_2_rnd+num2_3_rnd)/3))

# 4. The average of the three numbers is <average>

print("The average of the three numbers is", ((num2_1_rnd+num2_2_rnd+num2_3_rnd)/3))

# Question 7: Ask the user for an input of a symbol (in the example its *)

sym=input("Input a symbol: ")

# Print a diamond of the symbol that looks like the following. Include the spaces and the | character. 
# Hint: the print("symbol", end="") with \t and \n characters will be useful here.

#    *     |
#   ***    |
#  *****   |
# *******  |
#  *****   |
#   ***    |
#    *     |

sym = input("Input a symbol: ")


print("    " + sym + "    |")
print("   " + sym * 3 + "   |")
print("  " + sym * 5 + "  |")
print(" " + sym * 7 + " |")
print("  " + sym * 5 + "  |")
print("   " + sym * 3 + "   |")
print("    " + sym + "    |")