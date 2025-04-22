def hanoi(disco, origem, auxiliar, destino):
    if disco == 0: return
    hanoi(disco-1,origem,destino,auxiliar)
    print(origem, '->', destino)
    hanoi(disco - 1, auxiliar, origem, destino)

hanoi(3,"A","B","C")