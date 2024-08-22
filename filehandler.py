import csv
import addressbook as addB
import contact as cont

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_address_book(self, AddressBook: addB.AddressBook):
        try:
            with open(self.file_path, 'r') as file:
                file_read = csv.reader(file)
                for row in file_read:
                    AddressBook.add_contact(cont.Contacts(row[0], row[1], row[2], row[3], row[4]))
        except FileNotFoundError:
            print(f"Errore: Il file '{self.file_path}' non è stato trovato.")
        except PermissionError:
            print(f"Errore: Permessi insufficienti per leggere '{self.file_path}'.")
        except IsADirectoryError:
            print(f"Errore: '{self.file_path}' è una directory, non un file.")
        except OSError as e:
            print(f"Errore OS: {e}")

    def write_address_book(self, file_path, AddressBook: addB.AddressBook):
        try:
            with open(file_path, mode='w', newline='') as file:
                file_write = csv.writer(file)
                for contact in AddressBook.contacts:
                    file_write.writerow([contact.get_id(), contact.get_name(), contact.get_surname(), str(contact.get_number()), contact.get_email()])
        except FileNotFoundError:
            print(f"Errore: Il file '{file_path}' non è stato trovato.")
        except PermissionError:
            print(f"Errore: Permessi insufficienti per scrivere su '{file_path}'.")
        except IsADirectoryError:
            print(f"Errore: '{file_path}' è una directory, non un file.")
        except OSError as e:
            print(f"Errore OS: {e}")

    def get_last_id(self):
        id = 0
        try:
            with open(self.file_path, 'r') as file:
                file_read = csv.reader(file)
                for row in file_read:
                    id = int(row[0])
        except FileNotFoundError:
            print(f"Errore: Il file '{self.file_path}' non è stato trovato.")
        except PermissionError:
            print(f"Errore: Permessi insufficienti per leggere '{self.file_path}'.")
        except IsADirectoryError:
            print(f"Errore: '{self.file_path}' è una directory, non un file.")
        except OSError as e:
            print(f"Errore OS: {e}")
        return id