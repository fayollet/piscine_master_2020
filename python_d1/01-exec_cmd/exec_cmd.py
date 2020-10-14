#!/usr/bin/env python3
import os

__author__ = "courte_e"


def main():
    os.system(os.environ.get('MY_CMD', ''))

if __name__ == "__main__":
    main()
