#!/usr/bin/env python3
"""
Author : Me <ifeanyi.akawi85@gmail.com>
Date   : 11-12-2020
Purpose: Spit some Curses!
"""

import argparse
import random

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Heap abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='adjectives',
                        type=int,
                        default= 2)

    parser.add_argument('-n',
                        '--number',
                        help='Number of insults',
                        metavar='insults',
                        type=int,
                        default= 3)

    parser.add_argument('-s',
                        '--seed',
                        metavar= 'seed',
                        help='Random seed',
                        default= None,
                        type= int)

    # Get the result of parsing the command-line arguments. The argparse module will handle errors such as non-integer values.
    args = parser.parse_args()

    # ensure that the argument's values are positive integers
    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    elif args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    # At this point, all the user’s arguments have been validated, so return the arguments to the caller.
    return args


# --------------------------------------------------
def main():
    """The main program goes here"""

    # call the get_args() function
    args = get_args()
    
    # set the seed to the default value in the seed argument which is None, so if user specifies a seed it is captured instead of default
    # this ensures uniformity in all outputs across all machines
    random.seed(args.seed)

    # define the adjectives to output and split them on spaces 
    adjectives = """
                bankrupt base caterwauling corrupt cullionly detestable dishonest false filthsome filthy
                foolish foul gross heedless indistinguishable infected insatiate irksome lascivious
                lecherous loathsome lubbery old peevish rascaly rotten ruinous scurilous scurvy slanderous
                sodden-witted thin-faced toad-spotted unmannered vile wall-eyed
                """.split()

    # define the nouns to output and spilt them on spaces
    nouns = """
            Judas Satan ape ass barbermonger beggar block boy braggart butt carbuncle coward
            coxcomb cur dandy degenerate fiend fishmonger fool gull harpy jack jolthead knave liar
            lunatic maw milksop minion ratcatcher recreant rogue scold slave swine traitor varlet
            villain worm
            """.split()

    # for each iteration in the number of lines specified
    for _ in range(args.number):
        
        # get the adjectives that has been splitted to a list of strings
        # get the number of adjectives to be on each line using the 'args.adjectives'
        # pass both to the random.sample module which selects a sample of values given the numer passed to k argument
        # convert the obect returned to a string seperated by comma and a white space
        adj = ', '.join(random.sample(adjectives, k = args.adjectives))

        # get the nouns which have been splitted to a list of strings
        # pass the nouns to the random.choice module which selects just one value from a list of values
        noun = random.choice(nouns)

        # print the selected adjectives and the selected noun together with "You" and "!"
        print(f"You {adj} {noun}!")
        
# --------------------------------------------------
if __name__ == '__main__':
    main()
