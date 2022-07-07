"""
Optional Matching 
"""

import re
from re import Match, Pattern


if __name__ == "__main__":

    # wo is the optional match
    pattern: Pattern = re.compile(r'Bat(wo)?man')

    mo1: Match = pattern.search('The Adventure of Batman.')
    mo2: Match = pattern.search('The Adventure of Batwoman.')

    print(mo1.group())
    print(mo2.group())
