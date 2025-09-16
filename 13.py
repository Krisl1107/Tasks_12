def even(x):
    return (len(str(x)))%2==0

def sum_ch(x):
    k=0
    for ch in x:
        k+=int(ch)
    return k

def sum(x):
    mdl=(len(str(x)))//2
    str_1=str(x)[:mdl]
    str_2 = str(x)[mdl:]
    if sum_ch(str_1)==sum_ch(str_2):
        return True
    else:
        return False

num=int(input())
n=1
while ((even(num)) +( sum(num)))!=2:
    num = int(input())
    n+=1
else:
    print(n)
