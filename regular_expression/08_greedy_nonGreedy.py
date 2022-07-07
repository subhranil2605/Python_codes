"""
Greedy and Non-Greedy Method
"""

import re
from re import Match, Pattern


if __name__ == "__main__":

    gready_regex: Pattern = re.compile(r'(Ha){3,5}')
    mo1: Match = gready_regex.search("HaHaHaHaHa")
    print(mo1.group())

    
    non_gready_regex: Pattern = re.compile(r'(Ha){3,5}?')     
    mo2: Match = non_gready_regex.search("HaHaHaHaHa")
    print(mo2.group())
