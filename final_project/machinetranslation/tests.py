from machinetranslation.translator import english_to_french, french_to_english
import unittest

"""
This class is made for testing the Translator package
"""

class TestStringMethods(unittest.TestCase):
    # test function to test equality of two value
    def test_french(self):
        """
        args: none
        returns: errors if 
        """
        firstValue = french_to_english("Bonjour !")
        secondValue = "Hello!"
        # error message in case if test case got failed
        message = "First value and second value are equal !"
        # assertEqual() to check equality of first & second value
        self.assertEqual(firstValue, secondValue, message)
        self.assertNotEqual(firstValue, "","Not Empty Text")
    def test_english(self):
        firstValue = english_to_french("Good Morning!")
        secondValue = "Bonjour !"
        # error message in case if test case got failed
        message = "First value and second value are equal !"
        # assertEqual() to check equality of first & second value
        self.assertEqual(firstValue, secondValue, message)
        self.assertNotEqual(firstValue, "","Not Empty Text")
  
if __name__ == '__main__':
    unittest.main()