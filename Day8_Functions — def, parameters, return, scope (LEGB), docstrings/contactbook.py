contact_list = {}

def addContact():
    name = input("Enter the name you want to add in your contact list: ").lower()
    contact = input("Enter the contact number: ")
    contact_list[name] = contact
    print("Added Successfully")

def viewContact():
    for name, contact in contact_list.items():
        print(f"{name} : {contact}")

def searchContact():
    search = input("Enter the name you want to search in contact list: ").lower()
    if search in contact_list:
        print(contact_list[search])
        print(f"{search} is present in the contact list!")
    else:
        print(f"{search} is NOT in the contact list!")


def delContact():
    d = input("Enter the name you want to delete in the Contact list: ").lower()
    if d in contact_list:
        contact_list.pop(d)
        print(f"{d} deleted successfully!")
    else:
        print(f"{d} is not in the Contact list!")

is_Running = True

while is_Running:
    print("Please Enter the desired Operation")
    print("1: Add contact , 2: View Contact , 3: Search Contact , 4: Delete Contact , 5: Exit Program")

    option = int(input())

    if(option == 1):
        print(addContact())
    elif(option == 2):
        viewContact()
    elif(option == 3):
        searchContact()
    elif(option == 4):
        delContact()
    elif(option == 5):
        is_Running = False






    

    


