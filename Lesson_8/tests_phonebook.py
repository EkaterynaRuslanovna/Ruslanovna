import unittest
from task_3_class_phoneBook import Phonebook, Record


class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()
        self.test_record = Record(name="Kate", mobile_phone="1112234534", surname="Kate", birthday="20.06.95")
        self.test_record = Record(name="Test", mobile_phone="1112223334", surname="Test", birthday="20.05.95")
        self.phonebook.add_record(self.test_record)

    def test_find_record_by_name(self):
        records = self.phonebook.find_record_by_name("Поліція")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].mobile_phone, "102")

    def test_find_record_by_surname(self):
        records = self.phonebook.find_record_by_surname("Test")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].mobile_phone, "1112223334")

    def test_find_record_by_mobile_phone(self):
        record = self.phonebook.find_record_by_mobile_phone("101")
        self.assertEqual(record.name, "Пожарна служба")

    def test_find_record_by_birthday(self):
        records = self.phonebook.find_record_by_birthday("20.05.95")
        self.assertEqual(len(records), 1)

    def test_add_record(self):
        self.phonebook.add_record(Record(name="secondTest", mobile_phone="4567836548"))

    def test_update_record(self):
        updated_record = self.phonebook.update_record(mobile_phone="1112223334", new_name="UpdatedTest")
        self.assertEqual(updated_record.name, "UpdatedTest")
        with self.assertRaises(Exception):
            self.phonebook.update_record("102", new_name="Contact")

    def test_delete_record(self):
        self.phonebook.delete_record("1112223334")
        with self.assertRaises(Exception):
            self.phonebook.delete_record("102")


if __name__ == '__main__':
    unittest.main()
