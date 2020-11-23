#!/usr/bin/env python3
"""
Author : Me <ifeanyi.akawi85@gmail.com>
Date   : 23-11-2020
Purpose: Let me Howler at you!!
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs="*",
                        type= argparse.FileType('rt'),
                        default= [sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """The main program goes here"""

    args = get_args() # call the get_args function

    total_lines, total_bytes, total_words = 0, 0, 0 # These are the variables for the “total” line, if I need them.
    """
    Iterate through the list of
    arg.file inputs. I use the
    variable fh to remind me
    that these are open file
    handles, even STDIN.
    """
    for fh in args.file:
        num_lines, num_words, num_bytes = 0, 0, 0  # Initialize variables to count the lines, words, and bytes for each of this file.
        for line in fh: # Iterate through each line of the file handle.
            num_lines += 1 # For each line, increment the number of lines by 1.
            num_bytes += len(line) # The number of bytes is incremented by the length of the line.
            num_words += len(line.split()) # To get the number of words, we can call line.split() to break the line on whitespace. The length of that list is added to the count of words.
        
        total_bytes += num_bytes
        total_lines += num_lines
        total_words += num_words

        print(f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}') # Print the counts for this file using the {:8} option to print in a field 8 characters wide followed by a single space and then the name of the file.

    if len(args.file) > 1:
        print(f"{total_lines:8}{total_words:8}{total_bytes:8} total") # Check if we had more than 1 input. Print the “total” line.

# --------------------------------------------------
if __name__ == '__main__':
    main()
