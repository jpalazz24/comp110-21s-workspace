"""Utility functions for wrangling data."""

__author__ = "730242533"


from csv import DictReader
DATA_DIRECTORY="../../data"
DATA_FILE_PATH=f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_27.csv"



def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    # TODO 0.1) Complete the implementation of this function here.
    
    return rows

def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is the second parameter."""
    column_values: list[str] = []
    for row in table:
        column_values.append(row[column_name])
    return column_values

# TODO: Define the other functions here.

def columnar(dict_list: list[dict[str,str]]) -> dict[str, list[str]]:
    """Make a list of rows into a dictionary of columns."""
    dictionary: dict[str, list[str]] = {}
    for key in dict_list[0]:
        dictionary[key] = column_values(dict_list, key)
    return dictionary

def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a table with only the first N rows of data for each column."""
    new_table: dict[str, list[str]] = {}
    for column in table:
        values_list: list[str] = []
        i = 0
        while i < n:
            values_list.append(table[column][i])
            i += 1
        new_table[column] = values_list
    return new_table

def select(table: dict[str, list[str]], col_name: list[str]) -> dict[str, list[str]]:
    """Produce a new table with only a specific subset of the original columns."""
    new_table: dict[str, list[str]] = {}
    for name in col_name:
        new_table[name] = table[name] 
    return new_table

def count(values: list[str]) -> dict[str, int]:
    """Count the number of times a value is in a table."""
    count_dict: dict[str, int] = {}
    for item in values:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict