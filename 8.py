text=input()
words=text.split()
sort_words=sorted(words, key=len)
print(" ".join(sort_words))
