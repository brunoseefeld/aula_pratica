#Lista 2 impatech



def sum2list(lista1: list, lista2: list):
    #para cada elemento de lista1, criamos uma lista multiplicando-o por
    #todos da lsita 2, retorna a uma lista de listas dessa forma.

    
    #lista que terá todas as multiplicações

    r=[]
    for n1 in lista1:
        
        #lista que terá os múltiplos n1 x n2, para n2 em lsita2

        c=[]
        r.append(c)
       
       
        for n2 in lista2:
            c.append(n1*n2)
       
    return r



mcc1 = sum2list([1], [3, 5, 6])
mcc2 = sum2list([1, 2], [3, 5, 6])



def two_sum(nums:list, target: int):
    

    # vamos retornar os primeiros índices que encontrarmos tais que 
    # nums[i]+nums[j]=target
    #uma lista vazia é retornada caso não existam tais números. 

    index=[]  #índices que serão adicionados.

    for i in range(len(nums)):

        for j in range(i,len(nums)):
            if nums[i]+nums[j]==target:
                return[i,j]

     


nums = [ 7 , 3 , 4 , 2 , 11 , 15 ]
target=8


def dictwo_sum(nums,target):
    d={}

    for i,num in enumerate(nums):
        m=target-num
        if m in d:
            return [d[m],i]
        else:
            d[num]=i


print(dictwo_sum([7,1,2,3,2,4],9))










def average(lista_de_numeros:list):
    #media=soma/(quantidade de amostras)
    soma=0
    N=len(lista_de_numeros)

    for i in range(len(lista_de_numeros)):
        soma+=lista_de_numeros[i]
    return soma/N



av_test=[-1,1,-1,1,-1,1,1]


def minus_num(numbers:list,num:float):
    # for each number, put number-num in the new list

    for i in range(len(numbers)):
        numbers[i]-=num
    return numbers

#print(minus_num([0.5,.25,.5,.25,1.5,0],0.5))


def std_deviation(numbers:list):
    #calculatiing the average
    avg=average(numbers)

    #number of samples
    N=len(numbers)

    #calculating the square deviations:
    deviations=[]


    for x in minus_num(numbers,avg):
        deviations.append(x**2)

    #the standard mean deviation is sum of square mean deviations/N

    

    std=(average(deviations))**(.5)
    return  std


print(std_deviation([0.5,.25,.5,.25,1.5,0]))

#test+std=[0.5,.25,.5,.25,1.5,0]

def Tminus_one(lista, n):
    i=0
    lista1=[]
    while i<len(lista):
        a=lista[i]
        lista1+=[a-n]
        i+=1
    return lista1


print(Tminus_one([1,1,2,-1],1))






