# Create a program that asks the user for a number
# and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

guess = int(input("Please pick a number greater than 0: "))
divisor = None

for number in range(1, guess + 1):
    if guess % number == 0:
        print(number)