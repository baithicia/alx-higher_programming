#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for i in dir(hidden_4):
        if "__" not in i:
            print(i)
    my_str = input("i")
    names = [name.lower() for name in my_str.split()]
    names.sort()
    print("The sorted words are:")
    for name in names:
        print(name)
        

