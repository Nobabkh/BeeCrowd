hour, minute, fhour, fminute = map(int, input().split())
rhour = 0
rminute = 0
if(hour == fhour and minute == fminute):
    rhour = 24
    rminute = 0
elif(hour > fhour):
    rhour = (24-hour)+fhour
    rminute = fminute - minute
    if(rminute < 0):
        rhour-=1
        rminute = 60-1
else:
    rhour = fhour-hour
    rminute = fminute - minute
    if(rminute < 0):
        rhour-=1
        rminute = 60-1

print("O JOGO DUROU "+str(rhour)+" HORA(S) E "+str(rminute)+" MINUTO(S)")