#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel

class FileStorage:
    """Represent an abstracted storage engine."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all"""
        return FileStorage.__objects

    def new(self, obj):
        """new """
        oname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(oname, obj.id)] = obj

    def save(self):
        """"""
        od = FileStorage.__objects
        odict = {obj: od[obj].to_dict() for obj in od.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(odict, f)

    def reload(self):
        """reload items from file"""
        try:
            with open(FileStorage.__file_path) as f:
                obdict = json.load(f)
                for item in obdict.values():
                    class_name= item["__class__"]
                    del item["__class__"]
                    self.new(eval(class_name)(**item))
        except FileNotFoundError:
            return
