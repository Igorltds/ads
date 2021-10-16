class Casa () {
    var existencia:Boolean = true
    companion object fatory {
        var beleza:String = "linda"
        fun moscas () {print("32")}
    }
    
    fun get_beleza ():String {return beleza}
    fun moscaas () {moscas()}
}

fun main () {
    val casa01 = Casa()
    if (casa01.existencia == true) {println("foi verdadeiro")}
    casa01.existencia = false
    if (casa01.existencia == false) {println("foi falso")}
    print(casa01.get_beleza())
    casa01.moscaas()
}