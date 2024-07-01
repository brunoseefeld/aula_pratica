from matplotlib import pyplot as plt
import math


def pol(x: float):
    y= x**2-2*x
    return y

array=[]

a=-3/2 #beggining of interval
b=3/2 #end of interval
c=b-a #size of interval

N=1000 #ammount of points

delta=c/N #increment

for i in range(N):
    array.append(a+i*delta)

image=[pol(i) for i in array]

output=open('grafico.csv', 'w')
for j in range(len(array)):
    print(f"{array[j]},{image[j]}",file=output)

output.close()




