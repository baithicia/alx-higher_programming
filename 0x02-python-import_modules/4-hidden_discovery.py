#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for i in dir(hidden_4):
        if "__" not in i:
            print(i)
            for i in dir(hidden_4):
                name = [i.lower() for i in dir.split()]
                name.sort()
                for name in dir:
                    print(name, end = '')

   

