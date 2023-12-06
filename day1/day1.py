#!/usr/bin/env python

"""
AOC 2023: DAY 1

Author: Jennifer Kadowaki
E-mail: jkadowaki@arizona.edu
Last Updated: 2023 Dec 06
"""

################################################################################

def extract_calibration(text:str) -> int:
    """
    Extracts the first and last digits in a string and returns value as a two 
    digit number.
    """

    # Stores the first & last digits of the string
    first_digit = None
    last_digit  = None

    for val in text:
        # Skip letters & proceed to next
        if not val.isdigit():
            continue

        # Store value if first digit is empty
        if not first_digit:
            first_digit = val

        # Reset last digit value
        last_digit  = val

    return int(first_digit + last_digit)


################################################################################

def process_words(text:str) -> str:
    """
    Processes line in input calibration document to replace numbers written
    as text as single digit values.
    """

    # Conversion Table ------  # Edge Cases
    numbers = { 'one'   : 1,   # onEight
                'two'   : 2,   # twOne
                'three' : 3,   # threEight
                'four'  : 4,
                'five'  : 5,   # fivEight
                'six'   : 6,
                'seven' : 7,   # seveNine
                'eight' : 8,   # eighTwo, eighThree
                'nine'  : 9 }  # ninEight

    # EDGE CASE HANDLING
    # All edge cases appear to overlap by their first and last letters only.
    # Replace numbers as text with their respective digit values with their
    #     first & last letters appended at the beginning and end of the digit. 
    conversion = dict({  key: key[0] + str(val) + key[-1] 
                         for key, val in numbers.items()  })

    # Text Processing
    for key, val in conversion.items():
        text = text.replace(key, val)
    
    return text


################################################################################

def sum_calibrations(input_doc, part1=True):

    sum = 0

    with open(input_doc, "r") as f:   
        for line in f:
            if not part1:
                line = process_words(line)
            sum += extract_calibration(line)
    print(sum)
     

################################################################################

if __name__ == '__main__':

    sum_calibrations('input.txt', part1=True)
    sum_calibrations('input.txt', part1=False)


