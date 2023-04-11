#!/usr/bin/python3
"""module for creating User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """this class manage city objects"""

    state_id = ""
    name = ""
