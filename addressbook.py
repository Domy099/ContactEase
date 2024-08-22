import contact as cont
import os
import time

def clear_terminal():
    if os.name == 'nt':  # per Windows
        os.system('cls')
    else:  # per Unix/Linux/macOS
        os.system('clear')



def wait_user_input():
    wait_in = input("Premi un tasto per continuare....")
    clear_terminal()


class AddressBook:
    def __init__(self, contact=None):
        self.contacts = []
        if contact is not None:
            self.contacts.append(contact)

    def add_contact(self, contact):
        self.contacts.append(contact)


    def remove_contact(self, id):
        self.contacts.pop(id)


    def print_contact(self):
        for element in self.contacts:
            #print(element.get_name())
            print(element)
            print("\n")
        wait_user_input()


    def research_by_name(self, name):
        id_contacts = []
        for element in self.contacts:
            if element.get_name().casefold() == name.casefold():
                id_contacts.append(element.get_id())
        return id_contacts


    def research_by_surname(self, surname):
        id_contacts = []
        for element in self.contacts:
            if element.get_surname().casefold() == surname.casefold():
                id_contacts.append(element.get_id())
        return id_contacts


    def print_contact_by_id(self, id_list):
        contact_exist = False
        try:
            if len(id_list) > 0:
                print("Contatti trovati: ")
                for id in id_list:
                    for element in self.contacts:
                        if int(element.get_id()) == int(id):
                            print(element)
                            print("\n")
                            contact_exist = True
            else:
                print("Nessun contatto trovato")
                wait_user_input()
        except Exception:
            print("Si è verificato un errore")
        return contact_exist

    def contact_modify(self, id: object) -> object:
        clear_terminal()
        print("Cosa vuoi modificare?")
        print("1: Nome")
        print("2: Cognome")
        print("3: Numero di telefono")
        print("4: Email")
        print("5: Esci")
        modify_choice = int(input("Inserisci la tua scelta:"))

        while modify_choice != 5:
            if modify_choice == 1:
                name = input("Inserisci il nuovo nome:")
                self.contacts[id].set_name(name)
            elif modify_choice == 2:
                surname = input("Inserisci il nuovo cognome:")
                self.contacts[id].set_surname(surname)
            elif modify_choice == 3:
                try:
                    number = input("Inserisci il nuovo numero di telefono:")
                    self.contacts[id].set_number(number)
                except Exception as e :
                    print(f"Errore: {e}")
            elif modify_choice == 4:
                try:
                    email = input("Inserisci la nuova email:")
                    self.contacts[id].set_email(email)
                except Exception as e:
                    print(f"Errore: {e}")


            clear_terminal()
            print("Vuoi modificare un altro dato del contatto?")
            print("1: Nome")
            print("2: Cognome")
            print("3: Numero di telefono")
            print("4: Email")
            print("5: Esci")
            modify_choice = int(input("Inserisci la tua scelta:"))

    clear_terminal()