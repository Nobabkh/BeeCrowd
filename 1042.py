inumbers = input()
array = inumbers.split(" ")
i = 0
temp = []
while(i < len(array)):
    temp.append(int(array[i]))
    i+=1
temp.sort()
for st in temp:
    print(st)
print("")
for num in array:
    print(num)