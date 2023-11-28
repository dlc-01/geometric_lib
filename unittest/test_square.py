import unittest
from square import area, perimeter


class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        """
        Tests the area function.
        """
        # Test for side a = 4
        self.assertAlmostEqual(area(4), 16)

        # Test for side a = 6.9
        self.assertAlmostEqual(area(6.9), 6.9*6.9)

        # Test for side a = 52
        self.assertAlmostEqual(area(52), 52*52)

    def test_perimeter(self):
        """
        Test the perimeter function with different input values.
        """
        # Test for side a = 5
        self.assertAlmostEqual(perimeter(5), 20)

        # Test for side a = 6.9
        self.assertAlmostEqual(perimeter(6.9), 4*6.9)

        # Test for side a = 52
        self.assertAlmostEqual(perimeter(52), 4*52)

