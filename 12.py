import keyword

def k(x):
    return keyword.iskeyword(x)

def letters(x):
 return (ord(x) in range(65,91))+(ord(x) in range(97,123))==1

def nbrs(x):
 return (ord(x) in range(48,58))


def s_n(x):
 k=0
 for ch in x:
    if ((ord(ch)==95)+ letters(ch) + nbrs(ch))==1:
        k+=1
 return k==len(x)



def num(x):
    return x[0].isdigit()

text=input()
if (k(text))+(num(text))==0 and s_n(text)==1:
    print("Строка может быть именем в языке Python ")
else:
    print("Строка не может быть именем в языке Python ")
