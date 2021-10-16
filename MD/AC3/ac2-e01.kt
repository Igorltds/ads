enum class Notas(val nota: String){
    primeira("5"),
    segunda("0"),
    terceira("10"),
    quarta("7")
}

fun main (args: Array<String>) {
    val n1_semestre_letivo = Notas.primeira.nota
    println("Primeira nota: $n1_semestre_letivo")
    val n2_semestre_letivo = Notas.segunda.nota
    println("Segunda nota: $n2_semestre_letivo")
    val n3_semestre_letivo = Notas.terceira.nota
    println("Terceira nota: $n3_semestre_letivo")
    val n4_semestre_letivo = Notas.quarta.nota
    println("Quarta nota: $n4_semestre_letivo")
}

/*
enum class Notas(val id: String, val cod: String){
    Primeiro("0001", "pri1"),
    Segundo("0002", "sec2"),
    Terceiro("0003", "ter3"),
    Quarto("0004", "qua4")
}

fun main (args: Array<String>) {
    val n1_semestre_letivo = Notas.Primeiro.id
    println("Primeiro id: $n1_semestre_letivo")
    val n2_semestre_letivo =Notas.Segundo.id
    println("Segundo id: $n2_semestre_letivo")
    val n3_semestre_letivo = Notas.Terceiro.id
    println("Terceiro id: $n3_semestre_letivo")
    val n4_semestre_letivo = Notas.Quarto.id
    println("Quarto id: $n4_semestre_letivo")
}
    
	// estava tentando extrapolar o exercício para entender melhor, por isso os rastros lá em cima do "cod"
	
    print("\nNão entendi para que serve \n\n")
    
    val c1_semestre_letivo = Notas.Primeiro.cod
    println("Primeiro cod: $c1_semestre_letivo")
    val c2_semestre_letivo =Notas.Segundo.cod
    println("Segundo cod: $c2_semestre_letivo")
    val c3_semestre_letivo = Notas.Terceiro.cod
    println("Terceiro cod: $c3_semestre_letivo")
    val c4_semestre_letivo = Notas.Quarto.cod
    println("Quarto cod: $c4_semestre_letivo")

    print("\n AGORA ENTENDI! \n\n")
}
*/