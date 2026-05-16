# Grade Calculator....

marks = float(input("Enter Your Marks: "))
if marks >= 80 and marks <=100:
    print("Your Grade is A!")
elif marks >=70 and marks<80:
    print("Your Grade is B!")
elif marks >=60 and marks<70:
    print("Your Grade is C!")
elif marks >=50 and marks<60:
    print("Your Grade is D!")
elif marks >=40 and marks<50:
    print("Your Grade is E!")
elif marks < 40 and marks>= 0:
    print("Your Grade is F!")
elif marks < 0:
    print("Marks cannot be in negative numbers .")
else:
    print("Invalid Choice Please Enter Your marks in Numbers Between 1-100")



#Tax Calculator

income = float(input("Enter Your Income: "))
if income < 0:
    print("Enter a Positive Number")
elif income>= 0 and income <= 10000:
    print("10% Tax is Applied")
    print(f"Your Tax Amount is : {income * 0.10 : .2f}")
elif income >10000 and income<=20000:
    print("12% Tax is Applied")
    print(f"Your Tax Amount is : {income * 0.12 : .2f}")

elif income >20000 and income <=30000:
    print("15% Tax is Applied")
    print(f"Your Tax Amount is : {income * 0.15 : .2f}")

else:
    print("17% Tax is Applied")
    print(f"Your Tax Amount is : {income * 0.17 : .2f}")



