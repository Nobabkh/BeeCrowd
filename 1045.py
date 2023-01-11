inputs = input()
numbers = inputs.split()
i = 0
while(i < len(numbers)):
    numbers[i] = float(numbers[i])
    i+=1

numbers.sort(reverse=True)
A = numbers[0]
B = numbers[1]
C = numbers[2]

if(A >= B+C):
    print("NAO FORMA TRIANGULO")

else:
    if(pow(A, 2) == pow(B, 2)+pow(C, 2)):
        print("TRIANGULO RETANGULO")
    if(pow(A, 2) > pow(B, 2)+pow(C, 2)):
        print("TRIANGULO OBTUSANGULO")
    if(pow(A, 2) < pow(B, 2)+pow(C, 2)):
        print("TRIANGULO ACUTANGULO")
    if(A == B and B == C):
        print("TRIANGULO EQUILATERO")
    if((A == B and A != C) or (B == C and B != A) or (A == C and B != C)):
        print("TRIANGULO ISOSCELES")