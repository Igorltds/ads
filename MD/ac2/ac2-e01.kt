val reajuste:Double = 5.0

fun main () {
    var salario:Double = 2000.0
    salario = salario + salario * reajuste / 100
    print (salario)
}
