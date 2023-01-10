a, b, c, d = map(float, input().split())
average = a*2+b*3+c*4+d*1
average = average/10
inexam = False
print("Media :"+str(format(average, ".1f")))
if(average >= 7.0):
    print("Aluno aprovado.")
elif(average >= 5.0 and average < 7.0):
    inexam = True
    print("Aluno em exame.")
else:
    print("Aluno reprovado.")

if(inexam):
    mark = float(input())
    print("Nota do exame: "+str(format(mark, ".1f")))
    ava = average+mark
    ava = ava/2
    if(ava >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final: "+str(format(ava, ".1f")))