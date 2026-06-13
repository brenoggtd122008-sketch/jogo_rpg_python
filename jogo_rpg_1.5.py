mapa = [
    ["P", "0", "M", "0", "T"],
    ["0", "M", "0", "0", "0"],
    ["T", "0", "0", "M", "0"],
    ["0", "0", "M", "0", "T"],
    ["0", "T", "0", "0", "B"]
]

tesouros = [[0, 4], [2, 0], [3, 4], [4, 1]]
inimigos = [[0, 2], [1, 1], [2, 3], [3, 2], [4, 4]]

jogador_vida = 100
pocoes_cura = []

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
    print("(I) INVENTÁRIO\n")

    jogador = input("\nSUA AÇÃO --> ").upper()

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
                pocoes_cura.append("POÇÃO DE CURA")
                tesouros.remove(t)
                print("\nTESOURO ENCONTRADO - (POÇÃO DE CURA ADICIONADA AO SEU INVENTÁRIO)\n")

    if len(inimigos) == 0:
        pass
    else:
        for i in inimigos:
            v1, v2 = i[0], i[1]

            if posicao_atual == mapa[v1][v2]:
                inimigos.remove(i)

                nome_inimigo = "MONSTRO"
                inimigo_vida = 40
                dano_inimigo = 10

                if v1 == v2 == 4:
                    nome_inimigo = "CHEFE"
                    inimigo_vida = 100
                    dano_inimigo = 25

                while True:
                    print(F"\n---INIMIGO ENCONTRADO ({nome_inimigo})---\n")
                    print(F"SEU HP: {jogador_vida} | HP DO INIMIGO {inimigo_vida}\n")
                    print("(1) ATACAR\n(2) USAR POÇÃO DE CURA\n")

                    jogador = input("SUA AÇÃO --> ")

                    match jogador:
                        case "1":
                            inimigo_vida -= 20
                            if nome_inimigo == "CHEFE" and inimigo_vida <= 0:
                                print("\nVOCÊ VENCEU O CHEFE\n")
                                jogador_condicao = False
                                break
                            elif inimigo_vida <= 0:
                                print("\nVOCÊ VENCEU O MONSTRO\n")
                                break
                            else:
                                jogador_vida -= dano_inimigo

                        case "2":
                            if jogador_vida == 100:
                                print("\nVIDA CHEIA\n")
                            elif len(pocoes_cura) == 0:
                                print("\nVOCÊ NÃO POSSUI NENHUMA POÇÃO DE CURA\n")
                            else:
                                jogador_vida += 25
                                pocoes_cura.pop()
                                if jogador_vida > 100:
                                    jogador_vida = 100

                        case _:
                            print("\nCOMANDO INEXISTENTE\n")

    if not jogador_condicao:
        break

print("\nJOGO ENCERRADO\n")
