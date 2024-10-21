horaInicial, horaFinal = map(int, input().split())

if horaInicial - horaFinal < 0:
    print(f'O JOGO DUROU {horaFinal - horaInicial} HORA(S)')

elif horaInicial - horaFinal > 0:
    print(f'O JOGO DUROU {horaInicial - horaFinal} HORA(S)')

else:
    if horaInicial == horaFinal:
        print('O JOGO DUROU 24 HORAS(S)')