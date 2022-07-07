"""
Findall
"""

import re
from re import Match, Pattern


if __name__ == "__main__":

    pattern: Pattern = re.compile(r'(\+91)?(-)?(\d{10})')  

    mo: list = pattern.findall("1234567890 and +911234567890 and +91-1234567890")

    
    for phone_number in mo:
        s = ""
        for i in phone_number:
            s += i
        print(s)


