qtd_canais = int(input())

canais = []

for i in range(qtd_canais):
    nome, inscritos, monetizacao, premium = input().split(';')
    inscritos = int(inscritos)
    monetizacao = float(monetizacao)
    premium = premium == 'sim'
    canais.append([nome,inscritos,monetizacao,premium])

fixo_premium = float(input())
fixo_nao_premium = float(input())

bonus = []

for nome, inscritos, monetizacao, premium in canais:
    valor = monetizacao
    if premium:
        valor += fixo_premium * (inscritos // 1000)
    else:
        valor += fixo_nao_premium * (inscritos // 1000)
    bonus.append([nome,valor])

print("-----")
print("BÔNUS")
print("-----")
for nome, valor in bonus:
    print(f'{nome}: R$ {valor:.2f}')