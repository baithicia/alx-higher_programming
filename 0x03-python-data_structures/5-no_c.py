#!/usr/bin/python3
def no_c(my_string):
    string = ''
    for letter in my_string[:]:
        if letter != 'c' and letter != 'C':
            string.append("letter")
    return ''.join(string)
