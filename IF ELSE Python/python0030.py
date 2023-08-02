from time import sleep
velocidade = float(input('A qual velocidade este carro trafegava:'))

if velocidade > 80:
    print('Você foi multado por excesso de velocidade.')
    print('Calculando sua multa aguarde.')
    sleep(3)
    print(f'A multa vai custar {(velocidade - 80) * 7:.2f}R$.')

print(f'Trafegava {velocidade}km/h, esta velocidade e permitida.')
