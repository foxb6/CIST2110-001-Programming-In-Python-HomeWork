# HW5.py
# Author: Bodhi Fox

# This homework assignment tests on list in python

# Question 1: Create a list with 5 of your favorite foods. Print the list

book_list= ["wot", 'malazan', 'licanius', 'hyperion', 'dune']
print(book_list)
# Question 2: Using the list from question 1, print the first and last element of the list

print(book_list[0])
print(book_list[-1])

# Question 3: Using the list from question 1, print the 3rd element of the list

print(book_list[-3])

# Question 4: Using the list from question 1, print the 1st through 3rd elements of the list using list slicing

print(book_list[0:3])

# Question 5: Using the list from question 1, print the last 2 elements of the list using list slicing

print(book_list[3:5])

# Question 6: Using the list from question 1, create a for each loop that prints each element of the list

for book in book_list:
    print(book)  

# Question 7: Using the list from question 1, create a for loop that prints each element of the list in reverse order

for book in reversed(book_list):
    print(book)


# Question 8: Using the list from question 1, create a for loop that prints each element of the list and its index (hint use the enumerate() function)

for index, book in enumerate(book_list):
    print(index,book)

# Question 9: Using this list of lists, print the first element of the second list (hint: use indexing)
list = [[1,2,3],[4,5,6],[7,8,9]]

element = list[1][0]

print(element)


# Question 10: Create a function that will take in a list and return the list in reverse order
# Hint: You can take in a list as a parameter and return a list

def revlist(my_list):
    return list(reversed(my_list))


