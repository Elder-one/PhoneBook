def get_name_from_user(message: str) -> str:
    while True:
        output = input(message)
        for char in output:
            if not (char.isalpha() or char == " "):
                print("The name must contain letters and spaces only")
                break
        else:
            break
    return output


def get_phone_number_from_user(message: str) -> str:
    while True:
        output = input(message)
        if phone_number_is_valid(output):
            break
        print("Phone number must fit the format\n"
              "+[code]-XXX-XXX-XX-XX")
    return output


def phone_number_is_valid(user_string: str) -> bool:
    if user_string == "":
        return False
    if user_string[0] != "+":
        return False
    code_list: list = list(user_string[1:].split("-").__reversed__())
    if len(code_list) != 5:
        return False
    code_lengths = [2, 2, 3, 3]
    for code, code_length in zip(code_list, code_lengths):
        if len(code) != code_length:
            return False
        for char in code:
            if not char.isdigit():
                return False
    for char in code_list[-1]:
        if not char.isdigit():
            return False
    return True
