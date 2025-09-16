def letters(x,y):
    if x[-1]=="ь" or x[-1]=="ы" :
        if x[-2]==y[0]:
            return True
        else:
            return False

def right(x,y):
    if x[-1] == y[0].lower():
        return True
    else:
        return False


text=input()
words=text.split()
win=""
for i in range(0,len(words)-1):
    if (right(words[i],words[i+1])) and (letters(words[i],words[i+1].lower())):
        continue
    else:
        if i%2==0:
            win="Победил Петя"
        else:
            win = "Победил Вася"
        break


if win=="":
 if len(words)%2==0:
    win = "Победил Вася"
 else:
    win="Победил Петя"

print(win)
