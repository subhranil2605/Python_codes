"""
Matching Specific Repetitions with Braces
"""

import re
from re import Match, Pattern


if __name__ == "__main__":

    pattern1: Pattern = re.compile(r'(Ha){3}')  # (Ha)(Ha)(Ha)
    pattern2: Pattern = re.compile(r'(Ha){3,5}') # (Ha)(Ha)(Ha) | (Ha)(Ha)(Ha)(Ha) | (Ha)(Ha)(Ha)(Ha)(Ha)

    mo1: Match = pattern1.search("HaHaHa")
    mo2: Match = pattern2.search("HaHaHaHaHa")
    
    print(mo1.group())
    print(mo2.group())
