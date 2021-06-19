# adicionar conteudo em arquivo de texto

arquivo = open("arquivo.txt", "a", encoding="UTF-8")          # append

arquivo.write("\nEssa linha será adicionada no final do arquivo")
arquivo.write("\nEscreve outra linha")


arquivo.close()
