"""
Ejercicio Nro2 - Escriba un programa que tenga dos listas y que, a continuación, cree las siguientes listas (en las que no debe de haber elementos repetidos):

1.- Lista de elementos que aparecen en las dos listas.
2.- Lista de elementos que aparecen en la primera lista, pero no en la segunda.
3.- Lista de elementos que aparecen en la segunda lista, pero no en la primera.
4.- Lista de elementos que aparecen en ambas listas.

"""

lista1 = ["Hola", "Adios", "Manuel", "Bayona",1,2,3,4]
lista2 = ["Adios","Manuel", "Alejandro", "Saludos",1,4,5,6,7]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

#1
lista3 = lista1 + lista2
conjunto3 = set(lista3)
dosListasEnUno = list(conjunto3)
print(f"Una nueva lista con los elementos de ambas ha sido creada: {dosListasEnUno}")

#2
conjuntofinal = conjunto1 - conjunto2
elementosDeLaPrimeraLista = list(conjuntofinal)
print(f"Los elementos de la primera lista y no de la segunda son: {elementosDeLaPrimeraLista}")

#3
conjuntofinal = conjunto2 - conjunto1
elementosDeLaSegundaLista = list(conjuntofinal)
print(f"Los elementos de la segunda lista y no de la primera son: {elementosDeLaSegundaLista}")

#4
conjuntofinal = conjunto1 & conjunto2
elementosDeAmbasListas = list(conjuntofinal)
print(f"Los elementos que aparecen en AMBAS listas son: {elementosDeAmbasListas}")
