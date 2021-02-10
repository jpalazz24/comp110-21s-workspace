"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730242533"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    your_fortune: int = randint(1, 100)
    if your_fortune < 50:
        if your_fortune < 25:
            return "You will soon recieve good news."
        else:
            return "All of your dreams will soon be realized."
    else:
        if your_fortune < 75:
            return "Your hard work will pay off, keep pushing."
        else:
            return "Everything you have been waiting for is just around the corner, be patient."

 
# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
