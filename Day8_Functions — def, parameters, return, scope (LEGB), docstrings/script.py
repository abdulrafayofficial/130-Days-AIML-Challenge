def calcSum(a,b):
    print(a+b)
    return a+b

calcSum(3,4)
sum = calcSum(5,10)
print(sum)


def calcAvg(a,b,c):
    sum = a+b+c
    avg = sum/3
    return avg

avg = calcAvg(96,23,54)
print(avg)


# parameters vs Arguments
# parameters = placeholders for the actual values while declaring values (P_P)
# arguments = Actual values (A_A)



# =====================================================================
# =====================================================================
# =====================================================================

#DocStrings in Python:

'''
    This is a function of printing the difference of two variables.
'''

def calcDifference(a,b):
    '''
    This is a function of printing the difference of two variables.
    '''
    return a-b
print(calcDifference(5,3))
print(calcDifference.__doc__)

