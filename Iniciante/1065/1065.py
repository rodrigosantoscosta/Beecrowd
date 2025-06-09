lista = []

for i in range(5):
    lista.append(int(input()))

pares = 0 

for i in lista:
    if i % 2 == 0:
        pares += 1

print(f'{pares} valores pares')