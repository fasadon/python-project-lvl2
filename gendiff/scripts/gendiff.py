#!/usr/bin/env python3
"""Main program gendiff."""
import argparse

from gendiff.generate_diff import generate_diff
from gendiff.stylish import stylish


def main():
    """Interface gendiff."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()        
    stylish(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
