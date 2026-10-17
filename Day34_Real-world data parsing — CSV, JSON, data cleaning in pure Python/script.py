print('hello world')
import csv
import json



#File Handling
file_path = r'C:\Users\SL\OneDrive\Desktop\Study Corner\Python\Day 130 Challenge\Day34_Real-world data parsing — CSV, JSON, data cleaning in pure Python\test.txt'


csv_file_path = r"Day34_Real-world data parsing — CSV, JSON, data cleaning in pure Python\students.csv"

with open(file_path,'r',encoding="utf-8") as f:
    content = f.read()
    print(content)


with open(file_path,'r',encoding="utf-8") as f:
    for line in f:
        print(line.strip())

with open(csv_file_path,'r',encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(',')
        print(parts)

print()

#csv more accurate!!!
with open(csv_file_path,'r',encoding="utf-8",newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
    
#csv.DictReader
with open(csv_file_path,'r',encoding='utf-8',newline="") as f:
    reader = csv.DictReader(f)
    total_age = 0
    count = 0
    for row in reader:
        # print(row["name"],row["age"])
        print(row['name'],'lives in ',row['city'])
        total_age += int(row['age'])
        count +=1
    average_age = total_age/count
    print('Average Age: ',average_age)

#Writing in csv file:

output_path = r"C:\Users\SL\OneDrive\Desktop\Study Corner\Python\Day 130 Challenge\Day34_Real-world data parsing — CSV, JSON, data cleaning in pure Python\output.csv"
rows = [
    ["name", "age", "city"],
    ["Ali", 21, "Karachi"],
    ["Sara", 22, "Lahore"],
]
with open(output_path,'w',encoding='utf-8',newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['name','age','city']) # for writing one row
    writer.writerows(rows[1:]) # for writing multiple rows

students = [
    {"name": "Ali", "age": 21, "city": "Karachi"},
    {"name": "Sara", "age": 22, "city": "Lahore"},
    {"name": "Usman", "age": 23, "city": "Karachi, Sindh"},
]
clean_csv_output = r"C:\Users\SL\OneDrive\Desktop\Study Corner\Python\Day 130 Challenge\Day34_Real-world data parsing — CSV, JSON, data cleaning in pure Python\clean_students.csv"

fieldnames = ['name','age','city']
with open(clean_csv_output,'w',encoding='utf-8',newline="") as f:
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)


print('==========================================================')
print('-------------------JSON read/write --------------------')
print('==========================================================')


print('json.dump() ---> Writing in file.... : ')

student = {
    "name": "Ali",
    "age": 21,
    "city": "Karachi",
    "skills": ["Python", "SQL"],
    "is_student": True
}
student_JSON =  r"C:\Users\SL\OneDrive\Desktop\Study Corner\Python\Day 130 Challenge\Day34_Real-world data parsing — CSV, JSON, data cleaning in pure Python\student.json"

with open(student_JSON,"w",encoding="utf-8") as f:
    json.dump(student,f,indent=4)


print('json.load() ---> Reading in file.... : ')

with open(student_JSON,'r',encoding='utf-8') as f:
    data = json.load(f)

print(data)
print(data['name'])
print(data['skills'][0])
print(type(data))


print('json.loads() and json.dumps() ----> works with strings... : ')

text = json.dumps(student)
print(text)
print(type(text))

back = json.loads(text)
print(type(back))


print('-----------Data Cleaning----------')

dirty_students =  r"C:\Users\SL\OneDrive\Desktop\Study Corner\Python\Day 130 Challenge\Day34_Real-world data parsing — CSV, JSON, data cleaning in pure Python\dirty_students.csv"
dirty_rows = [
    ["name", "age", "city"],
    ["  Ali ", "21", "KARACHI"],
    ["sara", "22", "lahore"],
    ["Usman", "abc", "Karachi"],
    ["Ahmed", "", "Islamabad"],
    ["Ali", "21", "karachi"],
    ["Zara", "-5", "Lahore"],
    ["Bilal", "25", "  Multan"],
]
with open(dirty_students,'w',encoding='utf-8',newline="") as f:
    writer = csv.writer(f)
    writer.writerows(dirty_rows)
    #checking data:
with open(dirty_students, 'r', encoding='utf-8', newline="") as f:
    rows = list(csv.DictReader(f))

# print('Total rows: ',len(rows))

cleaned = []
removed = 0
duplicates = 0
seen = set()


def clean_age(value):
    try: 
        age = int(value)
    except ValueError:
        return None
    if age < 0  or age > 100:
        return None

    return age

for row in rows:
    name = row['name'].strip().title()
    city = row['city'].strip().title()
    age = clean_age(row['age'])

    if not name or age is None:
        removed += 1
        continue

    key = (name,age,city)
    if key in seen:
        duplicates += 1
        continue    
    seen.add(key)

    cleaned.append({'name':name, 'age':age, 'city':city})


ages = [row['age'] for row in cleaned]
mean_age = sum(ages) / len(ages)
min_age = min(ages)
max_age = max(ages)
print("Mean:", mean_age)
print("Min:", min_age)
print("Max:", max_age)


print("Removed bad rows:", removed)
print("Removed duplicates:", duplicates)
print("Clean rows:", len(cleaned))
for row in cleaned:
    print(row)


clean_output =  r"C:\Users\SL\OneDrive\Desktop\Study Corner\Python\Day 130 Challenge\Day34_Real-world data parsing — CSV, JSON, data cleaning in pure Python\clean_output_final.csv"

with open(clean_output,'w',encoding='utf-8',newline="") as f:
    writer = csv.DictWriter(f, fieldnames= ['name','age','city'])
    writer.writeheader()
    writer.writerows(cleaned)

print('cleaned data saved!')