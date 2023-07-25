km = float(input('Quantos km foram percorridos com o veiculo alugado:'))
dias = int(input('E por quantos dias ele foi alugado:'))

aluguel = (dias * 60) + (0.15 * km)

print(f'O aluguel deste veiculo custou {aluguel:.2f}, pois percorreu {km} km durante {dias} dias.')