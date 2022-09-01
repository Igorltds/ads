Abra esse arquivo do VSCode para ler mais fácil.

# Exercício de JavaScript

Para treinar o JavaScript de vocês, vamos desenvolver uma calculadora em JavaScript.

# Como Fazer

No diretório de vocês, dentro do arquivo *SpecRunner.html* com o layout da calculadora já pronto, além da execução dos testes. Já existe um arquivo *calculadora.js* dentro da pasta **src**. 

# Aquecimento

* Crie uma função coloca12 que coloca o valor 12 na tela da calculadora
* Faça os botões 0 e 1 funcionarem (ou seja, colocarem 0 e 1 na calculadora)

# Requisitos da calculadora

Os seguintes requisitos devem ser levados em consideração para a calculadora:

 * Os números ao serem clicados devem aparecer no campo de id *resultado*.
 * As operações também devem adicionar o símbolo no campo de resultado.
 * *NÃO* pode ser incluído uma operação se não houver nenhum número ou se já houver alguma operação no resultado.
 * O ponto é utilizado para números decimais.
 * Ao clicar no igual (=), o resultado da operação deve substituir a expressão no campo resultado.
 * Se houver apenas um número no campo, o botão igual não faz nada (mantém o número).
 * Se houver o primeiro número e a operação, sem o segundo número, o botão igual deve colocar uma mensagem de erro no resultado: _Erro de operação_.
 * O ponto (.) só pode ser adicionado uma vez por número.

# Informações adicionais



Strings no JavaScript são como vetores, podemos acessar letra a letra pelo seu índice.

Algumas funções podem ser interessantes para o exercício (pesquisem!):
 * isNaN(): diz se uma expressão é um número ou não.
 * parseInt(): transforma uma String em inteiro.
 * parseFloat(): transforma uma String em um decimal.
 * substring(): devolve parte de uma String, baseado no índice passado.


# Depois de terminar o exercicio

 Como os scripts precisarão do DOM carregado, usamos a palavra chave _defer_ no 
 SpecRunner.html

 O que acontece se você tirar essa palavra chave? 

 Experimente, mas **nao** entregue o arquivo sem defer.

## Desafio

Ao terminar o exercicio, tente adaptá-lo. O objetivo agora é garantir que você fez todas as alterações nos arquivos js, sem adicionar nenhum código js no html.

Ou seja, baixe a atividade novamente, e agora você só pode editar dentro da pasta **src**. Pode usar sua versão anterior (como inspiração, ou copiando e colando)

Você deve escrever todo o código de manipulação de javascript nesse arquivo no arquivo *calculadora.js*, ou em arquivos chamados a partir dele. 

Você pode criar outras funções e scripts (dentro da pasta **src**), mas não mexa em nenhum outro arquivo.

(Cumprir esse desafio não aumenta sua nota, mas é interessante pelo aprendizado de codificação js mais limpa)