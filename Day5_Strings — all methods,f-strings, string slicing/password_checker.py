#Password Generator!!

Rules = '''
Rule1 : Length should be atleast 8 characters
Rule2 : Atleast one letter should be Uppercase
Rule3 : Atleast one letter should be lowercase
Rule4 : There should be atleast one one number(digit)
Rule5 : There should be atleast one special Character (@, #, $)    
'''

print(Rules)
password = input("Enter your password: ")
score = 5


has_upper = False
has_lower = False
has_digit = False
has_special = False

for x in password:
    if x.isupper():
        has_upper = True
    elif x.islower():
        has_lower = True
    elif x.isdigit():
        has_digit = True
    elif x in "@#$":
        has_special = True

if len(password) < 8:
    print("Password length less than 8")
    score -= 1
if not has_upper:
    print("Atleast one character should be in UpperCase")
    score -=1
if not has_lower:
    print("Atleast one character should be in lowerCase")
    score -=1
if not has_digit:
    print("There should be atleast one digit")
    score -=1
if not has_special:
    print("One special character is required!")
    score -=1

    

    

print(f"Your score is {score}/5")
if score ==5:
    print("Congratulations your password is perfect")

    





