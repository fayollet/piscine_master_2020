#!/usr/bin/env python3
import sys
import os
import subprocess
import paramiko

__author__ = "courte_e"


def return_arg(arg=[]):
    """ Find and parse arguments from a list """
    return {arg[i]: arg[i + 1] for i in range(len(arg)) if arg[i][:2] == '--'}


def main():
    arg = return_arg(sys.argv[1:])
    arg['--password'] = os.environ.get(arg['--password'], '')
    for i in arg:
            if arg[i] == '':
                return 1
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(arg['--host'],
                   username=arg['--username'],
                   password=arg['--password'])
    [print(l.strip('\n')) for l in client.exec_command(arg['--command'])[1]]
    client.close()
    return 0


if __name__ == "__main__":
    main()
