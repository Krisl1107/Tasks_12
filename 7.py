text=input()
words=text.split()
min_word=[]
for el in words:
    min_word.append(len(el))
print(min(min_word))
