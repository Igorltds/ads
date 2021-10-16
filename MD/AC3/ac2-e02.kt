// Operadores de visibilidade
// private >> torna o recurso visivel apenas na classe
// public >> torna o recurso visivel para todas as sub-classes e objetos.
// protected >> torna o recurso visivel para todas as sub-classes, mas não para os objetos.
// internal >> Apenas classes deste arquivo podem utilizar esse recurso.
// o comando open permite que Carro4 se torne uma super classe.
open class Carro5{

    // Atributos da Classe
    private var modelo: String
    private var ano: Int
    protected var velocidade: Int
    public var cor : String
    private var valor: Double = 0.0

    // Construtor
    constructor(novoModelo:String, novoAno:Int) {
    println("Iniciando construtor 1 ...")
    this.modelo = novoModelo
    this.ano = novoAno
    this.velocidade = 0
    this.cor = "Branco"
    }
    fun mudaModelo(novoModelo:String){
        this.modelo = novoModelo
    }
    fun escreveModelo(){
        println(this.modelo)
    }
    fun escreveAno(){
        println(this.ano)
    }
    fun setValor(valor_novo: Double) {this.valor = valor_novo}
    fun getValor() {println(this.valor)}
    // permite que o método tipoTracao possa ser sobre escrito.
    open fun tipoTracao(): String{
        return "4X2"
    }
}
class Jeep(modelo:String, ano:Int, angulo:Int): Carro5(modelo,ano) {
    var anguloDeEntrada: Int= angulo
    override fun tipoTracao(): String{
        return "4X4"
    }
    fun escreveVelocidade(){
        println(velocidade)
    }
}
fun main(){
    var c: Carro5 = Carro5("Onix",2019)
    var j = Jeep("Troller",2013,47)
    println("--------")
    c.escreveModelo()
    c.escreveAno()
    //println(c.velocidade)
    println(c.cor)
    println(c.tipoTracao())
    println("--------")
    j.escreveModelo()
    j.escreveAno()
    println(j.tipoTracao())
    println(j.anguloDeEntrada)
    
    
    //------ exercício
    println("\n\n------ exercício")
    c.getValor() // ------------- getValor
    c.setValor(5.5) // ------------- setValor
    c.getValor() // ------------- getValor
}