import numpy as np
import random

#matriz 3x3 
matriz = np.diag([1,1,1])

print("------------------------------------")

#recorrer matriz
for i in range(3):
    for j in range(3):
        print(matriz[i][j])

print("------------------------------------")   
        
#Llenar num random
for i in range(3):
    for j in range(3):
        matriz[i][j] = random.randint(0,100)
print(matriz)

print("Biva las drgas y el rokan roll")