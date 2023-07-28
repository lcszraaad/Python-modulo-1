nome = str(input('Qual o seu nome completo:')).strip()
print('Analisando seu nome...')

print(f'Nome com todas as letras maiusculas: {nome.upper()} .')
print(f'Nome com todas as letras maiusculas: {nome.lower()} .')
print(f'Conta quantos caracteres tem o nome completo: {len(nome) - nome.count(" ")}.')
#print(f'Quantas letras tem o primeiro nome {nome.find(" ")}')

separa = nome.split()
print(f'O primeiro nome e {separa[0]} e contem {len(separa[0])} letras.')


