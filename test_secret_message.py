import unittest
from secret_message import encode_message

class TestMessage(unittest.TestCase):
    """Class to test the module secret_message"""

    def test_conversion(self):
        """To test if it is converting the message properly"""
        self.assertAlmostEqual(encode_message('hello'),'svool')
        self.assertAlmostEqual(encode_message('world'),'dliow')
        self.assertAlmostEqual(encode_message('Mairiyisel Gomez'),'nzrirbrhvo tlnva')
    
    def test_format_input(self):
        """To test if the message sent is alphabetical"""
        self.assertRaises(ValueError,encode_message,'1234')

if __name__ == '__main__':
    unittest.main()