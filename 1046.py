start, end = map(int, input().split())
hour = 0
if(start == end):
    hour = 24
elif(start < end):
    hour = end-start
else:
    hour = (24-start)+end


print("O JOGO DUROU "+str(hour)+" HORA(S)")