from input_output_module import load_contacts
from logic_module import addContact, viewContact, searchContact, delContact

contact_list = {}

load_contacts(contact_list)

is_Running = True

while is_Running:
    print("Please Enter the desired Operation")
    print("1: Add | 2: View | 3: Search | 4: Delete | 5: Exit")

    try:
        option = int(input())
    except ValueError:
        print('Sirf numbers 1-5 enter karo!')
        continue

    if option == 1:
        addContact(contact_list)
    elif option == 2:
        viewContact(contact_list)
    elif option == 3:
        searchContact(contact_list)
    elif option == 4:
        delContact(contact_list)
    elif option == 5:
        is_Running = False