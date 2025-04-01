def cria_canais(qtd_canais):
    canais = []
    for i in range(qtd_canais):
        nome, inscritos, monetizacao, premium = input().split(';')
        inscritos = int(inscritos)
        monetizacao = float(monetizacao)
        premium = premium == 'sim'
        canais.append([nome, inscritos, monetizacao, premium])
    return canais

def cria_bonus(canais, fixo_premium, fixo_nao_premium):
    bonus = []
    for nome, inscritos, monetizacao, premium in canais:
        valor = monetizacao
        if premium:
            valor += fixo_premium * (inscritos // 1000)
        else:
            valor += fixo_nao_premium * (inscritos // 1000)
        bonus.append([nome, valor])
    return bonus

def exibe_bonus(bonus):
    print('-' * 5)
    print('BÔNUS')
    print('-' * 5)
    for nome, valor in bonus:
        print(f'{nome}: R$ {valor:.2f}')

def main():
    qtd_canais = int(input())
    canais = cria_canais(qtd_canais)
    fixo_premium = float(input())
    fixo_nao_premium = float(input())
    bonus = cria_bonus(canais, fixo_premium, fixo_nao_premium)
    exibe_bonus(bonus)

main()