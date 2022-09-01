describe('Aquecimento', () => {
    beforeAll(() => {
        this.elementos = carregarConteudo()
        this.$resultado = this.elementos['calc'].querySelector('input')
        initCalculadora()
    })
    beforeEach(() => {
        this.$resultado.value = ''
    })
    it('Deve haver a função "coloca12", que coloca o número 12 na tela da calculadora', () => {
        coloca12();
        expect(this.$resultado.value.trim()).toBe('12')
    })
    it('Ao clicar no numero 0, ele deve aparecer na tela', () => {
        this.elementos['0'].click()
        expect(this.$resultado.value.trim()).toBe('0')
    })
    it('Ao clicar no numero 1, ele deve aparecer na tela', () => {
        this.elementos['1'].click()
        expect(this.$resultado.value.trim()).toBe('1')
    })
    it('Ao clicar nos numeros 001010, eles devem aparecer na tela', () => {
        this.elementos['0'].click()
        this.elementos['0'].click()
        this.elementos['1'].click()
        this.elementos['0'].click()
        this.elementos['1'].click()
        this.elementos['0'].click()
        expect(this.$resultado.value.trim()).toBe('001010')
    })
    

    
})
  