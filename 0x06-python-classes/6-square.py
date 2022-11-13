#!/usr/bin/python3
""" Printing a square"""

class Square:
    """defines a square  with private attributes"""
    def __init__(self,size=0, position =(0,0)):  
        """initializes private attributes"""
        self.size = size
        self.position = position
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
    @property
    def position(self):
        """getter method"""
        return self.__position
    @position.setter
    def position(self, value):
        if len(value) !=2:
            raise TypeError("Value must be a tuple of two positive integers")
        if (type(value[0]) is not int or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[1]) is not int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    def my_print(self):
        """Print method"""
        if (self.size == 0):
            print()
        else:
            for i in range(self.position[1]):
                print()
            for j in range(0, self.size):
                for e in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()




            
        



