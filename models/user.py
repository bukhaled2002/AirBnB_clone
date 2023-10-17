#!/usr/bin/python3
""" the base model"""
from models.base_model import BaseModel


class User(BaseModel):
    """this is a comment"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
