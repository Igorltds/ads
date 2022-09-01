class Carro (modelo:String, ano: Int = 1900, velocidade: Int = 0) {
    val modelo: String = modelo
    val ano: Int = ano
    val velocidade: Int = velocidade
    fun get_age ():Int {return ano}
}


fun main () {
    val c0 = Carro("Sally Carrera")
    val c1 = Carro("mate" )
    val c2 = Carro("Relâmpago McQueen", 2020, 1000*1000000)
    println(c1.get_age())
    println(c2.get_age())
    println("\nOuuu: (Fiz duas opções só para testar mesmo)\n")
    println(c1.ano)
    println(c2.ano)
    
}