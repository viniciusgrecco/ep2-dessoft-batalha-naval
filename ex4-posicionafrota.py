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