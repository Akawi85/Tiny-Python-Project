#!/usr/bin/env python3
"""
Author : Me <ifeanyi.akawi85@gmail.com>
Date   : 31-10-2020
Purpose: Let's encrypt the numbers. yay!!
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """The main program goes here"""

    args = get_args()
    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
              '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

    print(''.join([jumper.get(key, key) for key in args.text]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
