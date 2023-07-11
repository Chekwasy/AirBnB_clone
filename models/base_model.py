#!/usr/bin/python3
"""Python class called base_model that has the methods attributes and instances which other class will inherit from"""
import uuid
from datetime import datetime


class BaseModel:
    """ The class BaseModel that defines all common attributes and methods for other classes """

    id = None
    created_at = None
    updated_at = None
    name = None
    my_number = 0    

    def __init__(self):
        """Initialization method"""

        BaseModel.id = str(uuid.uuid4())
        BaseModel.created_at = datetime.now()
        BaseModel.updated_at = datetime.now()

    def __str__(self):
        """string representation of the instance"""

        st = "[" + str(BaseModel.__name__) + "]" + "(" + self.id + ")" + str(self.__dict__)
        return st

    def __dict__(self):
        """ to dict"""

        d = {
            "my_number": BaseModel.my_number,
            "name": BaseModel.name,
            "updated_at": BaseModel.updated_at,
            "id": BaseModel.id,
            "created_at": BaseModel.created_at
        }
        return d

if __name__ == "__main__":
    a = BaseModel()
    print(a.id)
    print(a)
