from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone):
        if phone.isdigit() and len(phone) == 10:
            super().__init__(phone)
        else:
            raise ValueError('Please provide a valid phone number')

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return 'Phone has been updated'
        return 'Phone has not been found'

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return 'Phone has been deleted'
        return 'Phone has not been found'
        
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return 'Phone has not been found'
        
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
   
    def __init__(self):
        super().__init__()
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record


    def find(self, name):
        if name in self.data:
            record = self.data[name]
            return f'{name}: {", ".join(phone.value for phone in record.phones)}'
        else:
            return "Contact has not been found"
            
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
            return 'Contact has been deleted'
        else:
            return 'Contact has not been found'
