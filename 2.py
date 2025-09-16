text=input()
s=0
quantity=[]
pr_ch=""
for ch in text:
    if ch == pr_ch:
        s+=1
    else:
        quantity.append(s)
        s=0
    pr_ch=ch
print(max(quantity)+1)
