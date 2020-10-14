#!/usr/bin/env python3
import sys

__author__ = "courte_e"


def main():
    """ Open and read file according to multiple arguments """
    file = [x for x in sys.argv[1:] if x[:2] != '--']
    arg = [x[2:] for x in sys.argv[1:] if x not in file]
    if 'lower' in arg and 'upper' in arg:
        return 1
    f = []
    c = []
    for i in file:
        try:
            f.append([i, open(i)])
        except Exception:
            if 'strict' in arg:
                c.append(file)
    if len(c) > 0:
        print("could not read the following files:", ', '.join(c))
        [p[1].close() for p in f]
        return 1
    for p in f:
        if 'verbose' in arg:
            print("# processing file", '.'.join(p[0].split('.')[:-1]))
        text = p[1].read()
        text = text.lower() if 'lower' in arg else text
        text = text.upper() if 'upper' in arg else text
        print(text)
        p[1].close()


if __name__ == "__main__":
    main()
