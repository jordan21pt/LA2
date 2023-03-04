'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que lista os cruzamentos de uma cidade 
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto 
maior o número de ruas que interliga.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos). 
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade, 
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo 
nível de criticidade deverão ser listados por ordem alfabética.
'''

def cruzamentos(ruas):
    
    cruz = {}
    
    lista = []
    for r in ruas:
        if r[0] == r[-1]:
            lista.append(r[0])
        else:
            lista.append(r[0])
            lista.append(r[-1])
    
    for letra in lista:
        if letra not in cruz:
            cruz[letra] = 1
        else:
            cruz[letra] += 1
    
    lista2 = [(k, v) for k,v in cruz.items()]   
    
    lista2.sort(key = lambda t: (t[1],t[0]))

    return lista2
