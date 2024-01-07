#!/usr/bin/python3
"""Unittest for max_integer[...]"""
max_integer =__import__('6-max_integer').max_integer
import unittest

class TestMaInteger(unittest.TestCase):

    def test_empty(self):
        result = max_integer([])
        self.assertEqual(result, None)

    def test_single(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive(self):
        self.assertEqual(max_integer([10, 4, 6]), 10)

    def test_negative(self):
        self.assertEqual(max_integer([-2, -5, -1]), -1)

    def test_integers(self):
        self.assertEqual(max_integer([-2, 3, -1]), 3)
    
    def test_duplicate(self):
        self.assertEqual(max_integer([4, 4, 4]), 4)
    
    def test_large(self):
        self.assertEqual(max_integer(list(range(1, 10001))), 10000) 
