"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""

def junta(velho, novo):
    
    resultado = ""
    for i in range(len(novo)):
        if novo[i] != '*':
            resultado += novo[i]
        else:
            resultado += velho[i]
            
    return resultado
    
    
def hacker(log):
    
    res = {}
    for (num, mail) in log:
        if mail not in res:
            res[mail] = num
        else:
            res[mail] = junta(res[mail], num)
    
    list = [(v,k) for k,v in res.items()]

    numeros = {}
    for (a,b) in list:
        numHastag = 0
        for i in a:
            if i == '*':
                numHastag += 1 
        numeros.update({b : numHastag})
    
    tripla = [(v, k, numeros[k]) for k,v in res.items()]
    tripla.sort(key = lambda t: (t[2], t[1]))

    resposta = [(v, k) for v, k, numeros[k] in tripla]

    return resposta
