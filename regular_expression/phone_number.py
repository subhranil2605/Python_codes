import re
from re import Pattern, Match


def phone_number_validator(number: str) -> str:
    """
    Phone number validator function,
    which checks if the phone number is of 10 numerical digits.
    """
    
    # pattern of the phone number
    # making the RegEx object
    pattern: Pattern = re.compile(r'\d{10}')

    # length of the number should be 10 or, it will raise an error!
    assert len(my_number) == 10, "Phone number should be of length 10!" 

    # find the phone number pattern from the string
    mo: Match = pattern.search(my_number)

    return f"Phone number is valid: {mo.group()}" if mo else "Invalid phone number!"



if __name__ == "__main__":
    my_number: str = "6294769160"

    print(phone_number_validator(my_number))
