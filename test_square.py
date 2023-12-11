import unittest
from square import area, perimeter


class TestSquareFunctions(unittest.TestCase):
    """
    Test square function.
    """
    def test_square_area_integer(self):
        """
        Test the area function by integer.
        """
        # Test for side a = 4
        self.assertAlmostEqual(area(4), 16)


    def test_square_area_float(self):
        """
        Test the area function by float
        """
        # Test for side a = 6.9
        self.assertAlmostEqual(area(6.9), 6.9*6.9)
    
    def test_square_area_big(self):
        """
        Test the area function by float and int
        """
        # Test for side a = 52
        self.assertAlmostEqual(area(520), 520*520)
        
    
    def test_square_perimeter_integer(self):
        """
        Test the perimeter function by integer.
        """
        # Test for side a = 5
        self.assertAlmostEqual(perimeter(5), 20)


    def test_square_perimeter_float(self):
        """
        Test the area function by float
        """
        # Test for side a = 6.9
        self.assertAlmostEqual(perimeter(6.9), 4*6.9)
    
    def test_square_perimeter_big(self):
        """
        Test the area function by float and int
        """
        # Test for side a = 520
        self.assertAlmostEqual(perimeter(520), 4*520)
        

