#!/usr/bin/python3
"""

"""


import json
from models.base_model import BaseModel

class FileStorage:
    """

    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Method returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """

        """
        new_1 = obj.__class__.__name__
        new_2 = obj.id
        new = new_1 + '.' + new_2
        self.__objects[new] = obj


    def save(self):
        """
        serialization
        """
        my_dict = {}
        with open(self.__file_path, 'a') as f:
            for key, value in self.__objects.items():
                my_dict[key] = value.to_dict()
            f.write(json.dumps(my_dict))
            #f.write(m)

    def reload(self):
        """
        deserialization
        """
        classes = {'BaseModel':BaseModel}
        try:
            with open(self.__file_path, 'r') as f1:
                file_store = json.loads(f1.read())
            for key, value in file_store.items():
                val = models.classes[value['__class__']](**value)
                #val = models.classes[file_store[key]['__class__']](**file_store[key])
                self.__objects[key] = val
        except:
            pass
