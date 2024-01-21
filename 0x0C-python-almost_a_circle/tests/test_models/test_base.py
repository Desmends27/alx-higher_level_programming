import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
#write test for display
class TestBaseClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.b1 = Base()
        cls.b2 = Base(10)
        cls.b3 = Base()
        cls.b4 = Base()
        cls.r1 = Rectangle(10,10)
        cls.r2 = Rectangle(12, 2, id=10)
        cls.r3 = Rectangle(2, 3)
        cls.sq1 = Square(2,2)
        cls.sq2 = Square(3, 3, id = 10)

    @classmethod
    def tearDownClass(cls):
        del cls.b1
        del cls.b2
        del cls.b3
        del cls.b4
        del cls.r1
        del cls.r2
        del cls.r3
        del cls.sq1
        del cls.sq2

    """ Test for Base Class  and id"""
    def test_id_is_none(self):
        self.assertEqual(TestBaseClass.b1.id, 1)
        self.assertEqual(TestBaseClass.r1.id, 4)
        self.assertEqual(TestBaseClass.sq1.id, 6)

    def test_id_is_not_none(self):
        self.assertEqual(TestBaseClass.b2.id, 10)
        self.assertEqual(TestBaseClass.r2.id, 10)
        self. assertEqual(TestBaseClass.sq2.id, 10)

    def test_nb_objects_is_updated(self):
        self.assertEqual(TestBaseClass.b3.id, 2)
        self.assertEqual(TestBaseClass.b4.id, 3)
        self.assertEqual(TestBaseClass.r3.id, 5)

    """ Test for Integer Validator """
    def test_height_not_num(self):
        with self.assertRaises(TypeError):
            t1 = Rectangle(10,"2")
    def test_height_less(self):
        with self.assertRaises(ValueError):
            t1 = Rectangle(10, -2)
    def test_x_not_number(self):
        with self.assertRaises(TypeError):
            t1 = Rectangle(10, 2, "4", 1)

    def test_x_less(self):
        with self.assertRaises(ValueError):
            t1 = Rectangle(10, 5, -2, 1)

    """ Tests for area """
    def test_area(self):
        self.assertEqual(TestBaseClass.r3.area(), 6)

    """ Test for upate#0 """
    def test_update0(self):
        TestBaseClass.r2.update(40, 3)
        TestBaseClass.sq1.update(1, 1)
        self.assertEqual(TestBaseClass.r2.id, 40)
        self.assertEqual(TestBaseClass.sq1.id, 1)



if __name__ == '__main__':
    unittest.main()
