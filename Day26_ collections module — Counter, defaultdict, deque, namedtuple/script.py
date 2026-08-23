from collections import Counter

words = ["A","B","C","D","E","F","A","F","D","D"]

def get_counter(words):
    dct = {}
    for w in words:
        if w in dct:
            dct[w] +=1

        else:
            dct[w] = 1
    return dct

result = get_counter(words)
print(result)


count = Counter(words)
print(count)
print(count["A"])



# ------------- defaultdict------------
#A dictionary that creates default values for missing keys automatically.

from collections import defaultdict


scores = defaultdict(int)
scores["AbdulRafay"] += 10
scores["Hamza"] += 5

print(scores["Huzaifa"])
print(scores) #Automatically assigned 0 to key huzaifa 

# print(int())



#-----------------------------------------
#------------   deque in python!  -----------------------------

from collections import deque
people = ['AbdulRafay','Hamza','Azan','Huzaifa']
queue = deque(people)
queue.append('AbdulWasay')
queue.popleft() #Normally we donot have popleft method

queue.rotate(-1) #moves everyone to one left position
queue.rotate() #moves everyone to one right position

queue.reverse()
print(queue)



#-------------------------------------------------
#------------------ namedtuple -------------------

from collections import namedtuple

# color = (55,155,255)
Color = namedtuple('Color',['red','green','blue'])
color = Color(55,155,255)
print(color.red)
print(color.green)
print(color.blue)



#-------------------------------------------------
#----------------- Warmup practice tasks ---------

text = "python python java python c++ java"
p = text.split()
result = Counter(p)
print(result)




names = ['ali','ahmad','bilal','basit','usman']
grouped = defaultdict(list)
for name in names:
    first_letter = name[0]
    grouped[first_letter].append(name)

print(dict(grouped))