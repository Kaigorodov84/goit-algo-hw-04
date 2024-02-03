def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def change_username_phone(command, contacts):
    command_parts = command.split() #розділ команди на слова
    if len (command_parts) != 3: # перевірка чи достатньо символів  
        return "Invalid command. U: change username phone"
    #витягуєм нове ім'я та номер телефону 
    username = command_parts[1]
    new_phone = command_parts[2]
    #перевіряєм чи контакт існує в списку
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
        