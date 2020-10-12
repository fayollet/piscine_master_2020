import sys

author = "courte_e"


def main():
    print(''.join((' ' + x) * (y + 1) for y, x in enumerate(sys.argv[1:]))[1:])


if __name__ == "__main__":
    main()
