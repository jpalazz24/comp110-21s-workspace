"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730252433"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    days_remaining: int = int(days_to_target(population, doses, doses_per_day, target))
    target_date: str = str(future_date(days_remaining))
    target_output: str = str("We will reach " + str(target) + "% vaccination in " + str(days_remaining))
    date_output: str = str(" days, which falls on " + target_date + ".")
    print(target_output + date_output)


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Calculation of days until target is reached."""
    return int(round((population * (target / 100) - (doses / 2)) / (doses_per_day / 2)))


# TODO 3: Define future_date function
def future_date(days_out: int) -> str:
    """Projected date function call."""
    today: datetime = datetime.today()
    days_until: timedelta = timedelta(days_out)
    date: datetime = today + days_until
    return date.strftime("%B %d, %Y")


if __name__ == "__main__":
    main()
