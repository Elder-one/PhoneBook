from phone_book import *


class App:

    def __init__(self, path: str):
        self.phone_book = PhoneBook(path)

    def start_page(self):
        response: int = 0
        while True:
            clean()
            print(" 1: Show all contacts")
            print(" 2: Find a contact")
            print(" 3: Save phone book")
            print("-1: Quit")
            response = get_int_response("Choose option --> ")

            if response == -1:
                return
            elif response == 1:
                self.all_contacts()
            elif response == 2:
                self.select_contacts()
            elif response == 3:
                self.phone_book.save_contacts()
            else:
                continue

    def all_contacts(self):
        while True:
            clean()
            self.phone_book.show_contacts(self.phone_book.contacts)
            print("Select contact ORD")
            print(" 0 to add new contact")
            print("-1 to go back")
            response = get_int_response("Choose option --> ")

            if response == 0:
                self.add_new_contact()
            elif response == -1:
                return
            elif (0 < response) and (response <= len(self.phone_book.contacts)):
                self.profile(self.phone_book.contacts[response-1])
            else:
                continue

    def add_new_contact(self):
        name = get_name_from_user("Name --> ")
        phone_number = get_phone_number_from_user("Phone number --> ")
        clean()
        info = get_str_response("Additional info --> ")
        self.phone_book.add_new_contact(name, phone_number, info)
        return

    def profile(self, contact: Contact):
        while True:
            clean()
            self.phone_book.show_contacts([contact])
            print(" 1. Edit contact")
            print(" 2. Delete contact")
            print("-1. Back")
            response = get_int_response("Choose option --> ")

            if response == 1:
                self.edit_contact(contact)
                return
            elif response == 2:
                self.phone_book.remove_contact(contact)
                return
            elif response == -1:
                return
            else:
                continue

    def edit_contact(self, contact: Contact):
        clean()
        new_name = contact.name
        new_phone = contact.phone_number
        new_info = contact.other_info

        while True:
            clean()
            response = get_str_response("New name (letters and spaces only!)\n"
                                        "or an empty string\n"
                                        "to keep it as it is --> ")
            if name_is_valid(response):
                new_name = response
                break
            elif response != "":
                continue
            if response == "":
                break

        while True:
            clean()
            response = get_str_response("New phone number\n"
                                        "format: +[code]-XXX-XXX-XX-XX\n"
                                        "or an empty string to keep it as it is\n"
                                        "--> ")
            if response == "":
                break
            elif phone_number_is_valid(response):
                new_phone = response
                break
            else:
                continue

        response = get_str_response("New info or an empty string\n"
                                    "to keep it as it is --> ")
        if response != "":
            new_info = response

        self.phone_book.edit_contact(contact, new_name, new_phone, new_info)
        return

    def select_contacts(self):
        while True:
            clean()
            response = get_str_response("Enter substring of phone number\n"
                                        "or fragment of the name --> ")
            clean()
            selection = self.phone_book.find_contacts(response)
            self.phone_book.show_contacts(selection)
            if len(selection) > 0:
                while True:
                    print("Select contact ORD")
                    print(" 0 to add new contact")
                    print("-1 to go back")
                    option = get_int_response("Choose option --> ")
                    if option == 0:
                        self.add_new_contact()
                        return
                    elif option == -1:
                        return
                    elif (option > 0) and (option <= len(selection)):
                        self.profile(selection[option-1])
                        return
                    else:
                        continue
            else:
                while True:
                    clean()
                    print(" 0: Add new contact")
                    print(" 1: Search again")
                    print("-1: Go back")
                    option = get_int_response("Choose option --> ")
                    if option == 1:
                        break
                    elif option == -1:
                        return
                    elif option == 0:
                        self.add_new_contact()
                        return
                    else:
                        continue
