import sys
import addressbook as addBook
import contact as cont
import filehandler as fh
import os
import time 


def clear_terminal():
    if os.name == 'nt':  # per Windows
        os.system('cls')
    else:  # per Unix/Linux/macOS
        os.system('clear')



def wait_user_input():
    input("Premi un tasto per continuare....")
    clear_terminal()
    return None


def menu():
    menu_choise = None
    print("Selezionare una voce dal menù:")
    print("1: Aggiungi un nuovo contatto")
    print("2: Visualizza tutti i contatti")
    print("3: Modifica un contatto")
    print("4: Elimina un contatto")
    print("5: Ricerca un contatto")
    print("6: Salva i contatti")
    print("7: Esci")
    check_choice = True
    while check_choice:
        try:
            sys.stdin.flush()
            menu_choise = int(input("Scelta utente:"))

            if not (menu_choise < 1 or menu_choise > 7):
                check_choice = False
            # out of range
            else:
                print("Scelta non valida, riprova")
        except ValueError:
            print("Scelta non valida, riprova")
    clear_terminal()
    return menu_choise


def req_info_contact():
    contact_info = []
    contact_info.append(input("Inserisci il nome del contatto: "))
    contact_info.append(input("Inserisci il cognome del contatto: "))
    try:
        contact_info.append(int(input("Inserisci il numero di cellulare del contatto: ")))
    except ValueError:
        raise ValueError("Hai inserito un numero di cellulare non valido")
    contact_info.append(input("Inserisci l'indirizzo email del contatto: "))
    sys.stdin.flush()
    return contact_info


def user_research(AddressBook: addBook.AddressBook):
    print("Selezione metodo di ricerca:")
    print("1: Ricerca per cognome")
    print("2: Ricerca per nome")
    try:
        user_choice = int(input("Scelta: "))
        # out of range
        while user_choice < 1 or user_choice > 2:
            user_choice = int(input("Scelta non valida, riprova:"))
        if user_choice == 1:
            surname = input("Inserisci il cognome da ricercare: ")
            id_contacts = AddressBook.research_by_surname(surname)
        elif user_choice == 2:
            name = input("Inserisci il nome da ricercare: ")
            id_contacts = AddressBook.research_by_name(name)
        return id_contacts
    except ValueError as ve:
        print("Hai inserito un valore non valido.")
        raise ve
    except Exception:
        print(f"Errore: Hai inserito un valore non valido")



print("ContactEase Solutions\n")


contact_id = 1
address_book = addBook.AddressBook()

file_path = "/Users/domenicoquarto/Developer/Profession AI/AI Engineering/Python/ContactEase/AddressBoook.csv"
file_handler = fh.FileHandler(file_path)
file_handler.read_address_book(address_book)
contact_id = file_handler.get_last_id()
user_choice = menu()


while user_choice != 7:
    if user_choice == 1:
        try:
            info_cont = req_info_contact()
            contact_id = contact_id + 1
            contact = cont.Contacts(contact_id, info_cont[0], info_cont[1], info_cont[2], info_cont[3])
            address_book.add_contact(contact)
        except Exception as e:
            print(f"Errore: {e}")
            wait_user_input()
    elif user_choice == 2:
        print("Elenco contatti:")
        address_book.print_contact()
        clear_terminal()
    elif user_choice == 3:
        try:
            print("Ricerca il contatto da modifica:")
            contact_exist = address_book.print_contact_by_id(user_research(address_book))
            if contact_exist:
                id = int(input("Inserisci l'id del contatto che vuoi modificare:"))
                while id > contact_id or id <0:
                    id = int(input("Id inserito non valido riprova:"))
                address_book.contact_modify(id)
        except ValueError:
            print("Hai inserito un valore non valido.")
            wait_user_input()
    elif user_choice == 4:
        try:
            print("Ricerca il contatto da eliminare:")
            contact_exist = address_book.print_contact_by_id(user_research(address_book))

            if contact_exist:
                id = int(input("Inserisci l'id del contatto che vuoi eliminare:"))
                while id > contact_id or id <0:
                    id = int(input("Id inserito non valido riprova:"))

                for element in address_book.contacts:
                    if int(element.get_id()) == id:
                        index = address_book.contacts.index(element)
                        address_book.remove_contact(index)
                clear_terminal()
        except ValueError:
            print(f"Eccezione: Valore inserito non valido")
        except Exception as e:
            print(e)
    elif user_choice == 5:
        try:
            contact_id = user_research(address_book)
            if len(contact_id) > 0:
                clear_terminal()
                address_book.print_contact_by_id(contact_id)
                wait_user_input()
            else:
                print("Nessun contatto trovato")
                wait_user_input()


        except Exception:
            print("Non è stato possibile eseguire la ricerca")
    elif user_choice == 6:
        try:
            print("Savataggio contatti, attendere.....")
            time.sleep(2)
            file_handler.write_address_book(file_path, address_book)
            clear_terminal()
        except Exception:
            print("Si è verificato un errore in fase di salvataggio!")
    
    sys.stdin.flush()
    user_choice = menu()
    clear_terminal()

print("Uscita dal programma.")
