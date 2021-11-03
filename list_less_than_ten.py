# Take a list, say for example this one:

#     a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# 1. Instead of printing the elements one by one,
# make a new list that has all the elements less than 5 from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only elements
# from the original list a that are smaller than that number given by the user.

# MAIN PROBLEM

a = [10, 50, 82, 1, 5, 92, 4, 2, 7]
new_list = []

for number in a:
    if number < 5:
        print(number)
        new_list.append(number)

# Extra 1
print(new_list)

# Extra 3
new_list = []
lower_than_number = int(input("Enter your own number to check if there are any numbers that are lower in the list. "))

for number in a:
    if number < lower_than_number:
        new_list.append(number)
print(new_list)
