
describe('Achar maior em um vetor', () => {
  it('Se o vetor estiver vazio, devolve undefined', () => expect(acharMaior([])).toEqual(undefined))
  it('Para [1,2,3,4,5] retorna 5', () => expect(acharMaior([1,2,3,4,5])).toEqual(5))
  it('Para [1,2,3,4,0] retorna 4', () => expect(acharMaior([1,2,3,4,0])).toEqual(4))
  it('Para [1,2,-3,4,0] retorna 0', () => expect(acharMaior([-1,-2,-3,-4,0])).toEqual(0))
})

describe('lista_de_compras', () => {
  it('Faz a lista ["laranjas"]', () => expect(lista_de_compras(["laranjas"])).toEqual("laranjas"))
  it('Faz a lista ["morangos","laranjas"]', () => expect(lista_de_compras(["morangos","laranjas"])).toEqual("morangos e laranjas"))
  it('Faz a lista ["morangos","laranjas","ovos"]', () => expect(lista_de_compras(["morangos","laranjas","ovos"])).toEqual("morangos, laranjas e ovos"))
  it('Faz a lista ["fandangos","morangos","laranjas","ovos"]', () => expect(lista_de_compras(["fandangos","morangos","laranjas","ovos"])).toEqual("fandangos, morangos, laranjas e ovos"))
})

describe('Achar maior distância em um vetor', () => {
  it('Se o vetor estiver vazio, devolve undefined', () => expect(acharMaiorDistancia([])).toEqual(undefined))
  it('Para [10,13,8,17,9] retorna 9', () => expect(acharMaiorDistancia([10,13,8,17,9])).toEqual(9))
  it('Para [10,13,8,17,9,6] retorna 11', () => expect(acharMaiorDistancia([10,13,8,17,9,6])).toEqual(11))
  it('Para [10,13,10,17,9] retorna 8', () => expect(acharMaiorDistancia([10,13,10,17,9])).toEqual(8))
})


describe('Inverter um vetor', () => {
  it('Se o vetor estiver vazio, devolve []', () => expect(inverter([])).toEqual([]))
  it('Para [10,13,8,17,9] retorna [9, 17, 8, 13, 10]', () => expect(inverter([10,13,8,17,9])).toEqual([9, 17, 8, 13, 10]))
  it('Para [10,13,8,17,9,6] retorna [6, 9, 17, 8, 13, 10]', () => expect(inverter([10,13,8,17,9,6])).toEqual([6, 9, 17, 8, 13, 10]))
  it('Para [10,13,10,17,9] retorna [9, 17, 10, 13, 10]', () => expect(inverter([10,13,10,17,9])).toEqual([9, 17, 10, 13, 10]))
  
})

describe('criar baralho', () => {
  it('Contem o valete de ouros', () => expect(cria_baralho().includes("Jo")).toEqual(true))
  it('Contem o valete de copas', () => expect(cria_baralho().includes("Jc")).toEqual(true))
  it('Contem o as de paus', () => expect(cria_baralho().includes("Ap")).toEqual(true))
  it('Contem 52 cartas', () => expect(cria_baralho().length).toEqual(13*4))
  it('Contem 3 de espadas', () => expect(cria_baralho().includes("3e")).toEqual(true))
})

describe('desamassa listas', () => {
  it('Desamassa [1,2,3]', () => expect(desamassa_lista([1,2,3])).toEqual([1,2,3]))
  it('Desamassa [1,[2,3],4]', () => expect(desamassa_lista([1,[2,3],4])).toEqual([1,2,3,4]))
  it('Desamassa [1,[2,3],[4]]', () => expect(desamassa_lista([1,[2,3],[4]])).toEqual([1,2,3,4]))
  it('OPCIONAL: Desamassa [1,[[2,3],[4]]]', () => expect(desamassa_lista([1,[[2,3],[4]]])).toEqual([1,2,3,4]))
})


