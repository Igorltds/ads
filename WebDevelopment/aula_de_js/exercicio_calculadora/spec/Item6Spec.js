describe('Regras Gerais', () => {
    beforeAll(() => {
        this.elementos = carregarConteudo()
        this.$resultado = this.elementos['calc'].querySelector('input')
        initCalculadora()
    })
    beforeEach(() => {
        this.$resultado.value = ''
    })
    it('Não deve adicionar uma operação caso não haja número digitado', () => {
        this.elementos['-'].click()
        expect(this.$resultado.value.trim()).toBe('')
    })
    it('Deve adicionar uma operação caso exita um número digitado', () => {
        this.elementos[7].click()
        this.elementos['+'].click()
        expect(this.$resultado.value.trim()).toBe('7+')
    })
    it('Não deve adicionar uma segunda operação logo após outra', () => {
        this.elementos[7].click()
        this.elementos['+'].click()
        this.elementos['-'].click()
        expect(this.$resultado.value.trim()).toBe('7+')
    })
    it('Não deve adicionar uma segunda operação após um segundo número', () => {
        this.elementos[7].click()
        this.elementos['+'].click()
        this.elementos[5].click()
        this.elementos['-'].click()
        expect(this.$resultado.value.trim()).toBe('7+5')
    })
})
  