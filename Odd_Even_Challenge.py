# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and
# one number to divide by (check). If check divides evenly into num,
# tell that to the user. If not, print a different appropriate message.

# MAIN PROGRAM
num = int(input("Enter any number greater than 0 to check: "))


if num % 2 == 0:
    print("You chose an even number.")
else:
    print("You chose an odd number.")

# EXTRA 1
if num % 4 == 0:
    print("Your number is also divisible by 4.")

# EXTRA 2
check = int(input("Enter a new number to see if your first number is divisible by this new number. "))

if num % check == 0:
    print("{0} is divisible by {1} ".format(num, check))
else:
    print("{0} is NOT divisible by {1} ".format(num, check))
