#!/usr/bin/python3
"""
AirBnb project - BaseModel class
"""


import uuid
from datetime import datetime


class BaseModel:
    """ This class defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ method constructor """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None:
            form = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "created_at":
                    self.created_at = datetime.strptime(value, form)
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value, form)
                if key == "name":
                    self.name = value
                if key == "my_number":
                    self.my_number = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """ print a readable string """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary with all keys/value of __dict__ of the instance
        """
        dictnew = {}
        dictnew['__class__'] = self.__class__.__name__

        formato = "%Y-%m-%dT%H:%M:%S.%f"
        dictnew['created_at'] = self.created_at.strftime(formato)
        dictnew['updated_at'] = self.updated_at.strftime(formato)
        dictnew['id'] = self.id
        dictnew['name'] = self.name
        dictnew['my_number'] = self.my_number
        return dictnew
