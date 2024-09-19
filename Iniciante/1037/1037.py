valorQualquer = float(input())

if  valorQualquer >= 0 and valorQualquer <= 25:
    print('Intervalo [0,25]')

if  valorQualquer > 25 and valorQualquer <= 50:
    print('Intervalo (25,50]')

if  valorQualquer > 50 and valorQualquer <= 75:
    print('Intervalo (50,75]')

if  valorQualquer > 75 and valorQualquer <= 100:
    print('Intervalo (75,100]')

if  valorQualquer < 0 or valorQualquer > 100:
    print('Fora de intervalo')