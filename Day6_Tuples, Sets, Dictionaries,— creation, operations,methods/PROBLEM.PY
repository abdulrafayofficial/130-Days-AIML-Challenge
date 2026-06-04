text = "Another productive way to use this tool to begin a daily writing routine. One way is to generate a random paragraph with the intention to try to rewrite it while still keeping the original meaning. The purpose here is to just get the writing started so that when the writer goes onto their day's writing projects, words are already flowing from their fingers."

word_list = text.lower().replace(".","").replace(",","").split()

words = {

}

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