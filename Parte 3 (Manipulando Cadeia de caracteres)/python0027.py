n = str(input('Digite seu nome completo:')).strip()
nome = n.split()

print(f'O seu primeiro nome é {nome[0]} e seu ultimo nome é {nome[len(nome) - 1 ]} .')
