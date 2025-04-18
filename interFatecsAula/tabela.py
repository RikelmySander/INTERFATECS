    # Uma empresa quer premiar seus funcionários de acordo
    # com a quantidade de anos que estão contratados e por
    # terem cumprido suas metas individuais. Para isso, a
    # empresa construirá uma tabela com os nomes dos
    # funcionários, salários, anos completos na empresa e
    # um campo com um indicativo de que o funcionário
    # cumpriu sua meta.
    #
    # A premiação será um bônus que corresponde ao próprio
    # salário do funcionário acrescido de 5% por cada ano
    # na empresa. Caso o funcionário tenha cumprido sua
    # meta, terá mais 10% sobre o bônus já conquistado.
    #
    # 1º) Seu programa deverá ler e armazenar os dados de
    #     todos os funcionários;
    # 2º) Em seguida, deverá exibir a tabela com os dados
    #     dos funcionários. Seja criativo no formato da
    #     tabela;
    # 3º) Por fim, seu programa exibirá outra tabela com o
    #     nome de cada funcionário e seu respectivo bônus.
    #
    # Obs.(1): O registro de cada funcionário estará em uma
    #          única linha, e os campos separados por ';'.
    # Obs.(2): A entrada encerrará quando o usuário
    #          pressionar [ENTER] sem digitar valores
    #          na linha, isto é, com uma linha em branco.
    #
    # Exemplo de    Matheus Oliveira;1000.0;3;sim [ENTER]
    # entrada:      Aline dos Santos;4000.0;4;sim [ENTER]
    #               Carla Oliveira;2500.0;2;não   [ENTER]
    #               Leon Kennedy;10000.0;10;sim   [ENTER]
    #               <linha vazia>                 [ENTER]
    #
    # Como o exemplo de entrada será interpretado:
    #
    # ------------------------------------------------
    #       NOME        |   SALÁRIO   |  TEMPO  | META
    # ------------------------------------------------
    # Matheus Oliveira  | R$  1000.00 |  3 anos | sim
    # Aline dos Santos  | R$  4000.00 |  4 anos | sim
    # Carla Oliveira    | R$  2500.00 |  2 anos | não
    # Leon Kennedy      | R$ 10000.00 | 10 anos | sim
    # ------------------------------------------------
    #
    # Como o exemplo de entrada será armazenado em Python:
    #
    # #                       0               1      2    3
    # funcionarios = [['Matheus Oliveira',  1000.0,  3, True ], # 0
    #                 ['Aline dos Santos',  4000.0,  4, True ], # 1
    #                 ['Carla Oliveira',    2500.0,  2, False], # 2
    #                 ['Leon Kennedy',     10000.0, 10, True ]] # 3
def maior(nomes):
    m = 0
    for nome in nomes:
        tamanho = len(nome)
        if tamanho > m:
            m = tamanho
    return m

def maior_nome_tabela(funcionarios):
    nomes = []
    for funcionario in funcionarios:
        nomes.append(funcionario[0])
    return maior(nomes)

def exibe_funcionarios(funcionarios):
    print('-' * 50)
    print(f'{"NOME":^{maior_nome_tabela(funcionarios)}} | {"SALÁRIO":^11} | {"TEMPO":^7} | META')
    print('-' * 50)
    for nome, salario, tempo, meta in funcionarios:
        print(f'{nome:{maior_nome_tabela(funcionarios)}}', end=' | ')
        print(f'R$ {salario:8.2f}', end=' | ')
        print(f'{tempo:2} anos', end=' | ')
        print('sim' if meta else 'não')
    print('-' * 50)

def exibe_bonus(bonus):
    print('-' * 30)
    print(f'{"NOME":^{maior_nome_tabela(funcionarios)}} | {"BÔNUS":^11}')
    print('-' * 30)
    for nome, valor in bonus:
        print(f'{nome:{maior_nome_tabela(bonus)}}', end=' | ')
        print(f'R$ {valor:8.2f}')
    print('-' * 30)

funcionarios = []

funcionario = input()

while funcionario != '':
    nome, salario, tempo, meta = funcionario.split(';')
    salario = float(salario)
    tempo = int(tempo)
    meta = (meta == 'sim')
    funcionarios.append([nome, salario, tempo, meta])
    funcionario = input()
exibe_funcionarios(funcionarios)

bonus = []

for funcionario in funcionarios:
    valor = funcionario[1] + (0.05 * funcionario[2] * funcionario[1])
    if funcionario[3]:
        valor = 1.10*valor
    bonus.append([funcionario[0],valor])

exibe_bonus(bonus)