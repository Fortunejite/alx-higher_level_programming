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

    def update(self, *args, **kwargs):
        """update the attribute"""

        if len(args) != 0:
            arg = list(args)
            for i in range(len(arg)):
                if i == 0:
                    self.id = arg[0]
                elif i == 1:
                    self.size = arg[1]
                elif i == 2:
                    self.x = arg[2]
                elif i == 3:
                    self.y = arg[3]
                else:
                    continue
        else:
            for i in kwargs:
                if i == "id":
                    self.id = kwargs[i]
                elif i == "size":
                    self.width = kwargs[i]
                elif i == "x":
                    self.x = kwargs[i]
                elif i == "y":
                    self.y = kwargs[i]
                else:
                    continue;

    def to_dictionary(self):
        dic = {}
        dic['id'] = self.id
        dic['width'] = self.width
        dic['height'] = self.size
        dic['x'] = self.x
        dic['y'] = self.y
        return dic
