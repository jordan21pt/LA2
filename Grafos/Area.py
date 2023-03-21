def area(p,mapa):
    
    x = p[0]
    y = p[1]
    #print("aqui:", mapa[2])
    #print("largura:",len(mapa))
  
  
    visitados = {(x,y)}
  
    a_visitar = [(x,y)]

    #pos_atual = a_visitar.pop(0)

    #print("aqui: ", mapa[pos_atual[0]][pos_atual[1]])

    #print("pos_atual:", pos_atual[1]-1)
    

  
    while a_visitar:
      pos_atual = a_visitar.pop(0)

      #andar para a direita
      if pos_atual[1]+1 < len(mapa) and mapa[pos_atual[0]][pos_atual[1]+1] != '*' and (pos_atual[0],pos_atual[1]+1) not in visitados:
        visitados.add((pos_atual[0],pos_atual[1]+1))
        a_visitar.append((pos_atual[0],pos_atual[1]+1))
        #print("dir", pos_atual[0],pos_atual[1])

      #andar para a esquerda
      if pos_atual[1]-1 >= 0 and mapa[pos_atual[0]][pos_atual[1]-1] != '*' and (pos_atual[0],pos_atual[1]-1) not in visitados:
        visitados.add((pos_atual[0],pos_atual[1]-1))
        a_visitar.append((pos_atual[0],pos_atual[1]-1))
        #print("esq", pos_atual[0],pos_atual[1])

      #andar para baixo
      if pos_atual[0]+1 < len(mapa) and mapa[pos_atual[0]+1][pos_atual[1]] != '*' and (pos_atual[0]+1,pos_atual[1]) not in visitados:
        visitados.add((pos_atual[0]+1,pos_atual[1]))
        a_visitar.append((pos_atual[0]+1,pos_atual[1]))
        p#rint("baixo", pos_atual[0],pos_atual[1])

      #andar para cima
      if pos_atual[0]-1 >= 0 and mapa[pos_atual[0]-1][pos_atual[1]] != '*' and (pos_atual[0]-1,pos_atual[1]) not in visitados:
        visitados.add((pos_atual[0]-1,pos_atual[1]))
        a_visitar.append((pos_atual[0]-1,pos_atual[1]))
        #print("cima", pos_atual[0],pos_atual[1])

      #print()

    #print(visitados)
    return len(visitados)
