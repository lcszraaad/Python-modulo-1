preco = float(input('Qual e o preco do produto? R$'))
novo = preco - (preco * 5 / 100)
print(f'O produto custava R${preco:.2f}, na promocao com desconto de 5% esta custando R${novo:.2f}.')
