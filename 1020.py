day = int(input())
ym = [365, 30]
i = 0
YMD = [0, 0, 0]
while(i < 2):
    if(ym[i] <= day):
        YMD[i] = int(day/ym[i])
        day = int(day%ym[i])

    else:
        i+=1
YMD[2] = day
print(str(YMD[0])+" ano(s)")
print(str(YMD[1])+" mes(s)")
print(str(YMD[2])+" dia(s)")