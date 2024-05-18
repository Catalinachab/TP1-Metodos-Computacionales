from matricesRalas import *
import numpy as np

D = MatrizRala(79008,79008)
W = MatrizRala(79008,79008)

archivo_citas = open('citas.csv', encoding='utf8')
for fila in archivo_citas:
    fila = fila.split(',')
    if fila[0] != 'from':

        W[int(fila[1])-1,int(fila[0])-1] = 1

        if D[int(fila[0])-1,int(fila[0])-1]:
            D[int(fila[0])-1,int(fila[0])-1] += 1
        else:
            D[int(fila[0])-1,int(fila[0])-1] = 1

print("hola, sali del primer ciclo")
for i in range(D.shape[0]):
    if D[i,i] != 0:
        D[i,i] = 1/D[i,i] 
print("sali del segundo ciclo")

vector_unos  =  MatrizRala(79008,1)
p_estrella_it = MatrizRala(79008,1)
for i in range(79008):
    vector_unos[i,0] = 1
    p_estrella_it[i,0] =  1/79008
print("sali del tercer ciclo")

d = 0.85
dif_abs = 1e16
dif_abs_prev = 0
epsilon = 0.0001
print("arranco a hacer k")
k = ((1-d)/79008)*vector_unos
print("hice k")
s = W@D
print("hice primer etapa de s")
s= d*s
print("hice s")

while abs(dif_abs - dif_abs_prev) > epsilon:
    print("entre al while 4")
    dif_abs_prev = dif_abs
    p_estrella_prev = p_estrella_it
    p_estrella_it = k + s@p_estrella_it
    dif_abs = 0
    print(f"p_estrella = {p_estrella}")
    
    for j in range(p_estrella_it.shape[0]):
        dif_abs += abs(p_estrella_it[j,0] - p_estrella_prev[j,0])
    
print(f"sali del cuarto ciclo")
ranking = []
for i in range(10):
    mayor = 0
    mayor_pos = 0
    print(f"seteo el papaer numero {i} del ranking")
    for j in range(10):
        if (p_estrella_it[j,0] > mayor) and ((j+1) not in ranking):
            mayor = p_estrella_it[j,0]
            mayor_pos = j+1
    ranking.append(mayor_pos)

print(ranking)