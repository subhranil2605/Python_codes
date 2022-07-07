"""
Grouping with Parentheses
"""

import re
from re import Match, Pattern



if __name__ == "__main__":

    # adding parentheses will create groups
    phone_num_regex: Pattern = re.compile(r"(\(\d{3}\))-(\d{3}-\d{4})")

    # finding phone number from a string using search() method that returns the Match object
    mo: Match = phone_num_regex.search('My number is (415)-555-4242')

    # print all the groups together
    print(mo.group(0))
    print(mo.group())

    # first group of the matched string
    print(mo.group(1))

    # second group of the matched string
    print(mo.group(2))

    # all the groups at once
    print(mo.groups())
