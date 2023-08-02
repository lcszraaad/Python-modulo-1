salario = float(input('O seu salario e de : R$'))

if salario <= 1250:

   novo = salario + (salario * 15/100)

else: novo = salario + (salario * 10/100)

print(f'Quem ganhava {salario:.2f}R$ passou a receber {novo:.2f}R$ . ')