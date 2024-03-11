#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) is cls:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """Saves storage dictionary to file"""
        objdict = {}
        for key in self.__objects.keys():
            objdict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(objdict, file)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                for o in json.load(file).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Method that delete objects"""
        try:
            del self.__objects[f"{type(obj).__name__}.{obj.id}"]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """
        Method that call reload method
        """
        self.reload()
