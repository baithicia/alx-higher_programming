#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv[1:0]
    argv_count = len(sys.argv)
    index = 1
    if argv_count is 0:
        print("{:d} arguments.".format(argv_count))
    elif argv_count is 1:
            print("{:d} argument:".format(sys.argv_count))
            print("{:d}:{:s}".format(index, sys.argv[1]))
    else:
        print("{:d} arguments:".format(argv_count))
        while index <= argv_count:
            print("{:d}: {:s}".format(index, sys.argv[index]))
            index += 1
