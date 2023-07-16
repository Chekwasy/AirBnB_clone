#!/usr/bin/python3
"""class amenity that inherit from basemodel for name"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The class amenity begins"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization for amenity"""

        super().__init__(*args, **kwargs)
