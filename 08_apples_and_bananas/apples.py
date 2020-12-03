#!/usr/bin/env python3
"""
Author : Me <ifeanyi.akawi85@gmail.com>
Date   : 3-12-2020
Purpose: Find and replace!
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file',
                        )

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  # ensure the user's input for this argument is one of the vowels
                        )

    args =  parser.parse_args()

    if os.path.isfile(args.text): # Check if the text argument is a file.
        args.text = open(args.text).read().rstrip() # If it is, read the file using str.rstrip() to remove any trailing whitespace.

    return args


# --------------------------------------------------
def main():
    """The main program goes here"""
    args = get_args()
    vowel = args.vowel

    # create a function that returns a new character
    def new_char(char):
        # return the optional vowel argument in lowercase if the specified character is among the lowercase vowel letters,
        # or return the optional vowel argument in uppercase if the character is among the uppercase vowel letters,
        # or return the character itself if the character is not among the vowel letters 
        return vowel if char in 'aeiou' else vowel.upper() if char in 'AEIOU' else char

    # apply the function for every input character in the text argument
    text = ''.join([new_char(char) for char in args.text])

    print(text)

# --------------------------------------------------
if __name__ == '__main__':
    main()
