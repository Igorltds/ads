fun main() {
    
    // Capturar erro ---------
    
	try {
    	val int = 10/0 
		println(int)    
    }
    catch (e:ArithmeticException) { println(e) }
	finally { println("This block always executes") }
    
    // Lançar erro ---------
    
    val test: Int = 2
    if (test == 2) {throw ArithmeticException("test é igual a 2")}
    
    
    
}