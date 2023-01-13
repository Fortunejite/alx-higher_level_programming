#!/usr/bin/python3
""" Module that will inherit"""


from models.base import Base
class Rectangle(Base):
    """Representation of a rectangle that inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
    
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Return the area of the rectangle class"""
        return self.height * self.width

    def display(self):
        """prints to stdout the rectangle imstance"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="");
            print("#" * self.width)

    def __str__(self):
        """Change the representation of the instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update the attribute"""
        
        if len(args) != 0:
            arg = list(args)
            for i in range(len(arg)):
                if i == 0:
                    self.id = arg[0]
                elif i == 1:
                    self.width = arg[1]
                elif i == 2:
                    self.height = arg[2]
                elif i == 3:
                    self.x = arg[3]
                elif i == 4:
                    self.y = args[4]
        else:
            for i in kwargs:
                self.i = kwargs[i]
