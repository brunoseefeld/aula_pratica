# Exercício 2


class Vector():
    def __init__(self, values : list) -> None:
        # Inicia o vetor com as coordenadas dadas por values

        self.values=values
        self.dim=len(self.values) 

    def add(self,other_vector):
        """ 
        adicionad outro vetor com as coordenadas other_vector.values

        """
        new_vector=[]

        if other_vector.dim!=self.dim:
            return new_vector
        else:
            for i in range(self.dim):
                new_vector.append(self.values[i]+other_vector.values[i])
        return Vector(new_vector)
    def dyadic_product(self, other_vector):
        matrix=[[] for i in range(self.dim)] #creating an empty matrix with number of lines= self.dim

        for line_i in range(self.dim):
            for u_val in other_vector.values:
                matrix[line_i].append(self.values[line_i]*u_val)
        return matrix
           

    

v=Vector([0,2,3.75])

u=Vector([1,.5])

sum=u.add(v)
#dprod=v.dyadic_product(u)


matrix=v.dyadic_product(u)
print(matrix)


#exercício 3


class Circle():
    def __init__(self, centro=[0,0], raio=1) -> None:
        self.centro=centro
        self.raio=raio


    def check(self, ponto:list):
        """
        verifica se o ponto está no círculo, dentro dele ou fora dele.

        """ 
        distancia2=(self.centro[0]-ponto[0])**2 +(self.centro[1]-ponto[1])**2

        if distancia2<self.raio**2:
            return 'o ponto está dentro do círculo '
        elif distancia2>self.raio**2:
            return  'o ponto está fora do círculo'
        else:
            return 'o ponto está sobre o círculo'
        



