#!/usr/bin/python3
"""class state that inherit from basemodel for state name"""
from models.base_model import BaseModel


class State(BaseModel):
    """The class user begins"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization for user"""

        super().__init__(*args, **kwargs)
