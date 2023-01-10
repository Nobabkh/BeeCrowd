a, b, c, d = map(int, input().split())

def BC_big():
    if(b > c and d > a):
        return True
    else:
        return False

def bigsum():
    if((c+d) > (a+b)):
        return True
    else:
        return False

def cdpos():
    if(c > 0 and d > 0):
        return True
    else:
        return False

if(BC_big() and bigsum() and cdpos() and (a%2==0)):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")