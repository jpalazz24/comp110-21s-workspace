"""A vaccination calculator."""

__author__ = "730242533"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

population: int = int(input("Population: "))
doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
vacc_target: int = int(input("Target percent vaccinated: "))

days_remaining: int = int(round((population * (vacc_target / 100) - (doses_administered / 2)) / (doses_per_day / 2)))
days_until: timedelta = timedelta(days_remaining)

today: datetime = datetime.today()
target_date: datetime = today + days_until

target_output: str = "We will reach " + str(vacc_target) + "% vaccination in "
date_output: str = str(days_remaining) + " days, which falls on " + target_date.strftime("%B %d, %Y") + "."

print(str(target_output + date_output))
