#!/usr/bin/python3
"""

"""
import uuid
from datetime import datetime

class BaseModel:
    """

    """
    def __init__(self):
        """

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """

        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """

        """
        self.update_at = datetime.now()

    def to_dict(self):
        """

        """
        dictnew = {}
        dictnew['__class__'] = self.__class__.__name__

        formato = "%Y-%m-%dT%H:%M:%S.%f"
        dictnew['created_at'] = self.created_at.strftime(formato)
        dictnew['update_at'] = self.update_at.strftime(formato)
        dictnew['id'] = self.id
        dictnew['name'] = self.name
        dictnew['my_number'] = self.my_number
        return dictnew
