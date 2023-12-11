import unittest
from rectangle import perimeter
from rectangle import area


class TestRectangleFunctions(unittest.TestCase):
    """
    Test rectangle function.
    """
    def test_rectangle_area_integer(self):
        """
        Test the area function by integer.
        """
        # Test for sides a = 10, b = 5
        self.assertEqual(area(10, 5), 50)


    def test_rectangle_area_float(self):
        """
        Test the area function by float
        """
        # Test for sides a = 15.2, b = 3.3
        self.assertEqual(area(15.2, 3.3), 15.2 * 3.3)
    
    def test_rectangle_area_float_int(self):
        """
        Test the area function by float and int
        """
        # Test for sides a = 15.2, b = 2
        self.assertEqual(area(15.2, 2), 15.2 * 2)
        
    
    def test_rectangle_perimeter_integer(self):
        """
        Test the perimeter function by integer.
        """
        # Test for sides a = 10, b = 5
        self.assertAlmostEqual(perimeter(10, 5), 30)


    def test_rectangle_perimeter_float(self):
        """
        Test the perimeter function by float
        """
        # Test for sides a = 15.2, b = 3.3
        self.assertAlmostEqual(perimeter(15.2, 3.3), 2*(15.2+3.3))
    
    def test_rectangle_perimeter_float_int(self):
        """
        Test the perimeter function by float and int
        """
        # Test for sides a = 20, b = 50.2
        self.assertAlmostEqual(perimeter(20, 50.2), 2*(50.2+20))
        
