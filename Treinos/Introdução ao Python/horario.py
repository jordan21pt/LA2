"""
Implemente uma função que calcula o horário de uma turma de alunos.
A função recebe dois dicionários, o primeiro associa a cada UC o
respectivo horário (um triplo com dia da semana, hora de início e
duração) e o segundo associa a cada aluno o conjunto das UCs em
que está inscrito. A função deve devolver uma lista com os alunos que
conseguem frequentar todas as UCs em que estão inscritos, indicando
para cada um desses alunos o respectivo número e o número total de horas
semanais de aulas. Esta lista deve estar ordenada por ordem decrescente
de horas e, para horas idênticas, por ordem crescente de número.
"""

def compara(aula1, aula2, ucs):
    r = 1
    if aula1 not in ucs or aula2 not in ucs: 
        #se a aula nao pertencer ao dic "ucs" assume-se que há sobreposicoes de acordo com os testes dados
        r = 0
    else:
        if ucs[aula1][0] == ucs[aula2][0]: # 'la2': ('quarta', 16, 2), 'cp': ('terca', 14, 2) --> aqui comparamos "quarta" e "terca"...
            if ucs[aula1][1] == ucs[aula2][1]: # aqui comparamos o 16 com o 14...
                r = 0
            elif ((ucs[aula1][1] + ucs[aula1][2]) >= ucs[aula2][1] and (ucs[aula1][1] + ucs[aula1][2]) <= (ucs[aula2][1] + ucs[aula2][2])) or ((ucs[aula2][1] + ucs[aula2][2]) >= ucs[aula1][1] and (ucs[aula2][1] + ucs[aula2][2]) <= (ucs[aula1][1] + ucs[aula1][2])):
                r = 0
    return r

def horario(ucs,alunos):
    
    print(ucs)
    print(alunos)
    
    tuplo = []
    for aluno in alunos.keys():
        for x in alunos.get(aluno):
            tuplo.append((aluno, x))
            
    print(tuplo)
    
    semSobre = []
    for aluno in alunos.keys():
        if aluno not in semSobre:
            semSobre.append(aluno)
            
    print("lista:", semSobre)
    
    for i in tuplo:
        for j in tuplo:
            if i[0] == j[0]: #comparar os numeros de aluno
                if i[1] == j[1]: # comparar se as cadeiras forem iguais, podemos ignorar este caso
                    continue
                else:
                    r = compara(i[1], j[1], ucs)
                    if r == 0: # quer dizer que ha sobreposição, então podemos remover este elemento da lista...
                        index = i[0]
                        if index in semSobre:
                            semSobre.remove(index)

    print("lista:", semSobre)
    
    tuplo2 = []
    for aluno in semSobre:
        cont = 0
        for alunoT in tuplo:
            if aluno == alunoT[0]:
                if alunoT[1] in ucs:
                    cont += ucs[alunoT[1]][2]
        tuplo2.append((aluno, cont))
        
    tuplo2.sort(key=lambda x: (-x[1], x[0]))
    print("tuplo2: ", tuplo2)
    
    return tuplo2
