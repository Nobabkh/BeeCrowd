notes = [100, 50, 20, 10, 5, 2, 1]
money = int(input())
i = 0
count = int(0)
while(i < 7):
    if(money >= notes[i]):
        count = int(money/notes[i])
        money = money%notes[i]

    else:
        print(str(count)+" nota(s) de R$ "+str(notes[i])+",00")
        count = 0
        i+=1