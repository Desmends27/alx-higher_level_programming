import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b1 = Base()
        cls.b2 = Base(10)
        cls.b3 = Base()
        cls.b4 = Base()

    @classmethod
    def tearDownClass(cls):
        del cls.b1
        del cls.b2
        del cls.b3
        del cls.b4

    def test_id(self):
        """ Test of id of base class is none, not none, updatable """
        self.assertEqual(TestBaseClass.b1.id, 1)
        self.assertEqual(TestBaseClass.b2.id, 10)
        self.assertEqual(TestBaseClass.b3.id, 2)
