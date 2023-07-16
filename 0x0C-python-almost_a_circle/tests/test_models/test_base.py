#!/usr/bin/python3
"""test zone"""
import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    def test_id_assigned_when_id_provided(self):
        """
        Test case when id is provided during initialization
        """
        instance = Base(12)
        self.assertEqual(instance.id, 12)

    def test_id_assigned_when_id_not_provided(self):
        """
        Test case when id is not provided during initialization
        """
        instance1 = Base()
        instance2 = Base()
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)


if __name__ == '__main__':
    unittest.main()
