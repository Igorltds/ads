interface Usuario {
    fun imprimir(){}
}


class Leitura:Usuario{
    override fun imprimir () {
    	println("Aplicando impreção 'leitura'")
    }
}


class Aluno:Usuario{
    override fun imprimir () {
        println("Aplicando impreção 'Aluno'")
    }
}


class Professor:Usuario{
    override fun imprimir () {
        println("Aplicando impreção 'Professor'")
    }
}


fun main(){
    val user_leitura = Leitura()
    user_leitura.imprimir()

    val user_aluno = Aluno()
    user_aluno.imprimir()

    val user_professor = Professor()
    user_professor.imprimir()
}
