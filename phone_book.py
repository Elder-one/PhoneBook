from input_tools import *


class PhoneBook:

    def __init__(self, path: str):
        self.path = path
        self.contacts: list = get_contacts_from_file(path)

    def add_new_contact(self, name: str, phone_number: str, info: str):
        self.contacts.append(Contact(name, phone_number, info))
        self.contacts.sort()

    def remove_contact(self, contact: Contact):
        self.contacts.remove(contact)

    def find_contacts(self, contact_sample: str) -> list:
        result = [el for el in self.contacts
                  if contact_sample in el.phone_number
                  or contact_sample in el.name]
        return result

    def edit_contact(self, contact: Contact, new_name: str,
                     new_phone_number: str, new_info: str):
        self.remove_contact(contact)
        self.contacts.append(Contact(new_name, new_phone_number, new_info))
        self.contacts.sort()
        return

    def show_contacts(self, contacts: list):
        print("{:4} {:12} {:18} {:9}".format("ORD",
                                         "NAME",
                                         "PHONE NUMBER",
                                         "INFO"))
        print("-" * (12 + 1 + 18 + 1 + 9))
        if len(contacts) == 0:
            print("Empty set")
        for id_, el in enumerate(contacts, start=1):
            print("{:3d}. ".format(id_) + str(el))
        print("-" * (12 + 1 + 18 + 1 + 9))

    def save_contacts(self):
        lines = ["$$".join([el.name, el.phone_number, el.other_info])
                 for el in self.contacts]
        try:
            with open(self.path, "w") as file:
                file.writelines(lines)
        except Exception:
            print(f"Unable to create file '{self.path}'")
