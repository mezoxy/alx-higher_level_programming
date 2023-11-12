#!/usr/bin/python3
"""The module: user"""
from base_model import BaseModel


class User(BaseModel):
    """User: Subclass of BaseModel"""
    email = ""
    password = ""
    first_name = "ayoub"
    last_name = ""

u = User()
print(u.first_name)
