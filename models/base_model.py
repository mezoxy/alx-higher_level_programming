#!/usr/bin/python3
"""The module: base_model"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
        BaseModel:
                    A class  that defines all common
                    attributes/methods for other classes
        Public instance attributes:
                    id, created_at and updated_at
        Public instance methods:
                    save(self), to_dict(self)
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        val = datetime.fromisoformat(val)
                        setattr(self, key, val)
                    elif key == "updated_at":
                        val = datetime.fromisoformat(val)
                        setattr(self, key, val)
                    else:
                        setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
           The magic method __str__ prints:
                    [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            save:   A public method that updates the public instance attribute
                    updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            to_dict: A public that returns  a dictionary containing all
                    keys/values of __dict__ of the instance:
        """
        dic = {
                key: va.strftime("%Y-%m-%dT%H:%M:%S.%f") if (key == "created_at" or key == "updated_at") else
                va for key, va in self.__dict__.items()}
        dic['__class__'] = self.__class__.__name__
        return dic
