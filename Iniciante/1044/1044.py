# Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

# Entrada
# A entrada contém valores inteiros.

# Saída
# A saída deve conter uma das mensagens conforme descrito acima.

a, b = map(int, input().split())

if b % a == 0:
    print('Sao Multiplos')
elif a % b == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')