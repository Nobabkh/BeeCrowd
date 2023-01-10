seconds = int(input())
hm = [3600, 60]
i = 0
HMS = [0, 0, 0]
while(i < 2):
    if(hm[i] <= seconds):
        HMS[i] = int(seconds/hm[i])
        seconds = int(seconds%hm[i])

    else:
        i+=1
HMS[2] = seconds
print(str(HMS[0])+":"+str(HMS[1])+":"+str(HMS[2]))