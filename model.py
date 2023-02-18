class Phonebook:
    '''Класс, для создания экземпляра записи в телефонной книге'''
    def __init__(self):
        self.contacts = {}

    def add_contact(self,name,phone_number):
        self.contacts[name] = phone_number

