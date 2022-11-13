#!/usr/bin/python3
"""calculates area of a square"""

class Square:
    """defines a square  with private attributes"""
    def __init__(self,size=0):  
        """initializes private attributes"""
        if type(size) != int:
            raise TypeError ("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
    def area(self):
        """method for calculating area of a square object"""
        return  (self.__size * self.__size)


