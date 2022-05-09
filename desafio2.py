# ----------- CLASSE -------------

class Constante():
    def __init__(self):
        self.aula = False
        self.min = 0
        self.presentes = 0

    def get_aula(self):
        return self.aula

    def set_aula_true(self):
        self.aula = True

    def get_min(self):
        return self.min

    def set_min(self, value):
        self.min = value

    def get_presentes(self):
        return self.presentes

    def set_increment_presentes(self):
        self.presentes += 1

# ----------- /CLASSE -------------

# ---------- OBEJETOS E VARIÁVEIS ---------

const = Constante()
chegadas = []
a = 0

# ---------- /OBEJETOS E VARIÁVEIS ---------

# ---------------- PROGRAMA ----------------

# Enquanto o usuário não digitar uma opção válida (inteiro), a variável 'a' continua sendo zero e o loop continua solicitando o mínimo de alunos.
while(a == 0):
    try:
        min = int(input("Minimo de alunos: "))
        a += 1
    except:
        print('Campo inválido!')
        a = 0

# Seta o valor de mínimo na constante.
const.set_min(min)

# Função que solicita ao usuário a inserção de um registro de chegada.
def get_registro():
    a = 0
    min = const.get_min()

    # Enquanto o usuário não digitar uma opção válida (inteiro), a variável 'a' continua sendo zero e o loop continua solicitando a chegada.
    while(a == 0):
        try:
            registro = int(input("Chegada: "))
            a += 1
        except:
            print('Campo inválido!')
            a = 0

    # Adiciona o registro à lista de chegadas.
    chegadas.append(registro)

    # Tratamento para alunos que não chegaram atrasados.
    if(registro <= 0):
        const.set_increment_presentes() # Incrementa o número de presentes.
        presentes = const.get_presentes() # Atribui o valor atual do parâmetro 'presentes' a uma variável.

        if(presentes >= min): # Caso o número de presentes seja maior ou igual ao número mínimo, terá aula.
            const.set_aula_true()

# Primeira chamada da função para solicitar registro de presença.
get_registro()

# Loop que pergunta ao usuário se deseja continuar, caso sim, realiza nova chamada da função para solicitar a presença.
while(1):
    resp = ' '

    while(resp != 'S' and resp != 'N'):
        resp = input("Cadastrar nova chegada? [S/N]: ")
        resp = resp.upper() # Será aceito 'S', 's', 'N', 'n' como respostas.

    if(resp == 'N'):
        break # Sai do loop

    get_registro() # Nova chamada à função para solicitar registro de presença.

# Imprime o resultado da lista de presenças.
print(f'{chegadas}')

# Testa o parâmetro booleano que diz se terá ou não terá aula, e imprime a resposta.
if(const.get_aula()):
    print('Aula normal.')
else:
    print('Aula cancelada.')

# ---------------- /PROGRAMA ----------------