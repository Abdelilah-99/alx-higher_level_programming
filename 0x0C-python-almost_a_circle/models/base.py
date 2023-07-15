#!/usr/bin/python3
"""base class"""
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of Base.
        If the id parameter is provided, it sets the id attribute
        of the instance to the given value.
        Otherwise, it increments the __nb_objects
        class attribute and assigns the resulting value to the id attribute of
         the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string representation.
        If the input is None or an empty list, it returns the string "[]".
        Otherwise, it uses the json.dumps()
        function to convert the list of dictionaries to a JSON string.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.
        It first checks if list_objs is None
        and assigns an empty list if it is.
        Then, it creates a filename based on the
        class name and opens a file with that name in write mode.
        It creates a list comprehension to generate
        a list of dictionaries using the to_dictionary() method of each obje
        ct in list_objs.
        Finally, it calls the to_json_string() method
        on the class cls (which is Base in this case)
        and writes the resul
        ting JSON string to the file.
        """
        if list_objs is None:
            list_objs = []
        f_name = "{}.json".format(cls.__name__)
        with open(f_name, "w") as f:
            dict = [obj.to_dictionary() for obj in list_objs]
            f.write(cls.to_json_string(dict))
