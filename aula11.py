import math

#criaremos uma classe que representa um polinômico de grau n com coeficientes dados

class Poly():
    def __init__(self, coefficients=[0]):

        #first element in the coefficients list is the constant term

        self.coeff=coefficients
        self.degree=len(coefficients)-1

    def eval(self, x):
        #calcula o valor do polinômio em x

        soma=0

        for i in range(len(self.coeff)):
            soma+=self.coeff[i]*math.pow(x,i)
        
        
        return soma
    

def sum2list(lista1,lista2):
    soma=[]

    minlength=min(len(lista1),len(lista2))

    maxlenght=max(len(lista1),len(lista2))

    for i in range(maxlenght):
        if i<minlength:
            soma.append(lista1[i]+lista2[i])

        else:
            if minlength==len(lista1):
                soma.append(lista2[i])
            else:
                soma.append(lista1[i])
    return soma






# sum of two polynomials
def poly_sum(p=Poly,q=Poly):
    sum=Poly()

    coefficients=sum2list(p.coeff,q.coeff)

    sum.coeff=coefficients

    
    

    return sum

Q=Poly()

P=Poly()


Q.coeff=[0,0,1]

P.coeff=[1,0,0,0,1]

PplusQ=poly_sum(P,Q)


print(PplusQ.coeff)









        

        