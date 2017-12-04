from unittest import TestCase
from adventofcode import inverse_captcha

class TestInverseCaptcha(TestCase):
  def test_consecutive_match(self):
    result = inverse_captcha("1122")
    self.assertEqual(result, 3)

  def test_all_match(self):
    result = inverse_captcha("1111")
    self.assertEqual(result, 4)

  def test_no_match(self):
    result = inverse_captcha("1234")
    self.assertEqual(result, 0)

  def test_circular_match(self):
    result = inverse_captcha("91212129")
    self.assertEqual(result, 9)

if __name__ == '__main__':
  unittest.main()