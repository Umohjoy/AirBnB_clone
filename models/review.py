#!/usr/bin/python3
"""It Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Helps in managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
