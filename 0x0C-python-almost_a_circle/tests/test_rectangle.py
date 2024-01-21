#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.r1 = Rectangle(10,10)
        cls.r2 = Rectangle(12, 2, id= 10)
        cls.r3 = Rectangle(10, 10)

    @classmethod
    def tearDownClass(cls):
        del cls.r1
        del cls.r2
        del cls.r3

    def test_inputs(self):
        """ Test for inputs for width and length """
        with self.assertRaises(TypeError):
            t1 = Rectangle(10, "1")
            t2 = Rectangle(10, 2, "1", 1)
        with self.assertRaises(ValueError):
            t1 = Rectangle(10, -2)
            t2 = Rectangle(10, 1, -1, 0)

    def test_id(self):
        """ Test for value of id """
        self.assertEqual(TestRectangleClass.r1.id, 4)
        self.assertEqual(TestRectangleClass.r2.id, 10)
        self.assertEqual(TestRectangleClass.r3.id, 5)

    def test_nb_objects_is_updated(self):
        TestRectangleClass.r3.update(id=11)
        self.assertEqual(TestRectangleClass.r3.id, 11)
