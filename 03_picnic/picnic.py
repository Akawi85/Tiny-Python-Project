#!/usr/bin/env python3
"""
Author : Me <ifeanyi.akawi85@gmail.com>
Date   : 31-10-2020
Purpose: A list of food for picnic!
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        help='Item(s) to bring',
                        nargs='+')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='sort the items',
                        default=False)
    return parser.parse_args()


# --------------------------------------------------
def main():
    """The main program goes here"""

    args = get_args()
    items_arg = args.items
    num_items = len(items_arg)

    items_arg.sort() if args.sorted else items_arg

    items_in_picnic = str()
    if num_items == 1:
        items_in_picnic = items_arg[0]
    elif num_items == 2:
        items_in_picnic = ' and '.join(items_arg)
    elif num_items > 2:
        items_arg[-1] = 'and ' + items_arg[-1]
        items_in_picnic = ', '.join(items_arg)
    print(f'You are bringing {items_in_picnic}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
