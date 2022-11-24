#!/usr/bin/python3
"""Console that contains the entry point of the comm interpreter"""
import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    ALX Africa AirBnB clone console
    contains the entry point of the comm interpreter
    quit nd EOF to exit the program
    help displays help
    an empty line + ENTER doesn't execute anything
    """
    prompt = "(hbnb) "
    attributes = ["updated_at", "created_at", "id"]
    specs = ["\'", "\""]
