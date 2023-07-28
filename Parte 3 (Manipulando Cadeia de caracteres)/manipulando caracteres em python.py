frase = 'Curso em video Python'

print(f'{frase[9]} :Imprimindo nono espaço da memoria.')
print(f'{frase[:5]} :Imprimindo do espaço 0 ate o 5 da memoria.')
print(f'{frase[:21]} :Imprimindo do espaço 0 ate o final da memoria.')
print(f'{frase[15:]} :Imprimindo do espaço 15 ate o final da memoria.')
print(f'{frase[9:21]} :Imprimindo nono espaço da memoria ate o espaço 21.')
print(f'{frase[9:21:2]} :Imprimindo do nono espaço da memoria ate o espaço 21 pulando de 2 em 2.')
print(f'{frase[9::3]} :Imprimindo do nono espaço da memoria ate ofinal pulando de 3 em 3. ')

print(f'{len(frase)} : Quantidade de espaços que o objeto ocupou na memoria')

frase.count('o') #Conta a quantidade de letra 'o' na frase.
frase.count('o',0,13) #conta a letra 'o' da posição 0 ate a 12.
frase.find('deo') #mostra a posição em qual foi encontrada a primeira string 'deo'.
frase.find('Android') #O resultado sera -1 significa que essa string não foi encontrada.

'Curso' in frase # vai indentifica se essa palavra existe na frase e dira true or false.

frase.replace('Python','Android') # vai substituir a palavra Python por Android.

frase.upper() #transforma letras minusculas em maiusculas.
frase.lower() #transforma letras maiusculas em minusculas.

frase.capitalize() # Transforma o primeiro caractere para maiusculo e todo resto em minusculo
frase.title() # Transforma em maiusculo todas as iniciais de palavras.

frase.strip()# Eliminas espalços inuteis na String.
frase.rstrip()#Elimina a direita.
frase.lstrip()#Elimina a esquerda.

frase.split()#Divide as strings através dos espaços entre elas.
'-'.join(frase)# Junta todos os elementos de frase com -
