#!/usr/bin/python3
"""
Base Model for AirBnB
"""
from datetime import datetime
import json
from uuid import uuid4
import models


class BaseModel:
     """Class that defines all common attr/methods for other classes"""

     def __init__(self, *args, **kwargs):
         """Initialization of Class"""

         if kwargs:
             for keys, values in kwargs.items():
                 if keys != "__class__":
                     if keys == "created_at" or keys == "updated_at":
                         values = datetime.strptime(values,
                                                    "%Y-%m-%dT%H:%M:%S.%f")
                         setattr(self, keys, values)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """ String Representation """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))
