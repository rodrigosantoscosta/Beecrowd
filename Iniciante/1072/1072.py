n = int(input())
dentro = 0
fora= 0
numeros = []

for x in range(n):
    x = int(input())
    numeros.append(x)

for i in numeros:
    if i >= 10 and i <=20:
        dentro+=1
    else:
        fora+=1

print(f'{dentro} in')
print(f'{fora} out')