'''
Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.
'''

def tabela(jogos):
    
    #dicionario com os pontos de cada clube
    tabClass = {}
    for (cc, gc, cf, gf) in jogos:
        if cc not in tabClass:
            tabClass.update({cc : 0})
        if cf not in tabClass:
            tabClass.update({cf : 0})

    for (cc, gc, cf, gf) in jogos:
        if gc > gf:
            tabClass[cc] += 3
        elif gc < gf:
            tabClass[cf] += 3
        else:
            tabClass[cc] += 1
            tabClass[cf] += 1
        
    #print(tabClass)
    
    #dicionario com os golos marcados por cada clube
    tabGolosM = {}
    for (cc, gc, cf, gf) in jogos:
        if cc not in tabGolosM:
            tabGolosM.update({cc : 0})
        if cf not in tabGolosM:
            tabGolosM.update({cf : 0})
    
    for (cc, gc, cf, gf) in jogos:
        tabGolosM[cc] += gc
        tabGolosM[cf] += gf
    
    #print(tabGolosM)
    
    
    #dicionario com os golos sofridos por cada clube
    tabGolosS = {}
    for (cc, gc, cf, gf) in jogos:
        if cc not in tabGolosS:
            tabGolosS.update({cc : 0})
        if cf not in tabGolosS:
            tabGolosS.update({cf : 0})
    
    for (cc, gc, cf, gf) in jogos:
        tabGolosS[cf] += gc
        tabGolosS[cc] += gf
    
    #print(tabGolosS)
    
    
    #criar uma lista com as informações dos dicionarios e 
    #dar sort a lista como pedido no enuciario
    tripla = [(k, v, (tabGolosM[k] - tabGolosS[k])) for k, v in tabClass.items()]
    tripla.sort(key = lambda t: t[0])
    tripla.sort(key = lambda t: t[2], reverse = True)
    tripla.sort(key = lambda t: t[1], reverse = True)
    
    #criar a lista como pedido no enunciado(clube, pontos)
    resposta = [(k,v) for k,v,c in tripla]

    return resposta
