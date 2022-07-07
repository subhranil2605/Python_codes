"""
Wildcard
"""

import re
from re import Match, Pattern


if __name__ == "__main__":

    # . match any character except newline
    pattern: Pattern = re.compile(r'.at')  

    mo = pattern.findall("The cat in the hat sat on the flat mat.")

    print(mo) if mo else print("The pattern does not exist!")

    

    # matching everything
    name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
    mo = name_regex.search('First Name: Subhranil Last Name: Sarkar')

    print(mo.group(1))
    print(mo.group(2))
