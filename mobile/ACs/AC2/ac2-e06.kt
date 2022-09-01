class Aluno (id: Int, nome: String, semestre: Int, listaa: List<Double>){
	val id: Int = id
	val nome: String = nome
    var semestre: Int = semestre
	var listaa: List<Double> = listaa
    fun imprimir_Notas () {
		for(i in listaa){println("$i")}
    } 
}


fun main () {
    val listaa:List<Double> = mutableListOf<Double>(5.5, 4.4, 10.0, 0.0, 5.7, 6.5, 7.9, 8.8, 9.9, 10.0)
    val aluno_igor = Aluno(1, "Igor", 3, listaa)
    aluno_igor.imprimir_Notas()
    
}