describe('Resultados', () => {
    beforeAll(() => {
        this.elementos = carregarConteudo()
        this.$resultado = this.elementos['calc'].querySelector('input')
        initCalculadora()
    })
    beforeEach(() => {
        this.$resultado.value = ''
    })
    it('Deve manter campo vazio se clicado com o campo vazio', () => {
        this.elementos['='].click()
        expect(this.$resultado.value.trim()).toBe('')
    })
    it('Deve manter número no campo se clicado com o campo com apenas um número', () => {
        this.elementos[3].click()
        this.elementos[5].click()
        this.elementos['='].click()
        expect(this.$resultado.value.trim()).toBe('35')
    })
    it('Deve colocar o texto "Erro de operação" campo se clicado com o campo com apenas um número e a operação', () => {
        this.elementos[3].click()
        this.elementos['+'].click()
        this.elementos['='].click()
        expect(this.$resultado.value.trim()).toBe('Erro de operação')
    })
    it('Deve mostrar o resultado se cliocado com o campo com um número, operação e outro número válido', ()=>{
        this.elementos[3].click()
        this.elementos['+'].click()
        this.elementos[1].click()
        this.elementos['='].click()
        expect(this.$resultado.value.trim()).toBe('4')
    })
})