def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def change_contact_phone(username, new_phone, contacts):
    if username in contacts:
        contacts[username] = new_phone
        return f"Phone number for {username} changed to {new_phone}."
    else:
        return f"Contact {username} not found in the contacts list."

def all_contacts(contacts):
    # Перевірити, чи є контакти для відображення
    if not contacts:
        return "No contacts available."
    # Вивести всі збережені контакти у консоль
    print("All contacts:")
    for name, phone_number in contacts.items():
        print(f"{name}: {phone_number}")

def get_phone_by_username(username, contacts):
    if username in contacts:
        return f"The phone number for {username} is {contacts[username]}."
    else:
        return f"Contact {username} not found in the contacts list."
