arquivo  = open('numeros IP.txt', 'r')
valido   = open('numeros IP valido.txt', 'w')
invalido = open('numeros IP invalido', 'w')

lista_ips = []

for linha in arquivo:
    lista_ips.append(linha.replace('\n', ''))

for ip in lista_ips:
    lista = ip.split('.')
    ip valido = True
    if int(lista[0]) < 1 or int