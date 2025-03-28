convidados_noiva = set()
convidados_noivo = set()

def TabelaVazia():
    for i in "LISTA FINAL", "APENAS NOIVA", "APENAS NOIVO", "POR AMBOS","POR APENAS UM DELES":
        if i != "POR APENAS UM DELES":
            print("-" * 20)
            print(i)
            print("-" * 20)
            print("*")
        else:
            print("-" * 20)
            print(i)
            print("-" * 20)

def TabelaConjuntos(noivo,noiva):
    print("-" * 20)
    for i in "LISTA FINAL", "APENAS NOIVA", "APENAS NOIVO", "POR AMBOS","POR APENAS UM DELES":
        print(i)
        print("-" * 30)
        print(noivo | noiva)

while True:
    convidados = input()
    if convidados == "":
        TabelaVazia()
        break
    else:
        nome_convidado, quem_convidou = convidados.split(";")
        if quem_convidou == "noivo":
            convidados_noivo.add(nome_convidado)
        else:
            convidados_noiva.add(nome_convidado)

print(convidados_noivo)
print(convidados_noiva)