#!/usr/bin/env python3
'''
Author: Akawi Ifeanyi Courage <ifeanyi.akawi85@gmail.com>
This program prints greets a user with his/her given name. Cheers!
'''

import argparse


def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """ Where the actual program begins """

    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == "__main__":
    main()
