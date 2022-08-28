import unittest

from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):
   def test_lookup_by_name(self):
      phonebook = PhoneBook()

      name = "Celio"
      phone = "994084772"

      phonebook.add(name, phone)

      phone_number = phonebook.lookup(name)
      self.assertEqual("994084772", phone_number)
