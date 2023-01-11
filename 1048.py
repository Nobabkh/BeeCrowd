salrange  = [0, 400.00, 800.00, 1200.00, 2000.00]
persentages = [15, 12, 10, 7, 4]
salary = float(input())
i = 0
percentage = 0
if(salary > 2000.00):
    percentage = 4
else:
    while(i < len(salrange) - 1):
        if(salary > salrange[i] and salary <= salrange[i+1]):
            percentage = persentages[i]
            break
        i+=1

print("Novo salario: "+str(format(salary+((salary/100)*percentage), ".2f")))
print("Reajuste ganho: "+str(format(((salary/100)*percentage), ".2f")))
print("Em percentual: "+str(percentage)+"%")