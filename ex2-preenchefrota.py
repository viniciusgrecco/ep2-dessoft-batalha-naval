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
    

frota = {
  "navio-tanque":[
    [[6,1],[6,2],[6,3]]
  ]
}
nome_navio = 'navio-tanque'
linha = 4
coluna = 7
orientacao = 'vertical'
tamanho = 3

resultado = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
print(resultado)