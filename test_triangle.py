import unittest
from triangle import area, perimeter


class TestTriangleFunctions(unittest.TestCase):
    def test_area(self):
        """
        Test the area function.
        """
        # Test for side a = 6, height = 4
        self.assertAlmostEqual(area(6, 4), 12)
        # Test for side a = 6.9, height = 5.2
        self.assertAlmostEqual(area(6.9, 5.2), 6.9*5.2/2)
        # Test for side a = 7.7, height = 10
        self.assertAlmostEqual(area(7.7, 10), 7.7*10/2)

    def test_perimeter(self):
        """
        Test the perimeter function.
        The function tests the perimeter function with different sets of side lengths and verifies the expected results.
        """

        # Test for sides a = 7, b = 5, c = 6
        self.assertAlmostEqual(perimeter(7, 5, 6), 18)
        # Test for sides a = 5.2, b = 4,6, c = 10.2
        self.assertAlmostEqual(perimeter(5.2, 4.6, 10.2), 20)
        # Test for sides a = 6.9, b = 228, c = 281.1
        self.assertAlmostEqual(perimeter(6.9, 228, 281.1), 516)

