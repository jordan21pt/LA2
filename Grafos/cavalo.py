'''

O objectivo deste problema é determinar quantos movimentos são necessários para 
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.

'''

def bfs(moves,o,d):
    dist = {}
    visitados = [o]
    a_visitar = [o]
    while a_visitar:
        atual = a_visitar.pop(0)
        if atual == d:
            break
        if atual not in dist:
            dist[atual] = 0
        for move in moves:
            if (move[0] + atual[0], move[1] + atual[1]) not in visitados:
                visitados.append((move[0] + atual[0], move[1] + atual[1] ))
                a_visitar.append((move[0] + atual[0], move[1] + atual[1]))
                dist[move[0] + atual[0], move[1] + atual[1] ] = dist[atual] + 1
        
    return dist[d]
            

def saltos(o,d):
    
    if o == d:
        return 0
        
    moves = ((2, 1),(1, 2),(-2, 1),(2, -1),(-2, -1),(-1, 2),(1, -2),(-1, -2))
    return bfs(moves,o,d)
    
