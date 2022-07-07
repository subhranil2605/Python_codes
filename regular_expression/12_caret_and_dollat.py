"""
Caret and Dollar
"""

import re
from re import Match, Pattern


if __name__ == "__main__":

    # ^ means the match must be at the beginning
    pattern: Pattern = re.compile(r'^Hello')  

    mo = pattern.search("Hello this is mine")

    print(mo.group()) if mo else print("The pattern is not at the beginning!!!!")

    
    # $ means the match must be at the end
    pattern: Pattern = re.compile(r'\d$')  

    mo = pattern.search("Hello this is mine for years 3")

    print(mo.group()) if mo else print("The pattern is not at the end!!!!")


    # mixed
    pattern: Pattern = re.compile(r'^\d+$')  

    mo = pattern.search("35151")

    print(mo.group()) if mo else print("The pattern not exists !!!!")
