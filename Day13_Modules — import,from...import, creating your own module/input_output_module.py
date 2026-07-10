import csv
import os

file_path = 'Day13_Modules — import,from...import, creating your own module\contact_update.csv'

def load_contacts(contact_list):  
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                for line in reader:
                    contact_list[line[0]] = line[1]
    except FileNotFoundError as e:
        print(f'Error: {e}')

def save_contacts(contact_list): 
    with open(file_path, 'w') as f:
        writer = csv.writer(f)
        for name, contact in contact_list.items():
            writer.writerow([name, contact])