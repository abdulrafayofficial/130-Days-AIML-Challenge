from input_output_module import save_contacts

class invalidNameError(Exception):
    pass

class invalidPhoneNumberError(Exception):
    pass

def addContact(contact_list):  
    try:
        name = input("Enter the name you want to add: ").lower()
        if name == '' or len(name) < 2:
            raise invalidNameError
    except invalidNameError:
        print('Name should not be empty!')
        return
    
    try:
        contact = input("Enter the contact number: ")
        if not contact.isdigit():
            raise invalidPhoneNumberError
    except invalidPhoneNumberError:
        print('Contact number should only contain numbers.')
        return
    
    contact_list[name] = contact
    print("Added Successfully")
    save_contacts(contact_list)  

def viewContact(contact_list):  
    for name, contact in contact_list.items():
        print(f"{name} : {contact}")

def searchContact(contact_list):  
    search = input("Enter the name to search: ").lower()
    if search in contact_list:
        print(contact_list[search])
        print(f"{search} is present!")
    else:
        print(f"{search} is NOT in the contact list!")

def delContact(contact_list):  
    d = input("Enter the name to delete: ").lower()
    if d in contact_list:
        contact_list.pop(d)
        print(f"{d} deleted successfully!")
        save_contacts(contact_list)  
    else:
        print(f"{d} is not in the contact list!")