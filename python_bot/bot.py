def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except Exception as e:
        raise e


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def main():
    contacts = {}
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
                    print(add_contact(args, contacts))
                except ValueError as e:
                    print(e)
            else:
                print("Invalid command.")
        except Exception:
            print("Please, enter a command.")


if __name__ == "__main__":
    main()
