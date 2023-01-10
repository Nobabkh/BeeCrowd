import math
a, b, c = map(float, input().split())
if(int(a) == 0 or b < c):
    print("Impossivel calcular")

else:
    r1 = (-b + math.sqrt(pow(b, 2) - (4 * a * c))) / (2 * a)
    r2 = (-b - math.sqrt(pow(b, 2) - (4 * a * c))) / (2 * a)
    print("R! = "+str(format(r1, ".5f")))
    print("R2 = "+str(format(r2, ".5f")))
    

