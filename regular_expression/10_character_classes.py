"""
Character Classes
"""

import re
from re import Match, Pattern


if __name__ == "__main__":

    """
    \d  => any numeric digit from 0 to 9
    \D  => any character that is not a numeric digit from 0 to 9
    \w  => any letter, numeric digit, underscore. "word" characters
    \W  => any character that is not a letter or numeric digit or underscore
    \s  => any space, tab or newline character
    \S  => any character that is not space or tab or newline

    [0-5] => numbers 0 to 5: similar to (0|1|2|3|4|5)
    """

    xmax_regex = re.compile(r'\d+\s\w+')

    mo = xmax_regex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, \
                       8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

    if mo: [print(m) for m in mo]


    
