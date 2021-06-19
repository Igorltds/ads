import unittest
import requests

#url_servidor = "advinhas-deploy.herokuapp.com"
url_servidor = "localhost:5000"

#Queremos um servidor, rodando em localhost:5000

'''
test_01
O servidor deve ter uma URL /jogo, que exibe o texto
"Advinhe o número"

Use templates!
'''

'''
test_02
O servidor deve permitir chutes. 

Insira o form a seguir na sua template

<form action="/jogo">
    <input type="number" min=0 max=100 name="chute"> 
    <input type="submit" value="chutar">
</form>

Se o usuário enviar um número por esse form, 
verá seu chute aparecer num <li>. Todos os chutes
já feitos aparecerão em <li>s individuais

Dica: o chute deverá vir via GET (como o formulário especifica)
e vai aparecer no dicionário request.args, com a chave "chute"
'''

'''
test_03
Ao acessar a URL /reseta, o jogo do usuário deve ser deletado,
a lista de chutes zerada e um novo número sorteado

(dica: o acesso ocorre com o verbo GET)
'''

'''
test_04, test_05 test_05a
Devo informar ao usuário se seu chute foi baixo ou alto.

Quando o ultimo chute foi abaixo do alvo, exibir
"Seu ultimo chute foi baixo!"

Quando foi acima,
"Seu ultimo chute foi alto!"

Se for exato, exibir
"Você fez um chute correto! Você acertou! Parabéns!"
'''

'''
test_06_restart_via_post
test_07_envio_via_post

O acesso na URL /restart pode ser feito via POST
O acesso na URL /jogo pode ser feito via POST, enviando o form com o chute

Dicas:
Para especificar uma URL com o verbo GET
@app.route("/jogo", methods=["GET"])

Para especificar uma URL com o verbo POST
@app.route("/jogo", methods=["POST"])

Para pegar o conteúdo do form enviado via POST
acessar o dicionário request.form
'''

'''
test_08

Cada usuário deve ter um objeto "jogo" separado.
Para isso, salve o seu usuário em um cookie

Para testar, abra um jogo no navegador normal e um no modo incognito.
Os dois jogos devem existir separadamente (chutar em um nao muda o outro)
'''
class TestStringMethods(unittest.TestCase):

    def test_01_jogo(self):
        s = requests.Session()
        r1 = s.get(f"http://{url_servidor}/jogo")
        if r1.status_code != 200:
            self.fail("url jogo nao implementada")
        if "divinhe" not in r1.text:
             self.fail("url jogo deve conter o texto 'Adivinhe o número'")
        
    
    def test_02_chute(self):
        s = requests.Session()

        #primeira jogada
        r1 = s.get(f"http://{url_servidor}/jogo?chute=50")
        if "50" not in r1.text:
             self.fail("url jogo deve conter o chute mais recente (50)")

        #segunda jogada
        r2 = s.get(f"http://{url_servidor}/jogo?chute=75")
        if "75" not in r2.text:
             self.fail("url jogo deve conter o chute mais recente (75)")
        if "50" not in r2.text:
             self.fail("url jogo deve conter os chutes anteriores (50)")

    def test_03_restart(self):
        s = requests.Session()
        r1 = s.get(f"http://{url_servidor}/restart")
        if r1.status_code != 200:
            self.fail("url restart nao implementada")
        if "50" in r1.text:
            self.fail("Após restart url jogo não deve conter chutes (50)")
        r2 = s.get(f"http://{url_servidor}/jogo?chute=50")
        if "50" not in r2.text:
             self.fail("url jogo deve conter o chute mais recente (50)")
    
    def test_04_alto_e_baixo(self):
        s = requests.Session()
        r1 = s.get(f"http://{url_servidor}/restart")
        if r1.status_code != 200:
            self.fail("url restart nao implementada")
        r2 = s.get(f"http://{url_servidor}/jogo?chute=500")
        #500 é maior que o maximo chute válido (100) -- assim, temos
        #certeza que é alto
        if "500" not in r2.text:
            self.fail("url jogo deve conter o chute mais recente (500)")
        if "alto" not in r2.text:
            self.fail("chutei alto, e deveria ter recebido essa informação")
        r3 = s.get(f"http://{url_servidor}/jogo?chute=-500")
        #-500 é pequeno demais para ser válido. Assim, temos certeza de que se trata de um chute baixo
        if "-500" not in r3.text:
            self.fail("url jogo deve conter o chute mais recente (-500)")
        if "500" not in r3.text:
            self.fail("url jogo deve o chute anterior (500)")
        if "baixo" not in r3.text:
            self.fail("chutei baixo, e deveria ter recebido essa informação")

    def test_05_das_tres_uma(self):
        s = requests.Session()
        r1 = s.get(f"http://{url_servidor}/restart")
        if r1.status_code != 200:
            self.fail("url restart nao implementada")
        if "alto" in r1.text and "baixo" in r1.text and "correto" in r1.text:
            self.fail("nao quero que voce me diga se o meu chute foi alto, baixo ou correto. Ainda não chutei nada!")
    
        r2 = s.get(f"http://{url_servidor}/jogo?chute=60")
        if "60" not in r2.text:
            self.fail("url jogo deve conter o chute mais recente (60)")
        vi_alto = "alto" in r2.text
        vi_baixo = "baixo" in r2.text
        vi_correto = "correto" in r2.text 
        if not vi_alto and not vi_baixo and not vi_correto:
            self.fail("ou eu chutei alto, ou baixo, ou foi correto. Mas nao recebi nenhuma dessas 3 respostas")
        if vi_alto and vi_baixo:
            self.fail("ou eu chutei alto, ou baixo, ou foi correto. Mas recebi duas dessas respostas")
        if vi_alto and vi_correto:
            self.fail("ou eu chutei alto, ou baixo, ou foi correto. Mas recebi duas dessas respostas")
        if vi_correto and vi_baixo:
            self.fail("ou eu chutei alto, ou baixo, ou foi correto. Mas recebi duas dessas respostas")
    
    def test_05a_mesmo_chute_mesma_dica(self):
        s = requests.Session()
        r1 = s.get(f"http://{url_servidor}/restart")

        #vamos usar bastante que se chute=10
        #a string f"o chute foi {chute}"
        #tem o "buraco" preenchido, e vale "o chute foi 10"
        for chute in [10,20,30,40,50,60,70,80,90]:
            r2 = s.get(f"http://{url_servidor}/jogo?chute={chute}")
            if str(chute) not in r2.text:
                self.fail(f"url jogo deve conter o chute mais recente ({chute})")
            vi_alto = "alto" in r2.text
            vi_baixo = "baixo" in r2.text
            vi_correto = "correto" in r2.text 
            if not vi_alto and not vi_baixo and not vi_correto:
                self.fail("ou eu chutei alto, ou baixo, ou foi correto. Mas nao recebi nenhuma dessas 3 respostas")

            for i in range(0,2):
                r_repeat = s.get(f"http://{url_servidor}/jogo?chute={chute}")
                if vi_alto and "alto" not in r_repeat.text:
                    self.fail("fiz o mesmo chute mas obtive resultado diferente!")
                if vi_baixo and "baixo" not in r_repeat.text:
                    self.fail("fiz o mesmo chute mas obtive resultado diferente!")
                if vi_correto and "correto" not in r_repeat.text:
                    self.fail("fiz o mesmo chute mas obtive resultado diferente!")

    def test_06_restart_via_post(self):
        s = requests.Session()
        r1 = s.post(f"http://{url_servidor}/restart")
        if r1.status_code != 200:
            self.fail("url restart nao funciona com o verbo post")
        
    def test_07_envio_via_post(self):
        s = requests.Session()
        r1 = s.post(f"http://{url_servidor}/restart")
        if r1.status_code != 200:
            self.fail("url restart nao funciona com o verbo post")
        r2 = s.post(f"http://{url_servidor}/jogo", data={"chute":"30"})#a variavel data representa envio via form
        if "30" not in r2.text:
            self.fail("url jogo deve conter o chute mais recente (30) -- note que dessa vez mandei via post")
        if "alto" not in r2.text and "baixo" not in r2.text and "correto" not in r2.text:
            self.fail("ou eu chutei alto, ou baixo, ou foi correto. Mas nao recebi nenhuma dessas 3 respostas")

    def test_08_sessions_separadas(self):
        s = requests.Session()
        r1 = s.get(f"http://{url_servidor}/restart")
        if r1.status_code != 200:
            self.fail("url restart nao implementada")
        r2 = s.get(f"http://{url_servidor}/jogo?chute=500")
        if "500" not in r2.text:
            self.fail("url jogo deve conter o chute mais recente (500)")
        if "alto" not in r2.text:
            self.fail("chutei alto, e deveria ter recebido essa informação")
        r3 = s.get(f"http://{url_servidor}/jogo?chute=-500")
        if "-500" not in r3.text:
            self.fail("url jogo deve conter o chute mais recente (-500)")
        if "500" not in r3.text:
            self.fail("url jogo deve o chute anterior (500)")
        if "baixo" not in r3.text:
            self.fail("chutei baixo, e deveria ter recebido essa informação")
        
        s2 = requests.Session()
        r4 = s2.get(f"http://{url_servidor}/jogo")
        if "-500" in r4.text:
            self.fail("url jogo está confundindo chutes de um usuário com o outro")
        if "500" in r4.text:
            self.fail("url jogo está confundindo chutes de um usuário com o outro")
        
        r5 = s.get(f"http://{url_servidor}/jogo")
        if "500" not in r5.text:
            self.fail("url jogo está confundindo chutes de um usuário com o outro")

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()
