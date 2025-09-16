def chk(x):
    if len(x) != 4:
        return False
    else:
        return True

def chk_2(x):
    for ch in x:
       if x.count(ch) != 1:
         return False
       else:
           return True

def b_c(x,y):
    b=0
    c=0
    for ch in x:
        if ch in y:
            c+=1
    for i in range(len(y)):
        if x[i]==y[i]:
            b+=1
            c-=1
    return print("Быков: ",b,"Коров:",c)


def game():
    win=""
    num_1= input("Введите четырёхзначное число, с неповторяющимися цифрами")
    while chk(num_1)+ chk_2(num_1)!=2:
        num_1 = input("Введите четырёхзначное число, с неповторяющимися цифрами")
    print("\n" * 25)
    for i in range(10):
        num_2=input("Ваше число")
        b_c(num_2,num_1)
        if num_1==num_2:
            win = "Победа"
            break
        else:
          continue

    if win=="":
        print("Вы проиграли")
    else:
        print(win)

game()
