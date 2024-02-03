from contacts_function import add_contact, parse_input, change_contact_phone, all_contacts, get_phone_by_username

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            # Перевірка, чи є досить аргументів для зміни номера телефону
            if len(args) != 2:
                print("Invalid command. Usage: change username new_phone")
            else:
                username, new_phone = args
                print(change_contact_phone(username, new_phone, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        elif command == "phone":
            if len(args) != 1:
                print("Invalid command. Usage: phone username")
            else:
                username = args[0]
                print(get_phone_by_username(username, contacts))
        else:
            print("Invalid command.")    

if __name__ == "__main__":
    main()

