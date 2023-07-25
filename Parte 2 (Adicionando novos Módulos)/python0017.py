import math #ou from math import hypot#
catop = float(input('Digite o valor do cateto oposto: '))
catad = float(input('Digite o valor do cateto adjacente: '))
hipot = (catop ** 2 + catad ** 2) ** (1/2)


print(f'Se o cateto oposto tem {catop} e o cateto adjacente tem {catad} a hipotenusa e {hipot:.2f}.')

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(co,ca)

print(f'Se o cateto oposto tem {co} e o cateto adjacente tem {ca} a hipotenusa e {hi:.2f}.')