#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nargs = len(sys.argv)
    args = nargs - 1
    add = 0
    if (args > 1):
        for i in range(1, args + 1):
            add = int(sys.argv[i]) + add
    print("{:d}".format(add))
