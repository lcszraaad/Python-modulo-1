frase = str(input('Digite uma frase:')).upper().strip()

print(f'A letra "A" apareceu {frase.count("A")} vezes.')
print(f'A primeira posição que a letra "A" aparece é {frase.find("A") + 1}. ')
print(f'A ultima posição em que a letra "A" aparece é {frase.rfind("A") + 1}. ')