def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao = [[linha,coluna]]
    if orientacao == 'vertical':
        i = 0
        while i < tamanho-1:
            linha += 1
            i += 1
            posicao2 = [linha,coluna]
            posicao.append(posicao2)
    if orientacao == 'horizontal':
        i = 0
        while i < tamanho-1:
            coluna += 1
            i += 1
            posicao3= [linha,coluna]
            posicao.append(posicao3)
    return posicao

def preenche_frota( dicfrota, nomenavio, linha, coluna, orientacao, tamanho ):
    if nomenavio not in dicfrota.keys():
        dicfrota[nomenavio] = [define_posicoes(linha,coluna,orientacao,tamanho)]
    else:
        dicfrota[nomenavio] += [define_posicoes(linha,coluna,orientacao,tamanho)]
    return dicfrota

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    return tabuleiro

def posiciona_frota(dic):
  tabuleiro = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
  for navio in dic:
    lista_navios = dic[navio]
    for navio in lista_navios:
      for posicao in navio:
        x = posicao[0]
        y = posicao[1]
        # Substituir no tabuleiro 
        tabuleiro[x][y] = 1

  return tabuleiro

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

def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao = [[linha,coluna]]
    if orientacao == 'vertical':
        i = 0
        while i < tamanho-1:
            linha += 1
            i += 1
            posicao2 = [linha,coluna]
            posicao.append(posicao2)
    if orientacao == 'horizontal':
        i = 0
        while i < tamanho-1:
            coluna += 1
            i += 1
            posicao3= [linha,coluna]
            posicao.append(posicao3)
    return posicao

def posicao_valida(dicnavios,linha,coluna,orientacao,tamanho):
    posiciona = define_posicoes(linha,coluna,orientacao,tamanho)
    soma = 0
    for i in posiciona:
         coordenada = i
         for e in dicnavios:
             navio = dicnavios[e]
             for c in navio:
                 for b in c:
                     if b == coordenada:
                         soma += 1
    for i in posiciona:
        for v in i:
            if v >= 10 or v < 0:
                return False
    if soma == 0:
        return True
    else:
        return False

while True:
    
    linha = int(input('linha: '))
    coluna = int(input('coluna: '))
    orientacao = int(input('orientacao: '))
    if orientacao == 1:
        orientacao = 'vertical'
    if orientacao == 2:
        orientacao = 'horizontal'
