convidados_noiva = set()
convidados_noivo = set()

def TabelaConjuntos(noivo,noiva):
    for x in "LISTA FINAL", "APENAS NOIVA", "APENAS NOIVO", "POR AMBOS","POR APENAS UM DELES":
        print("-" * 20)
        print(x)
        print("-" * 20)
        match x:
            case "LISTA FINAL":
                result = sorted(noivo | noiva)
            case "POR AMBOS":
                result = sorted(noiva & noivo)
            case "APENAS NOIVA":
                result = sorted(noiva - noivo)
            case "APENAS NOIVO":
                result = sorted(noivo - noiva)
            case "POR APENAS UM DELES":
                result = sorted(noivo ^ noiva)
        if result:
            print("\n".join(result))
        if x != "POR APENAS UM DELES":
            print('*')

while True:
    convidados = input()
    if convidados == "ACABOU":
        break
    nome_convidado, quem_convidou = convidados.split(";")
    if quem_convidou == "noivo":
        convidados_noivo.add(nome_convidado)
    else:
        convidados_noiva.add(nome_convidado)
TabelaConjuntos(convidados_noivo,convidados_noiva)