class PhoneBook:
   def __init__(self):
      self.phones = {}

   def add(self, name, phone):
      self.phones[name] = phone

   def lookup(self, name):
      return self.phones[name]
