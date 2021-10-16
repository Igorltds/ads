open class Animal() {
    open var colour: String = "White"
}
class Dog: Animal() {
    override var colour: String = "Black"
    fun sound() {
        println("Dog makes a sound of woof woof")
    }
}
class Cat: Animal(){
    override var colour: String = "Green"
    fun sound() { println("Cat makes a sound of meow") }
}
fun main(){
    var animal_dog: Dog = Dog()
    animal_dog.sound()
    var animal_cat: Cat = Cat()
    animal_cat.sound()
}