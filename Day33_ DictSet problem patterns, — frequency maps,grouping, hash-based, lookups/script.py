strg = 'abdulrafay'
freq = {}

for i in strg:
    freq[i] = freq.get(i,0) + 1


for i in strg:
    if freq[i] == 1:
        print(i)
        break

else:
    print('No Non-repeating Value.')


#------------------Problem 2 (Group Anagrams)-------------------------------

# print(sorted('eat'))
# print("".join(sorted('eat')))
# print("".join(sorted('tea')))

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}

for word in words:
    key = "".join(sorted(word))
    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print(list(groups.values()))


#------------------Longest Consecutive Sequence.-------------------------------

nums = [100, 4, 200, 1, 3, 2]
s = set(nums)
longest = 0

for num in nums:
    if num - 1 not in s:
        length = 1

        while num + length in s:
            length +=1


        if length > longest:
            longest = length 

print(longest)

