'''
Funçaõ que recebe uma lista de palavras em 
caixa baixa e retorna o maior prefixo comum entre elas.

Retorna '' caso não exista um prefixo comum


Para issio primeiro criamos uma função que retorna o prefixo comum entre duas palvras.

'''

def pref(palavra1,palavra2):
    pref=''

    min_size=min(len(palavra1),len(palavra2))

    for i in range(min_size):
        if palavra1[i]==palavra2[i]:
            pref+=palavra1[i]
        else:
            break
    return pref


def long_pref(palavras:list)->str:

    i=0

    prefix=palavras[i] #começando com a primeira palavras

    while i<len(palavras):

        prefix=pref(prefix,palavras[i]) #a nova palavra é o prefixo comum entre as duas adjacentes na lista
        i+=1

    return prefix








if __name__=="__main__":
    palavras=['flower','flow','florida', 'floco','vazio']

    print(long_pref(palavras))


