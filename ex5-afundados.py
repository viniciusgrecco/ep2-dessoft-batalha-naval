def afundados(embarcacoes,tabuleiro):
    contagem = 0
    for navio in embarcacoes:
        if navio == 'porta-aviões':
            lista_navios = embarcacoes[navio]
            for navio in lista_navios:
                 x = navio[0][0]
                 y = navio[0][1]
                 x1= navio[1][0]
                 y1= navio[1][1]
                 x2=navio[2][0]
                 y2=navio[2][1]
                 x3=navio[3][0]
                 y3=navio[3][1] 
                 coordenada1 = tabuleiro[x][y]
                 coordenada2 = tabuleiro[x1][y1]
                 coordenada3 = tabuleiro[x2][y2]
                 coordenada4 = tabuleiro[x3][y3]
                 if coordenada1 == 'X' and coordenada2 == 'X' and coordenada3 == 'X' and coordenada4 == 'X':
                    contagem += 1

        if navio == 'navio-tanque':
             lista_navios = embarcacoes[navio]
             for navio in lista_navios:
                 x = navio[0][0]
                 y = navio[0][1]
                 x1= navio[1][0]
                 y1= navio[1][1]
                 x2=navio[2][0]
                 y2=navio[2][1]
                 coordenada1 = tabuleiro[x][y]
                 coordenada2 = tabuleiro[x1][y1]
                 coordenada3 = tabuleiro[x2][y2]
                 if coordenada1 == 'X' and coordenada2 == 'X' and coordenada3 == 'X':
                    contagem += 1

        if navio == 'contratorpedeiro':
             lista_navios = embarcacoes[navio]
             for navio in lista_navios:
                x = navio [0][0]
                y = navio [0][1]
                x1 = navio [1][0]
                y1 = navio [1][1]
                coordenada1 = tabuleiro[x][y]
                coordenada2 = tabuleiro[x1][y1]
                if coordenada1 == 'X' and coordenada2 == 'X':
                     contagem += 1

        if navio == 'submarino':
             lista_navios = embarcacoes[navio]
             for navio in lista_navios:
                 for posicao in navio:
                     x = posicao[0]
                     y = posicao[1] 
                     coordenada1 = tabuleiro[x][y]
                     if coordenada1 == 'X':
                        contagem += 1
    return contagem