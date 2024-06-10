'''
Dada uma lista com 2N+1 elementos, apenas um de multiplicidade 1,
 encontrar esse  elemento.

 Implementação com complexidade linear

'''

def find_un(lista:list):
    vistos={} #usando dicionário para ter busca em tempo constante

    for i in range(len(lista)):
        if lista[i] not in vistos:
            vistos[lista[i]]=i
        else:
            del vistos[lista[i]]

    #transforming the keys into a list and acessing the first and only element
    unico=list(vistos.keys())[0]

    return unico



if __name__=="__main__":

    vistos=[1,1,2,3,5,2,5,99,3]

    print('o elemento unico da lista é ')
    print(find_un(vistos))
