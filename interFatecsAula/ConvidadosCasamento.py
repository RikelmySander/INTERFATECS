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
    for x in "LISTA FINAL", "APENAS NOIVA", "APENAS NOIVO", "POR AMBOS","POR APENAS UM DELES":
        print("-" * 30)
        print(x)
        print("-" * 30)
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
        print("\n".join(result))
        if x != "POR APENAS UM DELES":
            print('*')

while True:
    convidados = input()
    if convidados == "":
        TabelaVazia()
        break
    else:
        if convidados != 'ACABOU':
            nome_convidado, quem_convidou = convidados.split(";")
            if quem_convidou == "noivo":
                convidados_noivo.add(nome_convidado)
            else:
                convidados_noiva.add(nome_convidado)
        else:
            break
TabelaConjuntos(convidados_noivo, convidados_noiva)