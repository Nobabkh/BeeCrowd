a, b, c = map(float, input().split())

if(a+b > c and a+c > b and b+c > a):
    print("Perimetro = "+str(format(a+b+c, ".1f")))
else:
    print("Area = "+str(format(((a+b)/2)*c, ".1f")))