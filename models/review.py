#!/usr/bin/python3
""" Class Review """

from base_model import BaseModel


class Review(BaseModel):
    """ class attributes """
    place_id = "" + Place.id
    user_id = "" + User.id
    text = ""
