#!/usr/bin/env python3
import sys

__author__ = "courte_e"


def main():
    """ Print arg multiplied by the index of this arg """
    print(''.join((' ' + x) * (y + 1) for y, x in enumerate(sys.argv[1:]))[1:])


if __name__ == "__main__":
    main()
