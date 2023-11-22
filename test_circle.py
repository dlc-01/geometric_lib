import unittest
from circle import area
from circle import perimeter
import math
class CircleTestCase(unittest.TestCase):
    def test_area(self):
        """
        Test the area function for different radius values.
        """
        # Test for radius r = 2
        self.assertAlmostEqual(area(2), math.pi * 2 * 2)
        # Test for radius r = 6.9
        self.assertAlmostEqual(area(6.9), math.pi * 6.9 * 6.9)
        # Test for radius r = 100
        self.assertAlmostEqual(area(100), math.pi * 100 * 100)

    def test_perimeter(self):
        """
        Test the perimeter function.
        """
        # Test for radius r = 2
        self.assertAlmostEqual(perimeter(2), 2 * math.pi * 2)
        # Test for radius r = 6.9
        self.assertAlmostEqual(perimeter(6.9), 2 * math.pi * 6.9)
        # Test for radius r = 100
        self.assertAlmostEqual(perimeter(100), 2 * math.pi * 100)


