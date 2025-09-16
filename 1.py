text=input()
c=" "
sp=0
quantity=[]
for ch in text:
    if ch==c:
        sp+=1
    else:
        quantity.append(sp)
        sp=0
print(max(quantity))
