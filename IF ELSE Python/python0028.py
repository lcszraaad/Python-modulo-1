n1 = int(input('Sua nota na AV1 foi:'))
n2 = int(input('Sua nota na AV1 foi:'))
m = (n1+n2) / 2

if m>=6:
    print('Você foi aprovado!')
    if m>=8:
        print('Você está bem acima da média excelente.')

else:
    print('Você foi reprovado!')
