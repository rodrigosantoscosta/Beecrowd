PRECO_CACHORRO_QUENTE = 4.00
PRECO_X_SALADA = 4.50
PRECO_X_BACON = 5.00
PRECO_TORRADA_SIMPLES = 2.00
PRECO_REFRIGERANTE = 1.50


codigoItem, quantidadeItem = map(int,input().split())

    
if codigoItem == 1:
    print(f'Total: R$ {quantidadeItem * PRECO_CACHORRO_QUENTE:,.2f}')
if codigoItem == 2:
    print(f'Total: R$ {quantidadeItem * PRECO_X_SALADA:,.2f}')
if codigoItem == 3:
    print(f'Total: R$ {quantidadeItem * PRECO_X_BACON:,.2f}')
if codigoItem == 4:
    print(f'Total: R$ {quantidadeItem * PRECO_TORRADA_SIMPLES:,.2f}')
if codigoItem == 5:
    print(f'Total: R$ {quantidadeItem * PRECO_REFRIGERANTE:,.2f}')