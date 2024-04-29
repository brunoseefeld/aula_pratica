


#Função que calcula limites 


#limite à direita, com delta pequeno consideramos valore próximos a x
def R_lim(function, x_0, delta):
    x=x_0+delta
    return function(x)


#limite à esquerda

def L_lim(function, x_0, delta):
    x=x_0-delta
    return function(x)


#dividimos a tolerância por 100 para não correr o risco da diferença entro os limites laterais ser da ordem de delta.
def Lim(function, x_0,tolerance):
    Rlim=R_lim(function,x_0,tolerance/100)
    Llim=L_lim(function,x_0, tolerance/100)

    if abs(Rlim-Llim)<tolerance:
        return (Rlim+Llim)/2
    else:
        return 'o limite não existe'

#função que calcula a derivada de uma função contínua.
def Df(f,x_0,h):
    return (f(x_0+h)-f(x_0))/h




#método de Newton para encontrar raízses da função f:

def Newton(f,x_initial,tolerance):
    #começamos com um chute inicial
    x=x_initial
    while abs(f(x))>tolerance:
        #notação usando a equação da reta y=mx+b
        m=Df(f,x,tolerance/100)
        b=f(x)-m*x

        x=-b/m
    return x

        
            





    







