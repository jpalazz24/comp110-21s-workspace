"""EX03 - prime functions."""

__author__: str = "730242533"


def main() -> None:
    """Entrypoint of the program."""
    print(list_primes(3, 7))
    print(list_primes(10, 20))
    print(list_primes(25, 28))
    print(list_primes(-1, 5))
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))


def is_prime(number: int) -> bool:
    """A function determining if a number is prime or not."""
    i: int = 2
    answer: bool = True
    while i < number:
        if number % i != 0:
            i += 1
        else:
            answer = False
            i += 1   
    return answer


def list_primes(x: int, y: int) -> list[int]:
    """Function to return prime numbers between parameters."""
    list: list[int] = []
    while x < y:
        if x > 1 and is_prime(x) == True:
            list.append(x)
        x += 1
    return list


if __name__ == "__main__":
    main()