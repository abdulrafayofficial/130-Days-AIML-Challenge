contact_list = {}
while True:
    print("Please Enter Your Desired Operation: ")
    print("1: Add contact , 2: View Contact , 3: Search Contact , 4: Delete Contact , 5: Exit Program")
    option = int(input())

    if(option == 1):
       name =  input("Enter your Name: ").lower()
       contact_no =  input("Enter your Contact Number: ")
       contact_list[name] = contact_no

    elif(option ==2):
        print(contact_list)
    
    elif(option ==3):
        search = input("Enter the name you want to search: ").lower()
        if search in contact_list:
            print(contact_list[search])
            print("Contact is present in the List!!!")
        else:
            print("Contact is not in the list.")

    elif(option ==4):
        del_contact = input("Enter the name of the contact no you want to delete: ").lower()
        if del_contact in contact_list:
            contact_list.pop(del_contact)
        
    elif(option == 5):
        break
       

    

    
print(contact_list)