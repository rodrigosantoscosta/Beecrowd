tipoCha = int(input())
respostas = []
respostas =  list(map(int, input().split()))

quantidadeAcertos = 0


# if tipoCha == respostaA:
#     quantidadeAcertos = quantidadeAcertos + 1

# if tipoCha == respostaB:
#     quantidadeAcertos = quantidadeAcertos + 1

# if tipoCha == respostaC:
#     quantidadeAcertos = quantidadeAcertos + 1

# if tipoCha == respostaD:
#     quantidadeAcertos = quantidadeAcertos + 1

# if tipoCha == respostaE:
#     quantidadeAcertos = quantidadeAcertos + 1

for i in range(0, len(respostas)):
    if tipoCha == respostas[i]:
        quantidadeAcertos += 1

print(quantidadeAcertos)
