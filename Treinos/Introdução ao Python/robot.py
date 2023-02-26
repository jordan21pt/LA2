'''
Neste problema prentede-se que implemente uma função que calcula o rectângulo onde se movimenta um robot.

Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá receber uma sequência de comandos numa string.
Existem quatro tipos de comandos que o robot reconhece:
  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita 
  'H' - parar e regressar à posição inicial virado para cima
  
Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas (minímo no eixo dos X, mínimo no eixo dos Y, máximo no eixo dos X, máximo no eixo dos Y) que definem o rectângulo 
onde se movimentou desde o início da sequência de comandos ou desde o último comando 'H'.

A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)
'''

def direcao(direcaoAtual, comando):
    if comando == "E":
        if direcaoAtual == "ypos":
            direcaoAtual = "xneg"
        elif direcaoAtual == "xneg":
            direcaoAtual = "yneg"
        elif direcaoAtual == "yneg":
            direcaoAtual = "xpos"
        elif direcaoAtual == "xpos":
            direcaoAtual = "ypos"
    elif comando == "D":
        if direcaoAtual == "ypos":
            direcaoAtual = "xpos"
        elif direcaoAtual == "xpos":
            direcaoAtual = "yneg"
        elif direcaoAtual == "yneg":
            direcaoAtual = "xneg"
        elif direcaoAtual == "xneg":
            direcaoAtual = "ypos"
    return direcaoAtual

def robot(comandos):
    
    # (xneg,yneg,xpos,ypos)
    xneg = 0
    yneg = 0
    xpos = 0
    ypos = 0
    
    posAx = 0
    posAy = 0
    
    direcaoAtual = "ypos"
        
    lista = []
    for comando in comandos:
        if comando == "E" or comando == "D": # mudar a direcao
            direcaoAtual = direcao(direcaoAtual, comando)
        elif comando == "A": #incrementar a posicao
            if direcaoAtual == "xneg":
                posAx -= 1
                if posAx < xneg:
                    xneg = posAx
            elif direcaoAtual == "yneg":
                posAy -= 1
                if posAy < yneg:
                    yneg = posAy
            elif direcaoAtual == "xpos":
                posAx += 1
                if posAx > xpos:
                    xpos = posAx
            else:
                posAy += 1
                if posAy > ypos:
                    ypos = posAy
        else: # quando encontramos o H, damos save das variaveis na lista, ficam todas a zero e a direcao atual passa a ypos
            lista.append((xneg, yneg, xpos, ypos))
            direcaoAtual = ypos
            xneg = 0
            yneg = 0
            xpos = 0
            ypos = 0
            posAx = 0
            posAy = 0
    return lista
