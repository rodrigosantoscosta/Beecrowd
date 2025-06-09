lista = []

for i in range(6):
    lista.append(float(input()))

positivos = []
for i in lista:
    if i > 0:
        positivos.append(i)

print(f'{len(positivos)} valores positivos')