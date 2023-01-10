notes_coins = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

money = float(input())
name = "nota"
print("NOTAS:")
for coin in notes_coins:
    if(coin == 1.0):
        print("MOEDAS:")
        name = "moeda"

    if(money >= coin):
        print(str(int(money/coin))+" "+name+"(s) de R$ "+str(format(coin, ".2f")))
        money = money%coin
    else:
        print(str(0)+" "+name+"(s) de R$ "+str(format(coin, ".2f"))) 