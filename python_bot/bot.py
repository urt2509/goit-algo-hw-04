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


def update_contact(contact):
    path = PATH
    name, phone = contact
    contacts = get_contact_info(path)
    name = name.strip()
    phone = phone.strip()
    contacts[name] = phone
    try:
        with open(path, "w", encoding="utf-8") as file:
            for name in contacts:
                file.write(f"{name}:{contacts[name]}\n")

    except FileNotFoundError:
        print(f"File {path} not found")


def add_contact(args, path: str = PATH):
    try:
        name, phone = args
        contacts = get_contact_info(path)
        if name in contacts:
            print(f"Contact {name} is already exists")
        else:
            contact = name, phone
            contacts[name] = phone
            save_contact(contact)
            print("Contact added.")
    except ValueError as e:
        print("Please, enter name and phone")


def change_contact(args, path: str = PATH):
    try:
        name, phone = args
        contacts = get_contact_info(path)
        if name in contacts:
            contact = name, phone
            update_contact(contact)
            print("Contact updated.")
        else:
            print(f"There is no contact {name}")
    except ValueError as e:
        print("Please, enter name and new phone")


def show_phone(args, path: str = PATH):
    try:
        name, *args = args
        contacts = get_contact_info(path)
        if name in contacts:
            print(contacts.get(name))
        else:
            print(f"There is no contact {name}")
    except ValueError as e:
        print("Please, enter a name")


def show_all():
    path = PATH
    contacts = get_contact_info(path)
    if len(contacts):
        print(f"{contacts}")
    else:
        print("There are no contacts")


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
                add_contact(args)
            elif command == "change":
                change_contact(args)
            elif command == "phone":
                show_phone(args)
            elif command == "all":
                show_all()
            else:
                print("Invalid command.")
        except Exception:
            print("Please, enter a command.")


if __name__ == "__main__":
    bot_main()
