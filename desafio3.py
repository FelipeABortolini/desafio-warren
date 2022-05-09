# --------------- IMPORTAÇÕES ----------------------

from itertools import combinations_with_replacement # Importação de função que realiza combinações do mesmo elemento para o mesmo elemento sem importar a ordem com que aparecem.

# --------------- /IMPORTAÇÕES ----------------------

# ---------- OBEJETOS E VARIÁVEIS ---------

vector = []
n = 0
sum_vect_length = 0
dif_sum_main = -1
vect_min_dif = []
min_dif = -1
first_pass = True
continue_iteration = True
actual_lenght = 0

# ---------- /OBEJETOS E VARIÁVEIS ---------

# ----------------- FUNÇÕES -------------------

# Função para extrair o module de um número.
def module(num):
    if(num < 0):
        return -num
    else:
        return num


def get_data():

    # Enquanto o usuário não digitar uma opção válida (inteiro), a variável 'a' continua sendo zero e o loop continua solicitando o número resultado da soma.
    a = 0
    while(a == 0):
        try:
            n = int(input("Número resultado: "))
            a += 1
        except:
            print('Campo inválido!')
            a = 0

    get_num_vetor() # Solicita o primeiro número do vetor.

    # Loop que pergunta ao usuário se deseja continuar, caso sim, realiza nova chamada da função para solicitar novo número para o vetor.
    while(1):
        resp = ' '

        while(resp != 'S' and resp != 'N'):
            resp = input("Cadastrar novo número? [S/N]: ")
            resp = resp.upper() # Será aceito 'S', 's', 'N', 'n' como respostas.

        if(resp == 'N'):
            break # Sai do loop.

        get_num_vetor() # Nova chamada à função para solicitar novo número para o vetor.

    return(n) # Retorna o valor que deve ser a refrência de soma.


# Função que solicita ao usuário a inserção de um novo número ao vetor.
def get_num_vetor():
    a = 0

    # Enquanto o usuário não digitar uma opção válida (inteiro), a variável 'a' continua sendo zero e o loop continua solicitando o número.
    while(a == 0):
        try:
            num = int(input("Número: "))
            a += 1
        except:
            print('Campo inválido!')
            a = 0

    # Adiciona o número ao vetor.
    vector.append(num)

# ----------------- /FUNÇÕES -------------------


# ---------------- PROGRAMA ----------------

n = get_data()

minimo_vetor = min(vector)

while(continue_iteration):
    # Obtem todas as combinações do vetor, sem importar a ordem com que aparecem, com tamanho correspondente ao valor da vaiável 'sum_vect_length'.
    comb = combinations_with_replacement(vector, sum_vect_length)

    # Iteração entre as diferentes combinações geradas.
    for c in comb:
        comb_sum = sum(c) # Soma os elementos contidos na combinação em análise.

        dif_sum = module(comb_sum - n) # Tira o módulo da diferença entre a soma e o número que se deseja.

        # Primeira passagem, para atribuir o valor da diferença à variável que guarda o valor mínimo.
        if(first_pass):

            dif_sum_main = dif_sum
            min_dif = dif_sum
            first_pass = False

        elif(dif_sum < min_dif):

            dif_sum_main = dif_sum
            min_dif = dif_sum
            vect_min_dif.clear() # Limpa o vetor com as combinações de até então.
            actual_lenght = sum_vect_length # Parâmetro para não haver conflitos entre combinações de tamahos diferentes, mas com o mesmo valor de diferença em relação à soma.

        if(dif_sum == min_dif and actual_lenght == sum_vect_length):
            vect_min_dif.append(c) # Guarda as combinações com menor número de elemntos e mais próximas do valor de destino até então.

    # Aumenta em uma unidade o tamanho das combinações.
    sum_vect_length += 1

    # Caso o menor valor do vetor somado n vezes ultrapasse o valor desejado, a iteração é finalizada e os valores atuais são mantidos como resposta. (Considera-se n o número de elementos das próximas combinações).
    if(minimo_vetor * sum_vect_length > n):
        continue_iteration = False

    # Se a diferença entre a soma obtida e a desejada for 0, encerra-se as iterações e a resposta já está obtida.
    if(dif_sum_main == 0): break

# Impressão dos resultados.
print('\nSAÍDA DE DADOS:\n')
print(n)
for v in vect_min_dif:
    print(v)

# ---------------- /PROGRAMA ----------------