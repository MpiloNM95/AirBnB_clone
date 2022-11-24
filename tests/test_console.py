#!/usr/bin/python3
"""test the Console itself"""
import unittest
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import pep8
from unittest.mock import patch
from io import StringIO
import cmd


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                "Found code style errors (and warnings).")


class Test_Console(unittest.TestCase):
    """Tests the entire console"""

    def test_prompt(self):
        """tests the prompt"""
        with patch('sys.stdout', new=StringIO()) as f:
            expected = HBNBCommand.prompt
            self.assertEqual(expected, "(hbnb) ")

    def test_help_help(self):
        out1 = "List available commands with \""
        out2 = "help\" or detailed help with \"help cmd\"."
        out = out1 + out2
        """tests the help"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help help"))
            self.assertEqual(out, f.getvalue().strip())

    def test_help_EOF(self):
        out = "Exits on EOF"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(out, f.getvalue().strip())

    def test_help_quit(self):
        """tests the help quit"""
        out = "exits when typing quit"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(out, f.getvalue().strip())

    def test_help_quit(self):
        """tests the help quit"""
        out = "exits when typing quit"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(out, f.getvalue().strip())

    def test_help_emptyline(self):
        """Test empty line"""
        out = ""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("\n"))
            self.assertEqual(out, f.getvalue().strip())

    def test_help_create(self):
        """Test the create help"""
        out = """Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(out, f.getvalue().strip())

    def test_help_show(self):
        """Test the show help"""
        out = """Prints the string representation of an instance
        based on the class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(out, f.getvalue().strip())

    def test_help_destroy(self):
        """tests help destroy"""
        out = "method to delete an instance based on the class name and id"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(out, f.getvalue().strip())

    def setup(self):
        """Set up tests."""
        storage.reload()

    def test_create_BaseModel(self):
        """ Test create a BaseModel """
        out = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            xd = str(type(f.getvalue().strip()))
            self.assertEqual(out, xd)

    def test_show_error(self):
        """ Test only show error """
        out = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show asd"))
            self.assertEqual(out, f.getvalue().strip())

    def test_show_only(self):
        """ Test only show """
        out = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(out, f.getvalue().strip())
