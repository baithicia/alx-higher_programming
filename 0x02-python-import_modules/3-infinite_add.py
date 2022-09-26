#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    sum = 0
    print("number of arguments:", len(sys.argv))
    for i in range(1, len(sys.argv)):
        sum = sum + int(sys.argv[1])
    print (sum)


