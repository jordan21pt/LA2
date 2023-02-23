'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''

def isbn(livros):
    
    lista = []
    for livro in livros:
        lista.append((livro, livros[livro]) )
    
    lista2 = []
    for liv, cod in lista:
        sum = 0
        for i in range(0, len(cod)-1):
            if i % 2 == 0:
                sum += int(cod[i])
            else:
                sum += int(cod[i]) * 3
        sum += int(cod[12])
        lista2.append((liv, sum))
            
    resposta = []
    for liv, cod in lista2:
            if cod % 10 != 0:
                resposta.append(liv)
    
    resposta.sort()
    return resposta
