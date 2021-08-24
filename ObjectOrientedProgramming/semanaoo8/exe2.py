class Filme:
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero


#get
    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero


#set
    def set_titulo(self,novo_titulo):
        self.__titulo = novo_titulo
        
    def set_genero(self,novo_genero):
        self.__genero = novo_genero


### 