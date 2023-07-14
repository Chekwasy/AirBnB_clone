#!/usr/bi/python3
import json
import os
class FileStorage:
        __file_path = "file.json"
        __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    """def save(self):
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)"""

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_dict, file)


    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)

        else:
            pass

