#!/usr/bin/python3
"""Base Model module"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """Base Model class"""
    def __init__(self, *args, **kwargs):
        """Init function"""
        if kwargs:
            for i in kwargs.keys():
                if i == "created_at" or i == "updated_at":
                    date = datetime.fromisoformat(kwargs[i])
                    setattr(self, i, date)
                elif i != "__class__":
                    setattr(self, i, kwargs[i])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Str function"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """Save function"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict = self.__dict__
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
