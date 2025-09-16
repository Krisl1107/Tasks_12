text=input()
words=text.split()
win=""
for i in range(0,len(words)-1):
    if (words[i])[-1]== ((words[i+1])[0]).lower():
        continue
    else:
        if i%2==0:
            win="Победил Петя"
        else:
            win = "Победил Вася"

if win=="":
 if len(words)%2==0:
    win = "Победил Вася"
 else:
    win="Победил Петя"

print(win)
