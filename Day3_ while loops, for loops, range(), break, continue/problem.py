''' 
#Multiplication Table using for loop

num = int(input("Enter the number you want the table of: "))

for i in range(1,11):
    print(f"{num} * {i} = {num*i}")


#Multiplication Table using While loop

num2 = int(input("Enter an another number yOu want the table of: "))
i = 1
while(i<=10):
    print(f"{num2} * {i} = {num2*i}")
    i+=1

    '''

#----------------------------------------------------------------------

#Pattern Questions:

#Pattern1--> Right Triangle
'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
'''
n = 5
for i in range(n+1):
    for j in range(i+1):
        print("*" , end=" ")
    print()


#----------------------------------------------------------------------


'''
* * * * * * * * 
* * * * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''

a = int(input("Enter the number of Columns: "))
for i in range(a):
    for j in range(i , a):
        print("*", end=" ")

    print()

#----------------------------------------------------------------------


    



