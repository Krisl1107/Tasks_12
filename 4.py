text=input()
for ch in text:
    c=text.count(ch)
    if c==3:
        print(ch)
        break
