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

        if kwargs:
            args = ["id", "my_number", "name", "created_at", "updated_at"]
            for k, v in kwargs.items():
                if k in args:
                    if k == "updated_at" or k == "created_at":
                        v = datetime.fromisoformat(v)
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.name = self.__class__.__name__
            self.my_number = 0
            d = {
                "my_number": self.my_number,
                "name": self.name,
                "updated_at": self.updated_at,
                "id": self.id,
                "created_at": self.created_at
            }
            self.__dict__ = d
            from models import storage
            storage.new(self)

    def save(self):
        """Save method to update the updated_at attribute"""

        setattr(self, "updated_at", datetime.now())
        from models import storage
        storage.save()

    def __str__(self):
        """String representation of the instance"""

        st = "[" + str(BaseModel.__name__) + "]" + \
            "(" + self.id + ")" + str(self.__dict__)
        return st

    def to_dict(self):
        """Convert instance attributes to a dictionary"""

        dt = {
            "my_number": self.my_number,
            "name": self.name,
            "updated_at": self.updated_at.isoformat(),
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "__class__" : self.__class__.__name__
        }
        self.to_dict = dt
        return self.to_dict
