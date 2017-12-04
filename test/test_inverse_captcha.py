from unittest import TestCase
from adventofcode import *

class TestInverseCaptchaNext(TestCase):
  def test_consecutive_match(self):
    result = inverse_captcha_next("1122")
    self.assertEqual(result, 3)

  def test_all_match(self):
    result = inverse_captcha_next("1111")
    self.assertEqual(result, 4)

  def test_no_match(self):
    result = inverse_captcha_next("1234")
    self.assertEqual(result, 0)

  def test_circular_only_match(self):
    result = inverse_captcha_next("91212129")
    self.assertEqual(result, 9)


class TestInverseCaptchaHalfway(TestCase):
  def test_all_match(self):
    result = inverse_captcha_halfway("1212")
    self.assertEqual(result, 6)

  def test_no_match(self):
    result = inverse_captcha_halfway("1221")
    self.assertEqual(result, 0)

  def test_twos_only_match(self):
    result = inverse_captcha_halfway("123425")
    self.assertEqual(result, 4)

  def test_all_match(self):
    result = inverse_captcha_halfway("123123")
    self.assertEqual(result, 12)

  def test_ones_only_match(self):
    result = inverse_captcha_halfway("12131415")
    self.assertEqual(result, 4)

if __name__ == '__main__':
  unittest.main()