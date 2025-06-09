lista = []

for i in range(5):
    lista.append(int(input()))

pares = 0
impares = 0
negativos = 0
positivos = 0

for i in lista:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if i < 0:
        negativos+=1

    elif i != 0:
        positivos += 1

print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')