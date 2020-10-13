import sys
from typing import List

author = "courte_e"


def return_arg(arg: List[str] = []):
    """ Find and parse arguments from a list """
    a = {"level": [True, 'INFO'], "stdout": [False, False],
         "file": [True, []], "message": [True, []]}
    i = 0
    while i < len(arg):
        if arg[i][2:] in a and a[arg[i][2:]][0]:
            if i + 1 >= len(arg):
                return 1
            if isinstance(a[arg[i][2:]][1], list):
                a[arg[i][2:]][1].append(arg[i + 1])
            else:
                a[arg[i][2:]][1] = arg[i + 1]
            i += 1
        elif arg[i][2:] in a:
            a[arg[i][2:]][1] = True
        else:
            a["message"][1].append(arg[i])
        i += 1
    return {k: v[1] for k, v in a.items()}


def main():
    """ Log into file and/or stderr and / or stdout a message """
    arg = return_arg(sys.argv[1:])
    if arg['level'] not in ['INFO', 'ERROR']:
        sys.stderr.write("unknown logging level")
        return 3
    arg['stdout'] = (sys.stdout if arg['stdout'] else sys.stderr).write
    m = ''.join([arg['level'] + ' - ' + j + '\n' for j in arg['message']])
    for i in arg['file']:
        try:
            f = open(i, 'w')
            f.write(m)
            f.close()
        except Exception:
            pass
    arg['stdout'](m)


if __name__ == "__main__":
    main()
