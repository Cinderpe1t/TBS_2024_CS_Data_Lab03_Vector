"""
Name: Angelina Kim
Date: Fall 2024
Purpose: Demonstrate Vector3D class and operations.
"""

import unittest
import math
from vector import Vector3D

class TestVector(unittest.TestCase):
    """Test the Vector 3D class."""

    @classmethod
    def setUpClass(cls):
        cls.u = Vector3D(2,5,1)
        cls.v = Vector3D(-3, 1,1)
        cls.a = Vector3D(1, 0, 0)
        cls.b = Vector3D(0, 1, 0)
        cls.c = Vector3D(1, 1, 0)

    def test_str(self) -> None:
        """Test the __str__ method of the Vector3D class."""
        #from vector import Vector3D
        self.assertTrue(isinstance(self.u.__str__(), str),)
        self.assertIn("2", str(self.u))
        self.assertIn("5", str(self.u))
        self.assertIn("1", str(self.u))
        self.assertIn(",", str(self.u))
        self.assertIn("<", str(self.u))
        self.assertIn(">", str(self.u))
        self.assertIn("Vector", str(self.u))

        self.assertTrue(isinstance(self.v.__str__(), str),)
        self.assertIn("-3", str(self.v))
        self.assertIn("1", str(self.v))
        self.assertIn("1", str(self.v))
        self.assertIn(",", str(self.v))
        self.assertIn("<", str(self.v))
        self.assertIn(">", str(self.v))
        self.assertIn("Vector", str(self.v))

    def test_repr(self) -> None:
        """Test the __repr__ method of the Vector3D class."""
        self.assertTrue(isinstance(eval('self.u'), Vector3D),)
        self.assertTrue(isinstance(eval(repr(self.u)), Vector3D),)
        self.assertIn("2", repr(self.u))
        self.assertIn("5", repr(self.u))
        self.assertIn("1", repr(self.u))
        self.assertIn(",", repr(self.u))
        self.assertIn("(", repr(self.u))
        self.assertIn(")", repr(self.u))
        self.assertIn("Vector3D", repr(self.u))

        self.assertTrue(isinstance(eval('self.v'), Vector3D),)
        self.assertTrue(isinstance(eval(repr(self.v)), Vector3D),)
        self.assertIn("-3", repr(self.v))
        self.assertIn("1", repr(self.v))
        self.assertIn("1", repr(self.v))
        self.assertIn(",", repr(self.v))
        self.assertIn("(", repr(self.v))
        self.assertIn(")", repr(self.v))
        self.assertIn("Vector3D", repr(self.v))

    def test_add(self) -> None:
        """Test the __add__ and add method of the Vector3D class."""
        self.assertEqual(self.v.add(self.u).x, -1)
        self.assertEqual(self.v.add(self.u).y, 6)
        self.assertEqual(self.v.add(self.u).z, 2)
        self.assertEqual(self.u.add(self.v).x, -1)
        self.assertEqual(self.u.add(self.v).y, 6)
        self.assertEqual(self.u.add(self.v).z, 2)
        self.assertEqual(self.u.add(self.v), Vector3D(-1, 6, 2))
        self.assertEqual(self.v.add(self.u), Vector3D(-1, 6, 2))
        self.assertEqual(self.u + self.v, Vector3D(-1, 6, 2))
        self.assertEqual(self.v + self.u, Vector3D(-1, 6, 2))

    def test_subtract(self) -> None:
        """Test the __subtract__ and subtract method of the Vector3D class."""
        self.assertEqual(self.u.subtract(self.v).x, 5)
        self.assertEqual(self.u.subtract(self.v).y, 4)
        self.assertEqual(self.u.subtract(self.v).z, 0)
        self.assertEqual(self.u.subtract(self.v), Vector3D(5, 4, 0))
        self.assertEqual(self.u - self.v, Vector3D(5, 4, 0))
        self.assertEqual(self.v.subtract(self.u).x, -5)
        self.assertEqual(self.v.subtract(self.u).y, -4)
        self.assertEqual(self.v.subtract(self.u).z, 0)
        self.assertEqual(self.v.subtract(self.u), Vector3D(-5, -4, 0))
        self.assertEqual(self.v - self.u, Vector3D(-5, -4, 0))

    def test_length(self) -> None:
        """Test the __abs__ and length method of the Vector3D class."""
        self.assertAlmostEqual(self.u.length(), math.sqrt(30), places=10)
        self.assertAlmostEqual(abs(self.u), math.sqrt(30), places=10)
        self.assertAlmostEqual(self.v.length(), math.sqrt(11), places=10)
        self.assertAlmostEqual(abs(self.v), math.sqrt(11), places=10)

    def test_dot_product(self) -> None:
        """Test the __mul__ and dot_product method of the Vector3D class."""
        self.assertAlmostEqual(self.u.dot_product(self.v), 0, places=10)
        self.assertAlmostEqual(self.u * self.v, 0, places=10)
        self.assertAlmostEqual(self.v.dot_product(self.u), 0, places=10)
        self.assertAlmostEqual(self.v * self.u, 0, places=10)

    def test_scalar_product(self) -> None:
        """Test the __rmul__ and scalar_product method of the Vector3D class."""
        self.assertAlmostEqual(self.u.scalar_product(2), Vector3D(4, 10, 2), 
                               places=10)
        self.assertAlmostEqual(self.v.scalar_product(2), Vector3D(-6, 2, 2),
                               places=10)
        
    def test_is_perpendicular(self) -> None:
        """Test the is_perpendicular method of the Vector3D class."""
        self.assertEqual(self.u.is_perpendicular(self.v), True)
        self.assertEqual(self.v.is_perpendicular(self.u), True)
        self.assertEqual(self.u.is_perpendicular(self.v + self.u), False)
        self.assertEqual(self.v.is_perpendicular(self.u + self.v), False)

    def test_equal(self) -> None:
        """Test the __eq__ and __ne__ method of the Vector3D class."""
        self.assertEqual(self.u == self.v, False)
        self.assertEqual(self.u == self.u, True)
        self.assertEqual(self.v == self.v, True)
        self.assertEqual(self.v == self.u, False)
        self.assertEqual(self.u != self.v, True)
        self.assertEqual(self.u != self.u, False)
        self.assertEqual(self.v != self.v, False)
        self.assertEqual(self.v != self.u, True)

    def test_cross_product(self) -> None:
        """Test the __pow__ and cross_product method of the Vector3D class."""
        self.assertAlmostEqual(self.u.cross_product(self.v), 
                               Vector3D(4, -5, 17), places=10)
        self.assertAlmostEqual(self.u ** self.v, 
                               Vector3D(4, -5, 17), places=10)
        self.assertAlmostEqual(self.v.cross_product(self.u), 
                               Vector3D(-4, 5, -17), places=10)
        self.assertAlmostEqual(self.v ** self.u, 
                               Vector3D(-4, 5, -17), places=10)

    def test_cos(self) -> None:
        """Test the cos method of the Vector3D class."""
        self.assertAlmostEqual(self.u.cos(self.v), 0, places=10)
        self.assertAlmostEqual(self.v.cos(self.u), 0, places=10)
        self.assertAlmostEqual(self.a.cos(self.c), math.sqrt(2)/2, places=10)
        self.assertAlmostEqual(self.c.cos(self.a), math.sqrt(2)/2, places=10)

    def test_acos(self) -> None:
        """Test the acos method of the Vector3D class."""
        self.assertAlmostEqual(self.u.acos(self.v), 90, places=10)
        self.assertAlmostEqual(self.v.acos(self.u), 90, places=10)
        self.assertAlmostEqual(self.a.acos(self.c), 45, places=10)
        self.assertAlmostEqual(self.c.acos(self.a), 45, places=10)

    def test_sin(self) -> None:
        """Test the sin method of the Vector3D class."""
        self.assertAlmostEqual(self.u.sin(self.v), 1, places=10)
        self.assertAlmostEqual(self.v.sin(self.u), 1, places=10)
        self.assertAlmostEqual(self.a.sin(self.c), math.sqrt(2)/2, places=10)
        self.assertAlmostEqual(self.c.sin(self.a), math.sqrt(2)/2, places=10)

    def test_tan(self) -> None:
        """Test the tan method of the Vector3D class."""
        self.assertAlmostEqual(self.a.tan(self.c), 1, places=10)
        self.assertAlmostEqual(self.c.tan(self.a), 1, places=10)

if __name__=='__main__':
    unittest.main()