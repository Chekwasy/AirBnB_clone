#!/usr/bin/python3
"""This does serialization and deserialiazation"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """File storage class for storing instances of a dictionary through json"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all method to return dictionary of the class attribute"""

        return self.__objects

    def new(self, obj):
        """this method sets in the private object obj as the
        object and the key"""

        stringg = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[stringg] = obj

    def save(self):
        """serializes the object which is a dictionary"""

        dict_jfile = {}
        for k, v in self.__objects.items():
            dict_jfile[k] = v.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file1:
            jstr = json.dumps(dict_jfile)
            file1.write(jstr)

    def reload(self):
        """reload method to ressurate the object intstance dictionary"""

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file1:
                txt = file1.read()
                json_conv = json.loads(txt)
                for key, value in json_conv.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    ins = cls(**value)
                    self.__objects[key] = ins
