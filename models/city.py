#!/usr/bin/python3
""" City class """

from base_model import BaseModel


class City(BaseModel):
    """ class attributes """
    name = ""
    state_id = "" + State.id
