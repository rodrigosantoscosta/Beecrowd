valor = float(input())

print('NOTAS:')

print(f'{int(valor / 100)} nota(s) de R$ 100.00')
valor = valor % 100

print(f'{int(valor / 50)} nota(s) de R$ 50.00')
valor = valor % 50

print(f'{int(valor / 20)} nota(s) de R$ 20.00')
valor = valor % 20

print(f'{int(valor / 10)} nota(s) de R$ 10.00')
valor = valor % 10

print(f'{int(valor / 5)} nota(s) de R$ 5.00')
valor = valor % 5

print(f'{int(valor / 2)} nota(s) de R$ 2.00')
valor = valor % 2

print('MOEDAS:')

print(f'{int(valor / 1.00)} moeda(s) de R$ 1.00')
valor = valor % 1.00

print(f'{int(valor / 0.50)} moeda(s) de R$ 0.50')
valor = valor % 0.50

print(f'{int(valor / 0.25)} moeda(s) de R$ 0.25')
valor = valor % 0.25

print(f'{int(valor / 0.1)} moeda(s) de R$ 0.10')
valor = valor % 0.1

print(f'{int(valor / 0.05)} moeda(s) de R$ 0.05')
valor = valor % 0.05

print(f'{(valor / 0.01):,.0f} moeda(s) de R$ 0.01')