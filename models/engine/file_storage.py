#!/usr/bin/python3
"""

"""

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
        with open(self.__file_path, 'w+') as f:
            my_dict = {}
            for key, value in self.__objects.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """
        deserialization
        """
        try:
            with open(self.__file_path, 'r') as f1:
                file_store = json.load(f1)
                for key, value in file_store.items():
                    val = models.cls_dict[value['__class__']](**value)
                    self.__objects[obj_id] = val
        except FileNotFoundError:
            pass
