text=input()
words=text.split()
for el in words:
     if words.count(el)==2:
         print(el)
         break
