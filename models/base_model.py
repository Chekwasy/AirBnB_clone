#!/usr/bin/python3
"""
Python class called base_model that has the methods attributes
and instances which other class will inherit from
"""
import uuid
from datetime import datetime


class BaseModel:
    """ The class BaseModel that defines all common attributes and methods
    for other classes """

    def __init__(self, name=None, my_number=0):
        """Initialization method for instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.name = name
        self.my_number = my_number
        d = {
            "my_number": self.my_number,
            "name": self.name,
            "updated_at": self.updated_at,
            "id": self.id,
            "created_at": self.created_at
        }
        self.__dict__ = d

    def __str__(self):
        """string representation of the instance"""

        st = "[" + str(BaseModel.__name__) + "]" + "(" + self.id + ")" \
            + str(self.__dict__)
        return st

    def to_dict(self):
        """ to dict"""

        dt = {
            "my_number": self.my_number,
            "name": self.name,
            "updated_at": self.updated_at.isoformat(),
            "id": self.id,
            "created_at": self.created_at.isoformat()
        }
        self.to_dict = dt
        return self.to_dict

    def save(self):
        """saving method to change the updated time"""

        setattr(self, "updated_at", datetime.now())
