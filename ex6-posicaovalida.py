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
            
