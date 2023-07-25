medida = float(input('Uma distancia em metros: '))

dam = medida/10
hm = medida/100
km = medida/1000
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print(f'A medida de {medida} m corresponde a {dm} dm e {cm} cm e {mm} mm')

print(f'A medida de {medida} m corresponde a {dam} dam e {hm} hm e {km} km')
