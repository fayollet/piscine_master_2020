#!/usr/bin/env python3
import os

author = "courte_e"


def main():
    d = dict(os.environ)
    print("\n".join([i[3:] + ': ' + d[i] for i in d if i[:3] == "MY_"]))


if __name__ == "__main__":
    main()
