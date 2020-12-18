#!/usr/bin/env python3
"""
Author : Me <ifeanyi.akawi85@gmail.com>
Date   : 18-12-2020
Purpose: I am Mutant!!!
"""

import argparse
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    # check if the input text is a file and open if it is
    if os.path.isfile(args.text):
        args.text = open(args.text).read().strip()

    # ensure that the mutations are between 0 and 1
    if args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    elif args.mutations < 0:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """The main program gies here"""

    args = get_args()
    random.seed(args.seed)

    # get the string modules for lower case letters and punctuations which are values we'll use for replacing the input text or file
    # this needs to be sorted so that the values are consisted
    # sorting converts it to a list so we chnage it to a string using the string join method
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))

    # get the length of the text argument
    len_text = len(args.text)

    # get the number texts that should be mutated for each input text or file
    # multiply the length of the input file by he mutations argument (which ranges between 0 and 1)
    # this could return a float so the value returned is rounded to the nearest integer
    num_mutations = round(len_text * args.mutations)

    # create a new variable that converts the text argument to a list 
    new_text = list(args.text)

    # i returns an integer which determines the number of texts that will be altered
    # the integers are used to represent the position of strings in the text or file
    for i in random.sample(range(len_text), num_mutations):
        ''' 
        for each i integer returned by the loop,
        in the alpha string, replace the string in the ith position of the new_text list with nothing.
        select the string using the random.choice method.
        assign the alpha string to the new_text list
        '''
        new_text[i] = random.choice(alpha.replace(new_text[i], ''))

    # convert the new_text list back to a list and return
    print('You said: "{}"\nI heard : "{}"'.format(args.text, ''.join(new_text)))

    
# --------------------------------------------------
if __name__ == '__main__':
    main()
