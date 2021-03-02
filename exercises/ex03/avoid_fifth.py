"""EX03 - avoid_fifth function."""

__author__: str = "730242533"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))
    # Put print statements here to test your function
    # ex. print(avoid_fifth("hello there"))


def avoid_fifth(word: str) -> str:
    """Function removing e's."""
    i: int = 0
    no_e: str = ""
    while i < len(word): 
        if word[i] != "e" and word[i] != "E":
                no_e += word[i]
        i += 1
    return no_e


if __name__ == "__main__":
    main()