fun test(password: String) {
    if (password.length < 10)
    throw ArithmeticException("Senha Fraca")
    else
    println("Senha Forte")
}


fun main(args: Array<String>) {
    test("abcdefghij")
}
