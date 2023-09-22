#!/usr/bin/python3
"""
Python class called base_model that has the methods attribute
and instances which other class will inherit from
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    The class BaseModel that defines all common attributes and
    methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initialization method for instance attributes"""

        kwargs_len = len(kwargs)
        if kwargs_len > 0 and kwargs is not None:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "updated_at" or k == "created_at":
                        v = datetime.fromisoformat(v)
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """string representation of the instance"""

        st = "[" + str(self.__class__.__name__) + "]" + \
            " (" + self.id + ") " + str(self.__dict__)
        return st

    def to_dict(self):
        """ to dict"""

        custom = self.__dict__.copy()
        custom_dict = {}
        custom_dict.update({"__class__": self.__class__.__name__})
        for key in list(custom):
            if key in ("created_at", "updated_at"):
                custom_dict.update({key: getattr(self, key).isoformat()})
            elif key == "_sa_instance_state":
                custom.pop(key)
            else:
                custom_dict.update({key: getattr(self, key)})
        return custom_dict

    def save(self):
        """saving method to change the updated time"""

        if (self.updated_at):
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()
