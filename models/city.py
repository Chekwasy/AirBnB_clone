#!/usr/bin/python3
"""class city that inherit from basemodel for city name etc"""
from models.base_model import BaseModel


class City(BaseModel):
    """The class user begins"""

    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """Initialization for city"""

        super().__init__(*args, **kwargs)
