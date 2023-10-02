"""
HW 4: Debugging and Lists

Q1 Debugging

Throughout this homework, whenever you encounter an error, we would like you to 
explain in a comment what it was and how you fixed it. You can write all these errors 
at any place in the file.

#Most of my errors were small errors where I made a syntax error or indentation.



Q2 List Slicing and Striding:

Part 1: Create a variable (name it anything you want but make it descriptive!) that 
is assigned to a list with the numbers 0 to 50. You should not have to write each 
number manually.
"""

# Q2 PART 1 
number_list = [i for i in range(51)]

"""
Part 2: Create a function that takes in a list and squares each element in the list.
"""

# Q2 PART 2 CODE HERE
def square_elements(input_list):
    squared_list = [x ** 2 for x in input_list]
    return squared_list

"""
Part 3: You are given two lists: listA and listB. listA contains the integers 1 through 
10 while listB contains the integers 20 through 30. Return a single, new list containing
only the odd integers of both lists in sorted order.
"""

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listB = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# Q2 PART 3 
combined_list = listA + listB
    
# Filter out the odd integers
odd_numbers = [x for x in combined_list if x % 2 != 0]
    
    # Sort the filtered list
sorted_odd_numbers = sorted(odd_numbers)

"""
Q3 2D Lists
Using nested for loops, create and print a 5x5 2D list with the odd numbers from 1 to 25.
"""

# Q3 PART 1 CODE HERE
list_2D = []
#Hint: Outer loop will manage row indices, inner loop will manage column indices (or vice 
# versa).
for i in range(5):
    row = []
    for j in range(5):
        odd_number = i * 5 + j * 2 + 1
        row.append(odd_number)
    list_2D.append(row)
for row in list_2D:
    print(row)

"""
Now with your completed list_2D, replace all multiples of 3 with '?' character and print
the resulting 2D list.
"""

# Q3 PART 2 
for i in range(5):
    for j in range(5):
        if list_2D[i][j] % 3 == 0:
            list_2D[i][j] = '?'
for row in list_2D:
    print(row)

#What conditional can you use to check if numbers are multiples?
# You can use if number % divisor == 0: to check if a number is divisble by the divisor
"""
Q4 More List Practice

Write a function that takes in a list and returns a copy of that list with duplicate 
values removed.
"""

def remove_duplicates(a):
    unique_list = []
    for item in a:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

#It may be helpful to create an array to test your function.
test = [40, 10, 80, 50, 20, 60, 30]

