"""

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""

def aloca(prefs):
    
    final = [key for key in prefs] 
    final.sort()
    
    new_dict = {}
    n_alocados = []
    
    for aluno in final:
        if prefs.get(aluno):
            for a in prefs.get(aluno):
                if a not in new_dict:
                    new_dict.update({a: aluno})
                    break
            else:
                n_alocados.append(aluno)
                
    return n_alocados
