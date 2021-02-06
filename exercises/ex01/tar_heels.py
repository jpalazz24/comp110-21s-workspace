"""An exercise in remainders and boolean logic."""

__author__ = "730242533"


# Begin your solution here...
dividend: int = int(input("Enter an int: "))

if dividend % 2 != 0 and dividend % 7 != 0:
    print("CAROLINA")
else:
    if dividend % 2 == 0 and dividend % 7 == 0:
        print("TAR HEELS")
    else:
        if dividend % 2 == 0:
            print("TAR")
        else:
            print("HEELS")        
