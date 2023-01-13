#!usr/bin/python3
"""Class of a sqiare which inherits fron a Rectangle"""


from models.rectangle import Rectangle
class Square(Rectangle):
    """Square that inherits from Rectanglr"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    def __str__(self):
        return "[square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width
    @size.setter
    def size(self, value):
        self.width = value
        self.height = self.width
