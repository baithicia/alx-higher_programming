#!/usr/bin/python3
""" Printing a square"""

class Square:
    """defines a square  with private attributes"""
    def __init__(self,size=0):  
        """initializes private attributes"""
        
    def area(self):
        """method for calculating area of a square object"""
        return  (self.__size * self.__size)

    @property
    def size(self):
        """getter method"""
        return self.__size 
    
    @size.setter
    def size(self, value):
        """setter method"""
        if type(value) != int:
            raise TypeError ("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end = '')
        if self.size ==0:
            print()
            
        



