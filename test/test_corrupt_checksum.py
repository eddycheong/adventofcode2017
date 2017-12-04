from unittest import TestCase
from adventofcode import *

class TestMaxMinChecksum(TestCase):
  def test_spreadsheet_checksum(self):
    spreadsheet = [[5,1,9,5],
                   [7,5,3],
                   [2,4,6,8]]

    result = spreadsheet_checksum(spreadsheet)
    self.assertEqual(result, 18)

class TestEvenlyDivisibleChecksum(TestCase):
  def test_spreadsheet_checksum(self):
    spreadsheet = [[5,9,2,8],
                   [9,4,7,3],
                   [3,8,6,5]]

    result = evenly_divisble_checksum(spreadsheet)
    self.assertEqual(result, 9)

if __name__ == '__main__':
  unittest.main()