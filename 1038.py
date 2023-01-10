prices = [4.00, 4.50, 5.00, 2.00, 1.50]
x, y = map(int, input().split())
print("Total: R$ "+str(format(prices[x-1]*y, ".2f")))