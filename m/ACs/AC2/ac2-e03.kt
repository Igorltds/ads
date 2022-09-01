class Aluno (id:Int, nome: String, curso:String) {
	init{print("instanciando Um Aluno\nId: $id \nNome: $nome \nCurso: $curso\n\n")}
	companion object factory {fun exibir(){println("Chamando método estático")}}
}


fun main () {
	Aluno(1, "igor", "ads")
    Aluno.exibir()
}
