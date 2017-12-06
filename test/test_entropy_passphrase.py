from unittest import TestCase
from adventofcode import *

class TestValidPassphraseNoDuplicates(TestCase):
  def test_no_duplicates(self):
    result = valid_passphrase_duplicates("aa bb cc dd ee")
    self.assertEqual(result, True)

  def test_duplicates(self):
    result = valid_passphrase_duplicates("aa bb cc dd aa")
    self.assertEqual(result, False)

  def test_no_duplicates_with_subsets(self):
    result = valid_passphrase_duplicates("aa bb cc dd aaa")
    self.assertEqual(result, True)

class TestValidPassphraseNoAnagrams(TestCase):
  def test_no_anagrams(self):
    result = valid_passphrase_anagrams("abcde fghij")
    self.assertEqual(result, True)

  def test_anagrams(self):
    result = valid_passphrase_anagrams("abcde xyz ecdab")
    self.assertEqual(result, False)

  def test_no_anagrams_contains_subsets(self):
    result = valid_passphrase_anagrams("a ab abc abd abf abj")
    self.assertEqual(result, True)

  def test_no_anagrams_contains_subsets(self):
    result = valid_passphrase_anagrams("iiii oiii ooii oooi oooo")
    self.assertEqual(result, True)

  def test_anagrams_permutations(self):
    result = valid_passphrase_anagrams("oiii ioii iioi iiio")
    self.assertEqual(result, False)

if __name__ == '__main__':
  unittest.main()