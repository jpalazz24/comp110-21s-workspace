"""EX03 - palindromify function."""

__author__: str = "730242533"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))


def palindromify(word: str, length: bool) -> str:
    """Function to make a word a palindrome."""
    i: int = 0
    palindrome: str = ""
    last_letter: int = 1
    while i < len(word):
        if length:
            palindrome += word[len(word) - last_letter]
        else:
            while i < (len(word) - 1):
                palindrome += word[len(word) - (last_letter + 1)]
                last_letter += 1
                i += 1
        last_letter += 1
        i += 1
    return word + palindrome
            

if __name__ == "__main__":
    main()