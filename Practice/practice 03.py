"""Random Things
Write 3 different versions of code to generate a random Boolean (True or False)."""
import random
#1
random_choices = [True, False]
print(random_choices[random.choice(random_choices)])
#2
random_number = random.randint(0,1)
print(random_choices[random_number])
#3
# Generate a random number between 0 and 1
random_num = random.random()

# Convert the number to a Boolean value
random_bool = bool(round(random_num))

print(random_bool)

"""
More Random Conrad
Replace the literal values for the constants at the top (like MAX_INCREASE) with randomly generated values (within sensible ranges)."""

"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

MAX_INCREASE = random.uniform(0.01,0.20)
MAX_DECREASE = random.uniform(0.01,0.10)
MIN_PRICE = 0.01
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
number_of_days = 1
out_file = open("Stock Tracker", 'w')

price = INITIAL_PRICE
print(f"On day {number_of_days} price is: ${price:,.2f}")

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)
    number_of_days += 1


    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}")

    out_file.write(f"On day {number_of_days} price is: ${price:,.2f} \n")

out_file.close()

"""
ASCII Table
Computers use ASCII to define a character-encoding scheme for letters, digits, and other characters. It is useful to become familiar with ASCII since that is how string comparisons are made.

Mr. Black the school teacher wants an educational program for his school students to explore the details of ASCII. He wants the app to allow a student to input a character and see the corresponding ASCII code, and vice versa. A sample run of the program should look like (where g and 100 are user inputs):"""