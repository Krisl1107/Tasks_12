str1=input()
str2=input()
str3=input()
u_ch=set()
for ch in (str1+str2+str3):
    if (ch in str1) + (ch in str2) + (ch in str3)==1:
        u_ch.add(ch)
print(*u_ch)
