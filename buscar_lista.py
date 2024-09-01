#Creamos la lista b
lista = [
    [1,2,3],
    [5,6,7],
    [8,9,10]
    ]

#Declaramos la funcion buscar con párametros x
def buscar(l,x):

    for i  in range(len(lista)):  #Iterador i recorre
        for j in range(len(lista[i])) : #Iterador j recorre las columnas
          if lista[i][j]  == x :  #Comparamos si la la iteración es igual al numero

              return i,j # retornamos ambos iteradores

    return None  # si no encuentra el numero que estamos buscando en la lista retorna None

print(lista)
numero = int(input("Que numero desea buscar: "))
print("El numero esta en la posición ",buscar(lista,numero))



print("")
print("LISTA")
#ORDENAR LISTA
def bubble_sort(fila):

    n = len(fila) # Declaramos la variable que cuentes nuestra fila
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]



def ordenar_fila(m, i):
    # Ordena la fila especificada de la matriz
    if 0 <= i < len(lista):
        bubble_sort(lista[i])
    else:
        print("Esta fuera del rango.")

# Definición de la matriz 3x3
lista = [
    [9, 2, 5],
    [3, 8, 1],
    [6, 7, 4]
]

# Imprimir matriz original
for fila in lista :
  print(fila)




# Imprimir matriz después de ordenar, y seleccionamos la fila
print("\nMatriz después de ordenar la fila : 1")
for fila in lista:
    print(fila)


