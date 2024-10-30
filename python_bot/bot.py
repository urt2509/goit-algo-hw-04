PATH = "./contacts.txt"


def get_contact_info(path: str = PATH) -> dict | None:
    try:
        with open(path, "r", encoding="utf-8") as file:
            contacts = {}
            for line in file:
                elements = line.strip().split(":", 1)
                if len(elements) == 2:
                    key, value = elements
                    contacts[key] = value
                else:
                    pass
        return contacts

    except FileNotFoundError:
        print(f"File {path} not found")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except Exception as e:
        raise e


def save_contact(contact):
    path = PATH

    try:
        with open(path, "a+", encoding="utf-8") as file:

            name, phone = contact
            file.seek(0)

            file.write(f"{name}: {phone} \n")

    except FileNotFoundError:
        print(f"File {path} not found")
        return None


def add_contact(args, path: str = PATH):
    name, phone = args

    contacts = get_contact_info(path)

    if name in contacts:
        return f"Contact {name} is already exists"
    else:
        contact = name, phone
        contacts[name] = phone
        save_contact(contact)
        return "Contact added."


def change_contact(args, path: str = PATH):
    name, phone = args

    # contacts.update({name: phone})
    return "Contact updated."


def show_phone(name):
    phone = 0
    return f"{phone}"


def show_all():
    contacts = get_contact_info(PATH)
    if len(contacts):
        return f"{contacts}"
    else:
        return "There is no contacts"


def bot_main(path: str = PATH):

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        try:
            command, *args = parse_input(user_input)
            if command in ["exit", "close"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                try:
                    print(add_contact(args))
                except ValueError as e:
                    print("Please, enter name and phone")
            elif command == "change":
                try:
                    print(change_contact(args))
                except ValueError as e:
                    print("Please, enter name and new phone")
            elif command == "phone":
                try:
                    print(show_phone(args))
                except ValueError as e:
                    print("Please, enter a name")
            elif command == "all":
                print(show_all())
            else:
                print("Invalid command.")
        except Exception:
            print("Please, enter a command.")


if __name__ == "__main__":
    bot_main()
