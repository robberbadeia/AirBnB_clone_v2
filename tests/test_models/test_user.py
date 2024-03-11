#!/usr/bin/python3
""" Module to test User Class """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ initialisation """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Testing first name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Testing last name """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Testing email """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Testing pass """
        new = self.value()
        self.assertEqual(type(new.password), str)
