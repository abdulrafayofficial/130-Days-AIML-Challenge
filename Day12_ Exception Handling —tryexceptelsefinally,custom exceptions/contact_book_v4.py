import csv
import os

class invalidNameError(Exception):
    pass

class invalidPhoneNumberError(Exception):
    pass

contact_list = {}

def addContact():
    try:
        name = input("Enter the name you want to add in your contact list: ").lower()
        if name == '' or len(name) < 2:
            raise invalidNameError
    except invalidNameError:
        print('Name should Not be empty!')
        return
    
    try:
        contact = input("Enter the contact number: ")
        if not contact.isdigit():
            raise invalidPhoneNumberError
    except invalidPhoneNumberError:
        print('Contact Number should only contain numbers.')
        return

   
    contact_list[name] = contact
    print("Added Successfully")
    save_contacts()

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

def load_contacts():
    try:
        if os.path.exists("Day11_File IO — open, read,write, append, with statement, CSV basics\\contacts.csv"):
            with open(r"Day11_File IO — open, read,write, append, with statement, CSV basics\\contacts.csv","r") as contacts_csv:
                contacts_csv = csv.reader(contacts_csv)
                for line in contacts_csv:
                    contact_list[line[0]] = line[1]
    except FileNotFoundError as e:
        print(f'Error{e}')

def save_contacts():
    with open(r"Day11_File IO — open, read,write, append, with statement, CSV basics\\contacts.csv","w")as f:
        writer = csv.writer(f)
        for name, contact in contact_list.items():
            writer.writerow([name, contact])


    


def delContact():
    d = input("Enter the name you want to delete in the Contact list: ").lower()
    if d in contact_list:
        contact_list.pop(d)
        print(f"{d} deleted successfully!")
    else:
        print(f"{d} is not in the Contact list!")
    
    save_contacts()

load_contacts() 

is_Running = True

while is_Running:
    print("Please Enter the desired Operation")
    print("1: Add contact , 2: View Contact , 3: Search Contact , 4: Delete Contact , 5: Exit Program")

    try:
        option = int(input())
    except:
        print('only numbers from 1-5 are allowed to enter!')
        continue

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






    

    


