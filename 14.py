def wrd(x,y):
    if x==y:
        return print("Победа")
    else:
        return print("Вы проиграли")


def game():
    letters = []
    clue = input("Введите подсказку")
    word= input("Введите слово")
    print("\n" * 25)
    print(clue)
    s="*" * len(word)
    for i in range(len(s)):
        letters.append("*")
    print(s)
    for i in range(10):
        print("Буква или слово (0 - буква, 1 - слово)?",end="")
        num=input()
        if num=="1":
            awn=input("Что за слово?")
            wrd(awn,word)
            letters=[]
            break
        elif num== "0":
            awn = input("Какая буква?")
            if awn in word:
                for i in range(0, len(word)):
                    if awn == word[i]:
                        letters[i]=awn
                    else:
                        continue
                print("".join(letters))
            else:
                print("Такой буквы нет")
        else:
          print("введите 0 или 1")

    if "*" in letters:
        print("Вы проиграли")
    elif len(letters)==0:
        print("")
    else:print("Победа")

game()
