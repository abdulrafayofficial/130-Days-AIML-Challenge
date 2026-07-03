
                        # expression: the value you want to store in the set
                        # item: each element you get from the iterable
                        # iterable: something you can loop over, like a list, tuple, string, or range


# List Comprehensions
# Syntax:
        # newlist = [expression for item in iterable if condition == True]
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# The condition is optional and can be omitted:
# The expression is the current item in the iteration


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#Traditional way:
new_list = []
for fruit in fruits:
    if 'a' in fruit:
        new_list.append(fruit)

print(new_list)

#List Comprehension:(cool way!)

newlist = [fruit for fruit in fruits if 'a' in fruit]
print(newlist)


newlist = [x for x in range(10) if x < 5]
print(newlist)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Dictionary Comprehension:
                        # create dictionaries using an expression
                        # can replace for loops and certain lambda functions

                # Syntax:
                        # dictionary = {key:expression for (key,value) in iterable}
                        # dictionary = {key:expression for (key,value) in iterable if condition} --> with condition
                        # dictionary = {key:if/else for (key,value) in iterable} --> with if/else

cities_in_F = {'NewYork':32, 'Boston':75, 'Los Angeles':100, 'Chicago':50}
cities_in_C = {key:round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)


weathers = {'NewYork':'snowing', 'Boston':'sunny', 'Los Angeles':'sunny', 'Chicago':'cloudy'}
sunny_weather = {key:value for (key,value) in weathers.items() if value == 'sunny'}
print(sunny_weather)

cities = {'NewYork':32, 'Boston':75, 'Los Angeles':100, 'Chicago':50}
desc_cities = {key:('WARM' if value >=40 else 'COLD') for (key,value) in cities.items()}
print(desc_cities)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Set Comprehension:

        # Syntax:
                # {expression for item in iterable [if condition]}--> condition is optional
                # {expression for item in iterable if condition}



nums = {1,2,3,4,5}
values = {n for n in nums}
squares = {n*n for n in nums}
print(values)
print(squares)


even_squares = {n*n for n in range(11) if n%2 == 0}
print(even_squares)

labels = {"even" if n %2 ==0 else "odd" for n in range(1,6)}
print(labels)# {'even', 'odd'} --> set automatically removes duplicates ahahahhaha



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Nested List Comprehension

# Nested List Comprehensions are nothing but a list comprehension within another list comprehension which is quite similar to nested for loops.

#               Syntax:
                # new_list = [[expr for item in inner_iterable] for item in outer_iterable]

new_list = []
for i in range(6,8):
    inner = []
    for j in range(4,7):
        result = i*j
        inner.append(result)
    new_list.append(inner)

print(new_list)

lst = [[i*j for j in range(4,7)] for i in range(6,8)]
print(lst)