def main():
    qtd_leituras = int(input())
    for i in range(qtd_leituras):
        temperatura, umidade, previsao = input().split()
        temperatura = float(temperatura)
        umidade = float(umidade)
        previsao = int(previsao)
        if previsao == 1:
            print('NAO REGAR')
        elif temperatura > 30.0 and \
                umidade < 50.0:
            print('REGAR')
        else:
            print('NAO REGAR')
main()