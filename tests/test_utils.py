# -*- coding: utf-8 -*-


"""This module contains the tests."""

from unittest import TestCase

from test_project import add


class TestAdd(TestCase):
    """The tests for adding."""

    def test_identity(self):
        """This code assures, that x+0=x."""
        result = add(1, 0)
        self.assertEqual(1, result)

    def test_negation(self):
        """This code assures, that a + (-a) = 0."""
        result = add(1, -1)
        self.assertEqual(result, 0)
