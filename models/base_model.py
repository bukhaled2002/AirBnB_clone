#!/usr/bin/python3
""" the base model"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """printing the value"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        """ save the file """
        self.updated_at = datetime.today()

    def to_dict(self):
        """return the all dictionary"""
        dictcpy=self.__dict__.copy()
        dictcpy['created_at'] = self.created_at.isoformat()
        dictcpy['updated_at'] = self.updated_at.isoformat()
        dictcpy['__class__'] = self.__class__.__name__
        return dictcpy
