#!/usr/bin/python3
"""

"""

import os
import json
from models.base_model import BaseModel
import models

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
        return self.__objects

    def save(self):
        """
        serialization
        """
        dict_add = {}
        with open(self.__file_path, 'w') as f:
            for key, value in self.__objects.items():
                dict_add[key] = value.to_dict()
            json.dump(dict_add, f)
            #f.write(m)

    def reload(self):
        """
        deserialization
        """

        classes = {'BaseModel':BaseModel}
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as myFile:
                file_store = json.load(myFile)
                for key, value in file_store.items():
                    if '__class__' in value:
                        self.__objects[key] = classes[value['__class__']](**value)
        except:
            pass
        """
        try:
            with open(self.__file_path, 'r') as f1:
                file_store = json.load(f1)
                for key, value in file_store.items():
                    val = models.classes[value['__class__']](**value)
                #val = models.classes[file_store[key]['__class__']](**file_store[key])
                self.__objects[key] = val
        except:
            pass
        """
