#Ejercicio Nro1 - Escribir un programa donde tenga una lista, y que a continuación, elimine los elementos repetidos. Por último, mostrar la lista

lista = [1,2,3,7,8,9,2,1,3,5,4,8]
conjunto = set(lista)
lista = list(conjunto)
print(lista)