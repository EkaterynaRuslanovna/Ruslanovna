import unittest
from datetime import datetime
from Task_3_Class_Record import Record


class TestRecord(unittest.TestCase):
    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Record.validate_name("123")
        self.assertEqual(Record.validate_name("John"), "John")
        self.assertEqual(Record.validate_name("Ваня"), "Ваня")

    def test_surname_validation(self):
        with self.assertRaises(ValueError):
            Record.validate_surname("123")
        self.assertEqual(Record.validate_surname("Doe"), "Doe")
        self.assertEqual(Record.validate_surname("Павлович"), "Павлович")

    def test_mobile_phone_validation(self):
        with self.assertRaises(ValueError):
            Record.validate_mobile_phone("abc")
        with self.assertRaises(ValueError):
            Record.validate_mobile_phone("1234567")
        self.assertEqual(Record.validate_mobile_phone("1234567890"), "1234567890")

    def test_birthday_validation(self):
        with self.assertRaises(ValueError):
            Record.validate_birthday("01.13.90")
        with self.assertRaises(ValueError):
            Record.validate_birthday("01.01.30")
        with self.assertRaises(ValueError):
            Record.validate_birthday("01.01.")
        self.assertEqual(Record.validate_birthday("01.01.90"), datetime(1990, 1, 1))
        self.assertEqual(Record.validate_birthday(None), None)


if __name__ == '__main__':
    unittest.main()
