def triangulo(a,b,c):
    if a + b > c and a+c > b and b+c > a:
        if a == b and a == c:
            return 'Triângulo Equilátero'
        elif a == b or a== c or b==c:
            return 'Triângulo Isósceles'
        else:
            return 'Triângulo Escaleno'
    else:
        return 'Nao é um triângulo'