# Crie um programa que solicite ao usuário diversos registros
# de funcionários, os registros serão compostos dos seguintes campos
# (1) CPF; (2) nome completo; (3) salário.
# Ao final, o programa deverá exibir os dados de todos os funcionários e
# o total da folha de pagamento.
# Obs.(1): Armazene os dados em um dicionário.
# Obs.(2): a entrada de dados será encerrada quando um cpf zero for
#          inserido.
def exibe_funcionarios(funcionarios):
    print('-' * 40)

    print('REGISTROS DOS FUNCIONÁRIOS')

    print('-' * 40)

    for chave, valor in funcionarios.items():
        cpf = chave

        nome, salario = valor

        print(f'CPF: {cpf}\nNome: {nome}\nSalário: R$ {salario:.2f}')

    print('-' * 40)
def exibe_salario(funcionarios):
    print('-' * 40)

    print('SALARIO TOTAL')

    print('-' * 40)
    total = 0
    for chave, valor in funcionarios.items():
        nome, salario = valor
        total += salario

    print(f'Salário total: R$ {total:.2f}')

    print('-' * 40)

funcionarios = dict()

cpf = int(input('CPF? '))

while cpf != 0:
    nome = input('Nome? ')

    salario = float(input('Salário? R$ '))

    funcionarios[cpf] = [nome, salario]

    print('-' * 30)

    cpf = int(input('CPF? '))


exibe_funcionarios(funcionarios)
exibe_salario(funcionarios)
