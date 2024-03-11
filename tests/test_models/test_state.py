#!/usr/bin/python3
""" Module to test State Class """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Testing Class """

    def __init__(self, *args, **kwargs):
        """ initialisation """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Testing name """
        new = self.value()
        self.assertEqual(type(new.name), str)
