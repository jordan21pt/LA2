'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''

def apelidos(nomes):
    
    numApelidos = []
    
    for nome in nomes:
        cont = 0
        for i in range(0, len(nome)):
            if nome[i] == " ":
                cont += 1
        numApelidos.append(cont)
    
    tuplo = [(nomes[i], numApelidos[i]) for i in range(0, len(nomes))]
    tuplo.sort(key = lambda t: (t[1],t[0]))

    nomesOrd = []
    for t in tuplo:
        nomesOrd.append(t[0])
    
    return nomesOrd
