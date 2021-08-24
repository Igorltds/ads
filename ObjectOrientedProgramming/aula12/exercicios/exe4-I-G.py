arquivo = open("exercicio4.txt", "r")
ipValido = open("exercicio4-ip-valido.txt", "w")
ipInvalido = open("exercicio4-ip-invalido.txt", "w")

for linha in arquivo:
    ip = []
    linha = linha.split(".")
    for i in linha:
        ip.append(int(i))
    if ip[0] >= 1 and ip[0] <= 255 and ip[1] >= 0 and ip[1] <= 255 and ip[2] >= 0 and ip[2] <= 255 and ip[3] >= 0 and ip[3] <= 255:
      ipValido.write(str(ip) + '\n')
    else:
      ipInvalido.write(str(ip) + '\n')