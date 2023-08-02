a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

#verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

#verificando quem é maior
maior = a
if b > a and b > c:
    menor = b
if c > a and c > b:
    menor = c

print(f'O menor valor digitado foi {menor} .')
print(f'O maior valor digitado foi {maior} .')
