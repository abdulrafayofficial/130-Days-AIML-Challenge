'''

text = "Another productive way to use this tool to begin a daily writing routine. One way is to generate a random paragraph with the intention to try to rewrite it while still keeping the original meaning. The purpose here is to just get the writing started so that when the writer goes onto their day's writing projects, words are already flowing from their fingers."

word_list = text.lower().replace(".","").replace(",","").split()



words = {word:word_list.count(word) for word in word_list}

for w in word_list:
    if w in words:
        words[w] += 1
    else:
        words[w] = 1

# print(words)

sorted_words = sorted(words.items(),key= lambda x:x[1], reverse = True)
print(sorted_words)

print("Top 5 Words")
for word,count in sorted_words[:5]:
    print(f"{word}: {count}")
'''

#------------------------------------------------------------------------------------
# 1 se 20 tak sirf odd numbers ki list
odd_list = [x for x in range(1,21) if x%2 != 0]
print(odd_list)

#------------------------------------------------------------------------------------
# 1 se 50 tak sirf even numbers ka set

even_set = { x for x in range(1,51) if x % 2 == 0}
print(even_set)

#------------------------------------------------------------------------------------
# Words ki list mein se sirf 3+ letters wale words

para = 'The trees, therefore, must be such old and primitive techniques that they thought nothing of them, deeming them so inconsequential that even savages like us would know of them and not be suspicious. At that, they probably didnt have too much time after they detected us orbiting and intending to land. And if that were true, there could be only one place where their civilization was hidden'

wanted_words = {}

words = para.lower().replace('.',"").replace(',',"").split()

for word in words:
    if word in wanted_words:
        wanted_words[word] +=1
    else:
        wanted_words[word] = 1

print(wanted_words)

sorted_words = sorted(wanted_words.items(),key = lambda x:x[1], reverse = True)
print(sorted_words)

print("Top 5 Words")
for word,count in sorted_words[:5]:
    print(f"{word}: {count}")

#------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------
# 1 se 100 tak sirf 3 aur 5 dono se divisible numbers

lst = [x for x in range(1,101) if x%3==0 and x%5==0]
print(lst)

#------------------------------------------------------------------------------------
# Numbers ki list mein se sirf positive numbers
lst = [x for x in range(-50,51) if x>0]
print(lst)

#------------------------------------------------------------------------------------
# Words ki list mein har word ko uppercase mein convert karo

words = ['ali','ahmad','rafay','hamza']
upper_case_words = [word.upper() for word in words]
print(upper_case_words)

#------------------------------------------------------------------------------------


# Nested list — 2*2 matrix banao jahan value i+j ho

nums = [ [i + j for j in range(4,8)]for i in range(1,4)]
print(nums)