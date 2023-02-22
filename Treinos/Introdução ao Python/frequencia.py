'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

def frequencia(texto):
    
    lista = list(texto.split(" "))
    
    dic = {}
    for palavra in lista: 
        if palavra not in dic:
            dic.update({palavra : 1})
        else: 
            dic[palavra] += 1
            
    resposta = [(k,v) for k,v in dic.items()]
    resposta.sort(key = lambda t: (t[0]))
    resposta.sort(key = lambda t: (t[1]), reverse = True)

    resp = [k for k,v in resposta]
    
    return resp
