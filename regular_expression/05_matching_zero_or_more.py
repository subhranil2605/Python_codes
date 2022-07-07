"""
Matching Zero or More
"""

import re
from re import Match, Pattern


if __name__ == "__main__":

    pattern: Pattern = re.compile(r'Bat(wo)*man')

    mo1: Match = pattern.search('The Adventure of Batman.')
    mo2: Match = pattern.search('The Adventure of Batwoman.')
    mo3: Match = pattern.search('The Adventure of Batwowowowoman.')

    print(mo1.group())
    print(mo2.group())
    print(mo3.group())
