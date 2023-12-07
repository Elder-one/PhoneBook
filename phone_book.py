from input_tools import *


class PhoneBook:

    def __init__(self, path: str):
        self.path = path
        self.contacts: list = get_contacts_from_file(path)

    def add_new_contact(self):
        name: str = get_name_from_user("Input the name --> ")
        phone_number: str = (
            get_phone_number_from_user("Input"
                                       " the phone number --> "))
        info = get_str_response("Any additional info --> ")
        self.contacts.append(Contact(name, phone_number, info))
        self.contacts.sort()

    def remove_contact(self, contact: Contact):
        self.contacts.remove(contact)

    def find_contacts(self, contact_sample: str, by_number: bool = True) -> list:
        if by_number:
            result = [el for el in self.contacts
                      if contact_sample in el.phone_number]
        else:
            result = [el for el in self.contacts
                      if contact_sample in el.name]
        return result

    def edit_contact(self, contact: Contact, new_name: str,
                     new_phone_number: str, new_info: str):
        self.remove_contact(contact)
        self.contacts.append(Contact(new_name, new_phone_number, new_info))
        self.contacts.sort()
        return

    def show_contacts(self, contacts: list):
        print("%18s %18s %9s".format("NAME",
                                     "PHONE NUMBER",
                                     "INFO"))
        print("-"*(18+1+18+1+9))
        for el in contacts:
            print(el)

    def save_contacts(self):
        lines = ["$$".join([el.name, el.phone_number, el.other_info])
                 for el in self.contacts]
        try:
            with open(self.path, "w") as file:
                file.writelines(lines)
        except Exception:
            print(f"Unable to create file '{self.path}'")
