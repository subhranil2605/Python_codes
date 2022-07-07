import re

if __name__ == "__main__":
    
    # vowel
    vowel_regex = re.compile(r'[aeiouAEIOU]')

    vowels = vowel_regex.findall("My name is Subhranil Sarkar")

##    print(vowels)


    # letters and number
    my_pattern = re.compile(r'[a-zA-Z0-9]')

    mo = my_pattern.findall("Hello this will be selected but this is not :'/")

##    print(mo)
    
    

    # consonant
    consonant_regex = re.compile('[^aeiouAEIOU]')

    consonants = consonant_regex.findall("My name is Subhranil Sarkar")

    print(consonants)
