import unittest

from triangle import classTriangle

class TestTriangle(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(classTriangle(5, 5, 5), "Equilateral triangle")

    def test_right_triangle(self):
        self.assertEqual(classTriangle(3, 4, 5), "Right angle triangle")

    def test_isosceles_triangle(self):
        self.assertEqual(classTriangle(6, 6, 9), "Isosceles angle triangle")

    def test_scalene_triangle(self):
        self.assertEqual(classTriangle(5, 6, 7), "Scalene angle triangle")


if __name__ == "__main__":
    unittest.main(exit=False)