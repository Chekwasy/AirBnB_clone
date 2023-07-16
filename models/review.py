#!/usr/bin/python3
"""class reviews that inherit from basemodel for text place etc"""
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """The class user begins"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialization for user"""

        super().__init__(*args, **kwargs)
