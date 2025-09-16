def dbl_lttr(x):
    aw=""
    for ch in x:
        if x.count(ch)!=1:
            aw="false"
            break
        else:
            continue
    if aw=="false":
        return False
    else:
        return True

text=input()
words=text.split()
word_1=words[0]
for el in words:
    if (el!=word_1)+(dbl_lttr(el))==2:
        print(el)
