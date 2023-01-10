line1 = str(input())
line2 = str(input())
list1 = line1.split(" ")
list2 = line2.split(" ")

price = float(list1[1])*float(list1[2])
price += float(list2[1])*float(list2[2])
print("VALOR A PAGAR: R$ "+str(format(price, ".2f")))