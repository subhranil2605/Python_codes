"""
Matching Multiple Groups with the Pipe
"""

import re
from re import Match, Pattern



if __name__ == "__main__":

    # match one of many expressions
    phone_num_regex: Pattern = re.compile(r'Sachin|Virat')

    # Find the matched expression from the string
    mo1: Match = phone_num_regex.search('One of India\'s best ever batsman is Sachin, but Virat is also a legend.')
    mo2: Match = phone_num_regex.search('Virat is a legend and so Sachin.')


    print(mo1.group())
    print(mo2.group())
