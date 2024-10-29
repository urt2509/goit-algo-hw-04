PATH = "./contacts.txt"


def get_contact_info(path: str = PATH) -> list[dict]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            contacts = [dict(line.strip().split(" ") for line in file)]
            # print(f"There are contacts from file: {contacts}") already done

        return contacts

    except FileNotFoundError:
        print(f"File {path} not found")
        return None

    except Exception as e:
        print(f"Hello An unexpected error occurred: {e}")
        return []


def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except Exception as e:
        raise e


def save_contact(path, contacts):
    try:
        with open(path, "w", encoding="utf-8") as file:
            for name, phone in contacts.items():
                file.write(f"{name}: {phone} \n")

    except FileNotFoundError:
        print(f"File {path} not found")
        return None


# def add_contact(args, contacts):
#     name, phone = args

#     if name in contacts:
#         return f"This contact {name} with phone number {phone} is already exists"
#     else:
#         contacts.update({name: phone})
#         save_contact(PATH, contacts)
#         print(contacts)
#         return "Contact added."


def add_contact(args, path: str = PATH):
    name, phone = args
    # print(name, phone) already done

    contacts = get_contact_info(path)
    # print(f"This is add contacts {contacts}")  already done

    if name in contacts:
        print(name)  # NOT YET DOING
        return f"This contact {name} with phone number {phone} is already exists"
    else:
        contacts[name] = phone
        save_contact(PATH, contacts)
        print(contacts)
        return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    contacts.update({name: phone})
    return "Contact updated."


def bot_main(path: str = PATH):

    contacts = get_contact_info(path)
    # print(f"This is a contact_list {contacts} from file {path}") already done
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
                    # print(add_contact(args, contacts))
                    print(add_contact(args))
                except ValueError as e:
                    print("hello", e)
            elif command == "change":
                try:
                    print(change_contact(args, contacts))
                except ValueError as e:
                    print(e)
            else:
                print("Invalid command.")
        except Exception:
            print("Please, enter a command.")


if __name__ == "__main__":
    bot_main()
