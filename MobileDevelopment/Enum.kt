//enum simples

enum class Status {ATIVO, INATIVO}

// enum com construtor

enum class Conceitos(val nota: String) {
	APROVADO("A"),
	RECUPERACAO("B"),
	REPROVADO("C")

}


fun main(args: Array<String>) {
	val status = Status.ATIVO
	println(status)
	val conceito = Conceitos.APROVADO.nota
	println(conceito)
}