## questao 1

import string

x=True

oLyst=[1,2,3]
mylist=[[11,22,33,44],oLyst,["ola","tchau"]]

oLyst.append(4)



def dPalyndrome(string):
    f1_string=''
    for i in string:
        if i!= ' ':
            f1_string+=i
    f2_string=f1_string.lower()

    re_string=''

    for j in f2_string[::-1]:
        re_string+=j


    return (re_string==f2_string)
   





def gpalyndrome(p:str):
    for k in range(len(p)//2):
        if p[k]!=p[-1-k]:
            return False
    return True


#print(gpalyndrome("anna"))


def get_vogals(string) ->list: 
    vog=set()
    for i in string:
        if (92<=ord(i)<=122):
            vog.add(i)
    return list(vog)
    


frase="A casa é feita de papo"

#print(get_vogals(frase))

"""
A função encoder receve uma string "frase" e retorna a frase porém
com as letras minúsculas trocadas pela letra anterior



"""

def encoder(frase=str)->str:

    letras=string.ascii_lowercase



    encoded=''

    for i in frase:
        if i in letras:
            encoded+=letras[letras.index(i)-1]
      
        else:
            encoded+=i   #caracteres que não são letras minúsculas são apenas adicionados 
    

    return encoded





def isAnagram(word1,word2)->bool:

   

    #eliminando os espaços.

    word1=word1.replace(' ','')
    word2=word2.replace(' ','')

    
    
    #transformando as letras para minúsculas

    word1=word1.lower()
    word2=word2.lower()


   

 

    return sorted(word1)==sorted(word2)


print(isAnagram('Ana','Anaa'))




    

    

    
    


#print(isPalyndrome("ananas"))