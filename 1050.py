DDD = [61, 71, 11, 21, 32, 19, 27, 31]
Destination = ["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]

num = int(input())
try:
    print(Destination[DDD.index(num)])
except:
    print("DDD nao cadastrado")
