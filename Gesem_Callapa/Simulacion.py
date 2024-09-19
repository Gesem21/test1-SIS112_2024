print("SIMULACION DE EXRAMEN SIS-112")
print("Ingrese una serie de 9 numeros")
lista= [0,0,0],[0,0,0],[0,0,0]
for i in range(3):
    for j in range(3):
        matriz = int(input())
        lista[i][j]=matriz

suma=0
for i in range(3):
    for j in range(3):
        
        suma = suma + lista[i][j]
    
suma_columnas=[]
suma_filas=[]
for i in range(3):
    suma_columa1 += lista[i][1]
    suma_columa2 += lista[i][2]
    suma_columa3 += lista[i][3]
    suma_fila1 += lista[1][i]
    suma_fila2 += lista[2][i]
    suma_fila3 += lista[3][i]
    suma_columas.append(suma_columna)
    suma_filas.append(suma_columna)

a=max()
    
print(suma)
print(lista)
        