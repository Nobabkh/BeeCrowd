main = input()
list1 = main.split(" ")
temp = 0
for st in list1:
    num = int(st)
    if(temp < num):
        temp = num

print(str(temp)+" eh o maior")