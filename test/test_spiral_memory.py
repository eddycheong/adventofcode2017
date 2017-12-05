from unittest import TestCase
from adventofcode import *

class TestManhattanDistance(TestCase):
  def test_square_1(self):
    result = spiral_memory(1)
    self.assertEqual(result, 0)

  def test_square_12(self):
    result = spiral_memory(12)
    self.assertEqual(result, 3)

  def test_square_23(self):
    result = spiral_memory(23)
    self.assertEqual(result, 2)

  def test_square_1024(self):
    result = spiral_memory(1024)
    self.assertEqual(result, 31)

if __name__ == '__main__':
  unittest.main()