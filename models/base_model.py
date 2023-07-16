#!/usr/bin/python3
"""
Python class called base_model that has the methods attribute
and instances which other class will inherit from
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    The class BaseModel that defines all common attributes and
    methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initialization method for instance attributes"""

        kwargs_len = len(kwargs)
        if kwargs_len > 0:
            args = [
                "id",
                "my_number",
                "name",
                "created_at",
                "updated_at"
            ]
            for k, v in kwargs.items():
                if k in args:
                    if k == "updated_at" or k == "created_at":
                        v = datetime.fromisoformat(v)
                    if k == "name" and v is None:
                        continue
                    if k == "my_number" and v == 0:
                        continue
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.name = None
            self.my_number = 0
            d = {
                "updated_at": self.updated_at,
                "id": self.id,
                "created_at": self.created_at
            }
            if self.name is not None:
                d["name"] = self.name
            if self.my_number != 0:
                d["my_number"] = self.my_number
            self.__dict__ = d

    def __str__(self):
        """string representation of the instance"""

        st = "[" + str(BaseModel.__name__) + "]" + \
            "(" + self.id + ")" + str(self.__dict__)
        return st

    def to_dict(self):
        """ to dict"""

        dt = self.__dict__.copy()
        dt["__class__"] = str(BaseModel.__name__)
        dt["updated_at"] = self.updated_at.isoformat()
        dt["created_at"] = self.created_at.isoformat()
        return dt

    def save(self):
        """saving method to change the updated time"""
        from models import storage

        setattr(self, "updated_at", datetime.now())
        storage.new(self)
        storage.save()
