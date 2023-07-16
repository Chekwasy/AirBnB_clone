#!/usr/bin/python3
"""class place that inherit from basemodel for name etc"""
from models.base_model import BaseModel
from models.user import User
from models.city import City


class Place(BaseModel):
    """The class place begins"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialization for user"""

        super().__init__(*args, **kwargs)
