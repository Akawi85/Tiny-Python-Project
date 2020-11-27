#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        help='Letter(s)',
                        nargs='+')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type= argparse.FileType('rt'),
                        default='./gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """The main program goes here"""

    args = get_args()

    # create an empty dictionary to hold the look table
    lookup = {}

    for line in args.file:  #  Iterate through each line of the args.file, which will be an open file handle.

        first_letter = line[0].upper()  # get the first letter in uppercase of each line in the opened file

        # use the first letter as the key of the dictionary
        lookup[first_letter] = line.rstrip()  # set the value of each key to each line void of any white spaces to the right 

          
    # Use a for loop to iterate over each letter in args.letter.
    for letter in args.letter:

        if letter.upper() in lookup: # Check if the letter is a key in lookup dictionary, using letter.upper() to disregard case.

            print(lookup[letter.upper()]) # If so, print the value of the dictionary which is the line of text from the lookup dictionary.

        else:

            print(f"I do not know '{letter.upper()}'.") # Otherwise, print a message saying the letter is unknown.

# --------------------------------------------------
if __name__ == '__main__':
    main()
