class Aluno () {
    companion object factory {val tipo: String = "Aluno"}
    fun get_tipo ():String {return(tipo)
    }
}


class Turma () {
    companion object factory {val tipo: String = "Turma"}
    fun get_tipo ():String {return(tipo)
    }
}


class Professor () {
    companion object factory {val tipo: String = "Professor"}
    fun get_tipo ():String {return(tipo)
    }
}


fun main () {
    val obj = Aluno() //"Aluno", "Turma" ou "Professor"
    if (obj.get_tipo() == "Aluno") {
        val obj2 = Turma()
        print(obj2.get_tipo())
    }
}
