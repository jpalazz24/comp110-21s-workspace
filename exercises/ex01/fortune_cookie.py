"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730242533"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

your_fortune: int = randint(1, 100)

print("Your fortune cookie says...")

if your_fortune < 50:
    if your_fortune < 25:
        print("You will soon recieve good news.")
    else: 
        print("All of your dreams will soon be realized.")
else:
    if your_fortune < 75: 
        print("Your hard work will pay off, keep pushing.")
    else: 
        print("Everything you have been waiting for is just around the corner, be patient.")

print("Now, go spread positive vibes!")
