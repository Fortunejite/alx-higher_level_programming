#!/usr/bin/python3
"""The base module for this project.
"""


class Base:
    """The base class for this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        import json
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        lists = []
        string = ""
        name = cls.__name__ + ".json"
        if list_objs is not None:
            with open(name, 'w', encoding='utf-8') as f:
                for i in list_objs:
                    lists.append(i.to_dictionary())
                string = Base.to_json_string(lists)
                f.write(string)
        else:
            with open(name, 'w', encoding='utf-8') as f:
                string = Base.to_json_string(lists)
                f.write(string)

    @staticmethod
    def from_json_string(json_string):
        import json
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(3, 3)
        for i in dictionary:
            if i == "id":
                dummy.update(id=dictionary[i])
            elif i == "size":
                dummy.update(size=dictionary[i])
            elif i == "x":
                dummy.update(x=dictionary[i])
            elif i == "y":
                dummy.update(y=dictionary[i])
            elif i == 'height':
                dummy.update(height=dictionary[i])
            elif i == 'width':
                dummy.update(width=dictionary[i])
            else:
                continue
        return dummy

    @classmethod
    def load_from_file(cls):
        name = cls.__name__ + '.json'
        list_ = []
        try:
            with open(name, 'r') as f:
                string = f.read()
            string = Base.from_json_string(string)
            for i in string:
                r = cls.create(**i)
                list_.append(r)
            return list_
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        name = cls.__name__ + ".csv"
        header = ['id', 'width', 'height', 'x', 'y']
        rows = []
        import csv
        with open(name, 'w', encoding='utf-8') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(header)
            if cls.__name__ == 'Rectangle':
                for i in list_objs:
                    rows= []
                    rows.append(i.id)
                    rows.append(i.width)
                    rows.append(i.height)
                    rows.append(i.x)
                    rows.append(i.y)
                    csvwriter.writerow(rows)
            elif cls.__name__ == 'Square':

