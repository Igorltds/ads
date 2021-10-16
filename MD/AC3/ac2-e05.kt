interface Usuario {
    fun imprimir(){}
    fun estudo()
}


class Leitura:Usuario{
    override fun imprimir () {
    	println("Aplicando impreção 'Leitura'")
    }
    override fun estudo () {
    	println("Aplicando função 'estudos' dentro de 'Leitura'")
    }
}


class Aluno:Usuario{
    override fun imprimir () {
        println("Aplicando impreção 'Aluno'")
    }
    override fun estudo () {
    	println("Aplicando função 'estudos' dentro de 'Aluno'")
    }
}


class Professor:Usuario{
    override fun imprimir () {
        println("Aplicando impreção 'Professor'")
    }
    override fun estudo () {
    	println("Aplicando função 'estudos' dentro de 'Professor'")
    }
}


fun main(){
    val user_leitura = Leitura()
    user_leitura.estudo()

    val user_aluno = Aluno()
    user_aluno.estudo()

    val user_professor = Professor()
    user_professor.estudo()
}
