# Criação de um dicionário vazio (1).
d = {}

# Criação de um dicionário vazio (2).
d = dict()

# Tamanho de um dicionário.
print(len(d))

# Criação de um dicionário com itens.
# Obs.: Não há ordem nos itens de um dicionário e
#       as chaves devem ser únicas e de um tipo de
#       dados imutável.
d = {'ana':190, 'bia':192, 'clô':193}
d = dict([('ana',190), ('bia',192), ('clô',193)])

# Acessar um item do dicionário.
print(d[chave])

# Incluir um item no dicionário.
d[chave ainda não incluída] = valor

# Alterar um item do dicionário.
d[chave já incluída] = novo valor

# Remover um item do dicionário (1).
# Obs.(1): remove o item cuja chave é dada como argumento
#          e devolve como resposta o valor do item.
# Obs.(2): lança uma exceção caso não exista o item.
x = d.pop(chave)
print(x)

# Remover um item do dicionário (2).
# Obs.(1): remove um item arbitrário e devolve como resposta
#          uma tupla (chave, valor) referente ao item.
# Obs.(2): lança uma exceção caso o dicionário esteja vazio.
x = d.popitem()
print(x)
x = d.popitem()
print(x)

# Remover um item do dicionário (3).
del d[chave]

# Remover todos os itens do dicionário.
d.clear()

# Coletar apenas as chaves de um dicionário.
chaves = d.keys()
print(chaves)

# Coletar apenas os valores de um dicionário.
valores = d.values()
print(valores)

# Coletar os itens de um dicionário.
itens = d.items()
print(itens)

# Percorrer um dicionário (coletando as chaves).
for chave in d:
    print(chave)

for chave in d.keys():
    print(chave)

# Percorrer um dicionário (coletando os valores).
for valor in d.values():
    print(valor)

# Percorrer um dicionário (coletando os itens).
for item in d.items():
    print(item)

# Percorrer um dicionário (desempacotando os itens).
for chave, valor in d.items():
    print('Chave =', chave)
    print('Valor =', valor)
