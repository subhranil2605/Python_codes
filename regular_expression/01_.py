import re
from re import Match, Pattern



if __name__ == "__main__":

    # creating the regex object / Pattern
    phone_num_regex: Pattern = re.compile(r"\d{3}-\d{3}-\d{4}")

    # finding phone number from a string using search() method that returns the Match object
    mo: Match = phone_num_regex.search('My number is 415-555-4242')

    # group method returns the actual matched string
    print(mo.group())

