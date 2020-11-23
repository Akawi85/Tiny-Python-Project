#!/usr/bin/env python3
"""
Author : Me <ifeanyi.akawi85@gmail.com>
Date   : 23-11-2020
Purpose: Let me Howler at you!!
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    """
    The text argument is a string
    that may be the name of a file.
    """
    parser.add_argument('text',
                        type=str,
                        help='Input string or file',
                        metavar='text')

    """
    The --outfile option is also
    a string that names a file.
    """
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        default='')
    """
    Parse the command-line arguments
    into the variable args so that we can
    manually check the text argument.
    """
    args = parser.parse_args()

    """
    Check if args.text is the
    name of an existing file.
    """
    if os.path.isfile(args.text): # check if the text argument is a file
        args.text = open(args.text).read().rstrip() # If so, open it, read its contents and strip it of any excess spaces, then assign it back to args.text
    
    return args # Return the arguments to the caller.

# --------------------------------------------------
def main():
    """The main program goes here"""
    args = get_args() # Call get_args () to get the arguments to the program

    """
    if the user specifies the optional outfile argument,
    use the open function to check if the string he passed to the option is a file,
    if it is a file, open it and make the file a writeable text file,
    if it isn't a file, the open function makes a new file with the string as its name and also make it a writeable text file.
    Else, if the user doesn't specify the optional outfile argument, return a standard output.
    Assign if clauses to the out_fh variable

    write the contents of the required args.text argument in upper case to out_fh
    close the file handle
    """
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout 
    out_fh.write(args.text.upper() + '\n')
    out_fh.close()

# --------------------------------------------------
if __name__ == '__main__':
    main()
