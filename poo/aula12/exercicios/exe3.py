impares = open('umpares.txt', 'a+')
numeros = open('numeros ordenados.txt', 'a+')
pares = open('pares.txt', 'a+')

lista[]

for x in numeros:
    lsita.append(int(x))

for x in impares:
    lista.append(int(x))

lista.sort()

print(lista)


for n in lista:
    numeros.write(str(n)+ '\n')

impares.close()
pares.close()
numeros.close()
    