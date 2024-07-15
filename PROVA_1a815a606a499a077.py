
#Questão 1 
def my_code():
    return '1a815a606a499a077'


def my_name():
    return 'Bruno Eickhoff Seefeld'

#Questão 2

import math
class Bloco:
    def __init__(self,b_0:float,b_1:float,b_m:float):
        self.b_0=b_0
        self.b_1=b_1
        self.b_m=b_m



    def __str__(self) -> str:
        bloco=(self.b_0,self.b_1,self.b_m)

        y=([ float("%.2f" % i) for i in bloco])

        return f'{y}'
    
    def aplica_forca(self, F): #método da questão 4
        self.b_0=self.b_0+F.f_0*(1 -math.cos(self.b_m)*math.exp(-self.b_m))
        self.b_1=self.b_1+F.f_1*(1 -math.cos(self.b_m)*math.exp(-self.b_m))


    def __imul__(self,F):
        self.aplica_forca(F)
        return self
    
    def menos(self, outro):   #questão 5
        f_0=(self.b_0-outro.b_0)*(1-math.cos((self.b_m+outro.b_m)*0.5)*math.exp(-(self.b_m+outro.b_m)*0.5))
        f_1=(self.b_1-outro.b_1)*(1-math.cos((self.b_m+outro.b_m)*0.5)*math.exp(-(self.b_m+outro.b_m)*0.5))
        resultante=Forca(f_0,f_1)

        return resultante
    
    def __sub__(self,outro):
        return self.menos(outro)
        



    

class Forca:
    def __init__(self,f_0,f_1) -> None:
        self.f_0=f_0
        self.f_1=f_1
        self.norma= math.sqrt(f_0**2+f_1**2)


    def __str__(self) -> str:
        coord=[self.f_0,self.f_1]
        y=[float("%.2f " % i) for i in coord]
        return f'{y}'
    
    def __add__(self,outra):
        r0=self.f_0+ outra.f_0
        r1=self.f_1+ outra.f_1

        return Forca(r0,r1)

        
    
    def __rmul__(self,alpha):
        r0=self.f_0*alpha
        r1=self.f_1*alpha
        
        return Forca(r0,r1)
    
    def __sub__(self,outra):
        r0=self.f_0- outra.f_0
        r1=self.f_1- outra.f_1

        return Forca(r0,r1)

        






# Questão 3 
class Campo:
    def __init__(self, corpos:[Bloco]) -> None:
        self.blocos=corpos
        

    def __str__(self) -> str:
        string_blocos=[]
        for corpo in self.blocos:
            string_blocos.append(f'{corpo}')
        return ' ; '.join(string_blocos)
    
    #questão 7
    def caminhada(self,forcas):
        

        for corpo in self.blocos:
            for f in forcas:
                corpo.aplica_forca(f)

        return self
    
    # questão 8
    def carregue(self,filename:str):

        self.blocos=[]

        
        forcas=[]
        file=open(filename,'r')

        content=file.readlines()

        

        for line in content: #a última linha é vazia
            info=line.split()
            if info[0]=='Corpo:':   
                b_0=float(info[1])
                b_1=float(info[2])
                b_m=float(info[3])

                self.blocos.append(Bloco(b_0,b_1,b_m))

            else:
                
                f_0=float(info[1])
                f_1=float(info[2])
                forcas.append(Forca(f_0,f_1))

        self.caminhada(forcas)

            

        

        
        file.close()

        




    


#Questão 6
def colisao(tuple1,tuple2): 
    brm=math.log( 1+tuple1[1].b_m+tuple2[1].b_m )

    br0=(( tuple1[1].b_0-tuple2[1].b_0) * 
         (1-math.sin( math.sqrt(tuple1[1].b_m*tuple2[1].b_m) )*math.exp( -math.sqrt(tuple1[1].b_m*tuple2[1].b_m) )))

    br1=(( tuple1[1].b_1-tuple2[1].b_1) *
         (1-math.sin( math.sqrt(tuple1[1].b_m*tuple2[1].b_m) )*math.exp( -math.sqrt(tuple1[1].b_m*tuple2[1].b_m) )))

    br=Bloco(br0,br1,brm)

    fr=(((tuple1[0]-tuple2[0]).norma)+(tuple1[0]+tuple2[0]).norma) * .5 *  (tuple1[0]+tuple2[0])

    br.aplica_forca(fr)

    return br



b=Bloco(0,0,1)
f=Forca(0,5.847978678)

b.aplica_forca(f)

print(b)











        
    

