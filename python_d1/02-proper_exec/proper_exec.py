#!/usr/bin/env python3
import sys
import os
import subprocess

author = "courte_e"


def main():
    for c in os.environ.get('MY_CMD', '').split(','):
        proc = subprocess.Popen([c], stdout=subprocess.PIPE, shell=True)
        out = proc.communicate()[0].decode("utf-8")[:-1]
        print(str(out.upper()) if "--upper" in sys.argv[1:] else str(out))


if __name__ == "__main__":
    main()
