largura = float(input('Qual a largura da parede:'))
altura = float(input('Qual a altura da parede:'))

area = largura * altura
print(f'Sua parede tem dimensão de {largura:.2f}x{altura:.2f} e sua área é de {area:.2f}m.')

tinta = area / 2

print(f'Para pintar essa parede, voce necessitara de {tinta}l de tinta')
