mapa = [
    ["P", "0", "M", "0", "T"],
    ["0", "M", "0", "0", "0"],
    ["T", "0", "0", "M", "0"],
    ["0", "0", "M", "0", "T"],
    ["0", "T", "0", "0", "B"]
]

tesouros = [[0, 4], [2, 0], [3, 4], [4, 1]]
monstros = [[0, 2], [1, 1], [2, 3], [3, 2]]

jogador_vida = 100
pocoes_cura = 0

linha = 0
coluna = 0

jogador_condicao = True

while True:
    posicao_atual = mapa[linha][coluna]

    for i in mapa:
        for v in i:
            print(F"[{v}]", end="")
        print()

    print("\n(W) CIMA       | (D) DIREITA")
    print("(S) BAIXO      | (A) ESQUERDA")
    print("(I) INVENTÁRIO | (G) SALVAR/SAIR\n")

    jogador = input("\nCOMANDO --> ").upper()

    match jogador:

        case "W":
            if linha == 0:
                print("\nLIMITE DO MAPA\n")
            else:
                mapa[linha][coluna] = "0"
                linha -= 1
                mapa[linha][coluna] = "P"
        
        case "S":
            if linha == 4:
                print("\nLIMITE DO MAPA\n")
            else:
                mapa[linha][coluna] = "0"
                linha += 1
                mapa[linha][coluna] = "P"

        case "D":
           if coluna == 4:
                print("\nLIMITE DO MAPA\n")
           else:
                mapa[linha][coluna] = "0"
                coluna += 1
                mapa[linha][coluna] = "P"
        
        case "A":
          if coluna == 0:
                print("\nLIMITE DO MAPA\n")
          else:
                mapa[linha][coluna] = "0"
                coluna -= 1
                mapa[linha][coluna] = "P"
        
        case "I":
            print(F"\nVIDA: {jogador_vida}")
            print(F"POÇÕES DE CURA: {pocoes_cura}\n")

        case _:
            print("\nCOMANDO INVÁLIDO\n")

    if len(tesouros) == 0:
        pass
    else:
        for t in tesouros:
            v1, v2 = t[0], t[1]
            if posicao_atual == mapa[v1][v2]:
                pocoes_cura += 1
                tesouros.remove(t)
                print("\nTESOURO ENCONTRADO - (POÇÃO DE CURA ADICIONADA AO SEU INVENTÁRIO)\n")

    if len(monstros) == 0:
        pass
    else:
        for m in monstros:
            v1, v2 = m[0], m[1]
            if posicao_atual == mapa[v1][v2]:
                print("\nINIMIGO ENCONTRADO - (MONSTRO)\n")
                print("\n---BATALHA INICIADA---\n")
                monstros.remove(m)
                monstro_vida = 30

                while True:
                    print(F"\nHP: {jogador_vida} ----- VIDA DO MONSTRO: {monstro_vida}\n")
                    print("(1) - ATACAR\n(2) - USAR CURA\n")

                    jogador = input("COMANDO --> ")

                    match jogador:
                        case "1":
                            monstro_vida -= 15

                            if monstro_vida <= 0:
                                print("\nVOCÊ VENCEU\n")
                                break
                            else:
                                jogador_vida -= 10
                            
                            if jogador_vida <= 0:
                                print("\nVOCÊ PERDEU\n")
                                jogador_condicao = False
                                break

                        case "2":
                            if pocoes_cura <= 0:
                                print("\nVOCÊ NÃO TEM POÇÃO DE CURA\n")
                            else:
                                jogador_vida += 25
                                pocoes_cura -= 1

                        case _:
                            print("\nCOMANDO INEXISTENTE\n")

    if posicao_atual == mapa[4][4]:
        print("\nINIMIGO ENCONTRADO - (CHEFE)\n")
        print("\n---BATALHA INICIADA---\n")
        chefe_vida = 100

        while True:
            print(F"\nHP: {jogador_vida} ----- VIDA DO MONSTRO: {chefe_vida}\n")
            print("(1) - ATACAR\n(2) - USAR CURA\n")

            jogador = input("COMANDO --> ")

            match jogador:
                case "1":
                    chefe_vida -= 15

                    if chefe_vida <= 0:
                        print("\nVOCÊ VENCEU\n")
                        jogador_condicao = False
                        break
                    else:
                        jogador_vida -= 20
                            
                    if jogador_vida <= 0:
                        print("\nVOCÊ PERDEU\n")
                        jogador_condicao = False
                        break

                case "2":
                    if pocoes_cura <= 0:
                        print("\nVOCÊ NÃO TEM POÇÃO DE CURA\n")
                    else:
                        jogador_vida += 25
                        pocoes_cura -= 1

                case _:
                    print("\nCOMANDO INEXISTENTE\n")

    if not jogador_condicao:
        break

print("\nJOGO ENCERRADO\n")
