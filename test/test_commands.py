# test_commands.py
import unittest
from src.main import validate

class TestCommands(unittest.TestCase):

    def test_valid_commands(self):
        self.assertEqual(validate("find:hello"), "VALID")
        self.assertEqual(validate("replace:old:new"), "VALID")
        self.assertEqual(validate("delete:123"), "VALID")
        self.assertEqual(validate("find:a1b2"), "VALID")

    def test_invalid_commands(self):
        self.assertNotEqual(validate("find"), "VALID")
        self.assertNotEqual(validate("replace:old"), "VALID")
        self.assertNotEqual(validate("delete:abc"), "VALID")
        self.assertNotEqual(validate("fnd:hello"), "VALID")
        self.assertNotEqual(validate("find:hello:"), "VALID")

if __name__ == "__main__":
    unittest.main()
