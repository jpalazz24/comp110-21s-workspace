"""Example of elif."""
number: int = int(input("Pick a number: "))
answer: int = 50

# This for of nested else-if statement...
if number < answer:
    print("too low")
else:
    if number > answer:
        print("too high")
    else:
        print("you got it!")

# ...is the same as using elif in this way
if number < answer:
    print("too low")
elif number > answer:
    print("too high")
else:
    print("you got it")