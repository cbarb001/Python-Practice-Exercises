# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
# Add on to the previous program by asking the user for another number
# and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)

# Main Project
name = input("What is your name? ")
age = int(input("How old are you? "))

until_one_hundred = (int(100) - age) + 2021

message = "Hi {0}, you will be 100 years old in {1}. ".format(name, until_one_hundred)

print(message)

print("*" * 20)

# Extra 1
copies_of_message = int(input("How many copies of this message would you like to see? "))

print(message * copies_of_message)

print("*" * 20)

# Extra 2
for x in range(copies_of_message):
    print(message)

