'''

O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

'''
def dfs(adj,o):
    return dfs_aux(adj,o,set(),{})
    
def dfs_aux(adj,o,vis,pai):
    vis.add(o)
    for d in adj[o]:
        if d not in vis:
            pai[d] = o
            dfs_aux(adj,d,vis,pai)
    return vis


def maior(vizinhos):
    
    adj = {}
    for lista in vizinhos:
        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                if lista[i] not in adj:
                    adj[lista[i]] = set()
                if lista[j] not in adj:
                    adj[lista[j]] = set()
                adj[lista[i]].add(lista[j])
                adj[lista[j]].add(lista[i])
    
    if len(vizinhos) == 0:
        return 0
        
    if len(adj) == 0:
        return 1
    
    lista = []
    for ad in adj:
        print(ad,":", dfs(adj, ad))
        lista.append(len(dfs(adj, ad)))
 
    
    return max(lista)
    
    
