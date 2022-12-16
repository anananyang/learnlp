import unittest
import tests.context
from learnlp.dict.dictionary import dictionary

class TestDictionary(unittest.TestCase):
    def test_dictionary_count(self):
        self.assertTrue(dictionary.count() > 0)

if __name__ == '__mian__':
    unittest.main()