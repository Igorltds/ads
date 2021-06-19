const template = '<div class="calculadora"> <input type="text" id="resultado"/> <button class="numero">9</button> <button class="numero">8</button> <button class="numero">7</button> <button class="operacao somar">+</button> <button class="numero">6</button> <button class="numero">5</button> <button class="numero">4</button> <button class="operacao subtrair">-</button> <button class="numero">3</button> <button class="numero">2</button> <button class="numero">1</button> <button class="operacao multiplicar">*</button> <button class="numero">0</button> <button class="numero">.</button> <button class="resultar">=</button> <button class="operacao dividir">/</button></div>'

function carregarConteudo(){
    let calc = document.querySelector('div.calculadora'),
    elementos = {}
    if(!calc){
        let fixtureHolder = document.createElement('div')
        fixtureHolder.id = 'fixture-holder'
        fixtureHolder.innerHTML = template
        document.querySelector('.jasmine_html-reporter').appendChild(fixtureHolder)
        calc = document.querySelector('div.calculadora')
    }
    calc.querySelectorAll('button')
                .forEach(item => {
                    elementos[item.innerText] = item
                })
    elementos['calc'] = calc
    return elementos
}