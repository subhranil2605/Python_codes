
def length_validate(phone_number: str, type_number: str) -> bool:
    
    _valid_length = 0
    
    
    match type_number:
        case 'mob':
            _valid_length = 10
        case 'tel':
            _valid_length = 8
        case 'intl':
            _valid_length = 12

    return len(phone_number) is _valid_length


def phone_number_validate(phone_number: str, type_number: str) -> bool:
    return length_validate(phone_number, type_number) and phone_number.isnumeric()


def main():
    phone_number: str = "9474767880"
    type_number: str = 'mob'

    print("Valid Number") if phone_number_validate(phone_number, type_number) else print("Invalid Number")


if __name__ == "__main__":
    main()
