linhas = int(input())
sequencia = []
limite = 7
atual = 0
consecutivos = 0

for i in range (0, linhas):
    sequencia.append(input())

for i in range (0, linhas):
    atual = sequencia[i]
    proximo = sequencia[i + 1]
    
    if proximo == 1:
        break
    if proximo == 2:
        consecutivos = consecutivos + 1

print(consecutivos)