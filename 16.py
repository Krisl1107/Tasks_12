text=input()
c=[]
k=[]
aw=""
for ch in text:
    match ch:
     case "(":
        c.append(ch)
     case ")":
         if c != k:
          c.remove("(")
         else:
          c.append("")
          break
if c==k:
    print("Скобки расставлены правильно")
else:
    print("Скобки расставлены неправильно")
