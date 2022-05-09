# Função para obter o número reverso da entrada
def reverso(n):
    return int(str(n)[::-1]) # Transforma o número de entrada em string, mantém o seu tamanho e inverte os caracteres [::-1], após isso transforma a string em inteiro novamente

# Acima de 900000, é impossível a soma com seu reverso dar menor que 1000000.
for n in range(900000):

    n_reverso = reverso(n)
    soma = n + n_reverso

    # (n % 10 != 0): Teste se o número ou seu reverso não começa com zero. (soma % 2 != 0): Teste se o resultado é ímpar. (soma < 1000000): Teste se o resultado é menor que um milhão.
    if(n % 10 != 0 and soma % 2 != 0 and soma < 1000000):
        print(f'{n}: {n} + {n_reverso} = {soma}')
