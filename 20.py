un_1=["один","два"]
un_2=["одна","две"]
un=["","один","два","три","четыре","пять","шесть","семь","восемь","девять"]
teens = [
    "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
    "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]

tens = [
    "", "десять", "двадцать", "тридцать", "сорок",
    "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]

hun = [
    "", "сто", "двести", "триста", "четыреста",
    "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]


def num_1(x):
    print(un[int(x)])


def num_2(x):
    match int(x[0]):
     case 0:
        print(num_1(int(x[-1])))
     case 1:
        print(teens[int(x[-1])])
     case y if 2<=y<=9:
        print(tens[int(x[0])],end=" ")
        (num_1(int(x[-1])))


def num_3(x):
    s_1=x[-2:]
    print(hun[int(x[0])],end=" ")
    (num_2(s_1))


def num_4(x):
    s_1=x[-3:]
    match int(x[0]):
        case 0:
            print("тысяч",end=" " )
        case 1:
          print(un_2[0],"тысяча",end=" " )
        case 2:
          print(un_2[1], "тысячи", end=" ")
        case y if 3<=y<=4:
          print(un[int(x[0])], "тысячи", end=" ")
        case y if 5<=y<=9:
          print(un[int(x[0])], "тысяч",end=" ")
    (num_3(s_1))


def num_5(x):
    s_1 = x[-4:]
    match int(x[0]):
        case 0:
          print("", end="")
          print(num_4(s_1))
        case 1:
          print(teens[int(x[1])], "тысяч", end=" ")
          s_1 = x[-3:]
          print(num_3(s_1))
        case y if 2<=y<=9:
          print(tens[int(x[0])], end=" ")
          (num_4(s_1))


def num_6(x):
    s_1 = x[-5:]
    print(hun[int(x[0])],end=" ")
    (num_5(s_1))


def num_7(x):
    s_1 = x[-6:]
    match int(x[0]):
        case 0:
            print("миллионов",end=" " )
        case 1:
          print(un_1[0],"миллион",end=" " )
        case y if 2<=y<=4:
          print(un[int(x[0])], "миллиона", end=" ")
        case y if 5<=y<=9:
          print(un[int(x[0])], "миллионов",end=" ")
    (num_6(s_1))
    

def num_8(x):
    s_1 = x[-7:]
    match int(x[0]):
        case 0:
          print("", end="")
          (num_7(s_1))
        case 1:
          print(teens[int(x[1])], "миллионов", end=" ")
          s_1 = x[-3:]
          (num_6(s_1))
        case y if 2<=y<=9:
          print(tens[int(x[0])], end=" ")
          (num_7(s_1))
    

def num_9(x):
    s_1 = x[-8:]
    print(hun[int(x[0])],end=" ")
    num_8(s_1)
    


k=(input())
match len(k):
    case 1:
        (num_1(k))
    case 2:
        (num_2(k))
    case 3:
        (num_3(k))
    case 4:
        (num_4(k))
    case 5:
        (num_5(k))
    case 6:
        (num_6(k))
    case 7:
        (num_7(k))
    case 8:
        (num_8(k))
    case 9:
        (num_9(k))
