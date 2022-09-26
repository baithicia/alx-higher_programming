#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    sum = 0
    arguments_number = len(sys.argv)
    arguments = str(sys.argv)
    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[i + 1])
    print (int("{:d}".format(sum)))



