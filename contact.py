class Contact:

    def __init__(self, name: str, phone_number: str, info: str):
        self.name = name
        self.phone_number = phone_number
        self.other_info = info

    def __eq__(self, other):
        return self.phone_number == other.phone_number

    def __lt__(self, other):
        return self.phone_number < other.phone_number

    def __gt__(self, other):
        return self.phone_number > other.phone_number

    def __repr__(self):
        return "%18s %18s %s".format(self.name,
                                     self.phone_number,
                                     self.other_info)

