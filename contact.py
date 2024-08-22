import re
class Contacts:
    def __init__(self, id: int, name: str, surname: str, cellular_number: int, email: str) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.cellular_number = self.set_number(cellular_number)
        self.email = self.set_email(email)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_number(self):
        return self.cellular_number

    def get_email(self):
        return self.email

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_number(self, number):
        try:
            int_numb = int(number)
            return int_numb
        except ValueError:
            raise ValueError('Numero inserito non valido')

    def set_email(self, email):

        if re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$', email):
            return email
        else:
            raise ValueError('Mail inserita non valida')


    def __repr__(self):
        contact = f"Id: {self.get_id()}\nName: {self.get_name()}\nSurname: {self.get_surname()}\nCellular Number: {self.get_number()}\nEmail: {self.get_email()}"
        return contact