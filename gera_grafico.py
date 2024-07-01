import pandas as pd
import matplotlib.pyplot as plt

dados=pd.read_csv('grafico.csv')

X=dados.iloc[:,0:1]
Y=dados.iloc[:,1]


plt.plot(X,Y)

plt.show()



