# Student Grade Manager...:

import os
import csv

student_info = {}
file_path = r'C:\Users\SL\OneDrive\Desktop\Study Corner\Python\Day 130 Challenge\Day14_REVIEW + Mini Project\file.csv'

def addStudent():
    name = input('Enter Your Name: ').lower()

    if name in student_info:
        print('Student already exists!')
        return

    rollNo = int(input('Enter your Roll Number: '))
    student_info[name] = {'roll':rollNo, 'marks':{}}

    print(student_info)
 

def addMarks():
    name = input('Whose marks are we adding? ')
    if name not in student_info:
        print('Student does not Exist!')
        return

    subjects = int(input('For how many subjects do we need to enter marks? '))
    for subject in range(subjects):
        subject_name = input('Enter the subject name: ').lower()
        marks = int(input(f'Enter your Marks in {subject_name}: '))

        student_info[name]['marks'][subject_name] = marks

        print(student_info)


def calGPA():
    name = input('Whose GPA are we calculating?').lower()
    if name not in student_info:
        print('Student does not Exist!')
        return
    
    if len(student_info[name]['marks']) ==0:
        print('No marks Entered!!')
        return
    

    total = 0
    avg = 0

    for values in student_info[name]['marks'].values():
        total += values
        
    print(total)
    avg = total / len(student_info[name]['marks'])
    print(f'Averge marks: {avg:.2f}')
    gpa = (avg/100)*4
    print(f'GPA: {gpa:.2f}')


def saveFile():
    with open(file_path,'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'roll', 'subject', 'marks'])
        for name, data in student_info.items():
            for subject, marks in data['marks'].items():
                writer.writerow([name, data['roll'], subject, marks])


def loadFile():
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r', newline='') as f:
                reader = csv.reader(f)
                next(reader) 
                
                for row in reader:
                    name = row[0]
                    roll = int(row[1])      
                    subject = row[2]
                    marks = int(row[3])    
                    
                    if name not in student_info:
                        student_info[name] = {'roll': roll, 'marks': {}}
                    
                    student_info[name]['marks'][subject] = marks
                
    except FileNotFoundError:
        print("No file found!")

loadFile()


isRunning = True
while isRunning:
    print("Enter one of 3 options:")
    option = int(input('1: Add Student , 2: Add Marks, 3:Calculte GPA , 4: Save and Exit Program '))

    if option == 1:
        addStudent()

    elif option == 2:
        addMarks()

    elif option == 3:
        calGPA()

    elif option == 4:
        saveFile() 
        break


