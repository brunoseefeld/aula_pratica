#tempo

#o seguinte modulo permite realizar a contagem de tempo entre 

import time

from math import sqrt


#vamos calcular a raiz quadrada de 1000 números  utilizando dois métodos.


power_1=time.perf_counter()

for i in range(1000):
    y=i**0.5

power_2=time.perf_counter()



sqrt_1=time.perf_counter()

for i in range(1000):
    y=sqrt(i)

sqrt_2=time.perf_counter()


print("O tempo do método x**0.5 é %.32f e o tempo do método math.sqrt é %.32f" %(power_2-power_1, sqrt_2-sqrt_1))



