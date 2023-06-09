#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nargs = len(sys.argv)
    args = nargs - 1
    if (args == 0):
        print("{:d} arguments.".format(args))
    else:
        print("{:d} {:s}:".format(args,
              "argument" if args == 1 else "arguments"))
        for i in range(1, args + 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))
