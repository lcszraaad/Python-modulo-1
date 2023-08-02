distancia = float(input('Qual a distancia da viagem em KM:'))

if distancia < 200:
    print(f'A viagem vai custar {0.50*distancia}R$.')

else: print(f'A viagem vai custar {0.45*distancia}R$.')