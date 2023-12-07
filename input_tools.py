from contact import Contact


def get_str_response(message: str) -> str:
    return input(message)


def get_int_response(message: str) -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            continue


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


def get_contacts_from_file(path: str) -> list:
    result = []
    try:
        with open(path, "r") as file:
            for line in file:
                if line[-1] == ["\n"]:
                    line = line[:-1]
                name, phone_number, info = line.split("$$")
                result.append(Contact(name, phone_number, info))
    except Exception:
        return result
    finally:
        return result


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
